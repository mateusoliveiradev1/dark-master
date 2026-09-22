# Canal — Laudo Final (dark-forense)

## Identidade
- Nome público: **Laudo Final** · handle **@LaudoFinalBR**
- Idioma: **PT-BR** · Gênero: **true crime por perícia forense**
- 3 séries: **PERÍCIA RESOLVE · ARQUIVOS FRIOS · MENTE CRIMINOSA**
- Cadência: 1 long/dia (21h) + 1 Short (12h BRT).

## Branding
- Paleta: `#0A0A0C` · `#B91C1C` · `#EBB41E` · `#F5F5F4`
- Fontes: Bebas Neue + Inter.
- Abertura fixa: **"O laudo não mente."** — pausa — depois o detalhe forense mais estranho (não o crime).

## Voz
- Oficial em transição: `gerar_voz_pt.py` usa **`fr-FR-RemyMultilingualNeural`** (PT), alternativa `pt-BR-AntonioNeural`;
  `gerar_voz_gemini.py` (Algenib) e `gerar_voz_fish.py` (clone) disponíveis.
- **Inconsistência a resolver:** docs citam Antonio, Remy e Algenib. Escolher 1 voz oficial e travar.
- Não clonar voz de pessoas reais. Lab XTTS/F5 existe mas está desativado.

## Formato
- ~10 min (~1.400 palavras), 18–22 imagens Nano Banana (sem gore).
- Template de roteiro: HOOK 130w · CONTEXTO 350 · PRESSÃO 250 · O DIA 450 · **PERÍCIA 400** · FAMÍLIA 150 · TEORIAS 250 · CHAVES+OUTRO+TEASER 150.

## Projeto no disco
`D:\dark-forense`
- `canal/` (branding, identidade forense, protocolo anti-inauthentic, metadata, kit Nano Banana, keys).
- `scripts/` (~40 scripts) — orquestrador `build_video.py`.
- `videos/video01` (Eliza Samudio) completo.

## Invariantes
- GATE 100% de imagens.
- Suspeito vivo → "suspeito/acusado".
- 2+ fontes BR.
- Checklist de perfeição (`canal/CHECKLIST_PERFEICAO_PT.txt`).

## Status
- video01 completo; video02/03 scaffolded.
- 3ª língua/mercado (PT) → auto-dub abre EN.
