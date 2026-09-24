#!/usr/bin/env python3
"""script_builder.py — gera o PLANO de roteiro e valida a estrutura/orcamento.

Gera um blueprint (ROTEIRO_PLANO.md) com beats, orcamento de palavras, guias e
checklist de fatos — e cria/limpa o narration_v3.txt (TTS-safe, sem marcadores).

Uso:
  python scripts/script_builder.py --genre truecrime --porte padrao \
      --case "Hoffa" --date 1975 --place Detroit --sources "FBI vault; DOJ" \
      --out "<videoNN>/01_roteiro"

  python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_v3.txt" --porte padrao

  # canal com formato proprio (le playbooks/<canal>/roteiro.json):
  python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_pt.txt" \
      --channel laudo-final --genre forense

O roteiro (narration) fica SEM marcadores (o TTS nao fala nada alem da narracao).
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

PORTE = {
    "fino":   (1900, 2400),
    "padrao": (2900, 3300),
    "rico":   (3400, 3800),
    "30-35":  (4200, 5600),
    "45-60":  (6300, 9600),
    "60-70":  (8400, 11200),
}

PLAYBOOKS = Path(os.environ.get(
    "DARK_MASTER_PLAYBOOKS",
    str(Path.home() / ".config" / "opencode" / "skills" / "dark-master" / "playbooks")))


def channel_roteiro(channel, porte=None):
    """Le playbooks/<canal>/roteiro.json -> (label, (lo, hi)) ou None (com AVISO).
    Aceita 'palavras': [lo, hi] (formato unico, ex. Laudo ~10min) ou
    'portes': {fino/padrao/rico: [lo, hi]} + 'porte_default' (ex. CFD).
    Canal com formato proprio nao deve ser medido pelo porte generico da skill."""
    p = Path(channel).expanduser()
    pb = p if p.is_dir() else PLAYBOOKS / channel
    if not pb.is_dir():
        print(f"[AVISO] canal '{channel}' nao encontrado em {PLAYBOOKS} - usando porte generico da skill.")
        return None
    f = pb / "roteiro.json"
    if not f.exists():
        print(f"[AVISO] {f} ausente - usando porte generico da skill (crie o roteiro.json do canal).")
        return None
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except ValueError as e:
        print(f"[AVISO] roteiro.json invalido ({e}) - usando porte generico.")
        return None
    dur = d.get("duracao_min")
    portes = d.get("portes")
    if isinstance(portes, dict) and portes:
        use = porte if porte in portes else d.get("porte_default") or next(iter(portes))
        pw = portes.get(use)
        if not (isinstance(pw, list) and len(pw) == 2):
            print(f"[AVISO] roteiro.json: portes['{use}'] invalido - usando porte generico.")
            return None
        return f"canal:{pb.name} {use}" + (f" ~{dur}min" if dur else ""), (int(pw[0]), int(pw[1]))
    pw = d.get("palavras")
    if not (isinstance(pw, list) and len(pw) == 2):
        print("[AVISO] roteiro.json sem 'palavras': [lo, hi] - usando porte generico.")
        return None
    return f"canal:{pb.name}" + (f" ~{dur}min" if dur else ""), (int(pw[0]), int(pw[1]))

# genero -> lista (beat, proporcao, guia)
GENRES = {
    "generic": [
        ("COLD OPEN", 0.07, "cena/promessa que prende; sem intro"),
        ("CONTEXTO", 0.18, "o que o espectador precisa saber; stakes"),
        ("DESENVOLVIMENTO", 0.30, "o miolo; revelacoes em sequencia; sem momentos mortos"),
        ("VIRADA", 0.20, "a complicacao/revelacao que muda tudo"),
        ("CONSEQUENCIA", 0.17, "o que aquilo significa; impacto"),
        ("FECHAMENTO+TEASER", 0.08, "resposta + implicacao + gancho do proximo"),
    ],
    "truecrime": [
        ("HOOK", 0.04, "detalhe mais estranho VERIFICADO (nao o crime); pergunta que prende"),
        ("CONTEXTO", 0.16, "quem sao as pessoas, onde, quando; humaniza; mapa da rotina"),
        ("PRESSAO", 0.13, "os pesos antes do fato (brigas, dividas, telefonemas)"),
        ("O DIA", 0.22, "cronologia minuto a minuto; frases curtas; beats de 1 linha"),
        ("INVESTIGACAO", 0.19, "o que a policia fez/falhou; pistas fisicas; ciencia simples"),
        ("FAMILIA", 0.09, "quem luta pelo caso; respeito maximo"),
        ("TEORIAS", 0.13, "ate 3 teorias, pros e contras, sem afirmar"),
        ("CHAVES+OUTRO+TEASER", 0.04, "o que resolveria + CTA + teaser do proximo"),
    ],
    "darkhistory": [
        ("COLD OPEN", 0.08, "cena no presente, personagem/tempo/lugar; stakes antes do contexto"),
        ("CONTEXTO", 0.18, "o mundo da epoca; quem sao os personagens"),
        ("O MUNDO", 0.22, "como aquilo funcionava; tensao crescendo"),
        ("A VIRADA", 0.22, "o ponto sem volta; a revelacao"),
        ("CONSEQUENCIAS", 0.18, "o que mudou; o custo humano"),
        ("ARQUIVO", 0.08, "o que sabemos e o que nunca saberemos"),
        ("OUTRO+TEASER", 0.04, "implicacao que fica + proximo capitulo"),
    ],
    "financial": [
        ("COLD OPEN", 0.06, "abrir com um documento/numero que nao devia existir"),
        ("O ESQUEMA", 0.16, "como o dinheiro deveria fluir e onde quebrou"),
        ("OS PERSONAGENS", 0.16, "quem eram; o mundo em que operavam"),
        ("A ASCENSAO", 0.20, "como cresceu; sinais ignorados"),
        ("A QUEDA", 0.22, "o colapso; os numeros"),
        ("O DINHEIRO", 0.12, "onde foi parar; quem pagou"),
        ("LEGADO", 0.04, "o que sobrou; impacto"),
        ("OUTRO+TEASER", 0.04, "o proximo caso"),
    ],
    "forense": [
        ("HOOK", 0.04, "fato estranho do LAUDO; sem crime; pergunta verificavel"),
        ("VIDA_E_CONTEXTO", 0.13, "origem, familia, rotina e contexto que mudam a investigacao"),
        ("DESCOBERTA", 0.10, "primeira notificacao, horario, lugar, acao e reacoes"),
        ("LINHA_DO_TEMPO", 0.16, "antecedentes e sequencia do caso com datas e saltos marcados"),
        ("EVIDENCIAS", 0.24, "cadeia evidencia -> significado -> hipotese -> duvida"),
        ("PERICIA", 0.17, "exames, documentos e limites do que cada prova consegue mostrar"),
        ("CONTRADICAO", 0.07, "divergencia que muda a interpretacao ou enfraquece uma certeza"),
        ("RECONSTRUCAO", 0.05, "sequencia minima com graus de certeza"),
        ("CONFIRMADO_DESCONHECIDO", 0.04, "o que sabemos, o que nao sabemos e a ultima pergunta"),
    ],
    "short": [
        ("HOOK", 0.12, "frame 1 + fala <=8 palavras (0-3s): impossibilidade/pergunta/contradicao"),
        ("DESENVOLVIMENTO", 0.50, "1 ideia em progressao; micro-payoffs; mudanca visual 1,5-2s"),
        ("PAYOFF", 0.26, "entrega o que o hook prometeu; antes dos ultimos 2s"),
        ("LOOP", 0.12, "fim emenda no comeco (visual + sonoro); loop aberto"),
    ],
}

# porte de Short (palavras) — narracao ~2,5 palavras/segundo
PORTE_SHORT = {
    "13s": (28, 45),
    "25s": (48, 75),
    "45s": (90, 125),
}

META = [r"\bthis channel\b", r"\besse canal\b", r"\bin this video\b", r"\bnesse v[íi]deo\b",
        r"\bwatch the short\b", r"\bassista o short\b", r"\bsubscribe\b.*\bnow\b"]
GORE = [r"\bblood\b", r"\bsangue\b", r"\bgore\b", r"\bcorpse\b", r"\bdead body\b",
        r"\bintestin\w*\b", r"\bdismember\w*\b", r"\bmutilat\w*\b"]
TEASER = [r"\btomorrow\b", r"\bnext case\b", r"\bnext file\b", r"\bcoming next\b", r"\bnext week\b",
          r"\bnext episode\b", r"\bamanh[ãa]\b", r"\bsemana que vem\b", r"\bpr[óo]xima semana\b",
          r"\bpr[óo]xim[ao] (caso|epis[óo]dio|arquivo|laudo)\b"]
CLOSING = [r"\bpermanece\b", r"\bcontinua\b", r"\bnão (?:sabemos|foi poss[ií]vel|segue)\b",
           r"\bno que (?:sabemos|resta)\b", r"\bsem resposta\b", r"\bthe question remains\b",
           r"\bremains? (?:open|unanswered)\b"]
ALLEGED = [r"\balleged\b", r"\bsuspect\b", r"\baccused\b", r"\bsuspeit\w*\b", r"\bacusad\w*\b"]

# banco de arquetipos de hook (references/31) — {case} = caso/tema
HOOK_ARCHETYPES = {
    "1":  ("Impossibilidade", ["The {case} was locked from the inside.",
                               "The {case} could not have happened. It did."],
           ["O caso {case} estava trancado por dentro.", "O {case} nao podia ter acontecido. Aconteceu."]),
    "2":  ("Pergunta 2a pessoa", ["Would you do it for {case}?",
                                  "What would you do if {case} was the last thing you heard?"],
           ["Voce faria isso por {case}?", "O que voce faria se {case} fosse a ultima coisa que ouvisse?"]),
    "3":  ("Contradicao verificada", ["The report said one thing. {case} said another.",
                                      "Everyone believed {case}. The file says otherwise."],
           ["O laudo dizia uma coisa. {case} dizia outra.", "Todos acreditaram em {case}. O arquivo diz o contrario."]),
    "4":  ("Numero + stake", ["{case}. Three numbers that never add up.",
                              "One {case}. Zero answers."],
           ["{case}. Tres numeros que nunca fecham.", "Um {case}. Zero respostas."]),
    "5":  ("Relogio", ["{case} took 81 minutes. The search took 40 years.",
                       "It was over in minutes. {case} is still open."],
           ["{case} levou 81 minutos. A busca levou 40 anos.", "Acabou em minutos. {case} continua aberto."]),
    "6":  ("Antes/depois impossivel", ["This was taken two hours after {case}.",
                                       "The photo of {case} should not exist."],
           ["Esta foto e de duas horas depois de {case}.", "A foto de {case} nao deveria existir."]),
    "7":  ("Objeto-simbolo", ["All they found of {case} was one shoe.",
                             "One object is all that is left of {case}."],
           ["So acharam um sapato de {case}.", "Um objeto e tudo o que restou de {case}."]),
    "8":  ("Citacao/dialogo", ["'Help is coming,' they said. Then {case}.",
                               "One sentence explains {case}. Nobody listened."],
           ["'A ajuda vem', disseram. Entao {case}.", "Uma frase explica {case}. Ninguem ouviu."]),
    "9":  ("POV/imersao", ["You are the last person who saw {case}.",
                           "You have 30 seconds to understand {case}."],
           ["Voce e a ultima pessoa que viu {case}.", "Voce tem 30 segundos para entender {case}."]),
    "10": ("Segredo/proibido", ["The file on {case} was sealed for 60 years.",
                                "This part of {case} was never released."],
           ["O arquivo de {case} ficou selado por 60 anos.", "Esta parte de {case} nunca foi divulgada."]),
    "11": ("Loop declarado", ["Watch the corner of the frame. {case} is still there.",
                              "Remember this detail. It explains {case}."],
           ["Olhe o canto do quadro. {case} ainda esta la.", "Lembre deste detalhe. Ele explica {case}."]),
    "12": ("Erro sistemico", ["They searched the wrong place for 40 years. {case} knew.",
                              "{case} was never a mystery. It was an error."],
           ["Procuraram no lugar errado por 40 anos. {case} sabia.", "{case} nunca foi misterio. Foi um erro."]),
    "13": ("Micro-historia", ["At 9:00, {case} left. At 9:04, the last call. No answer.",
                              "Three sentences. That is all {case} left behind."],
           ["As 9h, {case} saiu. As 9h04, a ultima ligacao. Sem resposta.",
            "Tres frases. E tudo o que {case} deixou."]),
    "14": ("Escolha impossivel", ["Save the evidence or save the witness. {case} chose.",
                                  "One choice. That is what {case} came down to."],
           ["Salvar a prova ou salvar a testemunha. {case} escolheu.", "Uma escolha. Foi a que {case} se resumiu."]),
}


def words(t):
    return len(re.findall(r"\w+", t, flags=re.UNICODE))


def minutes_window(value):
    match = re.fullmatch(r"(\d{1,3})(?:-(\d{1,3}))?", (value or "").strip())
    if not match:
        raise ValueError("target-minutes deve ser 30 ou 30-35")
    first = int(match.group(1))
    last = int(match.group(2) or first)
    if first < 1 or last < first or last > 180:
        raise ValueError("target-minutes fora do intervalo")
    return int(first * 140), int(last * 160)


def load_claims(path):
    if not path:
        return [], "claims_path_missing"
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [], f"claims_invalid:{exc}"
    claims = data.get("claims", []) if isinstance(data, dict) else data
    if not isinstance(claims, list) or not claims:
        return [], "claims_empty"
    return claims, ""


def validate_claims(claims):
    errors = []
    ids = set()
    for index, claim in enumerate(claims, 1):
        if not isinstance(claim, dict):
            errors.append(f"claim_{index}:invalid")
            continue
        claim_id = str(claim.get("id", "")).strip()
        if not claim_id:
            errors.append(f"claim_{index}:missing_id")
        elif claim_id in ids:
            errors.append(f"claim_{claim_id}:duplicate_id")
        ids.add(claim_id)
        if not str(claim.get("text", "")).strip():
            errors.append(f"claim_{claim_id or index}:missing_text")
        if str(claim.get("layer", "")).upper() not in {"FATO", "REPORTADO", "LENDA", "HIPOTESE", "INTERPRETACAO"}:
            errors.append(f"claim_{claim_id or index}:invalid_layer")
        sources = claim.get("source_ids")
        if str(claim.get("layer", "")).upper() not in {"LENDA", "HIPOTESE"} and (not isinstance(sources, list) or not sources):
            errors.append(f"claim_{claim_id or index}:missing_sources")
    return errors


def timeline_events(path):
    if not path:
        return [], "timeline_path_missing"
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [], f"timeline_invalid:{exc}"
    events = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in {"data", "date", "---"} or set(cells[0]) <= set("-: "):
            continue
        if cells[0] not in {"?", "-"} and not re.match(r"^(?:\d{4}|\d{1,2}/\d{1,2}/\d{2,4})", cells[0]):
            continue
        events.append(cells)
    return events, "" if events else "timeline_empty"


def validate_source_ledger(path, claims):
    if not path or not Path(path).exists():
        return ["source_ledger_missing"]
    text = Path(path).read_text(encoding="utf-8")
    rows = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and re.fullmatch(r"S\d+", cells[0]):
            rows[cells[0]] = cells
    errors = []
    for claim in claims if isinstance(claims, list) else []:
        for source_id in claim.get("source_ids", []) if isinstance(claim, dict) else []:
            cells = rows.get(str(source_id))
            if not cells:
                errors.append(f"source_missing:{source_id}")
            elif sum(bool(cell) for cell in cells[1:]) < 2:
                errors.append(f"source_incomplete:{source_id}")
    return errors


def build_short_funnel(meta):
    case = meta.get("case", "(caso)")
    return "\n".join([
        f"# PLANO DE SHORT — {case}",
        f"# Long relacionado: {meta.get('target_long', 'videoNN')}",
        "",
        "## Contrato",
        "- Objetivo: acquire cold viewers and create a reason to open the long.",
        "- Use one verified claim only; do not retell the entire long.",
        "- Fala: starts by 0.5s; <=8 words in first 3s.",
        "- Texto na tela: <=6 words; frame 1 shows the object, contradiction or result.",
        "- Loop: visual, sonic and semantic handoff are explicit.",
        "- CTA: only in pinned comment/related video when it would break the loop.",
        "",
        "## Roteiro",
        "HOOK — visual frame 1: ",
        "HOOK — text on screen: ",
        "HOOK — speech: ",
        "SETUP — one sentence: ",
        "EVIDENCE — verified fact: ",
        "TURN — what changes the interpretation: ",
        "PAYOFF — what the viewer learns: ",
        "BRIDGE — why the long is necessary: ",
        "LOOP — first frame repeats: ",
        "LOOP — last sound repeats: ",
        "CTA — pinned comment/related video: ",
        "",
        "## Claims",
        "- Claim IDs used: ",
        "- Long beat supported: ",
        "- Forbidden: invented dialogue, invented evidence, generic fear language.",
    ]) + "\n"


def validate_funnel_plan(path):
    errors = []
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        return [f"short_funnel_plan_missing:{exc}"]
    required = [
        "Frame 1 visual:", "Texto na tela:", "Fala inicial:", "Promessa do Short:",
        "Payoff:", "Ponte:", "Emenda visual:", "Emenda sonora:", "Loop semântico:",
        "Comentário fixado:", "Related Video:"
    ]
    values = {}
    for label in required:
        match = re.search(r"(?mi)^-\s*" + re.escape(label) + r"\s*(.*)$", text)
        value = (match.group(1).strip() if match else "")
        if not value:
            errors.append(f"funnel_missing:{label}")
        values[label] = value
    screen = values.get("Texto na tela:", "")
    spoken = values.get("Fala inicial:", "")
    if screen and words(screen) > 6:
        errors.append(f"funnel_screen_text_longo({words(screen)}>6)")
    if spoken and words(spoken) > 8:
        errors.append(f"funnel_speech_hook_longo({words(spoken)}>8)")
    return errors


def build_plan(genre, porte, meta, window=None):
    lo, hi = window or PORTE[porte]
    mid = (lo + hi) / 2
    g = GENRES[genre]
    lines = [
        f"# PLANO DE ROTEIRO — {meta.get('case','(caso)')}",
        f"# Genero: {genre} | Porte: {porte} ({lo}-{hi} palavras, alvo ~{int(mid)})",
        f"# Data: {meta.get('date','')} | Local: {meta.get('place','')}",
        f"# Fontes: {meta.get('sources','')}",
        f"# Pergunta central: {meta.get('question','(definir)')}",
        "",
        "# Escreva o narration_v3.txt SEM marcadores (o TTS le so a narracao).",
        "# Use este plano para bater o orcamento por beat e a ordem.",
        "",
    ]
    acc = 0
    for beat, prop, guide in g:
        w = int(mid * prop)
        acc += w
        lines.append(f"[{beat}] ~{w} palavras — {guide}")
    lines += [
        "",
        f"# TOTAL alvo: ~{int(mid)} palavras (faixa {lo}-{hi}).",
    ]
    if genre == "short":
        lines += [
            "",
            "# CHECKLIST DE SHORT (references/31):",
            "# - Frame 1: payoff/tensao VISIVEL + texto na tela (<=6 palavras).",
            "# - Fala comeca <=0,5s; hook <=8 palavras nos primeiros 3s.",
            "# - 1 ideia so; payoff antes dos ultimos 2s.",
            "# - LOOP: fim emenda no comeco (visual + sonoro); loop aberto.",
            "# - Sem abstracao, sem data/local antes do gancho, sem meta-linguagem.",
            "# - CTA so no comentario fixado / Related Video (nao quebrar o loop).",
        ]
    lines += [
        "",
        "# PESQUISA OBRIGATORIA (preencher antes de escrever):",
        "# - CLAIMS.json: cada fato material com id, layer, source_ids e texto.",
        "# - PESQUISA_BRIEF.md: pergunta central, lacunas, contradicoes e fonte primaria.",
        "# - LINHA_DO_TEMPO.md: eventos completos relevantes, incluindo biografia e contexto.",
        "# - Toda data nova entra na tabela antes da narracao.",
        "# - FATO, REPORTADO, LENDA, HIPOTESE e INTERPRETACAO nunca sao misturados.",
    ]
    if meta.get("target_long"):
        lines += [
            "",
            f"# SHORT DE AQUISICAO: {meta.get('target_long')}",
            "# O Short deve abrir uma porta para o long, sem repetir a abertura nem revelar o payoff completo.",
            "# Anexe o plano em ROTEIRO_SHORT_PLANO.md e valide-o separadamente.",
        ]
    lines += [
        "",
        "# CHECKLIST DE FATOS (preencher antes de gerar voz):",
        "# - Vitimas (nomes/idades):",
        "# - Data:              Local:",
        "# - Fontes (2+):",
        "# - Suspeito vivo? (se sim -> alleged):",
        "# - Lendas a evitar:",
        "# - Divulgacao de IA: (no pacote de publicacao)",
    ]
    return "\n".join(lines) + "\n"


def validate(narration_path, porte, genre, window=None, claims_path=None,
             timeline_path=None, funnel_plan=None, strict=False):
    narration_path = Path(narration_path)
    txt = narration_path.read_text(encoding="utf-8", errors="replace")
    body = "\n".join(l for l in txt.splitlines() if not l.strip().startswith("#"))
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    total = words(body)
    lo, hi = window or PORTE[porte]
    flags = []
    if not paras:
        flags.append("vazio")
    if total < lo:
        flags.append(f"curto({total}<{lo})")
    elif total > hi:
        flags.append(f"longo({total}>{hi})")
    if genre == "short":
        if paras and words(paras[0]) > 8:
            flags.append(f"hook_short_longo({words(paras[0])}>8)")
        if len(paras) > 4:
            flags.append(f"muitos_blocos({len(paras)}>4)_1_ideia")
        if len(paras) >= 2:
            stop = {"the", "a", "o", "e", "de", "do", "da", "que", "and", "of", "to",
                    "in", "it", "was", "is", "um", "uma", "os", "as", "no", "na"}
            w1 = {w.lower() for w in re.findall(r"\w+", paras[0]) if w.lower() not in stop}
            w2 = {w.lower() for w in re.findall(r"\w+", paras[-1]) if w.lower() not in stop}
            if not (w1 & w2):
                flags.append("loop_nao_detectado(verificar emenda)")
    elif paras and words(paras[0]) > 160:
        flags.append(f"hook_longo({words(paras[0])})")
    low = txt.lower()
    meta_hits = [p for p in META if re.search(p, low)]
    gore_hits = [p for p in GORE if re.search(p, low)]
    tail = low[-max(400, len(low) // 4):]
    has_teaser = any(re.search(p, tail) for p in TEASER)
    has_closing = has_teaser or any(re.search(p, tail) for p in CLOSING)
    has_alleged = any(re.search(p, low) for p in ALLEGED)
    if meta_hits:
        flags.append(f"meta_linguagem({len(meta_hits)})")
    gore_advisory = genre in ("truecrime", "forense")
    if gore_hits and not gore_advisory:
        flags.append(f"gore({len(gore_hits)})")
    if genre != "short" and not has_closing:
        flags.append("sem_payoff_ou_teaser_final")
    if strict:
        brief_file = narration_path.parent / "PESQUISA_BRIEF.md"
        source_file = narration_path.parent / "PESQUISA_FONTE.md"
        if not brief_file.exists() or len(brief_file.read_text(encoding="utf-8").strip()) <= 120:
            flags.append("research_brief_missing")
        if not source_file.exists() or len(source_file.read_text(encoding="utf-8").strip()) <= 120:
            flags.append("source_ledger_missing")
        claims_file = Path(claims_path) if claims_path else narration_path.parent / "CLAIMS.json"
        claims, claims_error = load_claims(claims_file)
        if claims_error:
            flags.append(claims_error)
        else:
            flags.extend(validate_claims(claims))
            flags.extend(validate_source_ledger(source_file, claims))
        if genre in {"forense", "truecrime", "darkhistory", "financial"}:
            timeline_file = Path(timeline_path) if timeline_path else narration_path.parent / "LINHA_DO_TEMPO.md"
            events, timeline_error = timeline_events(timeline_file)
            real_events = [event for event in events
                           if len(event) >= 3
                           and event[1]
                           and "preencher" not in event[1].lower()]
            minimum = 3
            if genre == "forense":
                if lo >= 8400:
                    minimum = 15
                elif lo >= 6300:
                    minimum = 12
                elif lo >= 4000:
                    minimum = 8
            if timeline_error:
                flags.append(timeline_error)
            elif len(real_events) < minimum:
                flags.append(f"timeline_insuficiente({len(real_events)}<{minimum})")
        if funnel_plan:
            funnel_file = Path(funnel_plan)
            if not funnel_file.exists() or not funnel_file.read_text(encoding="utf-8").strip():
                flags.append("short_funnel_plan_missing")
            else:
                flags.extend(validate_funnel_plan(funnel_file))
    if not has_alleged:
        print("[advisory] nao encontrei suspeito/acusado/alegado; confirme se existe pessoa viva.")
    print(f"# Validacao de roteiro — {Path(narration_path).name}\n")
    print(f"  genero: {genre} | porte: {porte} ({lo}-{hi})")
    print(f"  paragrafos: {len(paras)} | palavras: {total}")
    if paras:
        print(f"  1o bloco (hook): {words(paras[0])} palavras")
    print(f"  fechamento no fim: {'sim' if has_closing else 'NAO'}")
    print(f"  research gate: {'PASS' if strict else 'ADVISORY'}")
    if gore_hits and gore_advisory:
        print(f"  [advisory] termos sensiveis do genero: {len(gore_hits)} (revisar gore real, nao a palavra)")
    print(f"\nRESULTADO: {'PASSOU' if not flags else 'FALHA'} {', '.join(flags)}")
    return not flags


def load_beats(path):
    """Carrega generos customizados de um JSON: {genero: [[beat, prop, guia], ...]}"""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:  # noqa
        print(f"[!] beats-file invalido: {e}"); return
    for g, beats in data.items():
        GENRES[g] = [(b[0], float(b[1]), b[2] if len(b) > 2 else "") for b in beats]
    print(f"[i] generos carregados: {', '.join(data.keys())}")


def gen_hooks(n, case, archetypes, lang):
    """Gera N variacoes de hook a partir do banco de arquetipos (references/31)."""
    keys = [k.strip() for k in (archetypes or "").split(",") if k.strip() in HOOK_ARCHETYPES]
    if not keys:
        keys = list(HOOK_ARCHETYPES)
    case = case or "the case"
    print(f"# {n} variacoes de hook — caso: {case} ({lang})\n")
    out = []
    i = 0
    while len(out) < n:
        k = keys[i % len(keys)]
        name, ens, pts = HOOK_ARCHETYPES[k]
        bank = ens if lang == "en" else pts
        tpl = bank[(i // len(keys)) % len(bank)]
        out.append((k, name, tpl.format(case=case)))
        i += 1
    for idx, (k, name, h) in enumerate(out, 1):
        print(f"{idx:>2}. [{k} {name}] {h}")
    print("\nLembrete: teste 1 variavel por vez; o arquetipo importa mais que a frase (references/31).")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--genre", default=None)
    ap.add_argument("--beats-file", help="JSON com generos customizados")
    ap.add_argument("--list-genres", action="store_true")
    ap.add_argument("--short", action="store_true", help="modo Short (porte 13s/25s/45s)")
    ap.add_argument("--porte", default=None, choices=list(PORTE) + list(PORTE_SHORT))
    ap.add_argument("--target-minutes", help="faixa de duracao, ex.: 30-35")
    ap.add_argument("--funnel", action="store_true", help="gera plano do Short de aquisicao junto ao long")
    ap.add_argument("--target-long", default="", help="identificador do long que o Short deve levar ate")
    ap.add_argument("--case", default="")
    ap.add_argument("--date", default="")
    ap.add_argument("--place", default="")
    ap.add_argument("--sources", default="")
    ap.add_argument("--question", default="")
    ap.add_argument("--out", help="pasta 01_roteiro (gera ROTEIRO_PLANO.md)")
    ap.add_argument("--validate", help="valida um narration existente")
    ap.add_argument("--claims", help="manifesto JSON de claims")
    ap.add_argument("--timeline", help="LINHA_DO_TEMPO.md")
    ap.add_argument("--funnel-plan", help="plano estruturado do Short")
    ap.add_argument("--strict", action="store_true", help="exige pesquisa, claims e linha do tempo")
    ap.add_argument("--channel", help="playbook do canal: le roteiro.json (porte proprio do canal)")
    ap.add_argument("--hooks", type=int, help="gera N variacoes de hook (references/31)")
    ap.add_argument("--archetypes", help="arquetipos do banco, ex.: 1,3,4,5")
    ap.add_argument("--lang", default="en", choices=["en", "pt"])
    a = ap.parse_args()

    if a.beats_file:
        load_beats(a.beats_file)
    if a.list_genres:
        for g in GENRES:
            print(g)
        return
    if a.hooks:
        gen_hooks(a.hooks, a.case, a.archetypes, a.lang)
        return

    is_short = a.short or a.genre == "short"
    genre = a.genre or ("short" if is_short else "generic")
    if genre not in GENRES:
        print(f"[!] genero desconhecido: {genre}. Use --list-genres ou --beats-file.")
        sys.exit(2)
    if a.funnel and is_short:
        print("[!] --funnel pertence ao plano long; use --genre short separadamente.")
        sys.exit(2)
    if is_short:
        porte = a.porte or "25s"
        if porte not in PORTE_SHORT:
            print(f"[!] porte de Short invalido: {porte}. Use 13s | 25s | 45s.")
            sys.exit(2)
        window = PORTE_SHORT[porte]
    elif a.target_minutes:
        try:
            window = minutes_window(a.target_minutes)
        except ValueError as exc:
            print(f"[!] {exc}")
            sys.exit(2)
        porte = f"custom {a.target_minutes}min"
    else:
        cr = channel_roteiro(a.channel, a.porte) if a.channel else None
        if cr:
            porte, window = cr
        else:
            porte = a.porte or "padrao"
            if porte not in PORTE:
                print(f"[!] porte de long-form invalido: {porte}. Use fino | padrao | rico | 30-35 | 45-60 | 60-70.")
                sys.exit(2)
            window = PORTE[porte]

    if a.validate:
        ok = validate(a.validate, porte, genre, window, a.claims, a.timeline, a.funnel_plan, a.strict)
        sys.exit(0 if ok else 1)

    if not a.out:
        print("Informe --out <pasta 01_roteiro> ou --validate <arquivo>")
        sys.exit(2)
    out = Path(a.out).expanduser()
    if out.name.lower().startswith("video") or re.match(r"^EP", out.name):
        out = out / "01_roteiro"
    out.mkdir(parents=True, exist_ok=True)

    plan = out / "ROTEIRO_PLANO.md"
    plan.write_text(build_plan(genre, porte, a.__dict__, window), encoding="utf-8")
    nar_name = "narration_short.txt" if is_short else "narration_v3.txt"
    nar = out / nar_name
    if not nar.exists():
        nar.write_text("", encoding="utf-8")
    if a.funnel:
        short_plan = out / "ROTEIRO_SHORT_PLANO.md"
        short_plan.write_text(build_short_funnel(a.__dict__), encoding="utf-8")
        short_narration = out / "narration_short.txt"
        if not short_narration.exists():
            short_narration.write_text("", encoding="utf-8")
        print(f"[OK] plano Short: {short_plan}")
        print(f"[OK] roteiro Short: {short_narration}")

    print(f"[OK] plano: {plan}")
    print(f"[OK] roteiro: {nar} (escreva a narracao aqui, sem marcadores)")
    print("\nProximo: escreva bloco a bloco e rode:")
    short_flag = " --short" if is_short else ""
    strict_flag = " --strict" if a.strict else ""
    if a.channel and not is_short:
        print(f'  python scripts/script_builder.py --validate "{nar}" --channel {a.channel} --genre {genre}{strict_flag}')
    else:
        target_flag = f' --target-minutes {a.target_minutes}' if a.target_minutes else f' --porte {porte}'
        print(f'  python scripts/script_builder.py --validate "{nar}"{target_flag} --genre {genre}{short_flag}{strict_flag}')


if __name__ == "__main__":
    main()
