#!/usr/bin/env python3
"""script_builder.py — gera o PLANO de roteiro e valida a estrutura/orcamento.

Gera um blueprint (ROTEIRO_PLANO.md) com beats, orcamento de palavras, guias e
checklist de fatos — e cria/limpa o narration_v3.txt (TTS-safe, sem marcadores).

Uso:
  python scripts/script_builder.py --genre truecrime --porte padrao \
      --case "Hoffa" --date 1975 --place Detroit --sources "FBI vault; DOJ" \
      --out "<videoNN>/01_roteiro"

  python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_v3.txt" --porte padrao

O roteiro (narration) fica SEM marcadores (o TTS nao fala nada alem da narracao).
"""
import argparse
import json
import re
import sys
from pathlib import Path

PORTE = {
    "fino":   (1900, 2400),
    "padrao": (2900, 3300),
    "rico":   (3400, 3800),
}

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
        ("HOOK", 0.05, "o fato estranho do LAUDO (nao o crime)"),
        ("CONTEXTO", 0.18, "vitima, familia, lugar"),
        ("O DIA", 0.20, "reconstrucao da cena"),
        ("PERICIA", 0.30, "o coracao: o que cada exame provou/desmentiu"),
        ("FAMILIA", 0.10, "quem luta"),
        ("TEORIAS", 0.13, "max 3, sem afirmar"),
        ("LAUDO+OUTRO+TEASER", 0.04, "fechamento forense + proximo"),
    ],
}

META = [r"\bthis channel\b", r"\besse canal\b", r"\bin this video\b", r"\bnesse v[íi]deo\b",
        r"\bwatch the short\b", r"\bassista o short\b", r"\bsubscribe\b.*\bnow\b"]
GORE = [r"\bblood\b", r"\bsangue\b", r"\bgore\b", r"\bcorpse\b", r"\bdead body\b",
        r"\bintestin\w*\b", r"\bdismember\w*\b", r"\bmutilat\w*\b"]
TEASER = [r"\btomorrow\b", r"\bnext case\b", r"\bnext file\b", r"\bcoming next\b",
          r"\bamanh[ãa]\b", r"\bpr[óo]ximo caso\b"]
ALLEGED = [r"\balleged\b", r"\bsuspect\b", r"\baccused\b", r"\bsuspeit\w*\b", r"\bacusad\w*\b"]


def words(t):
    return len(re.findall(r"\w+", t, flags=re.UNICODE))


def build_plan(genre, porte, meta):
    lo, hi = PORTE[porte]
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


def validate(narration_path, porte, genre):
    txt = Path(narration_path).read_text(encoding="utf-8", errors="replace")
    # remove linhas de comentario (#) para contagem
    body = "\n".join(l for l in txt.splitlines() if not l.strip().startswith("#"))
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    total = words(body)

    lo, hi = PORTE[porte]
    flags = []
    if not paras:
        flags.append("vazio")
    if total < lo:
        flags.append(f"curto({total}<{lo})")
    elif total > hi:
        flags.append(f"longo({total}>{hi})")
    if paras and words(paras[0]) > 160:
        flags.append(f"hook_longo({words(paras[0])})")
    low = txt.lower()
    meta_hits = [p for p in META if re.search(p, low)]
    gore_hits = [p for p in GORE if re.search(p, low)]
    has_teaser = any(re.search(p, low) for p in TEASER)
    has_alleged = any(re.search(p, low) for p in ALLEGED)
    if meta_hits:
        flags.append(f"meta_linguagem({len(meta_hits)})")
    if gore_hits:
        flags.append(f"gore({len(gore_hits)})")
    if not has_teaser:
        flags.append("sem_teaser_final")
    if not has_alleged:
        flags.append("sem_alleged(verificar)")

    print(f"# Validacao de roteiro — {Path(narration_path).name}\n")
    print(f"  genero: {genre} | porte: {porte} ({lo}-{hi})")
    print(f"  paragrafos: {len(paras)} | palavras: {total}")
    if paras:
        print(f"  1o bloco (hook): {words(paras[0])} palavras")
    print(f"  teaser no fim: {'sim' if has_teaser else 'NAO'}")
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--genre", default="generic")
    ap.add_argument("--beats-file", help="JSON com generos customizados")
    ap.add_argument("--list-genres", action="store_true")
    ap.add_argument("--porte", default="padrao", choices=list(PORTE))
    ap.add_argument("--case", default="")
    ap.add_argument("--date", default="")
    ap.add_argument("--place", default="")
    ap.add_argument("--sources", default="")
    ap.add_argument("--question", default="")
    ap.add_argument("--out", help="pasta 01_roteiro (gera ROTEIRO_PLANO.md)")
    ap.add_argument("--validate", help="valida um narration_v3.txt existente")
    a = ap.parse_args()

    if a.beats_file:
        load_beats(a.beats_file)
    if a.list_genres:
        for g in GENRES:
            print(g)
        return
    if a.genre not in GENRES:
        print(f"[!] genero desconhecido: {a.genre}. Use --list-genres ou --beats-file.")
        sys.exit(2)
    if a.validate:
        ok = validate(a.validate, a.porte, a.genre)
        sys.exit(0 if ok else 1)

    if not a.out:
        print("Informe --out <pasta 01_roteiro> ou --validate <arquivo>")
        sys.exit(2)
    out = Path(a.out).expanduser()
    # se passar o videoNN/, usa 01_roteiro/
    if out.name.lower().startswith("video") or re.match(r"^EP", out.name):
        out = out / "01_roteiro"
    out.mkdir(parents=True, exist_ok=True)

    plan = out / "ROTEIRO_PLANO.md"
    plan.write_text(build_plan(a.genre, a.porte, a.__dict__), encoding="utf-8")
    nar = out / "narration_v3.txt"
    if not nar.exists():
        nar.write_text("", encoding="utf-8")

    print(f"[OK] plano: {plan}")
    print(f"[OK] roteiro: {nar} (escreva a narracao aqui, sem marcadores)")
    print("\nProximo: escreva bloco a bloco e rode:")
    print(f'  python scripts/script_builder.py --validate "{nar}" --porte {a.porte} --genre {a.genre}')


if __name__ == "__main__":
    main()
