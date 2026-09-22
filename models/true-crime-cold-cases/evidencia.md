# Evidência — Cold cases (EUA)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "cold case documentary" --max 8` + `python scripts/niche_scan.py --cluster "unsolved cold case documentary" --max 8` + websearch
> Brief completo: `data/briefs/cold-case-documentary.md` · JSON: `data/briefs/cold-case-documentary.json`
> A saída bruta do cluster não foi salva em arquivo (execução manual); é reproduzível pelo comando acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: 11 únicos (8 no brief + 3 novos no cluster) | passam os 3 gates: **1** (meta ≥3) — Cold Cases Solved
- Fome do algoritmo (outlier ≥3×): **4 canais em cada scan** — sinal: **sim** (fome cross-canal no mesmo tema)
- Autocomplete: 75 termos (meta ≥15) | Trends: **ESTÁVEL** (recente 69 vs anterior 63)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido** — 10 dos 11 canais falham **apenas a idade** (87–348d), o que mostra formato performando, mas janela de canal novo ainda não confirmada. Em compensação: 1 canal de 35 dias com outlier 29,4×, fome de algoritmo em 4 canais nos dois scans e convergência de 3 canais no mesmo padrão em 7 semanas. Não é REPROVA (há sinal real e recente) e não é PASSA (falta o 3º canal jovem). Revalidar em 2–3 semanas com `--cluster "cold case documentary" --age 45`.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Red File | 97.600 | 208d | 8.486.833 | 171.137 | 011 | 10,5× — 12.649.042 — 2026-08-12 |
| Othram Studios | 58.800 | 208d | 15.261 | 42.397 | 011 | — |
| Explorer Vault | 5.610 | 154d | 27.442 | 21.902 | 011 | — |
| DARK LOGS | 32.700 | 231d | 45.273 | 51.007 | 011 | — |
| ZDF True Crime | 97.900 | 333d | 1.281.534 | 106.974 | 011 | 3,2× — 527.781 — 2026-09-08 |
| Crimewatch Central | 27.000 | 165d | 236.377 | 12.626 | 011 | 8,4× — 272.823 — 2026-07-14 |
| Walter \| True Crime | 4.570 | 149d | 18.892 | 4.173 | 011 | — |
| Detective Michael | 62.100 | 348d | 431.530 | 22.980 | 011 | 12,6× — 218.248 — 2026-08-25 |
| New Discovery | 49.300 | 215d | 81.982 | 57.182 | 011 | — |
| Cold Case Redemption | 18.900 | 87d | 189.752 | 16.031 | 011 | 7,3× — 121.039 — 2026-08-22 |
| **Cold Cases Solved** | **7.850** | **35d** | **352.463** | **15.319** | **111** | **29,4× — 192.537 — 2026-09-05** |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a idade falha. Scan 1 (brief) analisou 30 canais encontrados, 11 pequenos ≤365d, 8 por quota — 0/8 passaram. Scan 2 (cluster estreito) analisou 8 — 1/8 passou.

## Outliers (janela de 2–6 semanas)

- **Cold Cases Solved** — 29,4× — 192.537 views — "WISCONSIN 1974 Cold Case Solved After 50 Years…" — 2026-09-05 — padrão: caso real resolvido por genetic genealogy (caso Mary Schlais, preso em 2024; stocking cap) + título `[STATE] [YEAR]` + payoff de justiça.
- **Red File** — 10,5× — 12.649.042 views — ""Friendly" Cop Has No Idea Police Already Matched Her DNA After 23 Years" — 2026-08-12 — padrão: footage de interrogatório + DNA que fecha o caso décadas depois (caso Stephanie Lazarus/Sherri Rasmussen, 1986).
- **Detective Michael** — 12,6× — 218.248 views — "Doctors Extracted Two Liters Of Semen From There | True Crime Documentary" — 2026-08-25 — padrão sensacionalista/gráfico: **anti-modelo** — título e enquadramento que puxam limited ads; não copiar.
- **Crimewatch Central** — 8,4× — 272.823 views — "Colorado 1984 Bennett Family Massacre Cold Case SOLVED — Arrest Shocks Community" — 2026-07-14.
- **Cold Case Redemption** — 7,3× — 121.039 views — "WASHINGTON 1989 Cold Case Solved — A Coworker Caught the Killer" — 2026-08-22.
- **ZDF True Crime** — 3,2× — 527.781 views — "Cold Case Kasernen-Mord…" — 2026-09-08 (canal alemão, fora do recorte EN).

## Fome do algoritmo (cluster cross-canal)

Sim. Três canais diferentes com outlier no **mesmo tema** em 7 semanas — Crimewatch Central (14/07), Cold Case Redemption (22/08) e Cold Cases Solved (05/09) — todos no padrão "Cold Case Solved / [STATE] [YEAR]"; e Red File com o padrão DNA + interrogatório (12/08). O scan 1 já apontava 4 canais com outlier ≥3× (Red File, ZDF, Crimewatch Central, Detective Michael) e o scan 2 manteve 4 (Red File, Crimewatch Central, Cold Case Redemption, Cold Cases Solved). Janela de 2–6 semanas aberta para o recorte "resolvido por DNA".

## Demanda (autocomplete — top termos)

75 termos únicos (meta ≥15). Destaques: `cold case documentary`, `cold case documentary full episodes`, `cold case documentary uk`, `cold case murders documentary`, `cold case crime documentary`, `cold case investigation documentary`, `old cold case documentary`, `mississippi cold case documentary`, `cold case murders solved documentary`, `cold case solved`, `cold case resolved`, `cold case files`, `cold case documentary real stories`.

## Trends (YouTube 12m)

- Direção: **ESTÁVEL** (média recente 69 vs anterior 63) · Rising: nenhuma query listada pelo script.
- Leitura: termo de busca durável, sem pico — combina com biblioteca evergreen, não com aposta de tendência.

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` (yt_auth sem o escopo `youtube.force-ssl`; não rodei re-auth). Repetir depois do `python scripts/yt_auth.py`.

## Fontes web (2+)

- https://becomeviral.com/blog/faceless-youtube-true-crime-niche — formato documentário de 15–25 min; cold cases entre os formatos faceless de maior performance; sub-nichos ainda abertos para um player dominante.
- https://faceless.my/niches/faceless-true-crime-channel/ — cold cases "fully documented" (casos antigos resolvidos são mais seguros que investigações ativas); 20–40 min; RPM $12–25 e sponsors VPN/legal [ALEGADO].
- https://support.google.com/youtube/answer/6162278 — política oficial de advertiser-friendly: contexto documentário/educacional pesa; gráfico focal (sangue/violência sem contexto) = limited/no ads.
- https://latenights.live/how-the-new-youtube-rules-affect-documentary-clips-and-true- — atualização de jan/2026: monetização cheia para temas sensíveis não gráficos; checklist (fontes no description, aviso de conteúdo, capítulos).
- https://longformstudio.app/articles/true-crime-youtube-channel — sub-formatos (cold case, forensic-focus); forensic-focus tem o menor risco de yellow icon; YPP dobra em 01/02/2027; RPM reportado $6–9 non-graphic [ALEGADO]; relatos de flags de inautenticidade em documentário roteirizado.
- https://quasa.io/media/depictions-of-death-can-earn-ads-context-still-decides-the-icon — taxonomia de ago/2026 para mortes em conteúdo documental (green/yellow/no-ads).
- https://reachranking.com/youtube/UCNpjH9MosivtBOa45Hbu39g — Red File (@redfilechannel): stats e descrição "real police footage sourced directly from law enforcement" (formato interrogatório).
- https://www.prweb.com/releases/othram-launches-othram-studios-to-bring-real-forensic-investigations-to-a-global-audience-302748147.html — Othram Studios (abr/2026): long-form science-driven sobre casos resolvidos por DNA forense; milhares de identificações.
- https://www.cnn.com/2024/11/08/us/mary-schlais-wisconsin-cold-case-killer-arrested — caso Mary Schlais (Wisconsin 1974, genetic genealogy) = caso do outlier 29,4×.
- https://www.cbsnews.com/news/bite-mark-dna-tie-lapd-detective-to-1986-murder/ — caso Stephanie Lazarus/Sherri Rasmussen (DNA em marca de mordida, 23 anos) = caso do outlier 10,5× do Red File.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalva: um canal de 35 dias fez 29,4×, mas o padrão `[STATE] [YEAR] Cold Case Solved` já tem 3 canais convergindo (jul–set/2026) — o recorte genérico de "caso resolvido" pode saturar em semanas. Diferenciar por: forensic-focus (DNA/genetic genealogy em profundidade, menor risco de ad-limit), casos ainda abertos/arquivados (não só resolvidos) e documento primário por episódio. O formato "interrogation footage" (Red File) é forte, mas mais pesado em direitos e em ad-risk.
- **Riscos de advertiser/compliance:** yellow icon por thumbnail/primeiros 15s gráficos ou títulos sensacionalistas (ver outlier do Detective Michael como anti-modelo); conteúdo inautêntico em documentário roteirizado; casos ativos exigem cuidado extra; famílias e "alleged" para pessoas vivas.

## Queries mais estreitas (se REPROVA)

- **Executada:** `unsolved cold case documentary` (cluster, 8 canais; 1 passou os 3 gates; fome em 4 canais).
- **Não executada (limite de 1 segunda busca):** `cold case files 2026` — manter para a revalidação de 2–3 semanas, junto com `--age 45`.
