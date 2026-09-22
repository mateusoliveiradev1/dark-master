# Evidência — Pandemias e pragas

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "history of pandemics documentary" --max 8` + `python scripts/niche_scan.py --cluster "plague documentary"` + websearch
> Brief completo: `data/briefs/history-of-pandemics-documentary.md` · JSON: `data/briefs/history-of-pandemics-documentary.json`
> Custo: ~300 unidades de quota da Data API (2 scans). `--trends` retornou HTTP 429 (rate limit) na coleta — não repetido.

## Veredito: **REPROVA** (borderline)

- Canais pequenos analisados: **16** (8 por busca) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **1 canal** (Past Stories, 22,1× = flare) — abaixo do critério de fome (≥2 canais) e do tier PARCIAL do README
- Emergentes (≤90d + 2/3 gates): **1** (The Untold Chronicle, 74d)
- Autocomplete: **88 termos** (meta ≥15) | Trends: sem dados na coleta (429)
- Sinal qualitativo: **5 dos 16 canais ficam a um gate de distância** (só falham a idade ≤45d), com velocidades de 23k–437k views/dia — categoria aquecida, mas nenhum canal novo comprovadamente rompendo no cruzamento.

## Busca 1 — brief `history of pandemics documentary` (--max 8)

49 canais encontrados · 29 pequenos (≤365d) · 8 analisados. **0 passam os 3 gates.** Gates na ordem idade≤45d / 5 primeiros ≥10k / ≥1k views-dia.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| HISTORY SEDATED | 4.360 | 256d | 1.076 | 1.106 | 011 | 0 |
| Before Us | 542 | 80d | 12.430 | 403 | 010 | 0 |
| Blunderprint | 114 | 51d | 4.051 | 1.810 | 001 | 0 |
| **The Untold Chronicle** | 370 | 74d | 15.222 | 1.184 | 0**11** | 0 — **EMERGENTE** |
| World in stories | 2.380 | 230d | 2.559 | 1.585 | 001 | 0 |
| Kidknowshistory | 33 | 61d | 4.949 | 134 | 000 | 0 |
| The Curious World | 119 | 86d | 3.672 | 197 | 000 | 0 |
| El Último Registro | 181 | 70d | 1.755 | 921 | 000 | 0 |

## Busca 2 — cluster `plague documentary` (única segunda busca permitida; `epidemic history documentary` não executada)

47 canais encontrados · 28 pequenos (≤365d) · 8 analisados. **0 passam os 3 gates. 1 outlier.**

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| NARD Archives | 13.400 | 109d | 2.194.363 | 31.042 | 0**11** | 0 |
| Dulciana Sklarp | 19.500 | 293d | 774.917 | 437.550 | 0**11** | 0 |
| TravelTV | 1.800 | 112d | 5.245 | 2.727 | 001 | 0 |
| Istoriecuai | 3.620 | 129d | 36.404 | 23.032 | 0**11** | 0 |
| Past Stories | 100 | 172d | 170 | 181 | 000 | **1 — 22,1×** |
| Truth And Dare | 63 | 163d | 4.610 | 226 | 000 | 0 |
| The story of Jesus | 7.690 | 83d | 7.896 | 20.608 | 001 | 0 |
| Dark Verdict | 8.190 | 151d | 40.557 | 16.896 | 0**11** | 0 |

## Outliers (janela de 2–6 semanas)

- **Past Stories** — **22,1×** — 8.059 views — "1994 Surat Plague: क्या डर ने पूरे शहर को खाली कर दिया था?" — 2026-07-13 — padrão: surto esquecido + memória local (Surat, 1994), título-pergunta em Hindi num canal de 100 subs. ≥10× = **flare**; único da coleta.

## Fome do algoritmo (cluster cross-canal)

1 canal com outlier ≥3× — **não atinge o critério de fome** (≥2 canais no mesmo tema). A busca por `plague documentary` retornou velocidade alta em canais maiores, sem outliers internos: NARD Archives (31.042/dia), Dulciana Sklarp (437.550/dia), Istoriecuai (23.032/dia), Dark Verdict (16.896/dia) — todos fora do gate de idade ≤45d.

## Demanda (autocomplete — 88 termos)

- Termos: "uk", "in hindi", "by country", "bbc", "channel 4", "channel 5", "documentary documentary", "explained", "episode 1", "full", "part 1/2/3", "reaction", "netflix", "national geographic", "zombies".
- Leitura: demanda por **série em partes**, versões regionais e "explicado"; cauda longa contaminada por ruído (gacha, roblox, xqc, yfn lucci) → termo amplo; estreitar por surto específico na revalidação.

## Trends (YouTube 12m)

- `history of pandemics documentary`: sem dados.
- `plague documentary` e `black death`: HTTP 429 (rate limit) na coleta — **pendente**, repetir na próxima rodada.

## Comentários (demanda explícita)

Não coletado — `--comments` exige escopo `youtube.force-ssl` no `yt_auth.py` (falta rodar) e nenhum VIDEOID do cruzamento foi priorizado. Sinal indireto (Reddit): pedidos recorrentes de "good Black Death documentary" (r/Documentaries, r/history, r/historyteachers, threads 2011–2021) e comentário de que os docs antigos ficaram desatualizados pela ciência (pulgas humanas vs ratos) → lacuna para conteúdo atualizado.

## Fontes web (2+)

- https://www.youtube.com/watch?v=FtpXiT9mcoU — Walter Reconstructs History (19,4K subs): Peste Negra em 1348, **36.287 views em ~3 meses** (mai/2026), 41 min com capítulos, fontes acadêmicas citadas (DeWitte 2014 PLOS ONE; Green 2020 AHR; Spyrou 2022 Nature; Benedictow 2021) e disclaimer de reconstrução assistida por IA — formato convergente e teto modesto.
- https://theforgottenhistory.com/watch/fGjPg_RQJoQ — "This Is How You Survived a Plague Town", 25:41, **~4K views** (jul/2026), fontes na descrição (worldhistory.org, The Conversation, PMC, UCLA) — formato "arquivo + mito desmontado" ainda com audiência pequena.
- https://www.linkedin.com/posts/stephen-ngene-88184431_faceless-youtube-automation-channel-case-activity-7436818094670585857-aZvA — case faceless de documentário histórico: 256K subs, 31 uploads, 25,3M views, **RPM $8–12 [ALEGADO]**.
- https://www.linkedin.com/posts/im-saif-91a481371_passiveincome-youtube-youtubeautomation-activity-7418189542492643328-gl_Q — dark history faceless: 5K subs, ~20 vídeos, 50–110K views/upload [ALEGADO].
- https://blog.kliptory.com/how-to-make-faceless-youtube-documentaries/ — guia 2026 do formato documentário faceless; acervos públicos (Library of Congress, Internet Archive, Wikimedia).
- https://support.google.com/youtube/answer/1311392?hl=en — política de monetização (conteúdo inautêntico; 3 categorias após 16/07/2026).
- https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ — clarificação de 16/07/2026 (genérico/repetitivo, off-putting, persona de especialista).
- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage — jun/2026: 16 canais terminados em jan/2026 (35M de inscritos somados); faceless como dano colateral do crackdown.
- https://creatorblade.com/blog/youtube-inauthentic-content-policy-2026-stay-monetized — "formato pode repetir, substância não"; avaliação no nível do canal; 1 peça de pesquisa primária por vídeo.
- https://newmoneymatrix.org/youtube-inauthentic-content-policy-explained/ — faceless segue monetizável se cada vídeo tiver perspectiva original.
- https://www.reddit.com/r/Documentaries/comments/k8hig/ — demanda recorrente por documentário de peste; comentário sobre ciência desatualizada (pulgas humanas vs ratos).
- https://blog.terabox.com/insights/build-faceless-ai-history-channel-youtube-monetization — workflow "automatizado" de canal de história com IA; usar como **alerta de risco** (é o padrão que a política de jul/2026 penaliza), não como método.

## Saturação e riscos observados

- O formato genérico (explicador de Peste Negra de 10–30 min) está **saturado em 2026**: múltiplos uploads recentes identificados (Walter Reconstructs History 36.287 views; PON – Rediscovered History; Your Highness; Tim - Reborn History; Beyond the Bell; True Past 15,7K views) e um canal com pesquisa séria e fonte em tela (The Forgotten, 25:41) com ~4K views. O cruzamento nu não está entregando teto — a saída é estreitar ângulo (abaixo), não escalar volume.
- Riscos: política de conteúdo inautêntico (jul/2026) avaliada **no nível do canal** e com bucket "off-putting" para morte/doença; persona de especialista em saúde proibida de monetizar; dano colateral a faceless mesmo sem IA (TNW); disclosure de mídia sintética realista quando a arte puder enganar; perseguições históricas (pogroms de 1349) exigem tratamento sóbrio.
- Ainda admite canal novo? Só com ângulo comprovadamente estreito e prova de pesquisa (arquivo municipal, arqueogenética atual, surto fora da Europa). **Não** lançar como "mais um canal de Peste Negra".

## Queries mais estreitas (não executadas — quota)

- `black death quarantine rules documentary`
- `justinian plague documentary`
- `surat 1994 plague documentary`
- `cholera broad street pump documentary`
- `lazaretto venice documentary`
- `1918 flu documentary`
- `plague doctor myth documentary`

> Revalidar em 2–4 semanas com `--brief` numa destas; exigir ≥3 canais passando os 3 gates (ou o critério PARCIAL: fome ≥2 canais ou múltiplos emergentes ≤90d). Watchlist: The Untold Chronicle (74d, emergente 2/3), NARD Archives (109d, 2/3), Istoriecuai (129d, 2/3), Dark Verdict (151d, 2/3), Dulciana Sklarp (293d, 2/3).
