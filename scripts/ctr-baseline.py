#!/usr/bin/env python3
"""ctr-baseline.py — calcula CTR e diferença vs uma baseline fornecida.
Uso: python ctr-baseline.py --impressoes 100000 --cliques 5000 --baseline 4.0
Não prevê performance; é só aritmética de apoio."""
import argparse

def main():
    p = argparse.ArgumentParser(description="CTR vs baseline")
    p.add_argument("--impressoes", type=float, required=True)
    p.add_argument("--cliques", type=float, required=True)
    p.add_argument("--baseline", type=float, default=None, help="CTR baseline em %% (ex.: 4.0)")
    a = p.parse_args()

    if a.impressoes <= 0:
        print("Impressões devem ser > 0")
        return
    ctr = a.cliques / a.impressoes * 100.0
    print(f"Impressões: {a.impressoes:,.0f}")
    print(f"Cliques:    {a.cliques:,.0f}")
    print(f"CTR:        {ctr:.2f}%")
    if a.baseline is not None:
        d = ctr - a.baseline
        rel = (d / a.baseline * 100.0) if a.baseline else 0.0
        print(f"Baseline:   {a.baseline:.2f}%")
        print(f"Delta:      {d:+.2f} p.p. ({rel:+.1f}% rel.)")
        # heurística: CTR é contextual. Compare com o próprio canal.
        if abs(d) < 1.0:
            print("Leitura: diferença provavelmente dentro do ruído. Precisa de mais dados.")
        else:
            print("Leitura: diferença relevante — valide com mais impressões antes de concluir.")
    print("\nLembrete: CTR só é útil junto de retenção. 12% CTR com 20% AVD perde de 6% com 55%.")

if __name__ == "__main__":
    main()
