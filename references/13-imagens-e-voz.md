# 13 — Imagens e voz

Backends padronizados: **Nano Banana manual + Pollinations (fallback)** para imagem; motor de voz **provider-agnóstico** (`scripts/voice_engine.py`) — edge/kokoro/piper (grátis) e Azure/ElevenLabs/Fish/Gemini/OpenAI (pago). Guia completo: **`34-voz-tts.md`**.

## Imagem

### Nano Banana (padrão, manual)
- O usuário escreve prompts por cena num `03_imagens/PROMPTS.md` e gera externamente, revisando cada imagem.
- Vantagem: controle artístico + evita "cara de IA genérica" (importante p/ anti-inauthentic).
- Regra: **GATE 100%** — todas as imagens antes de gerar voz.

Estilo por canal (prefixo travado):
- **Cold File Diaries / Laudo Final:** dark cinematic forensic illustration, desaturated cold tones, deep blacks, subtle red accent, volumetric fog, 16:9, no text, no watermark, no blood, no gore, no real face, silhouettes from behind.
- **Financial Crime Files:** photorealistic documentary reconstruction, natural proportions, plausible lighting, no teal-orange, no lens flare, documentary photo language.
- **Midnight Archive:** arte procedural (código) + Wikimedia Commons PD/CC.

### Pollinations (fallback gratuito, automatizável)
```
https://image.pollinations.ai/prompt/{prompt_urlencoded}?width=1920&height=1080&nologo=true&model=flux
```
- Escreva só se `len(bytes) > 10000` (buffer até completar).
- Use para testes/volume quando não quiser gastar Nano Banana.

### QA de imagem
- Gerar **1 imagem teste** e aprovar o estilo antes de gerar todas.
- Auditar: ≥1280px, aspecto 1.70–1.85, ≥50KB, sem rosto real/gore/texto legível.
- Montar contact sheet para revisão humana.

### Auditoria automática de imagens (`image_audit.py`)

```bash
python scripts/image_audit.py "<videoNN>/03_imagens" --sheet --hash
```

Checa por imagem: **resolução**, **aspecto** (16:9), **tamanho de arquivo**, **brilho/desvio** (detecta imagem quase sólida = geração falhada), **saturação** e **duplicatas próximas** (average hash).
Gera `AUDITORIA_IMAGENS.md`, um `_contact_sheet.jpg` (revisão visual) e **sai com código 1 se houver falha**.

Flags: `baixa_res`, `aspecto`, `pequena`, `quase_solida`, `muito_escura`, `muito_clara`, `ilegivel`.

> É o **gate visual**: rode antes de gerar voz/motion (junto do GATE 100%).

## Voz

Motor unificado: `python scripts/voice_engine.py videoNN --root <canal> --channel <canal>` — lê o **contrato** (`playbooks/<canal>/voice.json` > bloco `provider`) e gera com qualquer provider. O guia completo (escolha, custos, licenças, clonagem, pronúncia, QA) está em **`34-voz-tts.md`**.

### Grátis (padrão de produção)
- **edge-tts** — 400+ vozes; documentário EN `en-US-ChristopherNeural` (-8%), investigativo `en-US-GuyNeural`; PT-BR `pt-BR-AntonioNeural`. Uso comercial é zona cinzenta [ALEGADO] — canal monetizado migra a mesma voz para **Azure** (licença comercial, mesmas vozes).
- **kokoro** (Apache 2.0, local, CPU) e **piper** (MIT nas vozes, local) — grátis e comercial-safe.

### Pago (naturalidade / clone)
- **ElevenLabs** — `eleven_multilingual_v2` long-form, `eleven_v3` expressivo, `eleven_flash_v2_5` barato; **IVC** (1min) testa, **PVC** (30min+) é a voz de marca. $0,05–0,10/1k chars.
- **Fish** — $15/1M bytes, clone 10–30s, 80+ idiomas, word timestamps. Licença comercial a partir do Plus.
- **Gemini** (30 vozes + estilo por prompt) e **OpenAI** (13 vozes + `instructions`) — baratos; chunking obrigatório (cota por request).

### Regras
- **Uma voz por canal, travada no contrato.** Canal novo define a própria — não copie de outro canal.
- Teste **200 palavras** (`--test`) antes de gerar o vídeo; `--estimate` mostra o custo antes de gastar.
- Cache por hash: bloco repetido nunca é pago 2x; fallback da cadeia **avisa** (nunca silencioso).
- Prosódia por bloco (hook/beat/outro/série) vem do contrato; pausas 0.35s/0.15s, trim, filtros e `loudnorm` (I=-16 CFD | -14 Laudo) idênticos em todos os providers.
- Legenda karaokê via faster-whisper (word timings) alinhada ao roteiro.

### Qualidade de narração (regras)
- Combine a voz com o formato: calma/medida para documentário; energia só onde cabe.
- Legenda é camada de compreensão, não conserto de fala ruim.
- Renderize 200 palavras de teste com nomes/preços/lista antes de fechar a voz.
- Voze consistente por canal (reconhecimento de marca).

## Checklist imagem/voz
- [ ] 1 imagem teste aprovada antes de lotear.
- [ ] GATE 100% (todas imagens prontas).
- [ ] Voz oficial do canal aplicada (`--channel` certo; contrato confere).
- [ ] `--test` de 200 palavras aprovado (pronúncia/ritmo) — ver `34`.
- [ ] Custo conferido (`--estimate`) e licença do provider ok para monetização (`34`).
- [ ] loudnorm no alvo do projeto.
- [ ] Captions alinhadas ao roteiro.
