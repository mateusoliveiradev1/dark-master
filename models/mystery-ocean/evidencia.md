# Evidência — Oceano profundo

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "deep sea mystery documentary" --max 8` + `python scripts/niche_scan.py --cluster "lost at sea documentary" --max 8` + autocomplete (`--suggest "lost at sea"`, `--suggest "ocean mystery"`) + websearch
> Brief completo: `data/briefs/deep-sea-mystery-documentary.md` · JSON: `data/briefs/deep-sea-mystery-documentary.json`
> A saída bruta do cluster `lost at sea documentary` não foi salva em arquivo (execução manual, limite de 1 segunda busca); é reproduzível pelo comando acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: **14 únicos** (8 no brief + 8 no cluster; 2 repetidos entre scans) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **4 canais no brief + 4 no cluster** (8 únicos) — sinal: **sim**, com flares de 1.431,9× e 1.169,3×
- Emergentes (≤90d + 2/3 gates): **5 canais únicos** — Atlas One, Hidden Earth, The Ocean Planet, Ice Cold History, Atlas of Civilizations
- Autocomplete: 100 termos no brief + 302 (`lost at sea`) + 171 (`ocean mystery`) | Trends: **não coletado** (429 nas duas tentativas)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido** — mas **16 de 16 análises falham apenas o gate de idade** e passam os outros dois (5 primeiros ≥10k e ≥1k views/dia), o mesmo padrão da rodada 1 de true crime. Há fome cross-canal em **dois** recortes (deep sea em ago/2026; lost at sea/survival em jul–set/2026), flares extremos em canais minúsculos e profundidade de busca alta em três eixos. Não é PASSA (nenhum canal ≤45d cruzou os 3 gates) e não é REPROVA (o formato está performando com sobra nos gates 2–3 e há fome recente). Revalidar em 2–4 semanas, olhando especificamente por entrantes ≤45d.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| Underwater Earth 4K (brief) | 25.300 | 130d | 900.884 | 41.907 | 011 | 12,7× — 359.886 — Mariana Trench — 2026-08-21 · 11,3× — 320.926 — Bermuda Triangle — 2026-08-12 · 3,4× — 95.949 — The Deep Ocean — 2026-08-23 |
| Shivan Decode (brief) | 4.320 | 294d | 14.318 | 16.099 | 011 | 1.431,9× — 3.513.928 — Mariana Trench: What Really Exists 11 KM Below — 2026-08-10 |
| GaiaDocs (brief) | 56.000 | 272d | 4.556.433 | 97.898 | 011 | — |
| Shadow Tales (brief) | 3.370 | 198d | 690.556 | 6.409 | 011 | 822,5× — 587.269 — Pacífico profundo (título em bengali) — 2026-08-24 |
| Hidden Planet Docs (brief) | 93.600 | 211d | 2.930.055 | 27.505 | 011 | — |
| Amaan Investigates (brief) | 26.000 | 178d | 301.770 | 15.057 | 011 | 4,5× — 398.757 — What's In the Ocean? — 2026-08-21 |
| Uncharted Depths (brief) | 29.800 | 319d | 23.367 | 30.054 | 011 | — |
| **The Ocean Planet (brief + cluster)** | **3.790** | **71d** | **115.132** | **16.378** | **011** | — |
| Atlas One (cluster) | 3.670 | 66d | 138.751 | 32.060 | 011 | 1.169,3× — 1.593.729 — Left On An Island For 15 Years — 2026-09-08 |
| Beers Homrez (cluster) | 157.000 | 287d | 101.010 | 380.906 | 011 | — |
| THE GEO VIBE (cluster) | 17.400 | 309d | 242.690 | 18.220 | 011 | 23,6× — 487.763 — 24 dias no Caribe (hindi) — 2026-07-31 |
| Hidden Earth (cluster) | 2.070 | 74d | 398.674 | 12.166 | 011 | 61,4× — 133.979 — The Impossible 76-Day Survival in the Atlantic — 2026-09-06 |
| Ice Cold History (cluster) | 2.070 | 68d | 60.170 | 6.214 | 011 | 227,3× — 105.022 — India's Lost Cities Found 120 Feet Under — 2026-09-19 |
| Atlas of Civilizations (cluster) | 21.900 | 68d | 15.197 | 74.113 | 011 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a **idade** falha. Brief: 35 canais encontrados, 12 pequenos ≤365d, 8 analisados (quota). Cluster: 47 encontrados, 24 pequenos/jovens, 8 analisados (quota). IDs dos canais do brief estão no JSON; a saída do cluster não foi persistida em arquivo.

## Outliers (janela de 2–6 semanas)

- **Shivan Decode** — 1.431,9× — 3.513.928 views — "Mariana Trench: What Really Exists 11 KM Below the Ocean?" — 2026-08-10 — padrão: pergunta de profundidade extrema + framing de mistério do que existe lá embaixo (canal de 4,3k subs → flare).
- **Atlas One** — 1.169,3× — 1.593.729 views — "They Were Left On An Island For 15 Years: True Survival Story" — 2026-09-08 — padrão: sobrevivência extrema real com "true story" no título (canal de 3,7k subs, 66 dias).
- **Shadow Tales** — 822,5× — 587.269 views — título em bengali sobre o Pacífico profundo — 2026-08-24 — padrão: mesmo tema deep sea em outro idioma; canal de 3,4k subs.
- **Ice Cold History** — 227,3× — 105.022 views — "India's Lost Cities Found 120 Feet Under…" — 2026-09-19 — padrão: arqueologia subaquática + descoberta recente; janela de 2 semanas.
- **Hidden Earth** — 61,4× — 133.979 views — "The Impossible 76-Day Survival in the Atlantic Ocean" — 2026-09-06 — canal de 2,1k subs e 74 dias.
- **THE GEO VIBE** — 23,6× — 487.763 views — "24 दिन Caribbean Sea में कैसे बचा?" — 2026-07-31 — sobrevivência no mar em hindi; quase 500k views.
- **Underwater Earth 4K** — 12,7× / 11,3× / 3,4× — 359.886 / 320.926 / 95.949 views — Mariana Trench, Bermuda Triangle e Deep Ocean, todos em ago/2026 — convergência de tema no mesmo canal em 12 dias.
- **Amaan Investigates** — 4,5× — 398.757 views — "What's In the Ocean?" — 2026-08-21.

> Nota metodológica: ratios altos em canais de 2–4k subs vêm de medianas baixas. O que importa aqui é o **viewport absoluto** (105k–3,5M views) em canais pequenos e recentes, que sustenta a fome.

## Fome do algoritmo (cluster cross-canal)

**Sim, em dois recortes:**

1. **Deep sea/Mariana (ago/2026):** Shivan Decode (08/10, 3,5M), Underwater Earth 4K (08/21, 359k; 08/12, 320k), Amaan Investigates (08/21, 398k) e Shadow Tales (08/24, 587k) — 4 canais diferentes em 3 semanas, com o mesmo tema "o que existe no fundo". Janela clássica de 2–6 semanas já parcialmente consumida (o flare é de 6 semanas atrás).
2. **Lost at sea/survival (jul–set/2026):** THE GEO VIBE (07/31, 487k), Hidden Earth (09/06, 133k), Atlas One (09/08, 1,59M) e Ice Cold History (09/19, 105k) — fome **fresca** (setembro) e ângulo menos saturado no EN faceless (sobrevivência + arqueologia subaquática).

## Demanda (autocomplete — top termos)

- Brief `deep sea mystery documentary`: **100 termos**. Destaques: `deep sea mystery documentary`, `mystery creatures of deep sea documentary`, `deep ocean mysteries`, `deep sea mystery documentary solved`, `deep sea mystery documentary real stories`, `deep sea mystery documentary lost`, `deep sea mystery documentary scary`, `deep sea mystery documentary yacht`, `deep sea mystery documentary series`, `deep sea mystery documentary national geographic`, `deep sea mystery documentary bbc`.
- `ocean mystery`: **171 termos**. Destaques: `ocean mystery documentary`, `ocean mysteries caught on camera`, `ocean mysteries bloop`, `deep ocean mysteries and wonders`, `sea mystery documentary`, `atlantic ocean mystery`, `ocean mystery stories`, `ocean mystery sound`; vários idiomas (hindi/tamil/telugu/malayalam/bangla).
- `lost at sea`: **302 termos** (ruidoso — música e jogos no meio). Termos de demanda real: `lost at sea story`, `lost at sea survival`, `lost at sea documentary`, `lost at sea steven callahan`, `stranded at sea`, `lost at sea at night`, `lost at sea book`, `lost at sea but never forgotten`.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` e retry de `--trends "deep sea documentary"` retornaram **HTTP 429** (rate limit do Google) em 2026-09-22. Fallback usado: autocomplete (profundidade alta nos três eixos). Revalidar com `--trends "deep sea documentary"` em outro horário.

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` (yt_auth sem o escopo `youtube.force-ssl`; tentativa em vídeo do recorte Point Nemo, `eHeT1G0I2jc`). Repetir depois de `python scripts/yt_auth.py`. O autocomplete `lost at sea steven callahan` sugere demanda explícita pelo caso Callahan nos eixos de sobrevivência.

## Convergência de formato (últimos uploads)

- **The Ocean Planet** (mirror divert.stream): últimos uploads são todos "FULL DOCUMENTARY" de ~3h, quase diários — "THE FINAL JOURNEY | Untold Stories of Ships That Never Returned", "DEEP SEA CREATURES", "PACIFIC ABYSS", "THE DEEP OCEAN", "EXTREME OCEAN" — convergência total em biblioteca longa; views recentes entre ~200 e 21k sugerem que o volume alto não garante tração (e que a versão commodity do nicho já existe).
- **Underwater Earth 4K**: 3 outliers na mesma janela (Bermuda, Mariana, abismo) — formato "mistério do fundo" convergente.
- **Atlas One / Hidden Earth / THE GEO VIBE**: sobrevivência no mar como formato único (1 caso = 1 vídeo).

## Fontes web (2+)

- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage — jun/2026: em jan/2026 o YouTube terminou 16 canais (35M de inscritos somados, ~US$10M/ano) sob a política de conteúdo inautêntico; algoritmo passou a favorecer rostos; enforcement no nível do canal (últimos 30 uploads); conteúdo educacional de nicho segurou melhor que canal amplo. Risco central do modelo.
- https://support.google.com/youtube/answer/1311392 — [OFICIAL] políticas de monetização: conteúdo "original e autêntico"; atualização de 15/07/2025 renomeia "repetitious" para "inauthentic"; mass-produzido/repetitivo/templated é inelegível. Base para a regra "1 peça primária por vídeo + estrutura variada".
- https://blog.autonolab.com/niches/2025-11-29-faceless-youtube-documentary — auditoria do nicho documentary: média de RPM **$12,6** [ALEGADO]; caso de validação do tema: New Nature, "This Discovery in the Mariana Trench…" com **11,8M views**; Uncovering, "Why Planes Disappear in the Bermuda Triangle" com **4,2M**; Everything Explained, "Drake Passage" com **3,1M**. Página marcada como "legacy research" — usar como histórico, não como dado atual.
- https://www.overseeros.com/blog/faceless-youtube-benchmark-report-2026 — benchmark de nichos faceless 2026: "true crime and mystery" = probabilidade média, formato narrative documentary, risco principal saturação/ética/carga de pesquisa; documentary explainer = alta probabilidade; validação em sprint de 30 uploads.
- https://www.youtube.com/@OceanlinerDesigns + https://www.oceanlinerdesigns.com/ — player estabelecido adjacente: 917k–927k subs, 539–542 vídeos, história marítima (Titanic, Lusitania, Gustloff com 334k views em 3 semanas; "MV Explorer's Sinking" 986k). Mostra o teto do segmento e o padrão "pesquisador com rosto".
- https://www.youtube.com/parttimeexplorer — 483k–485k subs, 183–184 vídeos; "The Mysterious Wreck of the Glenesslin (Oregon, 1913)" **811k views**; "The Disappearance of the SS Pacific (1856)" **701k views** — demanda provada para "naufrágio inexplicado" e "desaparecimento de navio".
- https://divert.stream/channel/UCFZ_h_YPm3lRy_Eg4mxqMfA — mirror do canal-evidência The Ocean Planet (3h "FULL DOCUMENTARY" quase diário; "THE FINAL JOURNEY | Ships That Never Returned" no mesmo dia da coleta) — convergência de formato e alerta de produção em massa.
- https://milx.app/en/trends/youtube-cpm-rpm-rates-2026-average-niches-countries-more — RPM/CPM 2026 por nicho e país (US CPM ~$14,67; Education $3–8) [ALEGADO]; não há linha de "documentary" — reforça que a classe $8–14 é estimativa de mercado.
- https://air.io/en/monetization/what-rpm-can-you-expect-from-shorts-in-2026 — Shorts RPM US médio **$0,328** no dataset da AIR [ALEGADO]; contraste que justifica o lane long-first.
- https://www.youtube.com/playlist?list=PLi-ZkGJwoGVQMX1NTCVgpfFiLnQfFr3l — playlist "Ocean Documentaries 2026" (feed do nicho: "darkest corners", criaturas, batalhas submarinas) — mostra a linguagem vigente e o risco de resvalar para o sensacionalismo.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalvas: (a) o recorte "deep sea/Mariana explainer" já tem múltiplos flares em ago/2026 — copiar o padrão puro tende a saturar nas próximas semanas; (b) o recorte "lost at sea/survival" está **fresco** (set/2026) e menos servido no EN faceless — melhor aposta para o piloto; (c) o lado "história marítima de naufrágios" tem players fortes com rosto (Oceanliner Designs 917k, Part-Time Explorer 483k) — um canal faceless deve vencer pelo arquivo + ciência (inquérito, batimetria, expedição), não pela mesma promessa de "especialista na tela"; (d) The Ocean Planet já mass-produz 3h de doc oceânico quase diário — a versão commodity existe; a diferenciação é pesquisa primária e estrutura própria (e é o que a política de conteúdo inautêntico cobra).
- **Gargalo real:** o gate de idade é o único que reprova (16/16 análises passam os gates 2 e 3). A pergunta da revalidação é se **novos entrantes ≤45d** aparecem — em 2–4 semanas o tier emergente atual (66–74d) estará fora da janela, sendo substituído ou não.
- **Riscos de advertiser/compliance:** mortes em naufrágios (não gráfico + contexto educacional tende a monetizar; imagem gráfica ou thumbnail de tragédia derruba); naufrágios de guerra = túmulos; precisão (casos com teorias conspiratórias precisam de rótulo explícito); direitos de footage jornalístico/arquivo; tragédias recentes (respeito às famílias, sem timing de oportunismo).

## Queries mais estreitas (se REPROVA)

- **Executada:** `lost at sea documentary` (cluster; 47 encontrados → 24 pequenos/jovens → 8 analisados; 0 gates; 5 emergentes; 4 com fome).
- **Não executadas (limite de 1 segunda busca):** `mariana trench documentary` e `unexplained disappearance at sea` — usar na revalidação de 2–4 semanas, junto com o filtro `--age 45` para forçar o corte da idade.
