# Evidência — Toxicologia forense

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "forensic toxicology documentary" --max 8` + retry estreito autorizado `python scripts/niche_scan.py --cluster "poisoning documentary" --max 10` (Data API) + `--suggest` (grátis) + websearch
> Brief completo: `data/briefs/forensic-toxicology-documentary.md` · JSON: `data/briefs/forensic-toxicology-documentary.json` (o cluster da busca 2 foi impresso no terminal, não salvo)
> Custo: ~300 unidades de quota (~10.000/dia) nos 2 scans; `--trends` tentado 4× ("forensic toxicology documentary", "forensic toxicology", "poisoning documentary", "poison") — **HTTP 429 nas quatro** (rate limit do Google).

## Veredito: **REPROVA**

- Canais pequenos analisados: **16** (8 por busca) | passam os 3 gates: **0** (meta ≥3)
  - busca 1 (`forensic toxicology documentary`): 0/8 — 2 canais passam 2 dos 3 gates (Brief Ledger, Crime Daily)
  - busca 2 (`poisoning documentary`): 0/8 — **5 canais passam 2 dos 3 gates** (Red File, AccordHistoryVoice, Hidden Genius, Тени Истории, Tamil Unmaigal), todos falhando só a idade ≤45d
- Fome do algoritmo (outlier ≥3×): **1 canal por busca** (The Crime Journal 25,0×; The Case Collector 6,6×) — **abaixo do critério de fome (≥2 canais)**; sinal do scan: `false` nas duas rodadas
- Emergentes (≤90d + 2/3 gates): **0** — os canais mais novos com 2/3 gates têm 105–272d; os ≤90d analisados (85d, 67d, 54d) têm 1/3 ou 0/3
- Autocomplete: **4 pools somando 514 termos únicos** (95 + 110 + 216 + 93) | Trends: sem dados (429)
- Leitura honesta: o subnicho tem **demanda real e ciclo quente em 2026** (julgamentos Kouri Richins e Kenneth Law no noticiário; docs de TV — Channel 4, BBC, 48 Hours), mas **não tem canal novo (≤45d) rompendo** no cruzamento e a fome cross-canal é fraca. O que existe é o tema **absorvido por canais genéricos de true crime** — nenhum dos 8 canais da busca 1 é dedicado a toxicologia, e os únicos canais realmente de toxicologia no YouTube são educação minúscula (The Toxicology Corner, 108 subs). **Não lançar como canal dedicado sem revalidar em 2–4 semanas** (`23`).

## Busca 1 — brief `forensic toxicology documentary` (--max 8)

30 canais encontrados · 20 pequenos (≤200k subs, ≤365d) · 8 analisados. **0 passam os 3 gates.** Gates na ordem idade≤45d / 5 primeiros ≥10k / ≥1k views-dia.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| **Brief Ledger** | 3.420 | 272d | **46.350** | **1.417** | 0**11** | 0 (mediana 7.508) |
| The Crime Journal | 975 | 189d | 8.256 | 647 | 000 | **25,0×** — 2.823 |
| True Crime Documentaries | 193 | 85d | 1.457 | 1.396 | 00**1** | 0 |
| World's Greatest Investigations | 173 | 67d | 3.642 | 885 | 000 | 0 |
| Forgotten Record | 44 | 197d | 2.872 | 211 | 000 | 0 |
| Crime Justice Alert | 390 | 181d | 8.761 | 419 | 000 | 0 |
| Crime Daily | 3.770 | 187d | 5.016 | **3.929** | 00**1** | 0 |
| TMK Criminal | 14 | 54d | 790 | 17 | 000 | 0 |

## Busca 2 — cluster `poisoning documentary` (única segunda busca permitida)

46 canais encontrados · 8 pequenos (≤200k subs, ≤365d) · 8 analisados. **0 passam os 3 gates. 5 passam 2/3.**

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Mediana / Outliers |
|---|---|---|---|---|---|---|
| Red File | 97.600 | 208d | 8.487.241 | 171.137 | 0**11** | 1.208.156 / 0 |
| AccordHistoryVoice | 23.000 | 105d | 73.065 | **350.937** | 0**11** | 12.182 / 0 |
| Hidden Genius | 14.000 | 148d | 711.226 | 22.782 | 0**11** | 103.220 / 0 |
| Tamil Unmaigal | 57.200 | 307d | 5.230.945 | 67.038 | 0**11** | 6.611 / 0 |
| Тени Истории | 1.230 | 125d | 280.132 | 8.225 | 0**11** | 15.123 / 0 |
| 사관FILES | 8.410 | 246d | 6.634 | 21.855 | 00**1** | 1.198 / 0 |
| **The Case Collector** | 3.380 | 128d | 5.061 | 4.513 | 00**1** | 1.614 / **6,6×** |
| Europe Beyond Headlines | 1.220 | 113d | 4.966 | 1.901 | 00**1** | 289 / 0 |

> Gates 2 e 3 calculados por mim a partir dos números impressos (o modo `--cluster` não imprime o campo gates). Nenhum dos 8 tem ≤45d; o mais novo do conjunto tem 105d.

## Outliers (janela de 2–6 semanas)

- **The Crime Journal — 25,0×** — 2.823 views — "Nolan Wells UPDATE: State Autopsy COMPLETE — New Audio, Phone Search Results…" — 2026-08-03 — canal de 975 subs com mediana de 113 views: o ratio é enorme, mas a **base é minúscula** (2,8k views); padrão: atualização de caso em curso com "autopsy" no título (perícia/arquivo). Evidência fraca.
- **The Case Collector — 6,6×** — 10.698 views — "For 16 Years She Got Away With 2 Murders — Until Her Last Husband…" — 2026-09-21 (1 dia antes da coleta) — canal de 3.380 subs, mediana 1.614; apareceu no cluster de poisoning. Outlier fresco, mas único no cluster.
- Nenhum outlier ≥10× (flare) na coleta — diferente de outros modelos da biblioteca (pandemics 22×, regimes 342×).

## Emergentes (≤90d + 2/3 gates — watchlist, não aprova)

- Busca 1: **0**. Os ≤90d analisados ficam em 1/3 (True Crime Documentaries, 85d, 1.396 views/dia mas 5 primeiros de 1.457) ou 0/3 (World's Greatest Investigations 67d; TMK Criminal 54d).
- Busca 2: **0**. Idade mínima do conjunto: AccordHistoryVoice 105d (2/3 gates, 350.937 views/dia) — a 15 dias do tier, com tração muito forte.

## Fome do algoritmo (cluster cross-canal)

- Busca 1: 1 canal com outlier ≥3× (The Crime Journal) → `signal: false` no JSON.
- Busca 2: 1 canal (The Case Collector) → abaixo do critério (≥2 canais no mesmo tema).
- **Sem fome confirmada.** O padrão cross-canal que os modelos PARCIAL mostram (2–3 canais com outlier do mesmo tema) não aparece: o tema poisoning é diluído em canais generalistas que o tratam como mais um caso.

## Demanda (autocomplete — 514 termos únicos em 4 pools)

- `forensic toxicology documentary` (95): profundidade **poluída** — cauda de variantes de idioma/região (`in hindi`, `australia`, `tamil`, `urdu`…) e sufixos sem sentido (`james webb`, `john oliver`, `hair transplant`) → o termo exato tem pouca diversidade informacional. Termos úteis: `bbc`, `channel 4`, `netflix`, `discovery channel`, `national geographic`, `laboratory`, `explained`, `on drugs`, `hair` (teste de cabelo), `full`, `episode 1`.
- `forensic toxicology` (110): **intenção de estudo/carreira**, não de documentário — `lecture`, `mcqs`, `questions and answers`, `revision`, `classes`, `playlist`, `mbbs`, `lab`, `cases`, `poisons`, `career`. Leitura: o público que busca o termo quer aprender a matéria (explica a existência de canais de aula minúsculos), não assistir doc.
- `poison documentary` (216): **intenção de true-crime**, com ruído de banda/filme (`poison` banda, `venom`, `toxic avenger`). Termos úteis: `poison crime documentary`, `poisoned water documentary`, `poison squad documentary`, `sweet poison documentary`, `salisbury poisoning documentary bbc`, `toxic beauty documentary`, `poison food documentary`, `poisonous animals documentary`.
- `poison murder` (93): confirma o intent criminal — `poison murders`, `poison murder case`, `poison murder documentary`, `murder by poison cases`, `poison murder mystery`; muito ruído de jogos/Arkham/Poison Ivy.
- Leitura: a demanda existe em **dois públicos separados** — (a) true crime por caso de envenenamento; (b) estudantes de toxicologia. O doc dedicado ("a perícia como protagonista") fica no meio e não é buscado por nenhum dos dois hoje.

## Trends (YouTube 12m)

- **Não coletado**: HTTP 429 (rate limit) em todas as tentativas, inclusive no `--brief`. Fallback usado: autocomplete (4 pools) + websearch.
- Sinal indireto de trajetória: ciclo de notícias de 2026 com dois julgamentos globais de envenenamento (Kouri Richins — culpa em 16/03/2026, sentença em 13/05/2026; Kenneth Law — guilty plea em 29/05/2026) e docs de TV no ar (Channel 4 "Poisoned: Killer in the Post", BBC "Litvinenko: The Mayfair Poisoning"). Repetir `--trends` na próxima rodada.

## Comentários (demanda explícita)

- **Não coletado nesta coleta** — `--comments` exige escopo `youtube.force-ssl` no `yt_auth.py` e um VIDEOID priorizado; nenhum dos outliers foi validado como on-topic a esse ponto. Sinal indireto: o mini-maratona "Love and Poison" do 48 Hours (2,7M views, ~1,6k comentários) mostra apetite por compilados de envenenamento; ler comentários de 1 vídeo do `poisoning documentary` no piloto.

## Fontes web (2+)

- https://support.google.com/youtube/answer/2801964 — [OFICIAL] política de conteúdo perigoso: proíbe "instructions to kill or harm" e "ingesting harmful substances (chemicals that may cause illness or poisoning)"; exceções com contexto educacional/documental (EDSA), às vezes com age-restriction. **Risco estrutural nº 1 do nicho: método/dose.**
- https://support.google.com/youtube/answer/6162278 — [OFICIAL] advertiser-friendly: sangue/violência/ferimento **como foco** restringe anúncios; contexto documentário/educacional conta a favor.
- https://longformstudio.app/articles/true-crime-youtube-channel — [ALEGADO] (11/08/2026) RPM reportado $6–9 para true crime educacional não-gráfico; **forensic-focus e courtroom são os enquadramentos com a moderação mais leve** ("here is what the evidence showed"); imagem gráfica na thumb/primeiros 15s → Limited Ads; enforcement inconsistente (vídeos antes monetizados sendo re-revisados); limiar do YPP dobra em 01/02/2027.
- https://youdark.com/for/true-crime — [ALEGADO] RPM $4–12 (tráfego EN US/UK/CA); saturação alta; comprimento ótimo 18–25 min; "cold case" +14% CTR vs "unsolved mystery"; flags de risco de desmonetização +38% YoY por linguagem gráfica.
- https://faceless.my/youtube/how-much-do-faceless-youtube-channels-make — [ALEGADO] (09/05/2026) History/true crime $4–10 RPM; retenção importa mais que CPM.
- https://reelpilot.app/blog/faceless-youtube-rpm-by-niche — [ALEGADO] (21/06/2026) True Crime & Mystery $3–7; History & Documentary $4–9.
- https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ — [ALEGADO] (07/09/2026) 98 nichos faceless: média $11,10, mediana $10,10; "Deep Dives" $16.
- https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline — [REPORTADO] (21/09/2026) timeline das mudanças de monetização 2025–2026 (inauthentic enforcement desde jan/2026; disclosure de IA).
- https://www.youtube.com/watch?v=wA_k5K12tng — 48 Hours, "Love and Poison": **2.749.337 views** (mai/2024, 19k likes, ~1,6k comentários) — compilado de envenenamento do canal de TV; prova de apetite pelo tema no YouTube (mas é marca/arquivo, não canal faceless).
- https://www.channel4.com/press/news/new-channel-4-documentary-poisoned-killer-post-uncovers-global-poisoning-scandal-linked + https://uk.news.yahoo.com/channel-4-kenneth-law-poisoned-killer-in-the-post-214112660.html — Channel 4 "Poisoned: Killer in the Post" (jul/2025): doc de envenenamento em 2 partes, ligado a 99 mortes no UK. **Duplo sinal: demanda pelo tema + zona de alto risco (suicídio).**
- https://abcnews.com/US/utah-mom-kouri-richins-set-sentenced-fatally-poisoning/story?id=132889104 e https://www.cnn.com/2026/05/13/us/kouri-richins-murder-sentencing — [REPORTADO] Kouri Richins: culpada em mar/2026, prisão perpétua em 13/05/2026 (fentanil no drinque; busca no celular por "dose letal" virou prova); a CNN nota que a acusação "não conseguiu provar como ela envenenou" — ângulo de perícia/documento. Ciclo de notícias = demanda ativa por conteúdo de envenenamento em 2026.
- https://www.bbc.com/news/articles/c70vg7glglyo e https://www.theguardian.com/world/2026/may/29/canada-kenneth-law-suicide-packets-hundreds-of-people-around-world — [REPORTADO] (29/05/2026) Kenneth Law: guilty plea por 14 mortes no Canadá, 79 mortes no UK admitidas; vendia nitrito de sódio online. **Linha vermelha: qualquer conteúdo que toque em método/suicídio está fora do modelo.**
- https://www.bbc.com/video/docs/episode/p0ld4ktl — BBC, "Litvinenko: The Mayfair Poisoning" (47 min) — formato de doc de envenenamento (envenenamento radiológico, investigação de Estado).
- https://thetoxpod.buzzsprout.com/ — The Toxpod (TIAFT, desde 2018, 90 episódios) — comunidade real de toxicologia forense existe, mas em podcast/nicho acadêmico; confirma o split de audiência (estudo × entretenimento).
- https://www.youtube.com/channel/UCTehcqjgwyKm4-y6sz7DOGw — The Toxicology Corner: **108 subs, 77 vídeos** — exemplo de que a oferta dedicada de toxicologia no YouTube é minúscula e educacional.
- https://www.youtube.com/watch?v=AvVTbE1L85I — "Deadly Poisons and Perfect Crimes — Real Life Forensic Murder Mysteries" — vídeo de formato "casos + toxicologia forense" no ar (canal não identificável por fetch/JS; sem números confiáveis — citado como existência de formato, não como evidência de performance).

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo? Não hoje, pelos gates.** O tema é absorvido por: (a) canais genéricos de true crime (busca 1: 8/8 são generalistas; o termo exato não encontra canal dedicado); (b) marcas/arquivos de TV (48 Hours, A&E, Channel 4, BBC); (c) canais de história/arquivo que tocam poisoning de passagem (cluster 2). A lacuna real — "a perícia como protagonista, caso a caso" — não tem canal-evidenciário rompendo. Se revalidar com ≥3 gates, o ângulo é esse.
- **Risco nº 1 — método/harm:** a política oficial proíbe instruções de dano e "ingesting harmful substances"; dosagem, síntese, aquisição e "como funciona o veneno" são a fronteira. Mitigação: narrar o **laudo e a investigação**, nunca o método; sem números que ensinem dose; EDSA explícito no enquadramento (1801964).
- **Risco nº 2 — adjacência de suicídio:** parte da demanda recente do tema vem de casos de auto-envenenamento (Kenneth Law, 2026). Conteúdo assim é restrito e contamina o canal — fora do modelo.
- **Risco nº 3 — advertiser limit:** [ALEGADO] linguagem gráfica/tema forte derruba o RPM de true crime de forma instável (YouDark +38% YoY; Longform Studio relata re-revisões); mitigação: forensic-focus, sem imagem gráfica em thumb/15s (6162278).
- **Risco nº 4 — inautenticidade:** "casos + arquivo" é exatamente o formato que a política de conteúdo inautêntico penaliza quando vira template; exigir 1 peça primária por vídeo e variação real (`09`).
- **Risco nº 5 — difamação/direitos:** pessoas vivas = alleged (Richins recorre — "convicta, recurso pendente"); footage de tribunal/TV tem dono.

## Queries mais estreitas (não executadas — quota; próximas rodadas)

- `arsenic poisoning documentary`
- `poisoning case files documentary`
- `toxicology lab documentary`
- `exhumation toxicology case`
- `polonium poisoning documentary`
- `forensic files poison episode`

> Revalidar em 2–4 semanas. Watchlist: **The Case Collector** (128d, 2/3 gates, outlier 6,6× — 1 dia de idade na coleta), **AccordHistoryVoice** (105d, 2/3, 350.937 views/dia — a 15 dias do tier emergente), Brief Ledger (272d, 011), Crime Daily (187d, 001, 3.929/dia), True Crime Documentaries (85d, 001, 1.396/dia — precisa dos 5 primeiros ≥10k). Se a próxima rodada não trouxer ≥2 canais com fome ou ≥1 emergente, **pivotar para o modelo 18** (`forensic-medical-mysteries`) em vez de insistir.
