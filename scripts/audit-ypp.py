#!/usr/bin/env python3
"""audit-ypp.py — checklist interativo do gate YPP + anti-inauthentic.
Uso: python audit-ypp.py            (interativo)
     python audit-ypp.py --check    (só imprime o checklist)
"""
import sys

ITEMS = [
    ("Substância varia entre vídeos (sem template intercambiável)", "09"),
    ("Cada vídeo tem pesquisa/insight/perspectiva própria", "09"),
    ("Sem imagem gráfica na thumb nem nos primeiros 15s", "09"),
    ("Pessoas vivas tratadas como 'suspeito/acusado'", "07"),
    ("Divulgação de IA quando voz/visual sintético", "09"),
    ("Metadados não duplicados entre vídeos", "09"),
    ("Título e thumb não repetem palavras", "04"),
    ("Capítulos válidos (00:00, >=3, >=10s, rótulos-resposta)", "01"),
    ("Primeiros 30s cumprem a promessa do título", "01"),
    ("Sem intro/logo antes do hook", "03"),
    ("Settings do canal auditados (18)", "18"),
    ("Publicar como não listado -> revisar -> público", "18"),
    ("Feed de inscrições + notificações marcado", "18"),
    ("Shorts: frame 1 entrega payoff/tensão, legenda na tela", "02"),
    ("Canal ativo (sem 6 meses parado)", "09"),
]

def run_interactive():
    print("GATE YPP + ANTI-INAUTHENTIC\n")
    fails = 0
    for i, (item, ref) in enumerate(ITEMS, 1):
        ans = input(f"[{i}/{len(ITEMS)}] {item} (ref {ref}) [s/n]: ").strip().lower()
        if ans not in ("s", "y", "sim", "yes"):
            fails += 1
            print("   -> PENDENTE")
    print()
    if fails:
        print(f"RESULTADO: BLOQUEADO ({fails} pendência(s)). Resolva antes de publicar.")
        sys.exit(1)
    print("RESULTADO: PASSOU. Pode publicar (upload manual).")

def print_check():
    for i, (item, ref) in enumerate(ITEMS, 1):
        print(f"[ ] {i:2d}. {item}  (references/{ref})")

if __name__ == "__main__":
    if "--check" in sys.argv:
        print_check()
    else:
        run_interactive() if sys.stdin.isatty() else print_check()
