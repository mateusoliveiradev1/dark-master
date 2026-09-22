# 12 — Pipeline de produção

Pipeline unificado + mapas para os **engines** que já existem nos projetos do usuário.

> **Canal novo:** siga o pipeline genérico abaixo. Os "engines" por projeto são reutilizáveis, mas **não obrigatórios** — um canal novo pode começar com scripts próprios. As vozes/regras de cada canal ficam no playbook (`playbooks/<canal>/`).

## Pipeline unificado

```
ideia/pacote → pesquisa → roteiro → linter → imagens (GATE 100%) → voz
   → captions (SRT/karaoke) → motion/assembly → tail/outro → chapters
   → Short → endcard → thumbs 3x → pacote de publicação → auditoria YPP → upload manual
```

**GATE 100%:** sem todas as imagens, não gera voz nem motion.

## Mapa etapa → script (projetos do usuário)

### Cold File Diaries — `C:\Users\Liiiraa\Downloads\canal dark1`
| Etapa | Script |
|---|---|
| scaffold | `scripts/novo_video.py` |
| orquestra tudo | `scripts/build_video.py videoNN [--from step]` |
| roteiro/linter | `scripts/linter_roteiro.py` |
| voz | `scripts/gerar_voz_v3.py` (edge-tts Christopher -10% + bed) |
| SRT norm | `scripts/gerar_srt_norm.py` |
| motion | `scripts/montar_motion.py` |
| tail | `scripts/finalizar_tail.py` |
| chapters | `scripts/remapar_chapters.py` |
| Short karaoke | `scripts/padrao_short.py` |
| endcard (short) | `scripts/endcard.py` |
| thumbs A/B/C | `scripts/fazer_thumb_v2.py` |
| pacote | `scripts/pacote_dia.py` → `validar_pacote.py` |
| auditoria | `scripts/auditar_tudo.py` · `auditar_imagens.py` |
| mid-rolls | `scripts/midrolls.py` |
| D+2/D+7 | `scripts/revisao_d2.py` |

### Financial Crime Files — `C:\Users\Liiiraa\Downloads\The-money-files`
- Orquestrador: `03_TOOLS/build_money.py` (12 passos com gates).
- Gráficos: `moneymap.py`, `timeline.py`, `evidence.py`.
- Voz: `gerar_voz_money.py` (GuyNeural). Bed: `padrao_bed_money.py`.
- SRT: `gerar_srt_norm.py` · Motion: `montar_motion_money.py` · Outro: `anexar_outro_money.py`.
- Short: `padrao_short_money.py` · Endcard: `endcard_money.py`.
- Pacote/audit: `pacote_dia.py`, `validar_pacote.py`, `linter_roteiro.py`.

### Laudo Final — `D:\dark-forense`
- Orquestrador: `scripts/build_video.py` (gates).
- Voz PT: `scripts/gerar_voz_pt.py` (edge-tts Remy/Antonio), `gerar_voz_gemini.py` (Algenib), `gerar_voz_fish.py` (clone).
- Motion: `montar_motion.py` · Bed: `padrao_bed.py`.
- Short: `padrao_short.py` · Tail: `finalizar_tail.py` · Endcard: `endcard.py`.
- QA: `qa_blocos.py`, `checar_pronuncia.py`, `auditar_imagens.py`, `validar_pacote.py`.

### The Midnight Archive — `C:\Users\Liiiraa\Downloads\canal-dark`
- Engine procedural (não alterar; reaproveitar):
  - `scripts/tts.py` (edge-tts Christopher -12% + prosódia por sentença)
  - `scripts/visuals.py` (arte procedural + shot variants)
  - `scripts/fetch_images.py` (Wikimedia PD/CC)
  - `scripts/music.py` (ambient procedural numpy)
  - `scripts/motion.py` (letterbox 2.39:1, grain, lower-thirds)
  - `scripts/render.py` (assembly beat-synced, 3 passos)
  - `scripts/branding.py`, `scripts/seo.py`
- Config: `scripts/config.py` · Roteiro: `content/ep1/script.py` · Backlog: `content/backlog.md`.

## Ordem de execução prática

1. `novo_video`/criar pasta → escrever roteiro → `linter_roteiro`.
2. Gerar/coletar **todas** as imagens (Nano Banana manual; ver `13`).
3. `gerar_voz` → `gerar_srt_norm`.
4. `montar_motion` → `finalizar_tail` → (`anexar_outro` se long).
5. `remapar_chapters` → `padrao_short` → `endcard`.
6. `fazer_thumb_v2` (3 variantes) → `pacote_dia` → `validar_pacote`.
7. `auditar_tudo` → upload manual → publicar.
8. D+2/D+7: `revisao_d2` → atualizar `15-outliers-e-aprendizados.md`.

## Invariantes (não quebrar)
- Voz oficial por canal (ver o playbook do canal em `playbooks/<canal>/`).
- 3 thumbs (Test & Compare).
- Chapters remapeados ao vídeo real.
- Upload **manual** (a não ser que o usuário peça API).
- Divulgação de IA + checklist `09`/`18`.
