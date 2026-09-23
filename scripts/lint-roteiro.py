#!/usr/bin/env python3
"""lint-roteiro.py — checagens de roteiro para canais dark (anti-IA + compliance).

Uso:
  python scripts/lint-roteiro.py caminho/para/narration_v3.txt
  python scripts/lint-roteiro.py caminho/para/narration_short.txt --short
  python scripts/lint-roteiro.py caminho/narration_pt.txt --cronologia caminho/LINHA_DO_TEMPO.md

Checa:
  - meta-linguagem banida (compliance) -> falha dura (exit 1)
  - gore/termos sensiveis -> falha dura (exit 1)
  - 25 tells de IA (references/17) + densidade por 1000 palavras
  - ritmo: aberturas de frase repetidas, travessoes em excesso
  - short: hook <= 12 palavras

Exit code: 1 apenas em falha dura (meta-linguagem/gore). Tells de IA sao advisory.
"""
import argparse
import re
import sys

BANNED = [
    r"\besse canal\b", r"\bneste canal\b", r"\bthis channel\b", r"\bassista o short\b",
    r"\bcurta e se inscreva\b", r"\bdeixe o like\b", r"\bnesse v[íi]deo\b", r"\bin this video\b",
]

AI_TELLS = {
    "not-X-but-Y": [
        r"\bn[aã]o\s+(?:[eé]|apenas|s[oó])[^.]{0,30}\bmas\b",
        r"\bn[aã]o\s+[eé]\s+s[oó][^.]{0,30}[,;]\s*[eé]\b",
        r"\bit'?s not (just|only) .{0,30},? it'?s\b",
        r"\b(is|was) not (just|only|merely) [^.]{0,40}[,;] ?(it'?s|but)\b",
    ],
    "closer de uma linha": [
        r"\bthat is the real (win|point)\b", r"\bread that again\b", r"\bleia (isso )?de novo\b",
        r"\bpense nisso\b", r"\bthink about that\b",
    ],
    "frases profundas": [
        r"\ba (verdadeira|real) quest[aã]o [eé]\b", r"\bno fundo\b", r"\bat its core\b",
        r"\bthe real question is\b", r"\bvira (uma )?armadilha\b",
    ],
    "run-up": [
        r"\bvamos mergulhar\b", r"\bhere'?s what you need to know\b", r"\bhonestly\?",
        r"\blet'?s dive\b", r"\bmergulhe\b", r"\bvamos nessa\b",
    ],
    "argumentar com ninguem": [
        r"\bn[aã]o [eé] sobre\b", r"\bto be clear\b", r"\bdon'?t get me wrong\b",
        r"\bdeixe-me ser clar[oa]\b", r"\bpara ser just[oa]\b",
    ],
    "qualificadores empilhados": [
        r"\b(could|might|may)\s+(potentially|possibly|conceivably)\b",
        r"\b(pode|poderia)\s+(potencialmente|possivelmente|talvez)\b",
    ],
    "voz passiva escondendo sujeito": [
        r"\bfoi (feito|dito|visto|considerado|relatado)\b",
        r"\bwas (done|said|seen|considered|reported)\b",
    ],
    "palavras de IA": [
        r"\bactually\b", r"\bcrucial\b", r"\bdelve\b", r"\brobust\b", r"\bseamless\b",
        r"\bleverage\b", r"\bfoster\b", r"\blandscape\b", r"\btapestry\b", r"\btestament\b",
        r"\bunderscore\b", r"\bmeticulous\b", r"\bpivotal\b", r"\bshowcase\b", r"\bvibrant\b",
        r"\bmergulhar\b", r"\brobusto\b", r"\baproveitar\b", r"\bfomentar\b", r"\bcen[aá]rio\b",
        r"\btape[cç]aria\b", r"\btestemunho\b", r"\bmet[íi]cul[oa]\b", r"\bcrucial\b",
    ],
    "significancia inflada": [
        r"\bmarca um momento\b", r"\bdeixa um legado\b", r"\bo futuro parece\b",
        r"\bthe future looks bright\b", r"\bum testamento\b",
    ],
    "conexao vaga": [
        r"\bassociad[oa] a\b", r"\bligad[oa] a\b", r"\bassociated with\b", r"\blinked to\b",
    ],
    "riders -ing": [
        r"\bhighlighting\b", r"\bunderscoring\b", r"\breflecting\b", r"\bdestacando\b",
        r"\brefletindo\b", r"\bevidenciando\b",
    ],
    "linguagem de venda": [
        r"\bnestled in the heart of\b", r"\bbreathtaking\b", r"\brenowned\b",
        r"\bdeslumbrante\b", r"\bno cora[cç][aã]o d[eo]\b",
    ],
    "autoridade emprestada": [
        r"\bespecialistas dizem\b", r"\bsegundo relatos\b", r"\bexperts say\b",
        r"\bstudies show\b", r"\ba ci[eê]ncia diz\b",
    ],
    "evitar is/are": [
        r"\bserve como\b", r"\brepresenta\b", r"\bconta com\b", r"\bserves as\b", r"\bboasts\b",
    ],
    "sobras de chat": [
        r"\bespero que ajude\b", r"\b[oó]tima pergunta\b", r"\bquer que eu\b",
        r"\bhope this helps\b", r"\bgreat question\b",
    ],
    "limite de conhecimento": [
        r"\bat[eé] meu [uú]ltimo treinamento\b", r"\bas of my last\b",
    ],
}

SENSITIVE = [
    r"\b(matar|matou|assassinou|estupr\w+|sangue|gore|corpo(s)? mutilad\w+)\b",
    r"\b(porn|sexo expl[íi]cito)\b",
]

SUSPECT_WORDS = [r"\bsuspeit", r"\bacusad", r"\balegad", r"\bsupost"]

MONTHS = {
    "pt": {"janeiro": 1, "fevereiro": 2, "marco": 3, "março": 3, "abril": 4, "maio": 5, "junho": 6,
           "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12},
    "en": {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
           "august": 8, "september": 9, "october": 10, "november": 11, "december": 12},
}
JUMP_MARKERS = [r"\bantes\b", r"\bmeses? antes\b", r"\banos? antes\b", r"\brecua\b", r"\bvolta a\b",
                r"\bflashback\b", r"\bna [eé]poca\b", r"\bmais cedo\b", r"\bearlier\b",
                r"\bbefore that\b", r"\bpreviously\b", r"\bmeses antes disso\b",
                # pretérito mais-que-perfeito = rewind explicitamente marcado ("tinha sido apreendido")
                r"\btinha sido\b", r"\bj[aá] tinha\b", r"\bhavia sido\b", r"\bhavia acontecido\b",
                # referencias historicas ("desde 1982", "na decada de...") nao sao violacao de ordem
                r"\bdesde\b", r"\bna d[eé]cada\b", r"\bno in[ií]cio dos anos\b"]


def parse_cell(s):
    """2010 | 2010-06 | 2010-06-09 | 09/06/2010 | ? -> (y,m,d) ou None."""
    s = (s or "").strip()
    if not s or s in ("?", "-"):
        return None
    for pat, order in ((r"^(\d{4})-(\d{1,2})-(\d{1,2})$", "ymd"),
                       (r"^(\d{4})-(\d{1,2})$", "ym"),
                       (r"^(\d{1,2})/(\d{1,2})/(\d{2,4})$", "dmy"),
                       (r"^(\d{4})$", "y")):
        m = re.match(pat, s)
        if m:
            g = [int(x) for x in m.groups()]
            if order == "ymd":
                return g[0], g[1], g[2]
            if order == "ym":
                return g[0], g[1], 0
            if order == "dmy":
                y = g[2] + 2000 if g[2] < 100 else g[2]
                return y, g[1], g[0]
            return g[0], 0, 0
    return None


def narration_dates(text, lang="pt"):
    """Datas faladas, em ordem: [(pos, (y,m,d), paragrafo)].
    Ano-solto que cai DENTRO de uma data mais especifica ('julho de 2010') nao conta de novo."""
    out = []
    months = "|".join(MONTHS[lang])
    for pi, para in enumerate(re.split(r"\n\s*\n", text)):
        low = para.lower()
        hits, spans = [], []

        def add(m, dt):
            spans.append((m.start(), m.end()))
            hits.append((m.start(), dt))

        for m in re.finditer(r"\b(\d{1,2}) de (" + months + r")(?: de (\d{4}))?\b", low):
            add(m, (int(m.group(3)) if m.group(3) else 0, MONTHS[lang][m.group(2)], int(m.group(1))))
        for m in re.finditer(r"\b(" + months + r") de (\d{4})\b", low):
            add(m, (int(m.group(2)), MONTHS[lang][m.group(1)], 0))
        for m in re.finditer(r"\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b", low):
            y = int(m.group(3))
            add(m, (y + 2000 if y < 100 else y, int(m.group(2)), int(m.group(1))))
        for m in re.finditer(r"\b(19|20)\d{2}\b", low):
            if any(s <= m.start() < e for s, e in spans):
                continue  # ano ja coberto por 'mes de ano' / 'dia de mes'
            add(m, (int(m.group(0)), 0, 0))

        seen = set()
        for pos, dt in sorted(hits):
            if dt in seen:
                continue
            seen.add(dt)
            out.append((pos, dt, para, pi))
    return out


def check_cronologia(text, tl_path, lang="pt", cold_open=3):
    """Ordem cronologica, saltos marcados, cobertura e datas fora da linha do tempo."""
    tl = []
    if tl_path:
        try:
            for line in open(tl_path, encoding="utf-8").read().splitlines():
                line = line.strip()
                if line.startswith("|"):
                    cells = [c.strip() for c in line.strip("|").split("|")]
                    if cells and cells[0].lower() not in ("data", "date") and set(cells[0]) > set("-: "):
                        dt = parse_cell(cells[0])
                        if dt:
                            tl.append(dt)
        except OSError:
            print(f"\n[CRONOLOGIA] linha do tempo nao encontrada: {tl_path}")
    tl.sort(key=lambda d: (d[0], d[1] or 99, d[2] or 99))
    dates = narration_dates(text, lang)
    print(f"\n[CRONOLOGIA] {len(dates)} data(s) falada(s)" + (f" | linha do tempo: {len(tl)} evento(s)" if tl else ""))

    def key(dt):
        return (dt[0], dt[1] or 0, dt[2] or 0) if dt[0] else None

    prev, jumps, min_seen = None, 0, None
    for pos, dt, para, pi in dates:
        k = key(dt)
        if k is None:
            continue
        if pi < cold_open:  # hook/cold open pode abrir no futuro; nao entra na ordem
            prev, min_seen = k, (k if min_seen is None or k < min_seen else min_seen)
            continue
        if prev and k < prev:
            marked = any(re.search(p, para.lower()) for p in JUMP_MARKERS)
            reset = min_seen is None or k < min_seen  # recuo ao inicio da historia (background) e ok
            if marked:
                jumps += 1
            elif not reset:
                snippet = para[max(0, pos - 40):pos + 60].replace("\n", " ")
                print(f"  ORDEM: {dt[0]}-{dt[1]:02d} aparece depois de {prev[0]}-{prev[1]:02d} "
                      f"sem marcador de salto -> \"...{snippet}...\"")
        prev = k
        min_seen = k if min_seen is None or k < min_seen else min_seen

    if tl:
        tl_years = {d[0] for d in tl}
        nar_years = {d[0] for _, d, _, _ in dates if d[0]}
        fora = sorted(nar_years - tl_years)
        if fora:
            print(f"  FORA DA LINHA DO TEMPO: {', '.join(str(y) for y in fora)} (falar so o que esta na tabela)")
        sem_eco = sorted(tl_years - nar_years)
        if sem_eco:
            print(f"  SEM ECO NO ROTEIRO: {', '.join(str(y) for y in sem_eco)} (evento da tabela nao narrado)")
    if jumps:
        print(f"  saltos marcados (ok): {jumps}")
    if not dates:
        print("  nenhuma data falada - se o caso e cronologico, ancore os blocos (ref 35)")

STOP = {"the", "a", "o", "e", "de", "do", "da", "que", "and", "of", "to", "in", "it",
        "was", "is", "um", "uma", "os", "as", "no", "na", "em", "para", "com"}


def words(t):
    return len(re.findall(r"\w+", t, flags=re.UNICODE))


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--short", action="store_true", help="checagens de Short (hook <=12 palavras)")
    ap.add_argument("--cronologia", help="LINHA_DO_TEMPO.md: checa ordem/saltos/cobertura das datas")
    ap.add_argument("--lang", choices=["pt", "en"], default="pt", help="idioma dos meses (cronologia)")
    ap.add_argument("--cold-open", type=int, default=3, help="blocos iniciais (hook/recuo) fora da checagem de ordem")
    ap.add_argument("--genero", default="generic",
                    choices=["generic", "truecrime", "forense", "darkhistory", "financial"],
                    help="truecrime/forense: 'sangue/matar' vira advisory (vocabulario do genero)")
    a = ap.parse_args()

    text = open(a.path, encoding="utf-8").read()
    low = text.lower()
    total = words(text)
    print(f"Arquivo: {a.path}")
    print(f"Palavras: {total}")

    hard = 0
    meta_hits = [(p, m.group(0)) for p in BANNED for m in re.finditer(p, low, re.IGNORECASE)]
    gore_hits = [(p, m.group(0)) for p in SENSITIVE for m in re.finditer(p, low, re.IGNORECASE)]
    print(f"\n[META-LINGUAGEM BANIDA] {len(meta_hits)} ocorrência(s)")
    for p, g in meta_hits[:10]:
        print(f"  ...{g}...")
    gore_advisory = a.genero in ("truecrime", "forense")
    label = "TERMOS SENSÍVEIS (advisory no gênero)" if gore_advisory else "TERMOS SENSÍVEIS (revisar)"
    print(f"[{label}] {len(gore_hits)} ocorrência(s)")
    for p, g in gore_hits[:10]:
        print(f"  ...{g}...")
    if meta_hits or (gore_hits and not gore_advisory):
        hard = 1

    tells_total = 0
    print("\n[TELLS DE IA]")
    for label, pats in AI_TELLS.items():
        hits = [m.group(0) for p in pats for m in re.finditer(p, low, re.IGNORECASE)]
        if hits:
            tells_total += len(hits)
            print(f"  {label}: {len(hits)} -> {', '.join(hits[:4])}")
    if not tells_total:
        print("  nenhum")

    density = (tells_total / total * 1000) if total else 0
    print(f"\nDensidade: {density:.1f} tells/1000 palavras")
    if density <= 2:
        print("  -> OK")
    elif density <= 5:
        print("  -> REVISAR (reescreva os trechos com tell)")
    else:
        print("  -> REESCREVER (densidade alta de IA)")

    sents = [s.strip() for s in re.split(r"[.!?…]+", text) if s.strip()]
    if len(sents) >= 8:
        firsts = {}
        for s in sents:
            w = re.findall(r"\w+", s.lower())
            if w:
                firsts[w[0]] = firsts.get(w[0], 0) + 1
        repeated = {w: c for w, c in firsts.items() if c >= 4 and w not in STOP}
        if repeated:
            print(f"\n[RITMO] aberturas repetidas: {repeated}")

    dash = len(re.findall(r"—", text))
    per100 = dash / total * 100 if total else 0
    if per100 > 1:
        print(f"\n[RITMO] travessoes: {dash} ({per100:.1f}/100 palavras > 1) — troque por '..' ou ponto")

    if a.cronologia:
        check_cronologia(text, a.cronologia, a.lang, a.cold_open)

    has_suspect = any(re.search(p, low, re.IGNORECASE) for p in SUSPECT_WORDS)
    print(f"\n[COMPLIANCE] 'suspeito/acusado/alegado' presente: "
          f"{'SIM' if has_suspect else 'NÃO (verifique se há pessoa viva)'}")

    if a.short:
        paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        if paras:
            hook = words(paras[0])
            print(f"\n[SHORT] hook (1o bloco): {hook} palavras "
                  f"{'OK' if hook <= 12 else '-> ENCURTAR (<=8 faladas)'}")

    print(f"\nRESULTADO: {'FALHA DURA (meta-linguagem/gore)' if hard else 'SEM FALHA DURA'}"
          f" | tells: {tells_total} | densidade: {density:.1f}/1000")
    print("Lembrete: rode também o gate anti-inauthentic (references/09).")
    sys.exit(hard)


if __name__ == "__main__":
    main()
