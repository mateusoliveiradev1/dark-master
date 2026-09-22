# 15 — Outliers e aprendizados

Registro vivo do que funcionou no canal do usuário. **Atualize após cada rodada D+2/D+7.**

## Dados reais (API, 21/09/2026)

| Vídeo | Formato | Views | Engaged | AVD | AVP% | Watch h | Subs |
|---|---|---|---|---|---|---|---|
| Yuba County Five | short | 1202 | 498 | 14s | 43.8% | 2.27 | 1 |
| D.B. Cooper ($200k) | short | 1190 | 451 | 22s | 67.2% | 3.05 | 1 |
| **Springfield Three** | **short** | 1180 | 532 | 47s | **136.7% (loop)** | **7.25** | **4** |
| Gardner Heist | long | 70 | 18 | 25s | 71.5% | 0.13 | 1 |
| Zodiac Killer | long | 66 | 22 | **907s** | — | 5.55 | 0 |
| D.B. Cooper (long) | long | 27 | 22 | 134s | 20.6% | 0.82 | 3 |
| Sodder Children | long | 20 | 18 | 114s | 16.0% | 0.57 | **5** |
| (demais longs) | long | 0–25 | | | | | |

**Total watch hours (30d): ~26h.**

### Leituras
- **O loop é o sinal mais forte:** Springfield (AVP >100%) rendeu mais watch time (7,25h) e inscritos (4).
- **O long retém quem chega** (Zodiac 907s; Sodder 20 views → 5 inscritos) — **falta é tráfego**.
- **3 Shorts outliers a ~48x a mediana** = o padrão a escalar.

## Cold File Diaries — outliers de Short (dados do usuário)
- **Cooper (video02)** ~1.213 views · **Springfield (video03)** ~1.210 · **Yuba (video05)** ~1.2K.
- Regras TRAVADAS derivadas deles (ver `playbooks/cold-file-diaries/operacao.md`):
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
