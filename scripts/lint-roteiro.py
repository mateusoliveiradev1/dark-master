#!/usr/bin/env python3
"""lint-roteiro.py — checagens de roteiro para canais dark (anti-IA + compliance).
Uso: python lint-roteiro.py caminho/para/narration_v3.txt
"""
import sys, re

# meta-linguagem / proibido (compliance)
BANNED = [
    r"\besse canal\b", r"\bneste canal\b", r"\bthis channel\b", r"\bassista o short\b",
    r"\bcurta e se inscreva\b", r"\bdeixe o like\b",
]
# tells de IA (fortes)
AI_TELLS = [
    r"\bn[aã]o\s+(?:[eé]|apenas|s[oó])[^.]{0,25}\bmas\b",   # não é X, mas Y
    r"\bn[aã]o\s+[eé]\s+s[oó][^.]{0,25}[,;]\s*[eé]\b",        # não é só X, é Y
    r"\bit'?s not (just|only) .{0,25},? it'?s\b",
    r"\bit'?s not just .{0,20},? it'?s\b",
    r"\bno mundo (de hoje|atual)\b", r"\bin today'?s\b",
    r"\bgame[- ]?changer\b", r"\bdeep dive\b", r"\bno fim do dia\b", r"\bat the end of the day\b",
    r"\bsem mais delongas\b", r"\bwithout further ado\b",
    r"\bvou ser (honesto|sincero)\b", r"\breal talk\b", r"\bhonestly\?",
    r"\b(neste vídeo|in this video) (nós |we )?(vamos|will)\b",
]
# termos sensiveis de anunciante (revisar)
SENSITIVE = [
    r"\b(matar|matou|assassinou|estupr\w+|sangue|gore|corpo(s)? mutilad\w+)\b",
    r"\b(porn|sexo expl[íi]cito)\b",
]
# pessoa viva -> deve haver "suspeito/acusado"
SUSPECT_WORDS = [r"\bsuspeit", r"\bacusad", r"\balegad", r"\bsupost"]

def scan(path, patterns):
    hits = []
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        for pat in patterns:
            for m in re.finditer(pat, line, flags=re.IGNORECASE):
                hits.append((i, m.group(0)))
    return hits

def main():
    if len(sys.argv) < 2:
        print("Uso: python lint-roteiro.py <arquivo.txt>"); return
    path = sys.argv[1]
    text = open(path, encoding="utf-8").read()
    words = len(re.findall(r"\w+", text, flags=re.UNICODE))
    print(f"Arquivo: {path}")
    print(f"Palavras: {words}  (PADRÃO dark ~1.300–1.600; RICO ~1.900+)")
    for label, pats in [("META-LINGUAGEM BANIDA", BANNED),
                        ("TELLS DE IA", AI_TELLS),
                        ("TERMOS SENSÍVEIS (revisar)", SENSITIVE)]:
        hits = scan(path, pats)
        print(f"\n[{label}] {len(hits)} ocorrência(s)")
        for i, g in hits[:20]:
            print(f"  linha {i}: ...{g}...")
    # suspeito
    has_suspect = any(re.search(p, text, flags=re.IGNORECASE) for p in SUSPECT_WORDS)
    print(f"\n[COMPLIANCE] 'suspeito/acusado/alegado' presente: {'SIM' if has_suspect else 'NÃO (verifique se há pessoa viva)'}")
    print("\nLembrete: rode também o gate anti-inauthentic (references/09).")

if __name__ == "__main__":
    main()
