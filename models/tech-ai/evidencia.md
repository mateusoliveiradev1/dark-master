# Evidência — IA e falhas de tech

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "AI failure documentary" --max 8` (Data API) → REPROVA → segunda busca permitida: `python scripts/niche_scan.py --cluster "AI incident documentary"` (Data API) + `--suggest` (HTTP livre, nos 2 candidatos a cluster) + websearch/webfetch.
> Brief completo: `data/briefs/ai-failure-documentary.md` · JSON: `data/briefs/ai-failure-documentary.json` (o cluster imprime em tela, não salva JSON).
> Quota: ~300 unidades (estimativa) de ~10.000/dia — 1 brief + 1 cluster; autocomplete e web não consomem quota da API do YouTube. Trends deu 429 e não foi lido nesta rodada.

## Veredito: **REPROVA**

- Busca 1 (`--brief "AI failure documentary"`): 46 canais encontrados, 26 pequenos ≤365d, 8 analisados | passam os 3 gates: **0** | emergentes (≤90d + 2/3): 1 (`cineforge`) | fome (outlier ≥3×): 2 canais — ambos micro e/ou fora do tema.
- Busca 2 (`--cluster "AI incident documentary"`): 47 canais encontrados, 17 pequenos ≤365d, 8 analisados | passam os 3 gates: **0** | fome: **0**.
- Autocomplete: 112 termos (busca 1), 106 (AI incident), 83 (algorithm) — profundidade acima da meta (≥15), mas com cauda de ruído de produção ("background music", "green screen", "generator", "hailey", "haiti").
- Trends: não lido (429 do Google nas tentativas do brief).

Leitura honesta: o cruzamento **formato×tópico não se sustenta** nos dados. A busca ampla está **poluída por conteúdo gerado por IA sobre IA** — o maior outlier da coleta é um canal indiano de "AI short films" sobre o Ramayana (181,4×, sem relação com o subnicho), e boa parte do autocomplete é vocabulário de produção ("generator", "green screen"), ou seja, criador procurando template, não espectador procurando documentário. A segunda busca (cluster "AI incident documentary") tem um canal com números fortes falhando só o gate de idade (BrainFuel TV), mas **nenhum canal pequeno passando os 3 gates e zero fome**. Os canais que provam o formato no espaço maior (ColdFusion, Asianometry, BobbyBroccoli) são veteranos de biblioteca — não são evidência de entrada para canal novo. **Não escalar.** Piloto, se houver, só com o cruzamento mais estreito (post-mortem com peça primária) e revalidação em 2–4 semanas — ver "Queries mais estreitas".

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

### Busca 1 — `--brief "AI failure documentary" --max 8`

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Sita Ram Productions | 28.200 | 247d | 396.309 | 39.933 | 011 | 181,4× — 870.362 — "Vishnu vs Yamraj — Dhruva's Death Failed! \| AI Short Film" (2026-07-30); 3,5× |
| cineforge | 45 | **35d** | 3.421 | 2.202 | **101** | — (**emergente**) |
| Emotion Vibes Official 1 | 156 | 83d | 2.982 | 1.277 | 011 | — |
| history xbyte | 170 | 58d | 4.092 | 490 | 000 | — |
| Pranjal Kesharwani | 352 | 129d | 13.099 | 234 | 010 | — |
| SystemFailureStudios | 10 | 30d | 252 | 105 | 100 | — |
| Mono_Teens | 308 | 172d | 47 | 2.543 | 001 | — |
| dudethatsai | 7 | 27d | 507 | 65 | 100 | 6,3× — 289 — "The Most Profitable Failure in Tech History" (2026-09-10) — único outlier ON-topic, em escala de 289 views |

### Busca 2 — `--cluster "AI incident documentary"` (janela 90d)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| BrainFuel TV | 33.800 | 139d | 2.148.935 | 248.018 | 011 | — (conteúdo não inspecionado; homônimos atrapalham a checagem — não conta como evidência) |
| ORBIS NETWORK | 148 | 158d | 260 | 381 | 000 | — |
| The Money Files | 6 | 86d | 268 | 45 | 000 | — |
| DarkVeo Studios | 4 | 20d | 1.395 | 74 | 100 | — |
| @TheAgentReport | 0 | 17d | 68 | 4 | 100 | — |
| Black Space Media | 7 | 53d | 2.178 | 66 | 000 | — |
| PixelGo | 7 | 118d | 162 | 2 | 000 | — |
| aqua eagle | 1 | 58d | 52 | 1 | 000 | — |

> Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha). Dos **16 canais pequenos** analisados nas duas buscas, **nenhum** passou os 3 gates; os 5 que tinham ≤45d falharam **todos** o gate de 5 primeiros ≥10k.

## Outliers (janela de 2–6 semanas)

- **Sita Ram Productions — 181,4× (flare aparente, FORA do tema)** — 870.362 views — "Vishnu vs Yamraj — Dhruva's Death Failed! | AI Short Film" — 2026-07-30 — não é documentário de falha de tech: é filme curto gerado por IA sobre mitologia. Serve como prova da **poluição da busca**, não como sinal do nicho.
- **dudethatsai — 6,3×** — 289 views — "The Most Profitable Failure in Tech History" — 2026-09-10 — único outlier on-topic, mas em escala de 289 views absolutas (canal de 7 subs): micro-sinal sem valor de evidência.
- Busca 2: **nenhum** outlier ≥3× em nenhum canal (0 fome).

## Fome do algoritmo (cluster cross-canal)

- A busca 1 reportou `signal: true` (2 canais com outlier ≥3×), mas a leitura honesta é **não**: os dois canais são o de filme curto mitológico (181,4×) e um microcanal de 7 subs (6,3×, 289 views). Sem padrão cross-canal no tema.
- A busca 2 ("AI incident documentary"): **zero** canais com outlier ≥3× na janela de 90 dias.
- Conclusão: o tema está **frio** no que os dados da API podem medir (canais pequenos e recentes).

## Referências de formato (fora dos gates — não contam como evidência de entrada)

- **ColdFusion** — 5,2M+ subs, ~570M views, 583 vídeos (canal de 2007); mini-docs de tecnologia e IA; uploads recentes: "Why Kids Can't Read Anymore" (450K), "What Happened to Dropbox?" (581K), "Big Tech is Being Kind of Dodgy" (736K) [ALEGADO — influtrend/showmeyourchannel, ago-set/2026]. Renda mensal estimada varia entre estimadores: $613–$9,7K (influtrend), $2,5K–$15,3K (youtubers.me) e ~$48K (starstat) [ALEGADO — a divergência entre estimadores é o dado, não os números].
- **Asianometry** — 957–960K subs, ~150M views, 713–717 vídeos; 99% long-form; evergreen 85%; upload a cada ~4 dias; recentes: "The EU Chips Act is a Failure" (165K), "Taiwan's DRAM Failure" (170K) [ALEGADO — outlierkit/alaxia, ago-set/2026].
- **BobbyBroccoli** — 810K subs, 73 vídeos, 71,5M views; "broccumentaries" de escândalos de ciência/tech em long (25 min–1,5 h); maior vídeo 17,3M views (18× a média do canal); Nebula-first + Patreon [ALEGADO — insidecreateurs/nebula.tv, ago/2026].
- Convergência do formato de referência: **long-form analítico com documento, sem rosto, evergreen, em série** — é o que os canais do espaço usam para segurar retenção e catálogo. Nada disso apareceu num canal ≤45d na coleta.

## Demanda (autocomplete — top termos)

- "AI failure documentary" (112 termos): `ai decline`, `ai crisis`, `ai extinction`, `bbc/dw/netflix/national geographic`, `explained`, `timeline`, `report`, `real stories`, `part 1/2`, `in hindi`, `india` — mistura de demanda de documentário com uma cauda grande de termos de **produção** (`background music`, `green screen`, `after effects`, `generator`, `writing`, `guide`).
- "AI incident documentary" (106 termos): `ai malfunction`, `ai threatens humanity`, `ai incident china/drone/death`, `discovery channel`, `explained`, `full`, `film`.
- "algorithm documentary" (83 termos): `trading algorithm documentary`, `tiktok algorithm documentary`, `social media algorithms documentary` — os únicos três sub-temas realmente nomeados; o resto é ruído (`anime`, `black metal`, `genshin`).

## Trends (YouTube 12m)

- Não lido: Google retornou **429 (rate limit)** na tentativa do brief; sem leitura própria nesta rodada. Proxy de trajetória fica por conta do autocomplete (acima) e da janela de fome (fria).

## Comentários (demanda explícita)

Não coletado — `--comments` exige escopo `youtube.force-ssl` no token (pendência registrada na rodada 1 da biblioteca). Se o modelo for reavaliado, minerar comentários de 1 vídeo do ColdFusion, 1 do Asianometry e 1 de um vídeo de incidente de IA (o tema "AI agents/governance" tem produção ativa).

## Fontes web (2+)

- https://support.google.com/youtube/answer/1311392?hl=en — [OFICIAL] política de monetização: "inauthentic content" (15/07/2025, renome de "repetitious content"); três famílias vedadas — genérico/repetitivo, "unsatisfying/off-putting" e AI personas em temas sensíveis (saúde, jurídico, finanças, política).
- https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos — [REPORTADO] jul/2026: YouTube detalha as 3 categorias de conteúdo inautêntico inelegíveis; mira content farming; não proíbe IA.
- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage — [REPORTADO] jun/2026: jan/2026 terminou 16 canais com 35M subs e 4,7B views; ranking passou a favorecer vídeos com rosto humano; faceless legítimos atingidos; ~$10M/ano estimados nos canais removidos; teste de pop-up de "AI slop" (mar/2026).
- https://www.hollywoodreporter.com/business/digital/faceless-creators-youtube-ai-damage-1236617586 — [REPORTADO] jun/2026: criadores faceless contratando apresentadores; casos de perda de monetização; "a maioria do mesmo conteúdo sem rosto está sendo desmonetizada" (Doctor NOS, 1,7M subs).
- https://tech.yahoo.com/ai/articles/more-1-million-youtube-channels-140000351.html — [REPORTADO] jan/2026: carta anual de Neal Mohan: 1M+ canais usando ferramentas de IA diariamente; YouTube diz que rótulos de IA não penalizam recomendação; foco em spam/clickbait/repetitivo.
- https://scalelab.com/en/why-youtube-is-cracking-down-on-ai-generated-content-in-2026 — [REPORTADO] onda de desmonetização de jan/2026 (16 grandes canais); o que mudou na aplicação da política.
- https://outlierkit.com/blog/youtube-ai-crackdown — [REPORTADO] canais de IA terminados em 2025; quais nichos prosperam em 2026 sob a política nova.
- https://oecd.ai/en/incidents/2026-05-06-a90d — [REGISTRO] incidente: TikTok recua em AI overviews após descrever Charli D'Amelio como "collection of blueberries" (mai/2026).
- https://oecd.ai/en/incidents/2026-02-18-05b5 — [REGISTRO] incidente: outage do sistema de recomendação do YouTube (fev/2026).
- https://oecd.ai/en/incidents/2026-07-28-5a37 — [REGISTRO] hazard: robô humanoide com IA cai em demo ao vivo na Computex 2026, Taipei (jul/2026).
- https://www.youtube.com/watch?v=Z-Lh1NYN7lE — [REPORTADO] post-mortem do caso PocketOS: agente de IA apaga banco de dados de produção em 9 segundos (mai/2026) — matéria-prima de episódio e exemplo de como o tema vira conteúdo de governance.
- https://influtrend.com/youtube/coldfusion · https://us.youtubers.me/coldfusion/youtuber-stats · https://starstat.yt/ch/coldfusion-net-worth — [ALEGADO] estimativas de ColdFusion (5,2M subs; renda mensal divergente entre as três casas).
- https://outlierkit.com/channel/asianometry · https://www.alaxia.site/asianometry — [ALEGADO] Asianometry: 957–960K subs, 713–717 vídeos, 99% long-form, ~150M views, upload a cada ~4 dias.
- https://insidecreateurs.com/en/channels/bobbybroccoli · https://nebula.tv/bobbybroccoli — [ALEGADO] BobbyBroccoli: 810K subs, 73 vídeos, 71,5M views, maior vídeo 17,3M; estratégia Nebula-first.

## Convergência de formato observada

- **ColdFusion:** mini-docs de tech/IA em long; títulos de pergunta/objeto ("What Happened to Dropbox?"; "Microsoft's $1 Billion Phone Disaster" em Short) [ALEGADO — showmeyourchannel].
- **Asianometry:** deep dives técnico-industriais, evergreen, cadência de ~4 dias, 99% long (outlierkit).
- **BobbyBroccoli:** long 25 min–1,5 h, animação própria (Blender), documento como centro.
- Convergência: **documentário analítico evergreen + documento primário + sem rosto + voz única**.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Não há evidência de que sim nas duas buscas (0/16 gates; 0 fome; 1 emergente irrelevante). O topo do espaço é de veteranos com biblioteca (ColdFusion 583 vídeos/18 anos; Asianometry 713 vídeos; BobbyBroccoli 73 vídeos desde 2010). O lado "AI failure" da busca está **contaminado por conteúdo gerado por IA sobre IA** — o oposto do que o modelo quer produzir.
- **Riscos de advertiser/compliance:** o tema morte/acidente (Therac-25, MCAS) pede modo técnico (sem gore, sem vítima, sem pânico). A política de conteúdo inautêntico (15/07/2025 + aperto de 2026) mira exatamente canais de template mass-produced; a fiscalização de jan/2026 removeu 16 canais com 4,7B views, e relatos de jun/2026 dizem que o ranking passou a favorecer rostos — um canal dark puro no espaço "tech/IA" opera contra a corrente e precisa de substância (peça primária, estrutura variável, voz própria) para não cair.
- **Riscos de desinformação/hype:** o nicho é celeiro de clipe viral não verificado ("robô ataca engenheiros") e de previsão catastrófica; cobrir falhas de IA sem separar [FATO]/[REPORTADO] transforma o canal exatamente no conteúdo que a plataforma está caçando. Regra: clipe sem fonte primária não entra; intenção de sistema não se afirma.

## Queries mais estreitas (próxima rodada)

- `algorithm documentary` — **candidata oferecida e NÃO rodada** nesta rodada (autocomplete 83: trading/tiktok/social media). Testar com `--cluster` na próxima.
- `trading algorithm failure documentary` — cruzamento mais estreito do lado financeiro (Knight/Flash Crash).
- `AI incident postmortem` · `AI agent failure` — lado engineering/DevOps, mais perto da audiência que lê Hacker News.
- `software outage documentary` · `automation failure documentary` — lado sistemas (outages/CrowdStrike).
- Alternativa de captação: `--cluster "algorithm documentary"` e `--cluster "AI agent failure"` com `--small 50000`; e `--comments` (após habilitar o escopo `force-ssl`) para fechar a camada de demanda de comentário.
