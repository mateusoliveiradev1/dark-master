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
}

PLAYBOOKS = Path(os.environ.get(
    "DARK_MASTER_PLAYBOOKS",
    str(Path.home() / ".config" / "opencode" / "skills" / "dark-master" / "playbooks")))


def channel_roteiro(channel):
    """Le playbooks/<canal>/roteiro.json -> (label, (lo, hi)) ou None (com AVISO).
    Canal com formato proprio (ex. Laudo Final ~10min) nao deve ser medido pelo porte generico."""
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
    pw = d.get("palavras")
    if not (isinstance(pw, list) and len(pw) == 2):
        print("[AVISO] roteiro.json sem 'palavras': [lo, hi] - usando porte generico.")
        return None
    dur = d.get("duracao_min")
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
        ("HOOK", 0.05, "o fato estranho do LAUDO (nao o crime)"),
        ("CONTEXTO", 0.18, "vitima, familia, lugar"),
        ("O DIA", 0.20, "reconstrucao da cena"),
        ("PERICIA", 0.30, "o coracao: o que cada exame provou/desmentiu"),
        ("FAMILIA", 0.10, "quem luta"),
        ("TEORIAS", 0.13, "max 3, sem afirmar"),
        ("LAUDO+OUTRO+TEASER", 0.04, "fechamento forense + proximo"),
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
        "# CHECKLIST DE FATOS (preencher antes de gerar voz):",
        "# - Vitimas (nomes/idades):",
        "# - Data:              Local:",
        "# - Fontes (2+):",
        "# - Suspeito vivo? (se sim -> alleged):",
        "# - Lendas a evitar:",
        "# - Divulgacao de IA: (no pacote de publicacao)",
    ]
    return "\n".join(lines) + "\n"


def validate(narration_path, porte, genre, window=None):
    txt = Path(narration_path).read_text(encoding="utf-8", errors="replace")
    # remove linhas de comentario (#) para contagem
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
        if paras and words(paras[0]) > 12:
            flags.append(f"hook_short_longo({words(paras[0])}>12)")
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
    has_teaser = any(re.search(p, low) for p in TEASER)
    has_alleged = any(re.search(p, low) for p in ALLEGED)
    if meta_hits:
        flags.append(f"meta_linguagem({len(meta_hits)})")
    gore_advisory = genre in ("truecrime", "forense")  # vocabulario do genero (sangue, corpo...)
    if gore_hits and not gore_advisory:
        flags.append(f"gore({len(gore_hits)})")
    if genre != "short":
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
    ap.add_argument("--case", default="")
    ap.add_argument("--date", default="")
    ap.add_argument("--place", default="")
    ap.add_argument("--sources", default="")
    ap.add_argument("--question", default="")
    ap.add_argument("--out", help="pasta 01_roteiro (gera ROTEIRO_PLANO.md)")
    ap.add_argument("--validate", help="valida um narration existente")
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
    if is_short:
        porte = a.porte or "25s"
        if porte not in PORTE_SHORT:
            print(f"[!] porte de Short invalido: {porte}. Use 13s | 25s | 45s.")
            sys.exit(2)
        window = PORTE_SHORT[porte]
    else:
        cr = channel_roteiro(a.channel) if a.channel else None
        if cr:
            porte, window = cr  # formato proprio do canal vence o porte generico
        else:
            porte = a.porte or "padrao"
            if porte not in PORTE:
                print(f"[!] porte de long-form invalido: {porte}. Use fino | padrao | rico.")
                sys.exit(2)
            window = PORTE[porte]

    if a.validate:
        ok = validate(a.validate, porte, genre, window)
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
    plan.write_text(build_plan(genre, porte, a.__dict__, window), encoding="utf-8")
    nar_name = "narration_short.txt" if is_short else "narration_v3.txt"
    nar = out / nar_name
    if not nar.exists():
        nar.write_text("", encoding="utf-8")

    print(f"[OK] plano: {plan}")
    print(f"[OK] roteiro: {nar} (escreva a narracao aqui, sem marcadores)")
    print("\nProximo: escreva bloco a bloco e rode:")
    short_flag = " --short" if is_short else ""
    if a.channel and not is_short:
        print(f'  python scripts/script_builder.py --validate "{nar}" --channel {a.channel} --genre {genre}')
    else:
        print(f'  python scripts/script_builder.py --validate "{nar}" --porte {porte} --genre {genre}{short_flag}')


if __name__ == "__main__":
    main()
