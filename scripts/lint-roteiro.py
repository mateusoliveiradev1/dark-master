#!/usr/bin/env python3
"""lint-roteiro.py — checagens de roteiro para canais dark (anti-IA + compliance).

Uso:
  python scripts/lint-roteiro.py caminho/para/narration_v3.txt
  python scripts/lint-roteiro.py caminho/para/narration_short.txt --short

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
    print(f"[TERMOS SENSÍVEIS (revisar)] {len(gore_hits)} ocorrência(s)")
    for p, g in gore_hits[:10]:
        print(f"  ...{g}...")
    if meta_hits or gore_hits:
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
