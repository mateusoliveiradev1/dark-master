# Evidência — Surtos e bio-riscos (investigação de surtos modernos)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "outbreak investigation documentary" --max 8` + `python scripts/niche_scan.py --cluster "patient zero documentary"` + websearch
> Brief completo: `data/briefs/outbreak-investigation-documentary.md` · JSON: `data/briefs/outbreak-investigation-documentary.json`
> Custo: ~300 unidades da Data API (2 scans). `--trends` retornou HTTP 429 nas duas tentativas (busca 1 e termo `patient zero`); `--comments` retornou `insufficientPermissions` (escopo `force-ssl` ausente no `yt_auth.py`).

## Veredito: **REPROVA**

- Canais pequenos analisados: **15** (7 na busca 1 + 8 no cluster; Viral Insight aparece nas duas) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **1 canal** (Just Lokesh, 5,7×) — abaixo do critério de fome (≥2 canais) e do tier PARCIAL do README
- Emergentes (≤90d + 2/3 gates): **0**
- Autocomplete: **96 termos** (meta ≥15), catálogo poluído por ruído pop
- Trends: **não coletado** (429 nas duas tentativas) — pendente
- Sinal qualitativo: o cruzamento atrai canais-agregador de notícia/curiosidade de baixíssima tração; nenhum canal novo provando formato. Existe janela de notícia real (Ebola RDC 2026 = 2º maior surto de Ebola registrado), mas ela é por **caso nomeado**, não pelo termo amplo.

## Busca 1 — brief `outbreak investigation documentary` (--max 8)

7 canais pequenos analisados. **0 passam os 3 gates.** Gates na ordem idade≤45d / 5 primeiros ≥10k / ≥1k views-dia.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Daily Search Buzz | 572 | 55d | 1.635 | 471 | 000 | 0 |
| CosmoX | 36 | 75d | 3.185 | 234 | 000 | 0 |
| Viral Insight | 946 | 141d | 3.568 | 677 | 000 | 0 |
| The Catastrophe File | 702 | 49d | 121 | 181 | 000 | 0 |
| Future Pulse | 1.020 | 123d | 3.003 | 956 | 000 | 0 |
| The Autopsy Files | 17 | 102d | 60 | 49 | 000 | 0 |
| Case Line Docs | 13 | 158d | 37 | 8 | 000 | 0 |

> Perfil da amostra: nomes de "arquivo/catástrofe/vari edade" sem foco declarado de epidemiologia — são canais de tópico variado que tocam surtos entre outros assuntos. Nenhum publica uma série de investigação consistente.

## Busca 2 — cluster `patient zero documentary` (única segunda busca permitida)

18 canais encontrados · 10 pequenos (≤200k subs e ≤365d) · 8 analisados (quota). **0 passam os 3 gates. 1 outlier.**

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Viral Insight | 946 | 141d | 3.568 | 677 | 000 | 0 |
| 歴史の足跡 | 2.830 | 152d | 3.060 | 1.696 | 001 | 0 |
| Vixol95 | 42 | 84d | 1.530 | 97 | 000 | 0 |
| Just Lokesh | 3 | 30d | 255 | 13 | 100 | **1 — 5,7×** |
| Six Axioms | 3 | 12d | 118 | 9 | 100 | 0 |
| Synerix Studio - Cinematic | 15 | 91d | 218 | 49 | 000 | 0 |
| World Crime Archives | 303 | 147d | 381 | 298 | 000 | 0 |
| Vedansh Maheshwari | 118 | 85d | 1 | 3.754 | 001 | 0 |

## Outliers (janela de 2–6 semanas)

- **Just Lokesh** — **5,7×** — 149 views — `He Was Called "Patient Zero"… But They Got It Wrong 😳 | AIDS` — 2026-09-05 — padrão: **correção do rótulo "patient zero"** (gancho de contradição verificada). Canal de 3 subs com mediana de 26 views → a razão é inflada por base minúscula; sem tração real e sem flare (≥10×).
- **Six Axioms** — canal de **12 dias** entrando no cruzamento (o feed ainda aceita entrantes <30d), mas com 118 views somadas nos 5 primeiros e 9 views/dia: entrada sem rompimento.

## Fome do algoritmo (cluster cross-canal)

1 canal com outlier ≥3× (Just Lokesh) — **não atinge o critério de fome** (≥2 canais no mesmo tema). O cluster `patient zero` é dominado por conteúdo de ficção/entretenimento (filmes, games, podcast) e por canais micro sem tração; o único sinal de "fome" apareceu no formato correção-de-rótulo, em escala microscópica.

## Demanda (autocomplete — 96 termos)

- Relevantes: `outbreak explained`, `outbreak epidemic`, `outbreak news today`, `outbreak investigation`, `outbreak investigation documentary covid`, `…india`, `…philippines`, `…bbc`, `…channel 4`, `…dw`, `…episode 1`, `…episode 2`, `…part 1/2/3`, `…full movie`, `…netflix`, `…national geographic`, `…crime investigation`, `…in hindi`.
- Ruído pesado: `black metal`, `lost ark`, `hailey bieber`, `roblox`, `johnny depp`, `gacha` → o termo principal é amplo e misto; a camada "documentary" mistura busca de catálogo (netflix/bbc) com curiosidade pop.
- Leitura: demanda por **série em partes** e por "explicado" se confirma; profundidade de cauda (96 termos) não é o gargalo — falta canal pequeno provando retenção no cruzamento.

## Trends (YouTube 12m)

- `outbreak investigation documentary` (via brief): HTTP 429 — não coletado.
- `patient zero`: HTTP 429 na segunda tentativa — **pendente**, repetir na próxima rodada. Fallback usado: `--suggest` (96 termos).

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` (o `yt_auth.py` está sem o escopo `force-ssl`). Tentativa feita no vídeo da FRONTLINE (`WG1aY5OOR2o`). Sinal indireto: Radiolab reexibiu "Patient Zero" em **21/08/2026** e podcasts de epidemiologia seguem ativos (`Patient Zero`, `Febrile #71`, `Epidemic`) → o arquétipo de investigação de surto mantém demanda em áudio, sem equivalente dark em vídeo mapeado.

## Fontes web (2+)

- https://www.reuters.com/world/africa/cracked-coffin-funeral-hunt-ebolas-patient-zero-2026-06-11 — investigação do "patient zero" no surto de Ebola/Bundibugyo na RDC: funeral de 04/02 como um dos primeiros superespalhamentos suspeitos, estirpe circulando 4–6 meses antes da confirmação em 15/05/2026, violência contra equipes de resposta. Caso-âncora da janela 2026.
- https://www.cdc.gov/mmwr/volumes/75/wr/mm7535e1.htm — MMWR: **5.458 casos confirmados e 2.606 mortes (48%)** até 21/08/2026; **2º maior surto de Ebola registrado**; 83% dos alertas investigados em 24h vs meta >90%.
- https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(26)00414-7/fulltext — revisão: 3.262 casos e 1.430+ mortes até 28/07/2026; vacinas e terapêuticas em ensaio (Solidarity PARTNERS); lacunas de preparação.
- https://www.pbs.org/wgbh/frontline/article/documentary-streaming-worlds-deadliest-ebola-outbreak — formato de referência: documentário-investigação contado pelas falhas da resposta internacional.
- https://www.youtube.com/watch?v=WG1aY5OOR2o — FRONTLINE "Outbreak": **4,4M views** no YouTube (documentário longo de investigação; teto de formato no nicho, canal grande).
- https://radiolab.org/podcast/patient-zero/transcript — Radiolab "Patient Zero" reexibido em 21/08/2026; o arquétipo é perene em áudio (e o rótulo, historicamente problemático).
- https://www.bbc.com/news/world-us-canada-53273382 — anatomia de superespalhamento (ensaio de coro: 61 presentes, 53 casos, 2 mortes) — modelo de reconstrução pessoa-lugar-tempo.
- https://support.google.com/youtube/answer/13813322?hl=en — política de desinformação médica: prevenção/tratamento/negação, com exceção para conteúdo educacional/documental.
- https://becomeviral.com/blog/faceless-youtube-health-wellness-niche — RPM [ALEGADO] saúde $8–18, medical/clinical $15–35 (exige autoridade), alerta YMYL.
- https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ — RPM médio $11,10 e mediana $10,10 em 98 nichos faceless [ALEGADO].
- https://www.usnews.com/news/health-news/articles/2026-01-30/most-doctor-made-youtube-health-videos-lack-strong-proof-study-finds — estudo JAMA: 62,5% dos vídeos de saúde feitos por médicos tinham evidência fraca/ausente; risco reputacional e de confiança do nicho.
- https://www.whiteglovecontent.com/niches/health — nota operacional [ALEGADO]: saúde monetiza como explicador educacional, não como conselho pessoal (evitar dose, cura, contra-guidance).

## Saturação e riscos observados

- O cruzamento amplo está **tomado por canais de tópico variado** (Daily Search Buzz, Viral Insight, CosmoX, Future Pulse, The Catastrophe File, The Autopsy Files, Case Line Docs), com 3–1.020 subs e 8–956 views/dia — nenhum formou audiência de epidemiologia. No cluster `patient zero`, o vizinho dominante é ficção/entretenimento. Não há evidência de que o termo nu admita canal novo passando os gates; a janela real é **por caso nomeado** (Ebola RDC 2026, superespalhamento, biossegurança) com peça primária.
- Riscos: (a) política de desinformação médica + balde "persona de IA em tema sensível" (saúde) — ref `09`; (b) "off-putting"/pânico em temas de morte e doença; (c) estigma e culpa a paciente zero (precedente Gaetan Dugas); (d) números de surto em curso mudam de semana a semana — a evidência envelhece rápido; (e) footage de agência de notícia = copyright/licença; (f) o padrão "doença massificada por IA" é um dos alvos explícitos da política de conteúdo inautêntico.
- Ainda admite canal novo? Só ancorado em **documento e caso nomeado** (MMWR/WHO/Reuters) e com série própria — não como "mais um canal de outbreak". Sem isso, REPROVA permanece.

## Queries mais estreitas (não executadas — quota)

- `ebola outbreak investigation documentary`
- `nipah virus outbreak documentary`
- `superspreader event documentary`
- `foodborne outbreak documentary`
- `smallpox birmingham 1978 documentary`
- `anthrax letters 2001 documentary`
- `h5n1 dairy cattle documentary`
- `wastewater surveillance documentary`

> Revalidar em 2–4 semanas com `--brief` numa destas; exigir ≥3 canais passando os 3 gates (ou o critério PARCIAL: fome ≥2 canais ou múltiplos emergentes ≤90d). Watchlist: **歴史の足跡** (152d, só o gate de views/dia, 1.696/dia), **Just Lokesh** (30d, outlier 5,7× microscópico), **Six Axioms** (12d, entrante <30d), **Vedansh Maheshwari** (85d, 3.754/dia), **Future Pulse** (123d, 956 views/dia — quase o gate de velocidade), **Viral Insight** (única presente nas duas buscas).
