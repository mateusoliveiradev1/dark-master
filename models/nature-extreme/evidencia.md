# Evidência — Catástrofes naturais

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "natural disaster documentary" --max 8` + retry estreito `python scripts/niche_scan.py --cluster "volcano documentary" --max 8` (Data API) + `--suggest` (HTTP livre) + checagem de convergência `--channel` (últimos uploads, com duração) + websearch.
> Brief completo: `data/briefs/natural-disaster-documentary.md` · JSON: `data/briefs/natural-disaster-documentary.json` (o cluster imprime em tela, não salva JSON).
> Quota: ~350 unidades (estimativa) de ~10.000/dia — 2 buscas pesadas (brief + cluster), 6 checagens de canal e resolução de handles; autocomplete/Trends são HTTP livre. O cluster de vulcões foi escolhido entre as duas opções do método porque o autocomplete deu 203 termos únicos contra 64 de "extreme weather documentary".

## Veredito: **PARCIAL**

- Canais pequenos analisados: 8 (ampla) + 8 (estreita) = **16** | passam os 3 gates: **0 + 1 = 1** (meta ≥3)
- Emergentes (≤90d + 2/3 gates): **4 + 2 = 6** — watchlist, não aprovam sozinhos
- Fome do algoritmo (outlier ≥3×): **4 + 3 = 7** canais (sinal: SIM nos dois cortes)
- Autocomplete: **87 + 203 = 290** termos (meta ≥15) | Trends: **429 nas duas consultas** (rate limit do Google; sem leitura própria — fallback autocomplete)

Leitura honesta: o cruzamento **ainda não fecha os 3 gates** (1 canal em 16 passa — Disaster Pulse, 28 dias, flare de 1.626,5×), mas **a demanda está quente nos dois cortes**: 6 emergentes (5 deles de 62–74 dias falhando só o gate de idade; 1 de 38 dias falhando só o gate dos 5 primeiros), 7 canais com outlier ≥3× (cinco deles com flare ≥10×) e profundidade de busca alta (290 termos; 203 só em vulcões). O gargalo continua sendo o gate de idade (≤45d), o mesmo padrão do resto da biblioteca. Sinal adicional: os rompimentos **maiores** estão em PT-BR e hindi (Um Documentário, Nature Khauf, Infinite Partways, Truth Untold) — o lane EN está mais jovem e menos cheio (The Last Day, Impossible Places Global, Disaster Pulse), o que é oportunidade e risco ao mesmo tempo. **Não escalar ainda**; revalidar em 2–4 semanas — se os emergentes cruzarem os 45 dias mantendo o desempenho, o modelo sobe para PASSA.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

### Busca 1 — `--brief "natural disaster documentary"` (41 canais achados; 12 pequenos e ≤365d; 8 analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Nature Khauf (@naturekhauf) | 57.500 | 69d | 16.019.889 | 276.918 | 011 | 4,9× — 6.865.469 — 2004 tsunami (hindi); 3,8× — 5.338.394 — Japan 2011 (**emergente**) |
| Shadow Frames (@shadowframes-global) | 24.700 | 262d | 2.827.324 | 38.179 | 011 | 44,1× — 6.057.460 — Kedarnath 2013 (hindi) |
| Um Documentário (@umdocumentario) | 83.000 | 163d | 3.186.513 | 152.243 | 011 | 12,1× — 5.454.987 — Miyako; 11,6× — 5.242.014 — Yungay; 3,2× — 1.459.094 — Galveston |
| The Last Day (@thelastday01) | 12.800 | 74d | 1.808.990 | 99.725 | 011 | 183,7× — 4.689.180 — Nepal 2026; 51,8× — 1.323.433 — megatsunami (**emergente**) |
| MTH Incredible Moments (@mthentertainment-us) | 18.100 | 100d | 2.640.482 | 137.197 | 011 | — |
| Extreme Disasters 01 (@extremedisasters01) | 23.700 | 65d | 27.416 | 489.965 | 011 | — (**emergente**; shorts de flood) |
| Unseen Earth 4K (@unseenearth4k1402) | 26.100 | 187d | 334.379 | 23.297 | 011 | — |
| 30sec science for you (@30secscienceforyou) | 4.750 | 38d | 6.409 | 91.622 | 101 | — (**emergente**) |

### Busca 2 — `--cluster "volcano documentary"` (44 canais achados; 16 pequenos e ≤365d; 8 analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| **Disaster Pulse** | 3.820 | **28d** | **101.360** | **28.916** | **111** | **1.626,5× — 689.642 — "ASIA'S DEADLIEST VOLCANO ERUPTS! Anak Krakatau..." (2026-09-06)** |
| Infinite Partways (@infinitepartways) | 26.000 | 62d | 1.232.693 | 256.404 | 011 | — (**emergente**; shorts em hindi) |
| Atlas of Civilizations | 21.900 | 68d | 15.197 | 74.113 | 011 | — (**emergente**; handle não resolvido) |
| Impossible Places Global (@impossibleplacesglobal) | 11.400 | 110d | 422.511 | 32.139 | 011 | 9,8× — 807.513 — "Living in Indonesia... Among Active Volcanoes" (2026-09-10) |
| Vanished Worlds | 17.200 | 119d | 37.575 | 25.174 | 011 | — |
| Truth Untold | 22.800 | 147d | 998.515 | 53.365 | 011 | 39,1× — 512.333 — vila no Irã entre rochas vulcânicas (hindi) |
| Documentary Overload | 40.500 | 346d | 195.333 | 24.298 | 011 | — |
| Krishna Docs | 3.510 | 246d | 152.081 | 5.475 | 011 | — |

> Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha). O cluster ranqueia os top-50 vídeos do tema em 90 dias e analisa os canais pequenos que aparecem ali; canais muito novos só entram se um vídeo já estiver nesse topo.

## Outliers (janela de 90 dias; oportunidade de 2–6 semanas quando recente)

- **Disaster Pulse — 1.626,5× (FLARE)** — 689.642 views — erupção do Anak Krakatau (set/2026), título de urgência ("ASIA'S DEADLIEST VOLCANO ERUPTS!") — 2026-09-06 — canal de 28 dias; mediana baixa (424) infla o ratio.
- **The Last Day — 183,7× (FLARE)** — 4.689.180 views — colapso de glaciar no Nepal (ago/2026), "The Glacier That Wiped Out a Valley", 19:19 — 2026-09-04 — padrão: evento recente + relógio + documento longo; o mesmo canal fez um segundo vídeo do tema (2026-09-08) e colheu só 53k — sinal de saturação rápida do ângulo.
- **The Last Day — 51,8× (FLARE)** — 1.323.433 views — "The Wave That Was Taller Than a Skyscraper", 12:32 — 2026-07-18 — megatsunami evergreen.
- **Shadow Frames — 44,1× (FLARE)** — 6.057.460 views — Kedarnath 2013 (hindi) — 2026-07-01.
- **Truth Untold — 39,1× (FLARE)** — 512.333 views — vila no Irã construída entre rochas vulcânicas (hindi) — 2026-09-08.
- **Um Documentário — 12,1× / 11,6× / 7,7× / 3,2×** — 5.454.987 (Miyako) / 5.242.014 (Yungay) / 3.456.751 (Peraliya) / 1.459.094 (Galveston) — série "A TRAGÉDIA DE [lugar]" — ago–set/2026.
- **Impossible Places Global — 9,8×** — 807.513 views — "Living in Indonesia | How 287 Million People Live Among Active Volcanoes" — 2026-09-10.
- **Nature Khauf — 4,9× / 3,8×** — 6.865.469 (2004 tsunami) / 5.338.394 (Japan 2011) — jul/2026, hindi.

## Fome do algoritmo (cluster cross-canal)

- **Ampla (natural disaster):** 4 canais com outlier ≥3× — Nature Khauf, Shadow Frames, Um Documentário, The Last Day. Padrão cross-canal: **tsunami/colapso nomeado + relógio no título** ("em poucos minutos", "3 minutes", "30 minutes") em EN, PT e hindi; dois casos de avalanche/glaciar (Yungay, Nepal) em canais diferentes.
- **Estreita (volcano):** 3 canais com outlier ≥3× — Disaster Pulse, Impossible Places Global, Truth Untold. Padrão cross-canal: **vulcão em erupção recente + ângulo humano** ("living among volcanoes") e **geologia + vila**; janela de 2–6 semanas aberta (Krakatau segue ativo em set/2026).
- Ressalva honesta: os flares de ratio altíssimo vêm de medianas baixas (canal de 28 dias, mediana 424); os números absolutos mais fortes estão nos canais PT/hindi (5–6,8M views por vídeo).

## Convergência de formato observada (últimos uploads, com duração)

- **The Last Day** (@thelastday01, EN): 18 vídeos desde 2026-07-09; uploads de **12:32–23:42 (maioria 18–20 min)**; cadência ~3–4 dias; mistura desastre + "what if" + dinossauros; outliers em 19:19 e 12:32. É a âncora EN do formato "disaster explainer longo".
- **Um Documentário** (@umdocumentario, PT-BR): 31 vídeos desde 2026-04-11; série **"A TRAGÉDIA DE [LUGAR]: [frase] | Documentário completo"**; **39:27–1:07:53 (maioria ~1h)**; cadência quase diária; 4 outliers ≥3×. Fingerprint de série mais forte da coleta.
- **Nature Khauf** (@naturekhauf, hindi): 8 vídeos desde 2026-07-14; **17:33–28:37**; desastres históricos (Surat 2006, Mumbai 2005, Messina 1908, Banqiao 1975, Kedarnath 2013); 364 mil–6,87M views por vídeo.
- **Extreme Disasters 01** (@extremedisasters01, EN): 42 vídeos desde 2026-07-18; **shorts de 21–25s** de flood footage; quase diário; pico de 704.875 views (2026-09-03). Prova do lane Short.
- **Infinite Partways** (@infinitepartways, hindi): 57 vídeos desde 2026-07-21; **shorts de 1:20–1:53**; natureza/ambiente/curiosidade; vários por dia; pico de 1.045.481 views (2026-09-08).
- **Impossible Places Global** (@impossibleplacesglobal, EN): 21 vídeos desde 2026-06-03; **"Living in [lugar] | [hook] | 4K Travel Documentary", 25:51–44:26**; quase diário; vulcões no ângulo humano (Indonésia 807k; Montserrat 82k).
- **Disaster Pulse:** handle não resolvido (o @disasterpulse é outro canal) — convergência não inspecionada; números de gates/outlier vêm do cluster.

## Demanda (autocomplete — top termos)

- **Ampla (87 termos):** national geographic, in hindi, catastrophes, hazards, explained, japan, australia, africa, philippines, part 1/2/3, movies (ruído de filmes), "natural disasters causes".
- **Estreita volcano (203 termos):** netflix, national geographic, for kids, in hindi, mt st helens, bbc, hawaii, fire of love, werner herzog, new zealand, david attenborough, iceland, **active volcano**, caldera, **eruption documentary**, **volcano disaster documentary**, apolaki (Filipinas).
- Leitura: a demanda de vulcão é **3× mais profunda** que a de clima extremo (203 vs 64) e tem casos nomeados — por isso o corte estreito foi volcano.

## Trends (YouTube 12m)

- **429 (rate limit do Google) nas duas consultas** — brief e retries via `--trends` falharam no mesmo dia; sem leitura de direção. Fallback: autocomplete (290 termos) + janela de fome (7 canais) como proxy de trajetória. Reexecutar em outro horário.

## Comentários (demanda explícita)

Não coletado nesta rodada — teste em vídeo do The Last Day (vfIaNeGVaVo) retornou `insufficientPermissions`; o escopo `youtube.force-ssl` precisa ser habilitado com `python scripts/yt_auth.py`. Próximo passo do piloto: minerar comentários de 1 vídeo do The Last Day, 1 do Um Documentário e 1 do Disaster Pulse.

## Fontes web (2+)

- https://sentrismg.com/blog/disaster-stories-niche — [ALEGADO/PRATICANTE] estúdio com rede de 4 canais (500K+ subs, 60M+ views): episódios de 20–37 min; "how this happened" monetiza melhor que "watch this happen"; evitar eventos com menos de ~1 ano; faixa pública de RPM $5–12 em 2026; nicho cheio de low-effort (slideshow de stock, TTS monótono, paráfrase de Wikipédia) — os mais expostos a demonetização e copyright; YPP = 1.000 subs + 4.000h ou 10M views de Shorts.
- https://younalyse.com/tools/rpm/history-documentaries — [ALEGADO] RPM médio $9 e CPM ~$18 para History & Documentaries (2026).
- https://air.io/en/air-data-findings/how-much-does-youtube-really-pay-in-2026-real-rpm-data-from-300-channels — [PRATICANTE] dados reais de Studio de 300 canais: mediana geral $2,30; Education & Science mediana $10,22; dispersão dentro do nicho maior que entre nichos — por que a classe $6–12 é [ALEGADO], não promessa.
- https://creatorblade.com/blog/faceless-youtube-channels-2026-six-figure-niches — [ALEGADO] o que a política mira: mass-produced, repetitive e "no transformation"; documentário com B-roll próprio e pesquisa original segue monetizável; "o algoritmo agora fingerprinta texto-fonte".
- https://faceless.my/youtube/top-faceless-youtube-channels — [REPORTADO] atualização de jul/2025 renomeou "repetitious" para "inauthentic content" e mira vídeos mass-produced de baixa variação sem direção humana; lane documentário segue crescendo.
- https://www.tubetube.io/how-much-do-faceless-youtube-channels-make — [PRATICANTE] CPM por país (França $1,90 → Índia $0,26): geografia da audiência muda o RPM mais que o tópico.
- https://support.google.com/youtube/answer/1311392 — [OFICIAL] políticas de monetização (conteúdo inautêntico).
- https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood — [OFICIAL] evento Nepal 26/08/2026 (debris avalanche/flood; página de resposta).
- https://science.nasa.gov/earth/earth-observatory/anak-krakatau-rumbles-again — [OFICIAL] erupção do Anak Krakatau em 05/09/2026 (imagem Landsat 8).
- https://www.reuters.com/business/environment/glacier-collapse-may-have-triggered-deadly-nepal-flash-flood-experts-say-2026-08-26 — [REPORTADO] colapso de glaciar como gatilho do desastre no Nepal.
- https://kathmandupost.com/world/2026/09/06/indonesia-s-anak-krakatau-eruption-halts-flights-schools-fishing — [REPORTADO] 301 voos afetados, ash a 50.000 pés (06/09/2026).
- https://www.straitstimes.com/asia/se-asia/mount-anak-krakatau-what-to-know-about-the-volcano-disrupting-indonesia-flights — [REPORTADO] contexto do Anak Krakatau (tsunami de 2018, >400 mortos; alerta nível 3).
- https://www.ncei.noaa.gov/news/day-historic-krakatau-eruption-1883 — [OFICIAL] Krakatoa 1883: ~36.000 mortos, som histórico.
- Canais verificados por URL: https://www.youtube.com/@thelastday01 · https://www.youtube.com/@umdocumentario · https://www.youtube.com/@naturekhauf · https://www.youtube.com/@extremedisasters01 · https://www.youtube.com/@infinitepartways · https://www.youtube.com/@impossibleplacesglobal

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Em parte. O EN está mais aberto (The Last Day rompeu com 74 dias e 183,7×; Impossible Places com 110 dias e 9,8×; Disaster Pulse com 28 dias e flare), enquanto PT/hindi já operam em escala industrial de série (Um Documentário quase diário com ~1h; Nature Khauf com 364 mil–6,9M por vídeo). O gargalo é o gate de idade (0/8 e 1/8; 6 emergentes, 5 deles de 62–74 dias), não a demanda.
- **O que está saturado:** o estilo "footage + TTS genérico + paráfrase de Wikipédia" (sentrismg) — e é exatamente o perfil que a política de conteúdo inautêntico e os claims de copyright atingem. A barreira de qualidade é o fosso.
- **Riscos de advertiser:** eventos recentes rendem limited ads; o Nepal (ago/2026) e o Krakatau (set/2026) ainda estão dentro da janela de luto — o modelo exige distância, verificação e enquadramento "como aconteceu" (não "veja acontecer").
- **Direitos:** footage de tempestades/caçadores tem licença restrita; a base segura é institucional/pública (USGS, NOAA, NASA EO, Wikimedia, Europeana, Internet Archive) + mapas e animações próprios.
- **Sensibilidade:** sem imagem de vítima, sem áudio de gritos, números só com fonte primária, eventos ativos com cuidado redobrado — "dados e respeito às vítimas".
- **Diferenciação com `dark-history-disasters`:** o flare do modelo industrial (One Documentary — Yungay, 27,1×) é um desastre **natural**; o território natureza/clima (terremoto, tsunami, vulcão, enchente, glaciar) é deste modelo. Minas, plantas químicas, fábricas e obras ficam no modelo industrial — não sobrepor.

## Queries mais estreitas (próxima rodada)

- `volcano documentary` — **TENTADA** nesta rodada: 1/3 gates + 2 emergentes + fome em 3 canais (flare 1.626,5×). Revalidar em 2–4 semanas (a janela amadurece os emergentes de 62–74 dias e o Krakatau segue ativo).
- `earthquake documentary` — não rodada (candidata nº 1 da próxima rodada).
- `tsunami documentary` — não rodada (padrão de outlier mais forte em PT/hindi).
- `flood documentary` — não rodada (shorts de flood com 704k+ e casos Mumbai/Surat no autocomplete).
- `glacier collapse documentary` — não rodada (evento de 2026 em alta; exige cuidado de distância).
- `extreme weather documentary` — preterida nesta rodada (64 termos vs 203 de volcano); opção para validar o subnicho de clima.
- Nota de captação: `--cluster` não salva JSON (imprime em tela) — se quiser registro, capturar a saída; habilitar `force-ssl` no `yt_auth.py` para `--comments`.
