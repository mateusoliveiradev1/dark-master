# Evidência — Psicologia dark (experimentos, comportamento e manipulação)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "psychology experiment documentary" --max 8` + 1 busca estreita (`--cluster "human behavior documentary" --max 8`) + leitura pontual de canal por API (14 canais; uploads com duração) + resolução de handles por página pública + `--suggest`/`--trends` + websearch (7 consultas).
> Brief completo: `data/briefs/psychology-experiment-documentary.md` · JSON: `data/briefs/psychology-experiment-documentary.json`
> A saída do `--cluster` foi transcrita do console (o `--out` exige `--json` no mesmo comando e não foi salvo em arquivo).

## Veredito: **PARCIAL**

- Canais pequenos analisados: **14 únicos** (8 no brief + 8 no cluster, com 2 repetidos: Stories hub e Layer Unlocked) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **4 canais distintos** (2 no brief, 2 no cluster) — sinal: **SIM**
- Emergentes (≤90d + 2/3 gates): **3** (En Dias Como Hoy 55d; ScenicMotionsBeyondVerse 77d; The First Humans 7M 41d) — os três são de Shorts/mid, formato incompatível com o lane long-first
- Autocomplete: **106 termos** em "psychology experiment documentary" (meta ≥15); **272 termos** na sonda extra "dark psychology"
- Trends (YouTube 12m): **indisponível** — 3 tentativas retornaram HTTP 429 ("psychology experiment documentary", "psychology documentary", "human behavior documentary"); fallback usado: `--suggest`

**Leitura honesta:** reprovou nas duas buscas permitidas (0/8 em cada). O gate de idade derruba 13 dos 14 canais; **11 falham só a idade** e passam os outros dois gates (alguns raspando: En Dias Como Hoy com 10.025 vs. 10.000 no gate dos 5 primeiros; Why Did God? com os 5 primeiros carregados por 1 único vídeo). O único canal que passa idade (The First Humans 7M, 41d, 652.795 views/dia) falha os 5 primeiros e é de Shorts/mid. O sinal real está em dois canais EN de documentário long-form a 2/3 gates: **History Mark: Exposed** (121d, 19.857 views/dia, outlier 42,1×) e **Why Did God?** (102d, 5.917 views/dia, outlier 2.221,7×). Faltam 76 e 57 dias para o gate de idade, respectivamente — não é REPROVA (há flare e convergência), e não é PASSA (não existe ainda 1 canal ≤45d, quanto mais 3). Nota metodológica do lane: documentário long-form publica de 1 a 3 vídeos por semana; 5 primeiros vídeos levam 3 a 5 semanas, então o canal mal é julgado antes dos 45 dias. Revalidar em 2–4 semanas.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

Brief "psychology experiment documentary" (42 encontrados, 20 pequenos, 8 analisados, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers / formato |
|---|---|---|---|---|---|---|
| Stories hub | 25.100 | 172d | 2.113.847 | 912.766 | 011 | 0 · Shorts virais 0:15–0:30 — incompatível |
| History Mark: Exposed | 14.600 | 121d | 904.398 | 19.857 | 011 | 42,1× — 1.156.973 — "The Genain Quadruplets … Study That Failed Them" |
| Unbaffled with Jim Al-Khalili | 46.600 | 146d | 470.675 | 22.348 | 011 | 0 · long 20–32 min de ciência; 1 long de psicologia (Split Brain, 11,6k) |
| En Dias Como Hoy… | 679 | 55d | 10.025 | 3.499 | 011 | 72,5× — 130.268 — "El experimento escolar … La Tercera Ola (1967)" (ES) |
| Layer Unlocked | 42.200 | 259d | 85.815 | 33.818 | 011 | 0 · hindi; Shorts de dark psychology 0:49–1:16 |
| Strategy of Marketing | 11.000 | 299d | 143.445 | 259.718 | 011 | 0 · marketing — fora do cruzamento |
| Singh Of War | 1.680 | 320d | 16.166 | 6.320 | 011 | 0 · fora do cruzamento |
| ScenicMotionsBeyondVerse | 2.250 | 77d | 111.656 | 122.755 | 011 | 0 · Shorts de espaço 0:04–0:36 — incompatível |

Cluster "human behavior documentary" (34 encontrados, 13 pequenos, 8 analisados, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers / formato |
|---|---|---|---|---|---|---|
| SoftCats | 100.000 | 255d | 740.701 | 307.419 | 011 | 0 |
| Stories hub | 25.100 | 172d | 2.113.898 | 912.766 | 011 | 0 · repetido |
| Why Did God? | 3.190 | 102d | 603.009 | 5.917 | 011 | 2.221,7× — 598.746 — "The Acali Raft Experiment …" |
| Mind Theory English | 9.620 | 338d | 113.039 | 1.727 | 011 | 0 |
| The First Humans 7M | 45.300 | 41d | 3.292 | 652.795 | 101 | 0 · emergente; mid/shorts 1:14–3:29 (Índia) |
| Explainer | 1.840 | 95d | 2.139 | 4.306 | 001 | 0 |
| ANINO | 510 | 165d | 2.638 | 1.191 | 001 | 186,4× — 144.489 — "Bakit Naaakit ang Isang Tao sa Bangkay?" (filipino) |
| Layer Unlocked | 42.200 | 259d | 85.815 | 33.818 | 011 | 0 · repetido |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). Leitura honesta dos passes parciais: o "5 primeiros" do Why Did God? é carregado por 1 vídeo (598.746 do total de 603.009); o de En Dias Como Hoy passou raspando (10.025 vs. 10.000).

## Outliers (janela de 2–6 semanas)

- **Why Did God?** — **2.221,7×** — 598.746 views — "The Acali Raft Experiment Might Restore Your Faith in Humanity" — 2026-06-25 — 10:37, long-form. Padrão: experimento social clássico contado como história, com payoff emocional no título. Contexto honesto: 99% das views do canal (603.546 em 10 vídeos) são desse único vídeo; os uploads seguintes fizeram 70–1.471 e o canal esfriou. É flare de estreia, não tração consolidada.
- **History Mark: Exposed** — **42,1×** — 1.156.973 — "The Genain Quadruplets – 4 Identical Sisters With Schizophrenia and the Study That Failed Them" — 2026-08-01 — 32:11. Segundo flare: 802.608 — "The Galvin Family … Six Schizophrenic Brothers" — 2026-07-10; terceiro: 181.961 — "The Dionne Quintuplets" — 2026-08-06. Padrão: família + estudo clínico + "o estudo que falhou".
- **En Dias Como Hoy…** — **72,5×** — 130.268 — "El experimento escolar que se salió de control en 4 días | La Tercera Ola (1967)" — 2026-09-15 — minidoc de 2:28 em espanhol; o canal repetiu o tema Stanford (1.259) dois dias depois.
- **ANINO** — **186,4×** — 144.489 — "Bakit Naaakit ang Isang Tao sa Bangkay?" — 2026-09-07 — filipino; canal de 510 subs fora do lane.

## Fome do algoritmo (cluster cross-canal)

Sinal **SIM**, com um tema puxando a fila: **o experimento da balsa Acali (1973)** foi recontado em pelo menos 6 canais/mídias em janelas recentes — Why Did God? (598.746, jun/2026), Echo Trace (29.416, ~3 meses), MonteLago (7.615, ~2 meses), Coast Files Podcast (09/09/2026), além do acervo duradouro (Horses, 6.033.742, 3 anos; Wendigoon, 8.362.928, 4 anos; Tor's Cabinet of Curiosities, 164.175, 1 ano). O experimento da Terceira Onda aparece em 2 canais diferentes em 3 meses (Why Did God? 1.471; En Dias 130.268). O caso de Stanford/Lucifer effect também em 2 (En Dias 1.259; Unbaffled tentou com Split Brain, 11,6k). Três temas com fome simultânea, todos do mesmo cruzamento: experimento clássico contado como documentário.

## Convergência de formato (últimos uploads, leitura de 2026-09-22)

| Canal | Uploads lidos | Duração | Convergência |
|---|---|---|---|
| History Mark: Exposed | 14 de 14 | 19:56 a 45:16 | total; família + estudo clínico; ~2,5/semana |
| Why Did God? | 10 de 10 | 8:07 a 13:15 | total; experimento social e comportamento; ~1/semana; zero Shorts |
| Unbaffled with Jim Al-Khalili | 20 últimos | 1:05 a 31:56 (6 longs) | parcial; ciência/quântica com entrevista — adjacente, não o cruzamento |
| En Dias Como Hoy… | 20 últimos | 0:33 a 2:28 | formato misto de Shorts/minidocs — incompatível com long-first |
| Layer Unlocked | 20 últimos | 0:35 a 1:16 | Shorts de "dark psychology" em hindi — incompatível (formato + idioma) |
| ScenicMotionsBeyondVerse | 20 últimos | 0:04 a 0:36 | Shorts de espaço — incompatível |
| Stories hub | 20 últimos | 0:15 a 0:30 | Shorts virais de histórias humanas — incompatível |
| The First Humans 7M | 25 últimos | 1:14 a 3:29 | pré-história/survival em mid-form (Índia) — incompatível |

Conclusão de formato: o cruzamento long-form EN existe e converge em **dois** canais (8–45 min, voiceover, arquivo, 1 a 3 por semana, zero Shorts). Os canais com views/dia gigantes que não convergem são de Shorts — o que descarta o lane short-first como evidência deste modelo e explica por que os "emergentes" são todos de formato incompatível.

## Demanda (autocomplete — top termos)

- "psychology experiment documentary" (106 termos): stanford prison experiment bbc · about money · about human psychology · debunked · channel 4 · discovery · netflix · compilation · examples · full. O espaço de perguntas é fundo e durável (experimento, pesquisador, país, década).
- "dark psychology" (272 termos, sonda extra): facts · and manipulation audiobook summary · books · book summary in hindi · tagalog · dating · stories · **dark psychology documentary**. Demanda de manipulação é alta, mas a oferta é dominada por Shorts/áudio-livros — daí o ângulo de mídia-literacia do modelo, não de "truques".

## Trends (YouTube 12m)

Não coletado — HTTP 429 em 3 tentativas (ver cabeçalho). Registrar como lacuna, não como sinal. Na revalidação, tentar "psychology documentary" novamente.

## Comentários (demanda explícita)

Não coletado via API: `--comments P003dY8b89I` (vídeo do outlier Acali, 598.746 views) retornou `insufficientPermissions` (escopo `youtube.force-ssl` ausente; rodar `python scripts/yt_auth.py`). Proxies usados: retellings do mesmo caso em 6+ canais/mídias; threads do Reddit pedindo exatamente este formato (abaixo).

## Fontes web (2+)

1. https://autotube.pro/blog/faceless-psychology-youtube-channel-ideas — 7 formatos faceless de psicologia (2026-09-12); regra "explique o conceito, não diagnostique"; source packet com estudo original + visão geral + crítica; atenção às regras de saúde do YouTube.
2. https://fluxnote.io/guides/faceless-youtube-channel-ideas-psychology — RPM de educação/psicologia **$4–12** [ALEGADO]; melhor faixa citada até **$20** em psicologia de finanças [ALEGADO]; afiliado de terapia até **$150** por conversão [ALEGADO]; diretrizes advertiser-friendly de jan/2026.
3. https://wealthytent.com/ai-faceless-channel — caso Unordinary Mind: 900k+ views no primeiro post, 110k inscritos e ~19k views/dia em ~3 meses [ALEGADO]; formato "psychology of", estética de sketch a lápis.
4. https://socialcounts.org/youtube-live-subscriber-count/UCpMnYjOekpzzZqNIe7i8D_w — verificação independente do UnordinaryMind: 122k inscritos, 33 vídeos, 5,37M views (set/2026). Confirma que o faceless de psicologia monetiza.
5. https://support.google.com/youtube/answer/13813322 — política de misinformation médica [OFICIAL]: saúde mental e tratamento estão no escopo; exceção para contexto educativo/documentário/científico.
6. https://support.google.com/youtube/answer/6162278 — diretrizes advertiser-friendly [OFICIAL]: "apresentar dados sobre psicologia humana" é exemplo de contexto científico elegível; gráfico/sensacional vai para limited/no ads.
7. https://outlierkit.com/resources/youtube-relaxes-monetization-controversial-content-2026/ — jan/2026 (TechCrunch): temas sensíveis não gráficos voltaram a ser elegíveis; revisão de anúncio em até 24h [REPORTADO].
8. https://www.updatic.com/youtube-monetization-guidelines-7-key-changes-for-creators/ — risco de "conselho não verificado" e credencial em saúde; caso de série de psicologia com 6× de views após apelação no novo quadro [ALEGADO].
9. https://coastfiles.com/2026/09/09/experiment-the-acali-raft/ — retelling do Acali em 09/09/2026: fome cross-mídia no tema.
10. https://www.documentary.org/project/raft · https://nordiskfilmogtvfond.com/news/stories/the-raft-marcus-lindeen-discusses-one-of-the-strangest-scientific-experiments-of-all-time — "The Raft" (Marcus Lindeen, 2018) sobre o experimento Acali; legitimidade do caso e material de referência (atenção a direitos: não é domínio público).
11. https://www.youtube.com/watch?v=wAfrop7LzVU — Mindplicit: canal faceless de "dark psychology" com ~200k inscritos demonetizado em março de 2026, segundo o próprio canal [REPORTADO] — anti-modelo de enquadramento.
12. https://www.reddit.com/r/psychologyresearch/comments/xssdtu/good_documentaries/ — demanda explícita: "hard to find anything science-based rather than something that mentions psychology but is really self help".
13. https://www.reddit.com/r/psychologystudents/comments/1k16496/experiments_on_psychology_youtube_channel/ — demanda por formato de experimentos em vídeo; Mind Field (Vsauce) como referência de audiência.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalva: o long-form EN convergente tem só 2 players jovens (121d e 102d) e nenhum gigante de formato idêntico dominando o recomendador; o tema "experimento social" tem fome cross-canal comprovada (Acali em 6+ canais). O risco é o oposto de saturação: oferta long-form escassa e muita oferta de Shorts — o diferencial é profundidade com fonte.
- **Risco de advertiser/YMYL:** saúde mental é território de misinformation policy; sem diagnóstico, sem conselho e com disclaimer, o enquadramento documentário/científico é o que a janela oficial de jan/2026 protege. "Truques de manipulação" e estética anti-establishment são o caminho para limited ads (caso Mindplicit).
- **Risco de inautenticidade:** o tema é ímã de Shorts com narração sintética (117 vídeos em 259 dias de um único canal hindi; feeds de Shorts virais no topo das duas buscas). Mitigação do modelo: 1 peça primária por episódio, estrutura variável, voz própria e long-form com fonte.
- **Risco ético/jurídico:** participantes de experimentos são pessoas reais, algumas vivas e identificáveis; imagem e nome só em contexto público documentado, sem detalhe clínico privado, sem culpar famílias.

## Queries mais estreitas

Tentadas nesta coleta (as duas permitidas):

- `--brief "psychology experiment documentary"` → REPROVA (0 de 8 passam; fome 2).
- `--cluster "human behavior documentary"` → REPROVA (0 de 8 passam; fome 2; 1 emergente de Shorts).

Próximas candidatas para revalidação (uma por vez, sem repetir as duas acima):

- "dark psychology documentary" — 272 termos de autocomplete na sonda; não foi a segunda busca desta rodada (limite de 1), fica como a mais promissora para o pilar manipulação.
- "social experiment documentary" — o tema com maior fome cross-canal (Acali, Terceira Onda, Stanford).
- "stanford prison experiment documentary" — termo de autocomplete; tema com 2 canais recentes e debate público (reanálise 2018).
- "psychology case study documentary" — para o pilar casos clínicos e famílias (Genain/Galvin).
