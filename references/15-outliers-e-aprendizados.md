# 15 — Outliers e aprendizados

Registro vivo do que funcionou no canal do usuário. **Atualize após cada rodada D+2/D+7.**

## Cold File Diaries — outliers de Short (dados do usuário)
- **Cooper (video02)** ~1.213 views · **Springfield (video03)** ~1.210 · **Yuba (video05)** ~1.2K.
- Regras TRAVADAS derivadas deles (ver `canais/cold-file-diaries-operacao.md`):
  - **PADRÃO SHORT 2 VENCEDOR** — não mexer no video02 (está viral).
  - **PADRÃO SHORT 3** — hook 0–3s = impossibilidade completa (≤3 fragmentos ou pergunta em 2ª pessoa); sem data/local/abstração no hook; karaokê conta a história no mudo; corte em loop aberto.
  - **PADRÃO SHORT 4 TEASE** (video23+) — 32s: hook 0–8s + 2 blocos do meio + CTA falado específico.
- Longs ficaram em ~20–25 views (48h) no período analisado.
- Thumbs finais dos outliers: `video02|03|05/04_video_final/thumb_videoNN_v2_*`.

## Status na época
- Cold File Diaries: ~14 inscritos, ~2.434 views/28d; top 48h = Short Cooper + Short Springfield.

## Lições a extrair quando tiver os prints
Anotar por outlier:
- **Hook** (primeira frase/frame).
- **Tipo de tema** e **série**.
- **Formato** (duração, ritmo).
- **Thumb** (variante vencedora A/B/C).
- **Fonte de tráfego** (feed, busca, sugerido).

## Protocolo de análise (rodar sempre)
1. Abrir Analytics → Shorts → ordenar por views.
2. Para o top 3, preencher a tabela abaixo.
3. Comparar vs mediana do canal (não vs benchmark genérico).
4. Replicar o **padrão** (não a frase exata) nos próximos 4–6 vídeos.
5. Registrar o que NÃO funcionou também.

## Tabela de outliers (preencher)

| # | Título | Tipo | Duração | Hook | Thumb | Views | Retenção | Subs | Lição |
|---|---|---|---|---|---|---|---|---|---|
| 02 | Cooper | | | | | ~1.213 | | | |
| 03 | Springfield | | | | | ~1.210 | | | |
| 05 | Yuba | | | | | ~1.2K | | | |
| | | | | | | | | | |

## Loop D+2/D+7
- Rodar `revisao_d2.py` → log em `00_CANAL/revisoes.csv`.
- Métricas: views, engaged views, shown-in-feed, chose-to-view %, AVD, % viewed, likes/coments/subs.
- Ação: dobrar no que ganhou; consertar 1 variável por vez no que perdeu.

> Cole aqui os prints/dados assim que tiver — a skill usa isso para calibrar hooks e thumbs do canal.
