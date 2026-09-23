# 12 — Pipeline de produção

Pipeline unificado + mapas para os **engines** que já existem nos projetos do usuário.

> **Canal novo:** siga o pipeline genérico abaixo. Os "engines" por projeto são reutilizáveis, mas **não obrigatórios** — um canal novo pode começar com scripts próprios. As vozes/regras de cada canal ficam no playbook (`playbooks/<canal>/`).
>
> **Contrato por canal (anti-clone):** voz, motion e estilo vêm de `playbooks/<canal>/{voice,motion,style}.json` — os scripts aceitam `--channel <nome>` (ou `canal.json` na raiz) e avisam quando caem no default. Contrato completo em `playbooks/README.md`. Nunca copie os valores de outro canal.
>
> **Motor de voz (free + pago):** `scripts/voice_engine.py` gera com qualquer provider do contrato (`provider.type`): edge/kokoro/piper (grátis) e Azure/ElevenLabs/Fish/Gemini/OpenAI (pago) — com `--test`, `--estimate`, cache por hash e fallback com aviso. Guia: `34-voz-tts.md`.

## Pipeline unificado

```
pesquisa → roteiro (script_builder) → linter → scaffold do vídeo (new_video: pastas + stubs + PROMPTS + package + voz)
   → prompts completos (prompt_builder) → imagens (GATE 100%) → auditoria de imagens (image_audit.py)
   → captions (SRT/karaoke) → motion/assembly → tail/outro → chapters
   → Short → endcard → thumbs 3x → pacote de publicação → auditoria YPP → upload manual
```

**GATES:** a **voz** só depende da narração + fatos (**liberada no scaffold**); o **motion** exige o **GATE 100%** (todas as imagens). Sem todas as imagens, **não gera motion**. Fluxo completo de escrita + scaffold: `30-roteiro-master.md`, PASSO 6.

## Mapa etapa → script (projetos do usuário)

### Cold File Diaries — `C:\Users\Liiiraa\Downloads\canal dark1`
| Etapa | Script |
|---|---|
| scaffold | `scripts/novo_video.py` |
| orquestra tudo | `scripts/build_video.py videoNN [--from step]` |
| roteiro/linter | `scripts/linter_roteiro.py` |
| voz | `scripts/gerar_voz_v3.py` (contrato `voice.json`: edge-tts Christopher + bed) — ou `voice_engine.py` da skill para outro provider (`--channel`) |
| SRT norm | `scripts/gerar_srt_norm.py` |
| motion | `scripts/montar_motion.py` (contrato `motion.json`) |
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

1. Escrever roteiro → `linter_roteiro`.
2. **Scaffold** (`novo_video`/`new_video`: pastas + stubs + PROMPTS + package) → **voz** (`gerar_voz`; só precisa da narração + fatos — `30` PASSO 6).
3. Completar prompts (porte) → gerar/coletar **todas** as imagens (Nano Banana manual; ver `13`) → `image_audit` (**GATE 100% antes do motion**).
4. `gerar_srt_norm` → `montar_motion` → `finalizar_tail` → (`anexar_outro` se long).
5. `remapar_chapters` (duração real) → `padrao_short` → `endcard`.
6. `fazer_thumb_v2` (3 variantes) → `pacote_dia` → `validar_pacote`.
7. `auditar_tudo` → upload manual → publicar.
   - **Etapas manuais no meio do pipeline:** o `build_video` **para no gate de thumbs** (3 variantes A/B/C são geradas por você) e o **pacote de publicação é autoral** (título/descrição/tags/chapters — o scaffold só cria os blocos vazios no formato do validador; `pacote_dia` monta o copiar-e-colar). Capítulos só depois do build (`remapar_chapters`).
8. D+2/D+7: `revisao_d2` → atualizar `15-outliers-e-aprendizados.md`.

## Invariantes (não quebrar)
- Voz/motion/estilo oficiais por canal (contrato `playbooks/<canal>/{voice,motion,style}.json`).
- 3 thumbs (Test & Compare).
- Chapters remapeados ao vídeo real.
- Upload **manual** (a não ser que o usuário peça API).
- Divulgação de IA + checklist `09`/`18`.
