# Evidência — Atentados políticos (assassinatos políticos, atentados e investigações oficiais)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "political assassination documentary" --max 8` (REPROVA) + UMA segunda busca `python scripts/niche_scan.py --cluster "assassination documentary" --max 8` (resultado persistido em `data/briefs/scout-assassination-cluster.json`) + leitura direta de uploads por ID (7 canais, com duração, views, likes e comentários) + `--trends "jfk documentary"` (429) + `--comments` (bloqueado por escopo) + 4 consultas de websearch
> Brief completo: `data/briefs/political-assassination-documentary.md` · JSON: `data/briefs/political-assassination-documentary.json`

## Veredito: **PARCIAL**

- Canais pequenos analisados: **14** (8 no brief + 6 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Emergentes (watchlist ≤90d + 2/3 gates): **1** — Anuj Bhardwaj (58d), mas fora do tópico (política e entretenimento da Índia)
- Fome do algoritmo (outlier ≥3×): **6 canais distintos** (4 no brief + 2 no cluster) — sinal **SIM**
- Autocomplete: **96 termos** em "political assassination documentary" (meta ≥15) | Trends YouTube 12m: **bloqueado (HTTP 429)** em duas tentativas

> Leitura honesta: nenhuma das duas buscas aprovou o gate de idade ≤45d, e nenhum canal do tópico em inglês sustentou os outros dois gates com o outlier no mesmo pacote. O sinal mais forte do tema em EN é o vídeo de Massoud no America's Wars (1.236,9× a mediana do próprio canal; 157.102 views; 52:30; 134 comentários) e o vídeo de César no Graven History (915.087 views; 7,7×; 1.296 comentários) — os dois em canais de história, não em canal dedicado a atentados. O resto dos números grandes vem de canais de mercados fora do inglês (AniHis Hindi 1,7M nos 5 primeiros; Capital of DOC) ou de fora do tópico (bodycam, crime comum, Shorts de meme). Pela legenda de `models/README.md` (fome em ≥2 canais + emergente sem gate completo = PARCIAL), o modelo fica **PARCIAL**, com lançamento condicionado a re-scan estreito. Sem aprovação, não escalar.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

Brief "political assassination documentary" (8 pequenos, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Anuj Bhardwaj | 35.200 | 58d | 1.876.517 | 46.798 | 011 | 3,1× — 826.861 — "He Tried to Kill YOGI... Then Everything Changed !" (01/08) |
| Inqalaab | 72.500 | 340d | 58.938 | 24.515 | 011 | 16,5× — 191.282 — "The Tragic Last Days \| The Untold Story of Pervez Musharraf" (27/08) |
| America's Wars | 4.570 | 221d | 1.138 | 4.320 | 001 | 1.236,9× — 157.080 — "Two Days Before 9/11: The Assassination of Ahmad Shah Massoud" (09/09) |
| Fact Documentary | 10 | 63d | 3.314 | 232 | 000 | 0 |
| قصص الكشاف | 6.900 | 297d | 45.926 | 1.381 | 011 | 0 |
| StoryHouse Africa | 1.250 | 298d | 119.593 | 866 | 010 | 0 |
| No Thoughts, Head Empty | 2.430 | 313d | 103.184 | 16.572 | 011 | 0 |
| Capital of DOC | 78 | 79d | 6.192 | 308 | 000 | 14,4× — 15.528 — "Indira Gandhi Assassination \| Kyu Li Gayi Unki Jaan? \| The Untold Story \| 2D Animation" (09/08) |

Cluster "assassination documentary" (47 canais encontrados; 6 pequenos e ≤365d; analisados 6; 0 passam os 3 gates — os 6 passam os outros dois):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| AniHis Hindi | 117.000 | 252d | 1.747.572 | 107.869 | 011 | 0 |
| Monu The Explainer | 18.400 | 192d | 407.848 | 43.895 | 011 | 0 |
| Graven History | 6.920 | 97d | 1.524.124 | 15.649 | 011 | 7,7× — 915.048 — "What Actually Happened to EVERY Senator Who STABBED Julius Caesar?" (14/07) |
| Frontline Responders | 15.900 | 242d | 18.196 | 16.626 | 011 | 0 |
| Explorer Vault | 5.660 | 154d | 27.457 | 21.902 | 011 | 0 |
| GRIPPED: Police, Crime, Action | 7.740 | 180d | 14.308 | 11.790 | 011 | 40,6× — 443.537 — "Police Hunt A Hitman After Triple Execution In New York" (14/09) |

Nota metodológica (igual à rodada de regimes): o scan calcula a soma dos 5 itens mais antigos entre os 15 uploads mais recentes. Em canais com ≥15 vídeos isso não equivale aos 5 primeiros da história do canal, e sim aos 11º–15º mais recentes. Os números acima são a saída do scan, sem ajuste.

## Outliers (janela de 2–6 semanas)

- **America's Wars** — 1.236,9× — 157.080 views — "Two Days Before 9/11: The Assassination of Ahmad Shah Massoud" — 2026-09-09 — padrão: contagem regressiva no título ("Two Days Before") + atentado real com consequência global; 52:30; 611 likes; 134 comentários. É o outlier on-topic mais forte em inglês da coleta.
- **Graven History** — 7,7× — 915.048 views — "What Actually Happened to EVERY Senator Who STABBED Julius Caesar?" — 2026-07-14 — padrão: "o que aconteceu com quem matou"; 23:03; 13.759 likes; 1.296 comentários. Prova apetite do público EN de história por assassinato + destino dos autores.
- **Inqalaab** — 16,5× — 191.282 views — "The Tragic Last Days | The Untold Story of Pervez Musharraf" — 2026-08-27 — padrão: "last days/untold story" de figura de poder; 20:51; 146 comentários no vídeo vizinho. Canal de política do Paquistão, tópico adjacente (morte, não atentado).
- **Capital of DOC** — 14,4× — 15.528 views — "Indira Gandhi Assassination | ... 2D Animation" — 2026-08-09 — padrão: atentado real em formato de animação 2D; 15:52; só 5 comentários (impulso de recomendação, sem comunidade).
- **GRIPPED: Police, Crime, Action** — 40,6× — 443.537 views — "Police Hunt A Hitman After Triple Execution In New York" — 2026-09-14 — fora do tópico (crime comum/bodycam).
- **Anuj Bhardwaj** — 3,1× — 826.861 views — "He Tried to Kill YOGI... Then Everything Changed !" — 2026-08-01 — política indiana em títulos ingleses; 30:40; 1.803 comentários no vídeo seguinte.

## Fome do algoritmo (cluster cross-canal)

Sinal **SIM**: 6 canais distintos com outlier ≥3×, em duas coletas independentes (4 no brief, 2 no cluster). A fome, porém, é rachada em três blocos:

1. **On-topic real (2):** America's Wars (Massoud, EN) e Capital of DOC (Indira, hindi/animação). Só o primeiro está em EN long-form de história.
2. **Assassinato como tema histórico (1):** Graven History (César, EN, 915k).
3. **Adjacente ou fora do tópico (3):** Inqalaab (política do Paquistão), Anuj Bhardwaj (política indiana), GRIPPED (crime comum nos EUA).

Conclusão de fome: existe janela de 2–6 semanas em torno de "atentado + consequência", mas o cluster "assassination documentary" é poluído por conteúdo hindi e por true crime genérico; nenhum canal dedicado ao cruzamento EN long-form apareceu.

## Convergência de formato (últimos uploads, leitura direta em 2026-09-22)

| Canal | Últimos uploads | Duração | Convergência |
|---|---|---|---|
| Anuj Bhardwaj | 8 recentes, política/entretenimento indiano (Yogi, Modi, Ambani, Salman Khan) | 24:52–33:59 (+1 trailer de 1:10) | parcial: long-form EN-title de alto volume (2/semana), mas fora do tópico |
| Inqalaab | 8 recentes, história política do Paquistão (Musharraf, Imran, Yahya, Maryam) | 16:12–53:35 | parcial: long-form, um episódio por figura; tópico adjacente |
| America's Wars | 8 recentes: 9/11 e Segunda Guerra (D-Day, Omaha) | 10:52–52:30 | média: história militar EN; só o episódio de Massoud é atentado |
| Graven History | 7 recentes: Roma antiga, Custer, Esparta, Wallace | 20:24–28:31 | alta em história EN com fórmula "What Actually Happened…"; tema assassinato é parte do mix |
| No Thoughts, Head Empty | Shorts de 7s de memes/curiosidade | 0:07 | fora do cruzamento (formato incompatível) |
| Capital of DOC | 8 recentes, história da Índia em animação 2D (hindi) | 7:58–23:00 | fora do formato (animação, hindi) |
| StoryHouse Africa | 8 recentes, história africana em long-form muito longo | 1:38–2:31:59 | baixa: views de 11 a 4.899; sem tração |

Notas da leitura direta:

- **America's Wars** rodou o canal quase inteiro entre 26 e 127 views por vídeo depois do flare de Massoud (157.102). O canal ainda não segurou o impulso, mas mantém o formato que o recomendador lê: 16:9, voiceover, 10–52 min, 1 upload/dia.
- **Graven History** (identificado por ID `UCwgn9GXoaStCqwqanfBN6DA`; existe um canal homônimo pequeno que não é o do scan) fez do vídeo de César o maior da casa e caiu para 1.095 e 1.420 views nos dois uploads seguintes (14/09 e 06/08). Flare sem sustentação.
- **Anuj Bhardwaj** tem a maior densidade de comentários da amostra (827 a 1.803 por vídeo recente), mas o público é da Índia e o canal é de política/entretenimento — vale como evidência de formato (long-form com título em inglês e 2 uploads/semana), não do tópico.
- **Inqalaab** publica 2–3 vezes por semana, mistura entrevista em urdu e narração; o outlier de Musharraf (16,5×) veio com 146 comentários.
- **Capital of DOC** e **StoryHouse Africa** completam o quadro de canais pequenos sem convergência: o primeiro é animação em hindi, o segundo é long-form longo demais e sem views.
- Nenhum dos canais lidos é 100% dedicado a atentados políticos. O cruzamento está aberto justamente aí.

## Demanda (autocomplete — top termos)

- "political assassination documentary" (96 termos únicos, meta ≥15): political assassination · american experience · bbc · channel 4 · dw · netflix · korea · japan · haiti · philippines · osama bin laden · full movie · episode 1 · explained · part 1 · china · german · in hindi · in urdu.
- Ruído relevante: gta 5, gacha, satyajit ray, david attenborough, james cameron — a query ampla mistura entretenimento e o tema. O espaço de perguntas, porém, é profundo e organizado por país e por caso, o que sustenta série evergreen (um caso por episódio).
- Termos de cauda que aparecem na busca do próprio YouTube e orientam o calendário: JFK (Reddit pede "autopsy evidence", 2026), Indira Gandhi (outlier de 14,4×), Massoud (outlier de 1.236,9×).

## Trends (YouTube 12m)

- "political assassination documentary": **HTTP 429** no brief.
- Retry único com "jfk documentary": **HTTP 429** de novo (rate limit do Google). Sem leitura de trajetória; fica como pendência para a próxima coleta.

## Comentários (demanda explícita)

API bloqueada: `--comments` retorna `insufficientPermissions` (escopo `youtube.force-ssl` ausente; rodar `python scripts/yt_auth.py`). Proxies usados:

- Contagens reais via Data API: 1.296 comentários no César do Graven (915.087 views), 134 no Massoud do America's Wars (157.102 views), 1.803 no vídeo da KPS Gill do Anuj (268.275 views), 5 no Indira do Capital of DOC (15.528 views).
- Reddit (demanda de espectador): r/letterboxd pede "good documentary that goes into details… about the day he was assassinated… than a documentary about his entire life" (2022, JFK); r/history pede material "historically accurate" e reclama de viés de conspiração (2015); r/JFKassasination em janeiro de 2026 discute documentário focado em evidência de autópsia e elogia material "grounded"; r/Documentaries e r/history pedem especificamente RFK (2012, 2018, 2021). O padrão é claro: querem o dia, o laudo e a investigação, não mais uma teoria.

## Fontes web

1. https://support.google.com/youtube/answer/6162278 — diretrizes advertiser-friendly: violência em contexto documentário é elegível; "momento visível da morte", sofrimento extremo e execuções ficam fora mesmo com contexto; "glorification of violence" = sem anúncio.
2. https://support.google.com/youtube/answer/9725604 — atualizações de agosto e setembro/2026: conteúdo sobre temas controversos, não gráfico, passou a ser elegível; morte em contexto educacional/documentário ganhou clareza; alegações falsas que minam confiança em processos democráticos não monetizam (e o documentário que marca a alegação como falsa segue elegível).
3. https://quasa.io/media/depictions-of-death-can-earn-ads-context-still-decides-the-icon — leitura da taxonomia verde/amarelo/sem anúncio para morte em documentário (22/08/2026).
4. https://mdntvlive.com/youtube-updates-monetisation-guidance-for-news-reports-depicting-death/ — cobertura da atualização de agosto/2026 para conteúdo que mostra morte.
5. https://support.google.com/youtube/answer/6345162 — EDSA: contexto tem de estar no vídeo/áudio, não só no título.
6. https://support.google.com/youtube/answer/2802008 — políticas de conteúdo violento/gráfico e exceções documentais.
7. https://www.theimedia.co/post/youtube-s-september-monetization-update-gives-creators-more-room-on-sensitive-topics — leitura da atualização de setembro/2026; apresentação (thumb, abertura) pesa na classificação.
8. https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ — tabela de 98 nichos (07/09/2026): Documentary $12,6 e Dark History $12,2 [ALEGADO].
9. https://fluxnote.io/blog/youtube-rpm-by-niche-2026 — History/Documentary com faixa de $6–14 e mediana de $9 nos EUA; limited ads corta de 50% a 80% do RPM [ALEGADO].
10. https://air.io/en/air-data-findings/how-much-does-youtube-really-pay-in-2026-real-rpm-data-from-300-channels — 300 canais auditados: mediana de $2,30; News & Politics $2,60; "o nicho define o piso, a operação decide onde você cai" [PRATICANTE].
11. https://longformstudio.app/articles/youtube-documentary-channel — economia do formato documentário, casos Fern e Fascinating Horror, retenção saudável de 30–45% em 15–30 min, CPM de $10–25 no gênero [ALEGADO].
12. https://www.youtube.com/watch?v=e8i-R3saBBs — "JFK Unsolved" (ABC7 News Bay Area, 2021): 1,6M de views, 21 mil likes, 1:21:03 — prova de demanda evergreen do caso.
13. https://www.youtube.com/watch?v=CAATSuUX2t4 — "The Most Shocking Assassinations That Made History" (Real Crime): 45:33, 6,8 mil views, set/2025 — mostra o formato compilado e o teto baixo dele.
14. https://www.reddit.com/r/letterboxd/comments/qsv81s/best_john_f_kennedy_documentary/ · https://www.reddit.com/r/history/comments/35myyg/ · https://www.reddit.com/r/JFKassasination/comments/1q0wmwc/ · https://www.reddit.com/r/Documentaries/comments/pd0zxk/ — demanda por documentário factual, evidência médica e casos RFK/JFK; reclamação recorrente de viés de conspiração.
15. https://www.maryferrell.org/pages/Multimedia.html — arquivo público de mídia sobre JFK/MLK/RFK (fonte de peça primária para episódios).

## Saturação e riscos observados

- **Saturação do cruzamento:** o tópico tem demanda alta e oferta majoritariamente de TV/streaming (Infamous Assassinations, Fatal Shot, especiais de emissora) e de canais de nicho adjacente (história militar, história clássica, política sul-asiática). Nenhum canal pequeno **dedicado** ao cruzamento EN long-form apareceu nas duas coletas. O espaço admite canal novo, mas a regra dos gates não foi satisfeita: 0 de 14.
- **Risco de advertiser:** alto se o pacote escorregar para imagem gráfica. A política separa contexto documental (elegível) de momento de morte, sofrimento extremo, execução e glorificação (sem anúncio). Thumbnail com sangue ou footage do ataque derruba para limited ads mesmo com roteiro educacional.
- **Risco político/legal:** atentados recentes e vivos (líderes em exercício, suspeitos vivos) exigem "alleged" e distância; nada de detalhe operacional. O formato do modelo trabalha com casos históricos e arquivo.
- **Risco de desinformação:** a política de agosto/2026 tira anúncio de alegação falsa sobre processos democráticos; a camada de conspiração do tema é o maior ímã de risco do nicho. Regra do modelo: teoria entra como teoria, com fonte e contra-argumento; a conclusão oficial entra sempre identificada.
- **Risco de inautenticidade:** o tema atrai compilação de conspiração, narração de IA sobre imagens genéricas e vídeos de "arquivo" sem licença. Antídoto: 1 peça primária por episódio, estrutura variável, posição assumida.
- **Risco de direitos:** newsreel, filmes de TV e fotos de imprensa têm dono; conferir licença por imagem antes do GATE 100%.

## Queries mais estreitas (para re-scan)

- "jfk documentary" — a segunda opção de cluster oferecida e não usada nesta coleta; é a maior base de demanda do tema.
- "massoud assassination documentary" — o outlier EN de maior força (1.236,9×).
- "indira gandhi documentary" — outlier de 14,4×, mas em hindi; testar recorte EN.
- "warren commission documentary" — subnicho de investigação oficial.
- "assassination attempt documentary" — cobre a prateleira de atentados fracassados/protocolo.
- Pendência: revalidar em 2–4 semanas; o gate de idade é monotônico, então o re-scan busca **canais novos** ≤45d, não a promoção dos atuais. Anuj Bhardwaj (58d) nunca vai cruzar o gate de idade — fica como evidência de formato e mercado.
