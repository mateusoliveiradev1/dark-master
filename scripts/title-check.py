#!/usr/bin/env python3
"""title-check.py — sinais ADVISÓRIOS de título (não prevê performance).
Uso: python title-check.py "4 maneiras de ganhar dinheiro com o Cloud que ninguém está falando"
     python title-check.py --file titulos.txt
"""
import argparse, re, sys

POWER_PT = {"ninguém", "segredo", "proibido", "impossível", "verdade", "erro", "nunca",
            "sempre", "finalmente", "pare", "descubra", "revelado", "chocante"}
POWER_EN = {"nobody", "secret", "forbidden", "impossible", "truth", "mistake", "never",
            "always", "finally", "stop", "insane", "revealed", "shocking", "why", "how"}

def analyze(t):
    words = re.findall(r"\w+", t, flags=re.UNICODE)
    low = [w.lower() for w in words]
    L = len(t)
    caps = [w for w in words if len(w) > 1 and w.isupper()]
    has_num = bool(re.search(r"\d", t))
    paren = bool(re.search(r"[\(\[]", t))
    q = t.strip().endswith("?") or low[:1] in (["why"], ["how"], ["what"], ["como"], ["por"], ["porque"], ["o", "que"])
    power = sorted(set(low) & (POWER_PT | POWER_EN))
    print(f"Título: {t}")
    print(f"  chars: {L}  palavras: {len(words)}")
    flags = []
    if L > 60: flags.append("acima de ~60 chars (mobile corta)")
    if L > 100: flags.append("ACIMA DE 100 chars (limite)")
    if not has_num: flags.append("sem número específico")
    if not caps: flags.append("sem palavra em CAPS (opcional)")
    if len(words) > 12: flags.append("frase longa")
    if not power: flags.append("sem 'power word' do nicho")
    if paren: print("  curiosidade entre parênteses: sim")
    if caps: print(f"  CAPS: {', '.join(caps)}")
    if power: print(f"  power words: {', '.join(power)}")
    if q: print("  formato pergunta: sim")
    print("  flags: " + ("; ".join(flags) if flags else "nenhum alerta heurístico"))
    print()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("title", nargs="?", default=None)
    p.add_argument("--file", default=None)
    a = p.parse_args()
    if a.file:
        with open(a.file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line: analyze(line)
    elif a.title:
        analyze(a.title)
    else:
        print("Passe um título ou --file. Ex.: python title-check.py \"Meu título\"")

if __name__ == "__main__":
    main()
