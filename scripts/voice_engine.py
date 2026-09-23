#!/usr/bin/env python3
"""voice_engine.py — motor de voz provider-agnostico (free + pago).

Uso:
  python scripts/voice_engine.py video27 --root "C:/.../canal dark1" --channel cold-file-diaries
  python scripts/voice_engine.py video27 --root <canal> --provider elevenlabs --voice <id> --test
  python scripts/voice_engine.py video27 --root <canal> --estimate
  python scripts/voice_engine.py --list [--lang en]

Providers: edge (free) | azure | elevenlabs | fish | gemini | openai | kokoro | piper.
Contrato: playbooks/<canal>/voice.json (bloco "provider") — ver references/34-voz-tts.md.
Saida: <videoNN>/02_audio/voice_FINAL.wav + captions.srt (+ cache _tts_*).

Regras travadas:
  - cache por hash: bloco ja gerado nunca chama a API de novo (--no-cache para forcar);
  - chunking por cota (gemini/openai/fish) — menos requests, menos variacao de tom;
  - rotacao de chave no 429/403 quando api_key_env tem varias;
  - fallback da cadeia com AVISO explicito (nunca silencioso);
  - concat SEMPRE re-encode (sample rates diferentes + -c copy dropa audio);
  - chaves NUNCA entram no JSON/commit — so o nome da env (api_key_env) ou arquivo local.
"""
import argparse
import asyncio
import base64
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import wave
from pathlib import Path

PLAYBOOKS = Path(os.environ.get(
    "DARK_MASTER_PLAYBOOKS",
    str(Path.home() / ".config" / "opencode" / "skills" / "dark-master" / "playbooks")))

PROVIDERS = ("edge", "azure", "elevenlabs", "fish", "gemini", "openai", "kokoro", "piper")

# Provider metadata: extensao, precisa de key, suporta rate/pitch nativos, custo (USD/1M chars).
PROVIDER_META = {
    "edge":       {"ext": "mp3", "key": False, "native_rate": True,  "native_pitch": True,  "cost": 0.0},
    "azure":      {"ext": "mp3", "key": True,  "native_rate": True,  "native_pitch": True,  "cost": 15.0},
    "elevenlabs": {"ext": "mp3", "key": True,  "native_rate": True,  "native_pitch": False, "cost": 100.0},
    "fish":       {"ext": "mp3", "key": True,  "native_rate": False, "native_pitch": False, "cost": 15.0},
    "gemini":     {"ext": "wav", "key": True,  "native_rate": False, "native_pitch": False, "cost": 12.0},
    "openai":     {"ext": "mp3", "key": True,  "native_rate": False, "native_pitch": False, "cost": 15.0},
    "kokoro":     {"ext": "wav", "key": False, "native_rate": True,  "native_pitch": False, "cost": 0.0},
    "piper":      {"ext": "wav", "key": False, "native_rate": True,  "native_pitch": False, "cost": 0.0},
}

# Custo alternativo do elevenlabs por modelo (flash e metade).
ELEVENLABS_MODEL_COST = {"eleven_flash_v2_5": 50.0, "eleven_turbo_v2_5": 50.0}

DEFAULT_ENV = {
    "azure": "AZURE_SPEECH_KEY", "elevenlabs": "ELEVENLABS_API_KEY", "fish": "FISH_API_KEY",
    "gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY",
}

# Vozes curadas por provider/idioma (sugestao — o canal define a sua no playbook).
CURATED = {
    "edge": {
        "en": ["en-US-ChristopherNeural", "en-US-GuyNeural", "en-GB-RyanNeural", "en-US-EricNeural"],
        "pt": ["pt-BR-AntonioNeural", "pt-BR-FranciscaNeural", "pt-BR-ThalitaMultilingualNeural"],
    },
    "kokoro": {
        "en": ["am_michael", "am_onyx", "am_fenrir", "af_heart", "bm_george"],
        "pt": ["pm_alex", "pf_dora", "pm_santa"],
    },
    "gemini": {
        "en": ["Algenib", "Charon", "Kore", "Orus", "Schedar", "Puck", "Fenrir"],
        "pt": ["Algenib", "Charon", "Kore", "Orus", "Schedar"],
    },
    "openai": {
        "en": ["onyx", "cedar", "marin", "sage", "echo", "alloy"],
        "pt": ["onyx", "cedar", "marin", "sage", "echo"],
    },
}

DEFAULT_CHUNK = {"gemini": 2000, "openai": 1400, "fish": 0}
MIN_CACHE_BYTES = 2000

CHAIN_FALLBACK_VOICE = {"edge": "en-US-GuyNeural", "kokoro": "am_michael",
                        "gemini": "Charon", "openai": "onyx"}


# ---------------------------------------------------------------- contrato
def resolve_playbook(channel):
    if not channel:
        return None
    p = Path(channel).expanduser()
    if p.is_dir():
        return p
    p = PLAYBOOKS / channel
    if p.is_dir():
        return p
    return None


def _read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def load_voice_cfg(channel, root):
    """Resolve voice.json: --channel -> DARK_CHANNEL -> root/canal.json -> erro guiado.

    Sem canal NAO cai no CFD em silencio (canal novo != clone): exige --voice explicito.
    """
    source = None
    data = None
    ch = channel or os.environ.get("DARK_CHANNEL")
    if ch:
        p = resolve_playbook(ch)
        if p:
            data = _read_json(p / "voice.json")
            source = str(p / "voice.json")
            if data is None:
                print(f"[AVISO] {source} ilegivel/ausente - seguindo sem contrato de voz.")
        else:
            print(f"[AVISO] canal '{ch}' nao encontrado em {PLAYBOOKS} - seguindo sem contrato.")
    if data is None and root:
        cj = _read_json(os.path.join(root, "canal.json"))
        if isinstance(cj, dict) and isinstance(cj.get("voice"), dict):
            data, source = cj["voice"], os.path.join(root, "canal.json")
    return data or {}, source


def normalize_provider(cfg, args):
    """Bloco provider (novo) ou engine/voice (legado). --provider/--voice sobrepoem."""
    prov = dict(cfg.get("provider") or {})
    if not prov:
        legacy = str(cfg.get("engine") or "edge-tts").lower()
        ptype = "edge" if legacy.startswith("edge") else (
            "azure" if "azure" in legacy else legacy.split("-")[0])
        prov = {"type": ptype if ptype in PROVIDERS else "edge"}
        if cfg.get("voice"):
            prov.setdefault("voice_id", cfg["voice"])
    if args.provider:
        prov["type"] = args.provider
    if args.voice:
        prov["voice_id"] = args.voice
    prov["type"] = str(prov.get("type") or "edge").lower()
    if prov["type"] not in PROVIDERS:
        raise SystemExit(f"provider '{prov['type']}' desconhecido. Use: {', '.join(PROVIDERS)}")
    if not prov.get("voice_id"):
        prov["voice_id"] = args.voice or (cfg.get("voice") if cfg else None)
    settings = dict(prov.get("settings") or {})
    if prov["type"] == "gemini":
        settings.setdefault("chunk_chars", DEFAULT_CHUNK["gemini"])
        settings.setdefault("style", "")
    elif prov["type"] == "openai":
        settings.setdefault("chunk_chars", DEFAULT_CHUNK["openai"])
    elif prov["type"] == "fish":
        settings.setdefault("chunk_chars", DEFAULT_CHUNK["fish"])
    prov["settings"] = settings
    return prov


def _voice_from_file(step, root):
    """Convencao dos projetos: <root>/canal/<tipo>_voice.txt (ex. fish_voice.txt do Laudo)."""
    vf = (step.get("settings") or {}).get("voice_file")
    if not vf and root:
        vf = os.path.join(root, "canal", f"{step['type']}_voice.txt")
    if not vf or not os.path.exists(vf):
        return None
    txt = Path(vf).read_text(encoding="utf-8").strip()
    return txt.split()[0] if txt else None


def build_chain(primary, cfg, root=None):
    """Cadeia primario + fallbacks. Strings viram dict; objeto mescla com o primario.
    Voz do fallback: explicita > arquivo local (canal/<tipo>_voice.txt) > mesma do primario
    (se mesmo tipo) > curada + AVISO."""
    for st in [primary] + [f for f in ((cfg.get("provider") or {}).get("fallback") or []) if isinstance(f, dict)]:
        if isinstance(st, dict) and not st.get("voice_id"):
            v = _voice_from_file(st, root)
            if v:
                st["voice_id"] = v
    chain = [primary]
    for fb in (cfg.get("provider") or {}).get("fallback") or []:
        if isinstance(fb, str):
            step = {"type": fb, "voice_id": None, "settings": {}}
        elif isinstance(fb, dict) and fb.get("type"):
            step = {"type": fb["type"], "voice_id": fb.get("voice_id"),
                    "model": fb.get("model"), "api_key_env": fb.get("api_key_env"),
                    "settings": dict(fb.get("settings") or {})}
        else:
            continue
        if step["type"] not in PROVIDERS:
            print(f"[AVISO] fallback '{step['type']}' desconhecido - ignorado")
            continue
        explicit = step.get("voice_id")
        step["voice_id"] = fallback_voice(step, primary)
        if step["voice_id"] and not explicit and step["type"] != primary["type"]:
            print(f"[AVISO] fallback '{step['type']}' sem voz propria - usando '{step['voice_id']}'")
        chain.append(step)
    return chain


def fallback_voice(step, primary):
    if step.get("voice_id"):
        return step["voice_id"]
    if step["type"] == primary["type"]:
        return primary.get("voice_id")
    if step["type"] == "azure" and str(primary.get("voice_id") or "").endswith("Neural"):
        return primary["voice_id"]  # upgrade edge->azure mantem a voz exata
    return CHAIN_FALLBACK_VOICE.get(step["type"])


def loudnorm_target(cfg):
    post = cfg.get("post") or {}
    if post.get("loudnorm"):
        return str(post["loudnorm"])
    m = re.search(r"loudnorm=I=(-?\d+(?:\.\d+)?)", (cfg.get("ducking") or {}).get("filters", ""))
    return m.group(1) if m else "-16"


def keys_for(prov, root):
    """Fontes de chave (nunca impressas): env (api_key_env) -> env default -> settings.key_file
    -> <root>/canal/<tipo>_key.txt. Valores com virgula/espaco viram lista (rotacao)."""
    names = []
    env_names = prov.get("api_key_env") or DEFAULT_ENV.get(prov["type"], "")
    names += [n.strip() for n in re.split(r"[,;\s]+", env_names) if n.strip()]
    if DEFAULT_ENV.get(prov["type"]):
        names.append(DEFAULT_ENV[prov["type"]])
    keys = []
    for n in names:
        v = os.environ.get(n)
        if v:
            keys += [k.strip() for k in re.split(r"[,;\s]+", v) if k.strip()]
        elif len(n) > 20 and not n.isupper():
            keys.append(n)  # valor colado direto (desencorajado, mas aceito)
    kf = (prov.get("settings") or {}).get("key_file")
    cands = [kf] if kf else []
    if root:
        cands.append(os.path.join(root, "canal", f"{prov['type']}_key.txt"))
    for c in cands:
        if c and os.path.exists(c):
            keys += [k.strip() for k in re.split(r"[,;\s]+", Path(c).read_text(encoding="utf-8")) if k.strip()]
    seen, out = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out


# ---------------------------------------------------------------- ffmpeg
def get_ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"


FFMPEG = get_ffmpeg()


def dur(path):
    r = subprocess.run([FFMPEG, "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        tail = (r.stderr or "")[-1200:]
        raise RuntimeError(f"ffmpeg falhou: {tail}")
    return r


# ---------------------------------------------------------------- HTTP
class KeyRing:
    """Rotaciona chaves no 429/403 sem parar o video no meio."""

    def __init__(self, keys, label):
        self.keys = list(keys)
        self.dead = set()
        self.i = 0
        self.label = label

    def current(self):
        return self.keys[self.i % len(self.keys)]

    def rotate(self, why=""):
        self.i += 1
        if self.i % len(self.keys) == 0:
            time.sleep(3)
        if why:
            print(f"   -> {self.label}: rotacionando chave ({why})")

    def kill(self, key):
        try:
            self.dead.add(self.keys.index(key))
        except ValueError:
            pass

    def exhausted(self):
        return len(self.dead) >= len(self.keys)


def http_json(url, body, headers, timeout=180):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def http_post(url, data, headers, timeout=180):
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def is_quota(e):
    s = str(e)
    return "429" in s or "quota" in s.lower() or "RESOURCE_EXHAUSTED" in s


def is_auth(e):
    s = str(e)
    return "401" in s or "403" in s or "PERMISSION_DENIED" in s or "invalid_api_key" in s.lower()


def with_retries(fn, ring, tries=6, base_sleep=6):
    last = None
    for t in range(tries):
        try:
            return fn(ring.current())
        except urllib.error.HTTPError as e:
            last = e
            if is_auth(e):
                print(f"   -> chave invalida/sem permissao ({e.code}); descartando")
                ring.kill(ring.current())
                if ring.exhausted():
                    raise RuntimeError("todas as chaves morreram")
                ring.rotate("auth")
                continue
            if is_quota(e):
                ring.rotate("429/quota")
                continue
            time.sleep(base_sleep * (t + 1))
        except Exception as e:
            last = e
            time.sleep(base_sleep * (t + 1))
    raise RuntimeError(f"falhou apos {tries} tentativas: {str(last)[:200]}")


# ---------------------------------------------------------------- providers
def synth_edge(text, out, prov):
    import edge_tts  # opcional: pip install edge-tts

    rate = prov.get("rate") or "+0%"
    pitch = prov.get("pitch") or "+0Hz"
    asyncio.run(edge_tts.Communicate(text, prov["voice_id"], rate=rate, pitch=pitch).save(out))


def synth_azure(text, out, prov, ring):
    region = os.environ.get("AZURE_SPEECH_REGION") or prov["settings"].get("region") or "eastus"
    lang = "-".join(prov["voice_id"].split("-")[:2])
    rate, pitch = prov.get("rate") or "0%", prov.get("pitch") or "0Hz"
    ssml = (f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='{lang}'>"
            f"<voice name='{prov['voice_id']}'><prosody rate='{rate}' pitch='{pitch}'>"
            f"{text.replace('&', '&amp;').replace('<', '&lt;')}</prosody></voice></speak>")
    url = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {"Ocp-Apim-Subscription-Key": "", "Content-Type": "application/ssml+xml",
               "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
               "User-Agent": "dark-master"}

    def call(key):
        h = dict(headers, **{"Ocp-Apim-Subscription-Key": key})
        data = http_post(url, ssml.encode("utf-8"), h)
        if len(data) < MIN_CACHE_BYTES:
            raise RuntimeError(f"resposta curta ({len(data)}b)")
        Path(out).write_bytes(data)

    with_retries(call, ring)


def synth_elevenlabs(text, out, prov, ring):
    model = prov.get("model") or "eleven_multilingual_v2"
    st = prov["settings"]
    vs = {k: st[k] for k in ("stability", "similarity_boost", "style", "use_speaker_boost") if k in st}
    speed = st.get("speed") or prov.get("speed")
    if speed:
        vs["speed"] = max(0.7, min(1.2, float(speed)))
    body = {"text": text, "model_id": model, "voice_settings": vs}
    url = (f"https://api.elevenlabs.io/v1/text-to-speech/{urllib.parse.quote(prov['voice_id'])}"
           f"?output_format=mp3_44100_128")

    def call(key):
        data = http_json(url, body, {"xi-api-key": key, "Content-Type": "application/json"})
        if len(data) < MIN_CACHE_BYTES:
            raise RuntimeError(f"resposta curta ({len(data)}b)")
        Path(out).write_bytes(data)

    with_retries(call, ring)


def synth_fish(text, out, prov, ring):
    body = {"text": text, "reference_id": prov["voice_id"], "format": "mp3", "mp3_bitrate": 128}
    headers = {"Authorization": "", "Content-Type": "application/json"}
    if prov.get("model"):
        headers["model"] = prov["model"]

    def call(key):
        h = dict(headers, **{"Authorization": f"Bearer {key}"})
        data = http_json("https://api.fish.audio/v1/tts", body, h, timeout=240)
        if len(data) < MIN_CACHE_BYTES:
            raise RuntimeError(f"resposta curta ({len(data)}b)")
        Path(out).write_bytes(data)

    with_retries(call, ring)


def synth_gemini(text, out, prov, ring):
    model = prov.get("model") or "gemini-2.5-flash-preview-tts"
    style = prov["settings"].get("style") or ""
    body = {"contents": [{"parts": [{"text": (style + text) if style else text}]}],
            "generationConfig": {
                "responseModalities": ["AUDIO"],
                "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": prov["voice_id"]}}}}}
    if prov["settings"].get("seed") is not None:
        body["generationConfig"]["seed"] = prov["settings"]["seed"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    def call(key):
        data = http_json(f"{url}?key={urllib.parse.quote(key)}", body,
                         {"Content-Type": "application/json"}, timeout=240)
        resp = json.loads(data)
        raw = base64.b64decode(resp["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
        if len(raw) < MIN_CACHE_BYTES:
            raise RuntimeError(f"audio curto ({len(raw)}b)")
        with wave.open(out, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(int(prov["settings"].get("sample_rate", 24000)))
            w.writeframes(raw)

    with_retries(call, ring)


def synth_openai(text, out, prov, ring):
    model = prov.get("model") or "gpt-4o-mini-tts"
    body = {"model": model, "voice": prov["voice_id"], "input": text, "response_format": "mp3"}
    if prov["settings"].get("instructions"):
        body["instructions"] = prov["settings"]["instructions"]

    def call(key):
        data = http_json("https://api.openai.com/v1/audio/speech", body,
                         {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, timeout=240)
        if len(data) < MIN_CACHE_BYTES:
            raise RuntimeError(f"resposta curta ({len(data)}b)")
        Path(out).write_bytes(data)

    with_retries(call, ring)


def synth_kokoro(text, out, prov):
    import numpy as np
    import soundfile as sf
    from kokoro import KPipeline  # pip install kokoro soundfile

    lang = prov["settings"].get("lang_code") or ("p" if str(prov["voice_id"]).startswith(("p", "b")) else "a")
    speed = float(prov.get("speed") or 1.0)
    global _KOKORO
    try:
        _KOKORO
    except NameError:
        _KOKORO = {}
    if lang not in _KOKORO:
        _KOKORO[lang] = KPipeline(lang_code=lang)
    audio = []
    for _, _, a in _KOKORO[lang](text, voice=prov["voice_id"], speed=speed):
        audio.append(a)
    if not audio:
        raise RuntimeError("kokoro nao retornou audio")
    sf.write(out, np.concatenate(audio), 24000)


def synth_piper(text, out, prov):
    model = prov["voice_id"]
    if not model or not os.path.exists(model):
        raise RuntimeError(f"piper precisa do caminho do modelo .onnx em voice_id (recebi '{model}')")
    try:  # API Python (pip install piper-tts) — mesmo padrao do gerar_voz_laudo.py
        from piper import PiperVoice
        global _PIPER
        try:
            _PIPER
        except NameError:
            _PIPER = {}
        if model not in _PIPER:
            _PIPER[model] = PiperVoice.load(model)
        v = _PIPER[model]
        with wave.open(out, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(v.config.sample_rate)
            for chunk in v.synthesize(text):
                w.writeframes(chunk.audio_int16_bytes)
        if os.path.getsize(out) > MIN_CACHE_BYTES:
            return
        raise RuntimeError("piper retornou audio curto")
    except ImportError:
        pass
    exe = prov["settings"].get("exe") or "piper"  # fallback: binario CLI
    speed = float(prov.get("speed") or 1.0)
    r = subprocess.run([exe, "-m", model, "-f", out, "--length_scale", f"{1.0 / max(speed, 0.1):.3f}"],
                       input=text.encode("utf-8"), capture_output=True)
    if r.returncode != 0 or not os.path.exists(out):
        raise RuntimeError(f"piper falhou: {(r.stderr or b'')[-300:]!r}")


def synth(step, text, out, root):
    """Despacha para o provider. Retorna True se gerou; levanta em falha."""
    t = step["type"]
    if t == "edge":
        synth_edge(text, out, step)
    elif t == "azure":
        synth_azure(text, out, step, step["_ring"])
    elif t == "elevenlabs":
        synth_elevenlabs(text, out, step, step["_ring"])
    elif t == "fish":
        synth_fish(text, out, step, step["_ring"])
    elif t == "gemini":
        synth_gemini(text, out, step, step["_ring"])
    elif t == "openai":
        synth_openai(text, out, step, step["_ring"])
    elif t == "kokoro":
        synth_kokoro(text, out, step)
    elif t == "piper":
        synth_piper(text, out, step)
    else:
        raise RuntimeError(f"provider sem adapter: {t}")


# ---------------------------------------------------------------- texto
def read_blocks(narr):
    txt = Path(narr).read_text(encoding="utf-8")
    return [p.strip() for p in txt.strip().split("\n\n")
            if p.strip() and re.search(r"[A-Za-zÀ-ú0-9]", p)]


def normalize_text(text, cfg):
    for k, v in (cfg.get("normalize") or {}).items():
        text = text.replace(k, v)
    return text


def chunk_text(text, limit):
    if not limit or len(text) <= limit:
        return [text]
    parts = re.split(r"(?<=[.!?…])\s+", text)
    out, cur = [], ""
    for s in parts:
        while len(s) > limit:  # sentenca gigante: corta em virgula/espaco
            cut = s.rfind(", ", 0, limit)
            cut = cut if cut > limit // 2 else s.rfind(" ", 0, limit)
            cut = cut if cut > 0 else limit
            out.append((cur + " " + s[:cut]).strip())
            cur, s = "", s[cut:]
        if cur and len(cur) + len(s) + 1 > limit:
            out.append(cur)
            cur = s
        else:
            cur = (cur + " " + s).strip() if cur else s
    if cur:
        out.append(cur)
    return out


def rate_pct(rate):
    if not rate:
        return 0.0
    m = re.search(r"(-?\d+(?:\.\d+)?)", str(rate))
    return float(m.group(1)) if m else 0.0


def series_of(vdir, cfg):
    """Serie GLOBAL do video (youtube_package.txt) — mesma regra dos scripts dos canais.
    Nao detectar serie no texto do bloco: a entrega e por serie do video inteiro."""
    try:
        t = Path(vdir, "youtube_package.txt").read_text(encoding="utf-8").upper()
        for s in (cfg.get("series_detect") or []):
            if s in t:
                return s
    except OSError:
        pass
    return cfg.get("default_series") or "default"


def prosody_for(text, idx, total, cfg, series=None):
    """Mesmas regras do contrato (hook/beat/outro/serie) — provider traduz o que suporta."""
    R = cfg.get("rules") or {}
    hook = R.get("hook") or {"rate": "-8%", "pitch": "-5Hz"}
    outro = R.get("outro") or {"rate": "-4%", "pitch": "-2Hz"}
    beat = R.get("beat") or {"rate": "-8%", "pitch": "-5Hz"}
    if idx == 0:
        return dict(hook)
    if idx >= total - int(R.get("outro_from_end", 2)):
        return dict(outro)
    if len(text) < int(R.get("beat_max_len", 150)) or "?" in text[:int(R.get("beat_question_pos", 80))]:
        return dict(beat)
    smap = cfg.get("series") or {}
    key = series or cfg.get("default_series") or "default"
    return dict(smap.get(key) or smap.get("default") or {"rate": "-5%", "pitch": "-3Hz"})


def provider_params(step, text, idx, total, cfg, series=None):
    """Traduz rate/pitch do contrato para o que o provider aceita (speed/atempo/pitch nativo)."""
    pr = prosody_for(text, idx, total, cfg, series)
    pct = rate_pct(pr.get("rate"))
    step = dict(step)
    step["rate"] = pr.get("rate")
    step["pitch"] = pr.get("pitch")
    meta = PROVIDER_META[step["type"]]
    if meta["native_rate"]:
        if step["type"] == "elevenlabs":
            step["speed"] = max(0.7, min(1.2, 1 + pct / 100.0))
        elif step["type"] in ("kokoro", "piper"):
            step["speed"] = max(0.5, min(1.5, 1 + pct / 100.0))
    step["atempo"] = 1 + pct / 100.0 if not meta["native_rate"] and pct else 0.0
    return step, pr


# ---------------------------------------------------------------- pipeline
def voice_pipeline(args, cfg, prov, blocks, narr, vdir, outdir):
    settings = prov["settings"]
    chunk_limit = int(settings.get("chunk_chars") or 0)
    trim = cfg.get("trim") or {"start": 0.1, "end_pad": 0.8}
    gaps = cfg.get("gaps") or {"short_max_len": 150, "short": 0.35, "normal": 0.15}
    filters = (cfg.get("post") or {}).get("voice_filters") or "highpass=f=70,lowpass=f=8000,volume=1.2"
    target = loudnorm_target(cfg)
    cache_on = not args.no_cache

    steps = build_chain(prov, cfg, args.root)
    if not args.dry_run:
        usable = []
        for st in steps:
            if not st.get("voice_id"):
                if st is steps[0]:
                    raise SystemExit(f"[ERRO] provider '{st['type']}' sem voz definida (--voice ou provider.voice_id)")
                print(f"[AVISO] fallback '{st['type']}' sem voz resolvivel - removido da cadeia")
                continue
            if PROVIDER_META[st["type"]]["key"]:
                keys = keys_for(st, args.root)
                if not keys:
                    if st is steps[0]:
                        raise SystemExit(
                            f"[ERRO] provider '{st['type']}' exige chave e nenhuma foi encontrada.\n"
                            f"       Defina {st.get('api_key_env') or DEFAULT_ENV.get(st['type'])} "
                            f"ou salve {args.root}/canal/{st['type']}_key.txt")
                    print(f"[AVISO] fallback '{st['type']}' sem chave - removido da cadeia")
                    continue
                st["_ring"] = KeyRing(keys, st["type"])
            usable.append(st)
        steps = usable
        print(f"provider: {steps[0]['type']} | cadeia: {' -> '.join(s['type'] for s in steps)}"
              + (f" | chave(s): {len(steps[0]['_ring'].keys)}" if "_ring" in steps[0] else ""))
    warn_pitch = set()

    def cache_path(step, i, ci, ch):
        key = "|".join([step["type"], str(step.get("model")), str(step.get("voice_id")),
                        str(step.get("rate")), str(step.get("pitch")),
                        json.dumps(step.get("settings") or {}, sort_keys=True), ch])
        h = hashlib.md5(key.encode()).hexdigest()[:12]
        return os.path.join(outdir, f"_tts_{step['type']}_{i:02d}_{ci:02d}_{h}.{PROVIDER_META[step['type']]['ext']}")

    def with_rate(path, step):
        """Aplica atempo (rate de providers sem speed nativo) em arquivo deterministico (cacheavel)."""
        if not step.get("atempo") or abs(step["atempo"] - 1.0) <= 0.005:
            return path
        t = path.rsplit(".", 1)[0] + "_t." + path.rsplit(".", 1)[1]
        if not os.path.exists(t):
            run([FFMPEG, "-y", "-i", path, "-af",
                 f"atempo={max(0.5, min(2.0, step['atempo'])):.4f}", t])
        return t

    series = series_of(vdir, cfg)
    if series and series != cfg.get("default_series"):
        print(f"serie do video: {series}")
    parts, timeline = [], []
    dead = set()
    for i, para in enumerate(blocks):
        text = normalize_text(para, cfg)
        _, pr = provider_params(steps[0], text, i, len(blocks), cfg, series)
        chunks = chunk_text(text, chunk_limit) if not args.dry_run else [text]
        chunk_files = []
        for ci, ch in enumerate(chunks):
            if args.dry_run:
                out = cache_path(provider_params(steps[0], text, i, len(blocks), cfg, series)[0], i, ci, ch)
                print(f"  bloco {i+1:02d} chunk {ci+1}: {len(ch):5d} chars -> {os.path.basename(out)}"
                      f" (rate {pr.get('rate')} pitch {pr.get('pitch')})")
                chunk_files.append(out)
                continue
            used, cached = None, False
            for cand in steps:  # cache de qualquer provider da cadeia evita pagar de novo
                if cand["type"] in dead:
                    continue
                cand2, _ = provider_params(cand, text, i, len(blocks), cfg, series)
                cp = cache_path(cand2, i, ci, ch)
                if cache_on and os.path.exists(cp) and os.path.getsize(cp) > MIN_CACHE_BYTES:
                    used, cached = cand2, True
                    if cand2["type"] != steps[0]["type"]:
                        print(f"   [nota] cache do fallback '{cand2['type']}' "
                              f"(use --no-cache para regerar no primario)")
                    break
            if used is None:
                live = [c for c in steps if c["type"] not in dead]
                for si, cand in enumerate(live):
                    cand2, _ = provider_params(cand, text, i, len(blocks), cfg, series)
                    cp = cache_path(cand2, i, ci, ch)
                    try:
                        synth(cand2, ch, cp, args.root)
                        used = cand2
                        if si > 0:
                            print(f"   [!] bloco {i+1} gerado pelo FALLBACK '{cand2['type']}'")
                        break
                    except Exception as e:
                        if PROVIDER_META[cand["type"]]["key"]:
                            dead.add(cand["type"])  # auth/quota: nao martelar a cada bloco
                        if si + 1 < len(live):
                            print(f"[AVISO] provider '{cand['type']}' falhou no bloco {i+1} ({str(e)[:120]}) "
                                  f"- caindo para '{live[si+1]['type']}'")
                        else:
                            raise SystemExit(f"[ERRO] provider '{cand['type']}' falhou no bloco {i+1}: {str(e)[:250]}")
                if used is None:
                    raise SystemExit(f"bloco {i+1}: todos os providers da cadeia falharam")
            if used["type"] not in ("edge", "azure") and used.get("pitch") and used["type"] not in warn_pitch:
                warn_pitch.add(used["type"])
                print(f"   [nota] provider '{used['type']}' nao suporta pitch nativo - "
                      f"'{used.get('pitch')}' sera ignorado (rate e aplicado).")
            out = with_rate(cache_path(used, i, ci, ch), used)
            tag = "cache" if cached else "ok"
            print(f"  bloco {i+1}/{len(blocks)} chunk {ci+1}/{len(chunks)} {tag} ({len(ch):5d} chars)")
            chunk_files.append(out)
        # junta chunks do bloco (re-encode: nunca -c copy entre taxas)
        if len(chunk_files) > 1 and not args.dry_run:
            lst = os.path.join(outdir, f"_chunks_{i:02d}.txt")
            with open(lst, "w", encoding="utf-8") as f:
                for p in chunk_files:
                    f.write(f"file '{p}'\n")
            merged = os.path.join(outdir, f"_block_{i:02d}.wav")
            run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-ar", "44100", "-ac", "1", merged])
            chunk_files = [merged]
        parts.append(chunk_files[0])
        timeline.append((chunk_files[0], para))

    if args.dry_run:
        print(f"\n[dry-run] {len(blocks)} blocos, {sum(len(chunk_text(normalize_text(b, cfg), chunk_limit)) for b in blocks)} chunks")
        print(f"[dry-run] filtros: {filters}")
        print(f"[dry-run] loudnorm I={target} | trim {trim} | gaps {gaps}")
        print(f"[dry-run] saida: {os.path.join(outdir, 'voice_FINAL.wav')} + captions.srt")
        return None

    # trim + gaps + concat
    trimmed = []
    silence = str(trim.get("mode", "")).lower() == "silence" or "silence" in trim
    for p in parts:
        d = dur(p)
        t = p.replace("_tts_", "_ttst_").replace("_block_", "_blockt_")
        if silence:
            s = trim.get("silence") or {}
            sd, ed = s.get("start_duration", 0.06), s.get("end_duration", 0.10)
            th = s.get("threshold", "-45dB")
            af = (f"silenceremove=start_periods=1:start_duration={sd}:start_threshold={th}:detection=peak,"
                  f"areverse,silenceremove=start_periods=1:start_duration={ed}:start_threshold={th}:detection=peak,"
                  f"areverse,asetpts=PTS-STARTPTS")
        else:
            af = f"atrim=start={trim['start']}:end={max(d - trim['end_pad'], 0.05):.2f},asetpts=PTS-STARTPTS"
        run([FFMPEG, "-y", "-i", p, "-af", af, t])
        trimmed.append(t)
    sil_n = os.path.join(outdir, "_sil_norm.mp3")
    sil_s = os.path.join(outdir, "_sil_short.mp3")
    run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
         "-t", str(gaps["normal"]), sil_n])
    run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
         "-t", str(gaps["short"]), sil_s])
    lst = os.path.join(outdir, "_voice_list.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for p, (_, para) in zip(trimmed, timeline):
            gap = sil_s if len(para) < int(gaps["short_max_len"]) else sil_n
            f.write(f"file '{p}'\nfile '{gap}'\n")
    raw = os.path.join(outdir, "voice_raw.wav")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-ar", "44100", "-ac", "1", raw])
    vpol = os.path.join(outdir, "_voice_pol.wav")
    run([FFMPEG, "-y", "-i", raw, "-af", filters, "-ar", "44100", "-ac", "1", vpol])
    vd = dur(vpol)

    final = os.path.join(outdir, "voice_FINAL.wav")
    if args.bed:
        vol = args.bed_vol or 0.08
        bed = os.path.join(outdir, "_bed.wav")
        bd = dur(args.bed)
        loops = int(vd // max(bd, 1)) + 2
        fade = max(vd - 3, 0)
        run([FFMPEG, "-y", "-stream_loop", str(loops), "-i", args.bed, "-filter_complex",
             f"[0:a]volume={vol},atrim=0:{vd:.2f},afade=t=in:st=0:d=2,"
             f"afade=t=out:st={fade:.2f}:d=3[bed]", "-map", "[bed]", "-ar", "44100", "-ac", "1", bed])
        duck = (cfg.get("ducking") or {}).get("filters") or (
            "[0:a]asplit=2[voxmix][voxkey];[1:a][voxkey]sidechaincompress="
            "threshold=0.015:ratio=10:attack=8:release=450:makeup=1[bedduck];"
            "[voxmix][bedduck]amix=inputs=2:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11")
        run([FFMPEG, "-y", "-i", vpol, "-i", bed, "-filter_complex", duck, "-ar", "44100", "-ac", "1", final])
    else:
        run([FFMPEG, "-y", "-i", vpol, "-af", f"loudnorm=I={target}:TP=-1.5:LRA=11",
             "-ar", "44100", "-ac", "1", final])

    # SRT por bloco (mesmo contrato do gerar_voz_v3; gerar_srt_norm refina depois)
    srt = os.path.join(outdir, "captions.srt")
    if os.path.exists(srt) and not os.path.exists(srt + ".bak_voicegen"):
        shutil.copy2(srt, srt + ".bak_voicegen")
    tcur = 0.0

    def ts(s):
        h, m = int(s // 3600), int((s % 3600) // 60)
        sec, ms = int(s % 60), int((s % 1) * 1000)
        return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"

    with open(srt, "w", encoding="utf-8") as sf:
        for bi, (p, (_, para)) in enumerate(zip(trimmed, timeline), 1):
            d = dur(p)
            gap = gaps["short"] if len(para) < int(gaps["short_max_len"]) else gaps["normal"]
            txt = para[:160].replace("\n", " ") + ("..." if len(para) > 160 else "")
            sf.write(f"{bi}\n{ts(tcur)} --> {ts(tcur + d)}\n{txt}\n\n")
            tcur += d + gap
    print(f"VOZ PRONTA: {final} ({dur(final)/60:.2f} min) | provider {prov['type']} | {srt}")
    return final


# ---------------------------------------------------------------- modos
def cmd_list(args):
    print("Providers:\n")
    for p in PROVIDERS:
        m = PROVIDER_META[p]
        key = "exige chave" if m["key"] else "sem chave"
        print(f"  {p:12s} {key:12s} custo ~${m['cost']:>5.1f}/1M chars")
    print("\nVozes curadas (sugestao - trave a sua no playbook):\n")
    for p, langs in CURATED.items():
        for lang, vs in langs.items():
            print(f"  {p:8s} [{lang}] {', '.join(vs)}")
    if args.lang:
        try:
            import edge_tts
            voices = asyncio.run(edge_tts.list_voices())
            sel = [v["ShortName"] for v in voices if v["Locale"].startswith(args.lang)][:40]
            print(f"\nedge-tts [{args.lang}] ({len(sel)} primeiras): {', '.join(sel)}")
        except Exception as e:
            print(f"\n(edge-tts indisponivel para listar vozes: {str(e)[:80]})")


def cmd_estimate(args, cfg, blocks, prov):
    chars = sum(len(normalize_text(b, cfg)) for b in blocks)
    words = sum(len(b.split()) for b in blocks)
    est_min = words / 145.0
    print(f"Roteiro: {len(blocks)} blocos | {words} palavras | {chars} chars | ~{est_min:.1f} min narrados\n")
    print(f"{'provider':12s} {'modelo':28s} {'$/video':>9s}")
    rows = [("edge", "-", 0.0), ("kokoro", "-", 0.0), ("piper", "-", 0.0),
            ("azure", "neural", 15.0), ("fish", "s1/s2-pro", 15.0),
            ("gemini", "2.5-flash-tts", 12.0), ("openai", "gpt-4o-mini-tts", 15.0),
            ("elevenlabs", "flash_v2_5", 50.0), ("elevenlabs", "multilingual_v2", 100.0)]
    for name, model, per_m in rows:
        if name == prov["type"] and name == "elevenlabs":
            model = prov.get("model") or model
            per_m = ELEVENLABS_MODEL_COST.get(model, per_m)
        mark = "  <- canal" if name == prov["type"] else ""
        print(f"{name:12s} {model:28s} ${chars/1e6*per_m:8.2f}{mark}")
    print("\n(estimativa por lista; cache evita pagar bloco repetido; plano mensal pode sair mais barato)")


def cmd_test(args, cfg, prov, blocks, outdir):
    text = " ".join((args.text or " ".join(blocks)).split()[:200])
    words = len(text.split())
    series = series_of(str(Path(outdir).parent), cfg)
    step, pr = provider_params(prov, text, 0, 99, cfg, series)
    ext = PROVIDER_META[step["type"]]["ext"]
    out = os.path.join(outdir, f"_teste_voz.{ext}")
    if PROVIDER_META[step["type"]]["key"]:
        keys = keys_for(step, args.root)
        if not keys:
            raise SystemExit(f"[ERRO] teste com '{step['type']}' exige chave (env {step.get('api_key_env') or DEFAULT_ENV.get(step['type'])})")
        step["_ring"] = KeyRing(keys, step["type"])
    print(f"teste de voz: {words} palavras | provider {step['type']} | voz {step.get('voice_id')} | rate {pr.get('rate')}")
    synth(step, normalize_text(text, cfg), out, args.root)
    print(f"TESTE OK: {out} ({dur(out):.1f}s) - ouca antes de gerar o video")


def main():
    ap = argparse.ArgumentParser(description="Motor de voz provider-agnostico (free + pago)")
    ap.add_argument("video", nargs="?", default=None, help="videoNN")
    ap.add_argument("--root", default=os.getcwd(), help="raiz do projeto do canal")
    ap.add_argument("--channel", help="playbook do canal (nome em playbooks/ ou pasta)")
    ap.add_argument("--provider", choices=list(PROVIDERS), help="sobrepoe o provider do contrato")
    ap.add_argument("--voice", help="sobrepoe a voz do contrato")
    ap.add_argument("--text", help="texto para --test (default: inicio da narracao)")
    ap.add_argument("--bed", help="arquivo de musica para mixar com ducking")
    ap.add_argument("--bed-vol", type=float, help="volume do bed (default 0.08)")
    ap.add_argument("--no-cache", action="store_true", help="ignora cache e regenera")
    ap.add_argument("--dry-run", action="store_true", help="mostra o plano sem gerar")
    ap.add_argument("--test", action="store_true", help="teste de 200 palavras no provider real")
    ap.add_argument("--estimate", action="store_true", help="custo estimado por provider")
    ap.add_argument("--list", action="store_true", help="lista providers e vozes curadas")
    ap.add_argument("--lang", help="filtro de idioma no --list (ex. en, pt)")
    args = ap.parse_args()

    if args.list:
        cmd_list(args)
        return

    cfg, source = load_voice_cfg(args.channel, args.root)
    if not cfg:
        print("[AVISO] sem contrato de voz (--channel ou canal.json na raiz).")
    prov = normalize_provider(cfg, args)
    if not prov.get("voice_id"):
        raise SystemExit(
            "[ERRO] nenhuma voz definida. Passe --voice <id> ou configure provider.voice_id "
            f"no playbook do canal. Sugestoes: python {os.path.basename(__file__)} --list --lang en")
    if source:
        print(f"contrato: {source}")

    vdir = None
    if args.video:
        vdir = args.video if os.path.isabs(args.video) else os.path.join(args.root, args.video)
        narr = next((os.path.join(vdir, "01_roteiro", f) for f in
                     ("narration_v3.txt", "narration.txt", "narration_pt.txt")
                     if os.path.exists(os.path.join(vdir, "01_roteiro", f))), None)
        if not narr:
            raise SystemExit(f"[ERRO] sem narracao em {vdir}/01_roteiro/ (narration_v3.txt)")
        blocks = read_blocks(narr)
        outdir = os.path.join(vdir, "02_audio")
        os.makedirs(outdir, exist_ok=True)
    else:
        if not (args.estimate or args.test):
            raise SystemExit("Uso: voice_engine.py videoNN --root <canal> [--channel <canal>] | --list | --estimate")
        blocks = [args.text] if args.text else ["Texto de teste."]
        outdir = os.path.join(args.root, "02_audio")
        os.makedirs(outdir, exist_ok=True)

    print(f"voz: {prov.get('voice_id')} | provider: {prov['type']} | blocos: {len(blocks)}")

    if args.estimate:
        cmd_estimate(args, cfg, blocks, prov)
        return
    if args.test:
        cmd_test(args, cfg, prov, blocks, outdir)
        return

    voice_pipeline(args, cfg, prov, blocks, narr, vdir, outdir)


if __name__ == "__main__":
    main()
