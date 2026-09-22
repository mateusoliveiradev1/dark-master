# Evidência — Desastres industriais

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "industrial disaster documentary" --max 8` + retry estreito `python scripts/niche_scan.py --cluster "mining disaster documentary" --max 8` (Data API) + `--suggest` (HTTP livre) + websearch
> Brief completo: `data/briefs/industrial-disaster-documentary.md` · JSON: `data/briefs/industrial-disaster-documentary.json` (o cluster estreito imprime em tela, não salva JSON).
> Quota: ~300 unidades (estimativa) de ~10.000/dia — 2 buscas pesadas (brief + cluster) + autocomplete HTTP livre. A rodada de 00:22 do mesmo dia (mesmo brief) já registrava USCSB e 4 canais minúsculos; a segunda passada refrescou os números abaixo.

## Veredito: **PARCIAL**

- Canais pequenos analisados: 8 (ampla) + 8 (estreita) | passam os 3 gates: **0 + 1 = 1** (meta ≥3)
- Emergentes (≤90d + 2/3 gates): **1 + 3 = 4** — watchlist, não aprovam sozinhos
- Fome do algoritmo (outlier ≥3×): **3 + 3 = 6** canais (sinal: SIM nos dois cortes)
- Autocomplete: 88 termos (ampla) + 110 termos (estreita, com casos nomeados) | Trends: ALTA na ampla (recente 25 vs anterior 0, base baixa); a estreita deu 429 (rate limit) sem leitura própria

Leitura honesta: o cruzamento **formato×tópico ainda não fecha os gates** na primeira tentativa — a busca ampla reprova 0/8 e só o cluster estreito de mineração produz **1 canal passando os 3 gates** (One Documentary, 19 dias, documentário longo com outlier de 27,1×). O que existe é **fome ativa** (6 canais com outlier ≥3×, incluindo dois flares ≥10×) e **quatro emergentes de 53–86 dias** que falham apenas o gate de idade (≤45d). O padrão é o mesmo do resto da biblioteca: o gargalo é o gate de idade, não a demanda. **Não escalar ainda**; revalidar em 2–4 semanas — se os emergentes cruzarem os 45 dias mantendo o desempenho, o modelo sobe para PASSA.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

### Busca 1 — `--brief "industrial disaster documentary"` (44 canais achados; 26 pequenos e ≤365d; 8 analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Nature Khauf | 57.500 | 69d | 16.019.788 | 276.918 | 011 | — (**emergente**) |
| THE VAULT LEDGER | 639 | 199d | 78.827 | 15.934 | 011 | — |
| NXT level Spot | 367 | 99d | 46.742 | 7.148 | 011 | — |
| Rule of Five History | 161 | 53d | 1.022 | 3.769 | 001 | — |
| BeyondTheOutback | 41 | 57d | 5.077 | 133 | 000 | 4,5× — 1.989 — "Western Australia Is Hiding Something Deeply Disturbing" (2026-08-09) |
| Romio Uncovered | 24 | 75d | 4.148 | 58 | 000 | 5,0× — 1.723 — tragédia de Bhopal em hindi, 2D animation (2026-07-29) |
| Story4u | 18 | 81d | 2.945 | 67 | 000 | 39,6× — 1.543 — "Bhopal Gas Tragedy 1984 \| Full Documentary" (2026-08-02) |
| The Factory Record | 361 | 204d | 355 | 40 | 000 | — |

### Busca 2 — `--cluster "mining disaster documentary"` (41 canais achados; 17 pequenos e ≤365d; 8 analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| **One Documentary** | 1.020 | **19d** | **281.573** | **14.521** | **111** | **27,1× — 47.558 — "THE YUNGAY DISASTER: The Mountain That Buried an Entire City in Just 3 Minutes \| Full Documentary" (2026-09-13)** |
| DailyTwist 5 | 23.500 | 86d | 15.966 | 201.335 | 011 | — (**emergente**) |
| SkibidiThing | 222 | 61d | 84.484 | 70.457 | 011 | — (**emergente**) |
| Atlas Belgesel | 12.000 | 53d | 67.925 | 21.487 | 011 | — (**emergente**, provável conteúdo em turco — formato não inspecionado) |
| ARCHIV \| HUMAN HISTORY | 4.030 | 252d | 169.915 | 58.679 | 011 | — |
| Expediente Zero | 7.210 | 307d | 18.299 | 7.264 | 011 | 5,8× — 11.814 — "EL LAGO QUE SE FUE POR UN AGUJERO" (2026-08-15, espanhol) |
| Faultline Chronicles | 415 | 47d | 644 | 6.634 | 001 | — |
| Wonder Theory | 150 | 69d | 8.463 | 533 | 000 | 32,4× — 6.608 — "9 Miners Were Trapped Underground for 77 Hours" (2026-09-20) |

> Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha). O cluster ranqueia os top-50 vídeos do tema em 90 dias e analisa os canais pequenos que aparecem ali; canais muito novos só entram se um vídeo já estiver nesse topo.

### Canal-referência institucional (fora dos gates — não conta como evidência de entrada)

- **USCSB** (US Chemical Safety Board): 427.000 subs | 7.178d | 5 primeiros 8.133.453 | 10.506/dia | gates 011 | outlier 7,0× — "The Danger of Popcorn Polymer: Incident at the TPC Group Chemical Plant" (3.774.221 views, coleta 00:22). É fonte pública de animações 3D oficiais e baliza de tom do nicho, não concorrente de entrada.

## Outliers (janela de 2–6 semanas)

- **One Documentary — 27,1× (FLARE)** — 47.558 views — mega-deslizamento de Yungay (1970), título com tempo ("in Just 3 Minutes") + "Full Documentary" — 2026-09-13 — padrão: desastre + relógio + promessa de documento completo.
- **Wonder Theory — 32,4× (FLARE)** — 6.608 views — "9 Miners Were Trapped Underground for 77 Hours" — 2026-09-20 — padrão: resgate de mina + número de sobrevivência (tema mining puro).
- **Story4u — 39,6× (FLARE)** — 1.543 views — Bhopal 1984 em hindi (2026-08-02) — fome micro em canal de 18 subs.
- **Romio Uncovered — 5,0×** — 1.723 views — Bhopal 1984, 2D animation em hindi (2026-07-29) — mesmo tema do anterior, outro canal.
- **Expediente Zero — 5,8×** — 11.814 views — "EL LAGO QUE SE FUE POR UN AGUJERO" (2026-08-15, espanhol).
- **BeyondTheOutback — 4,5×** — 1.989 views — "Western Australia Is Hiding Something Deeply Disturbing" (2026-08-09) — geologia/desastre na Austrália.

## Fome do algoritmo (cluster cross-canal)

- **Ampla:** 3 canais com outlier ≥3× (BeyondTheOutback 4,5×; Romio Uncovered 5,0×; Story4u 39,6×). Padrão cross-canal real: **Bhopal 1984 em hindi (2 canais diferentes)** + mistério geológico na Austrália. Sinal: aberto, mas em canais minúsculos (1,5k–2k views absolutos) e fora do EN.
- **Estreita (mining):** 3 canais com outlier ≥3× (One Documentary 27,1×; Wonder Theory 32,4×; Expediente Zero 5,8×). Padrão cross-canal: **resgate/sobrevivência em mina** com números no título ("77 hours", "3 minutes"). Sinal: aberto — janela de 2–6 semanas.
- Ressalva honesta: os flares são de **view count absoluto baixo** (1,5k–47k) e dois fora do inglês; a fome é de nicho pequeno, não de audiência massiva.

## Demanda (autocomplete — top termos)

- **Ampla (88 termos):** bbc, discovery, netflix, national geographic, real stories, part 1/2/3, full, compilation, india, australia, africa, japan, korea, europe, germany, upsc, in hindi.
- **Estreita mining (110 termos):** casos nomeados — `knox mine disaster documentary`, `coal mine disaster documentary`, `westray mine disaster documentary`, `sunshine mine disaster documentary`, `sago mine disaster documentary`, `chilean mine disaster documentary`; além de `mining disaster`, `mine collapse`, `mining accident documentary`.
- **Estreita factory (105 termos, opção não tomada):** `factory explosion documentary`, `by dhruv rathee` (demanda de criador indiano), `bangla dubbing` (Rana Plaza/Bangladesh), `channel 4`, `national geographic`.

## Trends (YouTube 12m)

- Ampla: **ALTA** (interesse recente 25 vs anterior 0 — base baixa, leitura frágil).
- Estreita (mining): **429 rate limit do Google** na consulta; sem leitura própria nesta rodada — o proxy de trajetória fica por conta do autocomplete nomeado (110 termos) e da janela de fome.

## Comentários (demanda explícita)

Não coletado nesta rodada — `--comments` exige escopo `youtube.force-ssl` no token (pendência registrada no README da rodada 1: "falta escopo force-ssl no yt_auth.py"). Próximo passo do piloto: rodar `python scripts/yt_auth.py` uma vez e minerar comentários de 1 vídeo do One Documentary, 1 do USCSB e 1 do Fascinating Horror.

## Fontes web (2+)

- https://socialblade.com/youtube/handle/fascinatinghorror — Fascinating Horror: 1,45M subs, ~325M views, 460 vídeos, criado em 17/01/2019; últimos 30 dias: +10K subs, 5,55M views, 4 uploads; ganhos estimados $1,4K–$22K/mês [ALEGADO].
- https://hypeauditor.com/youtube/UCFXad0mx4WxY1fXdbvtg0CQ — 1,5M subs; média 344,3 mil views/vídeo; Shorts média 50,3 mil; receita mensal estimada $6,6K–$9,4K em 2026 [ALEGADO].
- https://becomeviral.com/blog/fascinating-horror-case-study — [ALEGADO] CPM estimado $6–12; modelo voice-only com acervo público (National Archives, Library of Congress, Wikimedia, Europeana); sem música; cadência semanal; "nicho pouco saturado no nível de qualidade".
- https://www.csb.gov/the-us-chemical-safety-and-hazard-investigation-board-youtube-channel-surpasses-400000-subscribers-marking-a-major-milestone-in-viewership-and-engagement — [OFICIAL] 400 mil subs, 100+ vídeos, 70M+ views, animações 3D (11/12/2025).
- https://www.csb.gov/us-chemical-safety-board-receives-award-for-its-much-watched-safety-video-youtube-channel — [OFICIAL] Silver Play Button em fev/2025 (364 mil subs à época); top vídeos: 3,7M ("Blowout in Oklahoma"), 3,3M ("Popcorn Polymer"), 3,2M ("Fatal Exposure: DuPont").
- https://support.google.com/youtube/answer/1311392?hl=en — [OFICIAL] políticas de monetização; atualização de 15/07/2025 renomeia "repetitious content" para "inauthentic content" (mass-produced/repetitious inelegível).
- https://www.techrepublic.com/article/news-youtube-ai-video-monetization-rules/ — [REPORTADO] jul/2026: YPP aperta regras para vídeos genéricos/repetitivos/de template e personas sintéticas; não proíbe IA, mira produção em massa.
- https://mashable.com/article/youtube-monetization-ai-slop-mass-produced-videos — [REPORTADO] mudanças anti-"AI slop"; canais faceless em si não são penalizados automaticamente.
- https://www.youtube.com/watch?v=Wh54FeC9JEI — vídeo-outlier do One Documentary (título e duração ~40:03; canal @OneDocumentary confirmado); página bloqueia fetch direto (bot check).
- https://www.youtube.com/watch?v=pfSiq7HdWfY — Plainly Difficult (Flixborough, 18:32): concorrente de porte médio no mesmo espaço; vídeos do canal aparecem entre 400 mil e 900 mil views no search.
- https://www.reddit.com/r/Documentaries/comments/1inh8kj/flood_fire_and_destruction_the_great_johnstown/ — demanda por docs de desastre (Johnstown Flood) no r/Documentaries.
- https://www.reddit.com/r/ifyoulikeblank/comments/1hir2c4/iil_youtube_documentaries_about_nature_natural/ — pedidos explícitos de docs que expliquem como o desastre aconteceu (comunidade pede o passo a passo).

## Convergência de formato observada

- **One Documentary:** título-padrão "THE X: [frase de impacto] | Full Documentary", duração ~40 min (crawl do vídeo), outlier de 27,1×; outros uploads não inspecionados (página bloqueada ao fetch; handle @OneDocumentary confirmado).
- **Fascinating Horror:** uploads recentes de 10–12 min (10:43; 11:08; 10:53 conforme busca), cadência ~semanal, voice-only, sem música [ALEGADO].
- **USCSB:** 5–20 min, animações 3D oficiais com dados de investigação [OFICIAL].
- **Convergência do nicho:** documentário de arquivo + voiceover contido + 10–20 min (flagships 30–40). É o formato que o recomendador lê no cruzamento.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Em parte. O topo é de canais estabelecidos e institucionais (Fascinating Horror 1,45M; USCSB 400K; Plainly Difficult e derivados na casa das centenas de milhares de views), mas a passagem do One Documentary (19 dias, outlier 27,1×) mostra que o feed ainda entrega canal novo quando o pacote (título + documento longo) é forte. O gargalo continua sendo o gate de idade: os 4 emergentes têm 53–86 dias e passam 2/3 gates.
- **Riscos de advertiser/compliance:** morte e ferimento são o núcleo do tema — mitigação por engenharia/inquérito, zero gore, zero vítima em foco, autoclassificação; a política de conteúdo inautêntico (15/07/2025, aperto em jul/2026) mira exatamente docs de desastre mass-produced com template fixo e narração sintética — o modelo exige 1 peça primária e estrutura variável por episódio.
- **Direitos e sensibilidade:** acervos públicos são a base [ALEGADO — becomeviral], mas cada clipe/documento deve ser checado caso a caso; evitar desastres recentes sem distância e imagens de vítimas/famílias.

## Queries mais estreitas (próxima rodada)

- `mining disaster documentary` — **TENTADA** nesta rodada: 1/3 gates + 3 emergentes + fome 3 canais. Revalidar em 2–4 semanas (a janela amadurece os emergentes de 53–86 dias).
- `factory disaster documentary` — opção não tomada (105 termos; demanda Indiana/Bangladesh forte no autocomplete).
- `mine collapse documentary` — não rodada.
- `chemical plant explosion documentary` — não rodada.
- `dam failure documentary` — não rodada.
- Alternativa de captação: rodar o cluster mining com `--small 50000` para ver canais ainda menores e o `--comments` após habilitar o escopo `force-ssl`.
