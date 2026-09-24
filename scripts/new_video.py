#!/usr/bin/env python3
"""new_video.py — cria a pasta padrao de um video novo.

Uso:
  python scripts/new_video.py 27 "Hoffa" HEISTS --root "C:/.../canal dark1"
  python scripts/new_video.py 03 "D.B. Cooper" HEISTS --root "<canal>" --style truecrime-cfd

Cria:
  <root>/videoNN/{01_roteiro,02_audio,03_imagens,04_video_final}
  01_roteiro/narration_v3.txt     (cabecalho + placeholder)
  01_roteiro/narration_short.txt  (placeholder do Short separado)
  01_roteiro/TEMPLATE.txt         (copiado de 00_CANAL/TEMPLATE_ROTEIRO*.txt, se existir)
  01_roteiro/tease.txt            (placeholder)
  01_roteiro/PESQUISA_BRIEF.md
  01_roteiro/PESQUISA_FONTE.md
  01_roteiro/CLAIMS.json
  01_roteiro/LINHA_DO_TEMPO.md
  01_roteiro/SHORT_FUNNEL.md
  03_imagens/PROMPTS.md           (esqueleto via prompt_builder, se disponivel)
  youtube_package.txt             (template de publicacao)
"""
import argparse
import json
import os
import re
import shutil
from pathlib import Path

SUBS = ["01_roteiro", "02_audio", "03_imagens", "04_video_final"]

PLAYBOOKS = Path(os.environ.get(
    "DARK_MASTER_PLAYBOOKS",
    str(Path.home() / ".config" / "opencode" / "skills" / "dark-master" / "playbooks")))


def resolve_playbook(channel):
    """--channel <nome|pasta> -> pasta do playbook (contrato voice/motion/style.json)."""
    if not channel:
        return None
    p = Path(channel).expanduser()
    if p.is_dir():
        return p
    p = PLAYBOOKS / channel
    if p.is_dir():
        return p
    print(f"[AVISO] canal '{channel}' nao encontrado em {PLAYBOOKS} — seguindo sem contrato de canal.")
    return None


def channel_suffix(pb):
    """Sufixo travado do canal (style.json > image_suffix)."""
    if not pb:
        return None
    try:
        d = json.loads((pb / "style.json").read_text(encoding="utf-8"))
        return d.get("image_suffix")
    except (OSError, ValueError):
        return None

LINHA_TMPL = """# LINHA DO TEMPO — {case}

> Tabela canonica do episodio (ref 35). Toda data falada no roteiro tem que existir aqui.
> Camadas: [FATO] = documento oficial | [REPORTADO] = imprensa/relato | [LENDA] = evitar.
> `fato` e ROTULO CURTO (<= ~60 chars) - e o que aparece no plate da edicao.
> `data`: YYYY | YYYY-MM | YYYY-MM-DD | DD/MM/YYYY | ? (fato sem data).

| data | fato | camada | fonte |
|---|---|---|---|
| ? | [preencher: evento 1] | FATO | |
| ? | [preencher: evento 2] | REPORTADO | |
| ? | [preencher: evento 3] | FATO | |
"""

BRIEF_TMPL = """# BRIEF DE PESQUISA — {case}

## Caso
- ID:
- Gênero:
- Duração-alvo:
- Pergunta central:
- Ângulo editorial:

## Pessoas
| Pessoa | Papel | Status jurídico | Fonte |
|---|---|---|---|

## Linha de vida
| Data | Evento | Camada | Claim | Fonte |
|---|---|---|---|---|
| ? | | FATO | | |

## Evidências
| Evidência | O que mede | O que prova | O que não prova | Fonte |
|---|---|---|---|

## Contradições e lacunas
- Contradição:
- O que continua desconhecido:
- Lendas a evitar:

## Fontes
| ID | Fonte | Tipo | Data | URL | Localizador | Limitações |
|---|---|---|---|---|---|---|
| S001 | | primária/secundária | | | | |

## Plano narrativo
- Cold Open:
- Cadeia de evidências:
- Virada:
- Reconstrução:
- Payoff:
"""

CLAIMS_TMPL = {
    "case_id": "",
    "version": 1,
    "claims": []
}

SHORT_TMPL = """# SHORT→LONG — {case}

## Roteiro
- Long alvo:
- Objetivo do Short:
- Claim usada:
- Pergunta que o Short abre:
- Ponte:
- Beat do long que expande a pergunta:
- Motivo real para abrir o long:

## Frame e hook
- Frame 1 visual:
- Texto na tela: (máximo 6 palavras)
- Fala inicial: (máximo 8 palavras)
- Promessa do Short:
- Payoff:

## Progressão
- Evidência:
- Virada:
- Ponte:

## Loop
- Emenda visual:
- Emenda sonora:
- Loop semântico:
- Comentário fixado:
- Related Video:

## QA
- [ ] Short satisfatório sozinho
- [ ] Long valioso sozinho
- [ ] Não repete as 10 primeiras palavras
- [ ] Não inventa prova, diálogo ou confissão
"""

PACKAGE_TMPL = """# {title}
TITLE: 
ALT 2: 
ALT 3: 

ANGULO: 

DESCRIPTION (copiar e colar):
B1 HOOK (150 chars, keyword): 
B2 RESUMO (150-250 palavras): 
B3 FONTES + disclaimer IA: 
B4 HASHTAGS (3-5): 

TAGS: 

CHAPTERS (PENDENTE - remapear pos-build com a duracao real):
0:00 

THUMB SPEC (validador): bg= | l1= | l2= | serie= | sub=

CHECKLIST UPLOAD: [ ] conteudo alterado/IA [ ] legenda revisada [ ] playlist [ ] end screen [ ] comentario fixado

SHORT (sobe junto):
TITLE (copiar): 
DESCRIPTION (copiar e colar): 
FIXAR COMENTARIO: 
"""


def find_template(root: Path):
    for pat in ("TEMPLATE_ROTEIRO*.txt", "TEMPLATE_ROTEIRO*.md"):
        for p in (root / "00_CANAL").glob(pat) if (root / "00_CANAL").exists() else []:
            return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("number")
    ap.add_argument("case")
    ap.add_argument("series", nargs="?", default="")
    ap.add_argument("--root", required=True)
    ap.add_argument("--style", default="truecrime-cfd")
    ap.add_argument("--channel", help="playbook do canal (usa style.json/image_suffix no PROMPTS.md)")
    a = ap.parse_args()

    pb_dir = resolve_playbook(a.channel)
    suffix = channel_suffix(pb_dir)
    root = Path(a.root).expanduser()
    root.mkdir(parents=True, exist_ok=True)
    num = re.sub(r"\D", "", a.number).zfill(2) if re.sub(r"\D", "", a.number) else a.number
    vid = root / f"video{num}"
    if vid.exists():
        print(f"[!] ja existe: {vid}")
    for s in SUBS:
        (vid / s).mkdir(parents=True, exist_ok=True)

    case = a.case.strip()
    title = f"video{num} - {case}" + (f" ({a.series})" if a.series else "")

    # roteiro
    rot = vid / "01_roteiro" / "narration_v3.txt"
    if not rot.exists():
        rot.write_text(
            f"# {title}\n# Roteiro (blocos: HOOK, CONTEXTO, PRESSAO, O DIA, INVESTIGACAO, "
            f"FAMILIA, TEORIAS, CHAVES+OUTRO+TEASER)\n# Preencha um paragrafo por bloco de TTS.\n\n",
            encoding="utf-8")
    # template (nao sobrescrever)
    tmpl = find_template(root)
    if tmpl and not (vid / "01_roteiro" / "TEMPLATE.txt").exists():
        shutil.copy(tmpl, vid / "01_roteiro" / "TEMPLATE.txt")
    # tease (nao sobrescrever)
    tease = vid / "01_roteiro" / "tease.txt"
    if not tease.exists():
        tease.write_text("TEASE-A | para NN | \nTEASE-B | para NN | \nCTA | especifico | \n", encoding="utf-8")
    # pesquisa/fontes (nao sobrescrever) — camadas [FATO]/[REPORTADO]/[LENDA]
    pesq = vid / "01_roteiro" / "PESQUISA_FONTE.md"
    if not pesq.exists():
        pesq.write_text(
            f"# PESQUISA/FONTES — {case}\n\n"
            "> Uma camada por linha: [FATO] / [REPORTADO] / [LENDA]. 2+ fontes por caso. Nada sem fonte.\n\n"
            "| ID | Camada | Afirmação | Fonte | URL | Localizador | Limitações |\n"
            "|---|---|---|---|---|---|---|\n"
            "| S001 | FATO | | | | | |\n"
            "| S002 | REPORTADO | | | | | |\n\n"
            "- [LEGENDA/LENDA a evitar] \n",
            encoding="utf-8")
    brief = vid / "01_roteiro" / "PESQUISA_BRIEF.md"
    if not brief.exists():
        brief.write_text(BRIEF_TMPL.format(case=case), encoding="utf-8")
    claims = vid / "01_roteiro" / "CLAIMS.json"
    if not claims.exists():
        claim_data = dict(CLAIMS_TMPL)
        claim_data["case_id"] = case
        claims.write_text(json.dumps(claim_data, ensure_ascii=False, indent=2), encoding="utf-8")
    short_funnel = vid / "01_roteiro" / "SHORT_FUNNEL.md"
    if not short_funnel.exists():
        short_funnel.write_text(SHORT_TMPL.format(case=case), encoding="utf-8")
    short_narration = vid / "01_roteiro" / "narration_short.txt"
    if not short_narration.exists():
        short_narration.write_text("", encoding="utf-8")
    # linha do tempo (nao sobrescrever) — casos cronologicos (ref 35)
    ldt = vid / "01_roteiro" / "LINHA_DO_TEMPO.md"
    if not ldt.exists():
        ldt.write_text(LINHA_TMPL.format(case=case), encoding="utf-8")
    # pacote
    pkg = vid / "youtube_package.txt"
    if not pkg.exists():
        pkg.write_text(PACKAGE_TMPL.format(title=title), encoding="utf-8")
    # prompts (via prompt_builder, se existir)
    pb = Path(__file__).resolve().parent / "prompt_builder.py"
    prompts = vid / "03_imagens" / "PROMPTS.md"
    if pb.exists() and not prompts.exists():
        import subprocess, sys
        cmd = [sys.executable, str(pb), "--style", a.style, "--count", "0",
               "--title", title, "--out", str(prompts)]
        if suffix:
            cmd += ["--suffix", suffix]
        subprocess.run(cmd, capture_output=True, text=True)

    print(f"[OK] criado: {vid}" + (f" (canal: {a.channel})" if a.channel else ""))
    for s in SUBS:
        print(f"     {s}/")
    print("     youtube_package.txt")
    print("\nProximos passos (scaffold completo = pastas + stubs + PROMPTS + package + voz):")
    print("  1. preencha PESQUISA_BRIEF.md, PESQUISA_FONTE.md e CLAIMS.json")
    print("     caso cronologico (forense/truecrime): preencha 01_roteiro/LINHA_DO_TEMPO.md")
    print("     escreva o long em 01_roteiro/narration_v3.txt e o Short em 01_roteiro/narration_short.txt")
    print("  2. planeje o Short em SHORT_FUNNEL.md e valide-o separadamente")
    print(f"  3. complete os prompts por PORTE (header ja com o sufixo do canal): {prompts}")
    print("  4. voz liberada (so depende da narracao e do GATE de fatos); MOTION so com GATE 100% das imagens")
    print(f"  5. gere as imagens e valide: python scripts/image_audit.py \"{vid/'03_imagens'}\" --sheet")


if __name__ == "__main__":
    main()
