# Evidência — Regimes e repressão (ditaduras, regimes autoritários e aparato repressivo)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "dictatorship documentary" --max 8` + 1 busca estreita `python scripts/niche_scan.py --cluster "secret police documentary" --max 8` (resultado persistido em `data/briefs/scout-secret-police-cluster.json`) + leitura direta de uploads por ID (10 canais: 3 do brief e 7 do cluster; com duração, views e comentários) + `--suggest`/`--trends` + `--comments` (bloqueado por escopo) + websearch (5 consultas)
> Brief completo: `data/briefs/dictatorship-documentary.md` · JSON: `data/briefs/dictatorship-documentary.json`

## Veredito: **PARCIAL**

- Canais pequenos analisados: **14** (6 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Emergentes (watchlist ≤90d + 2/3 gates): **2** — Cold Line (71d) e History Unveiled (65d)
- Fome do algoritmo (outlier ≥3×): **8 canais distintos** (3 no brief + 5 no cluster) — sinal **SIM**
- Autocomplete: **81 termos** em "dictatorship documentary"; **220** em "stalin documentary"; **240** em "north korea documentary" (meta ≥15)
- Trends YouTube 12m: "dictatorship documentary" **ALTA** (recente 37 vs anterior 0, leitura frágil); as tentativas extras de Trends deram HTTP 429

> Leitura honesta: nenhuma das duas buscas aprovou o gate de idade ≤45d. O sinal de fome e de emergente existe, mas os canais ou são antigos demais (Dictators Files, 340d) ou pequenos demais para segurar o flare (History Unveiled ficou em 481 inscritos). O scan reporta REPROVA porque exige ≥3 canais passando; pela legenda de `models/README.md` (fome + emergentes sem gate completo = PARCIAL), o modelo é **PARCIAL**, com lançamento condicionado a re-scan. Sem aprovação, não escalar.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

Brief "dictatorship documentary" (6 pequenos, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| MILO | 13.900 | 341d | 348.651 | 3.732 | 011 | 8,3× — 439.415 — "MOBUTU : Le Dictateur qui a volé l'Afrique" |
| Untold war Story | 3.110 | 115d | 4.903 | 3.362 | 001 | 341,8× — 140.841 — "When Romania Executed Its Dictator on Live TV *Warning Real Footage" |
| COSMO FILE | 373 | 188d | 81.629 | 434 | 010 | 99,4× — 72.729 — "Your Life as Kim Jong Un's Daughter" |
| Investigate Africa | 12.500 | 308d | 129.690 | 12.504 | 011 | 0 |
| Rafael Cerqueira | 16.600 | 145d | 59.066 | 11.830 | 011 | 0 |
| GEOPOWERS | 42.800 | 328d | 359.819 | 62.011 | 011 | 0 |

Cluster "secret police documentary" (48 canais encontrados; 16 pequenos e ≤365d; 8 analisados, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Cold Line | 4.220 | 71d | 1.749.086 | 24.495 | 011 | 14,0× — 982.915 — "'Friendly' Grandpa Has No Idea Police Just Exposed His Dark Secret" |
| The African Reporter | 5.210 | 190d | 538.901 | 3.839 | 011 | 80,6× — 446.927 — "Ali Nuno Dubat: The Untold Story \| Kenya's Most Feared Police Commander" |
| GRIPPED: Police, Crime, Action | 7.730 | 180d | 14.292 | 11.790 | 011 | 68,1× — 744.625 — "How A Fake $20 Bill Led Agents To A North Carolina Serial Killer" |
| Dictators Files: The Dark Side of Power | 18.200 | 340d | 24.145 | 10.398 | 011 | 3,6× — 23.009 — "How the Cheka Became the NKVD — The Secret Police That Built Stalin's Empire" |
| History Unveiled | 481 | 65d | 24.090 | 3.587 | 011 | 20,2× — 16.588 — "The Secret Recording of Saddam's 1979 Purge — He Wanted the World to See It" |
| Battlefield History | 1.350 | 259d | 125.240 | 27.337 | 011 | 0 |
| Forbidden Mysteries | 34.800 | 363d | 12.281 | 17.063 | 011 | 0 |
| zolma1400 | 4.220 | 350d | 17.078 | 4.638 | 011 | 0 |

Nota metodológica: o scan calcula a soma dos 5 itens mais antigos da amostra dos 15 uploads mais recentes. Em canais com ≥15 vídeos isso não equivale aos 5 primeiros da história do canal, e sim aos 11º–15º mais recentes. Os números acima são a saída do scan, sem ajuste.

Leitura honesta dos quase:

- **Cold Line** (71d, 4.220 subs) passa 2 de 3 gates e tem outlier de 14×, mas o tópico é bodycam/conteúdo policial nos EUA, não regime. Entrou no cluster pela palavra "police". Não é evidência do cruzamento do modelo, apenas do formato (long-form voiceover de 20–44 min).
- **History Unveiled** (65d, 481 subs) é o único canal pequeno 100% no tópico com 2 de 3 gates: outlier de 20,2× no purge de 1979 e um flare de 202.285 views no vídeo do Uday Hussein (≈246× a mediana de 823), mas os uploads seguintes caíram para 138–4.395 views. O canal ainda não segurou o impulso.
- **Dictators Files** (340d, 18.200 subs) é o canal mais convergente do nicho: 12 de 12 uploads recentes são long-form de regime, 16–25 min, cerca de 1 vídeo a cada 2 dias, 10.398 views/dia. Falha apenas no gate de idade.
- **Untold war Story** (115d, 3.110 subs) tem o maior outlier do estudo (341,8×; 140.841 views; 467 comentários) com "execuções filmadas", formato adjacente e de maior risco de advertiser; os uploads seguintes ficaram entre 48 e 261 views.
- **MILO** (341d, 13.900 subs, francês) mostra o mesmo mecanismo em francês (Mobutu, 8,3×; 439.415 views); **COSMO FILE** (188d, 373 subs) fez 99,4× com "Your Life as Kim Jong Un's Daughter" e não convergiu.
- **Battlefield History** (Shorts de 5–8s), **Forbidden Mysteries** (história geral mista), **zolma1400** (drama com narração IA, 38–56 min) e **The African Reporter** (política/crime do Quênia) completam o cluster; nenhum é long-form de regime.

## Outliers (janela de 2–6 semanas)

- **Untold war Story** — 341,8× — 140.841 — "When Romania Executed Its Dictator on Live TV *Warning Real Footage" — 2026-09-07 — padrão: execução histórica filmada, 15:52, 467 comentários. Risco: o aviso "Warning Real Footage" beira imagem gráfica e limited ads.
- **History Unveiled** — ≈246× (contra mediana de 823) — 202.285 — "The Brutal Horrors of Saddam Hussein's 'Spoiled Son'… Uday Hussein" — 2026-08-27 — padrão: a família do ditador como ângulo humano; apenas 72 comentários (densidade baixa para o volume, consistente com impulso por recomendação).
- **History Unveiled** — 20,2× — 16.588 — "The Secret Recording of Saddam's 1979 Purge — He Wanted the World to See It" — 2026-07-23 — padrão: documento filmado como peça primária; 24:56.
- **The African Reporter** — 80,6× — 446.927 — "Ali Nuno Dubat: The Untold Story | Kenya's Most Feared Police Commander" — 2026-07-01 — padrão: biografia de repressor; canal de política/crime queniano.
- **GRIPPED: Police, Crime, Action** — 68,1× — 744.625 — "How A Fake $20 Bill Led Agents To A North Carolina Serial Killer" — 2026-09-18 — fora do tópico (crime nos EUA).
- **Cold Line** — 14,0× — 982.915 — "'Friendly' Grandpa Has No Idea Police Just Exposed His Dark Secret" — 2026-08-22 — fora do tópico (bodycam).
- **MILO** — 8,3× — 439.415 — "MOBUTU : Le Dictateur qui a volé l'Afrique" — 2026-06-26 — mecanismo idêntico em francês, 24:25.
- **Dictators Files** — 3,6× — 23.009 — "How the Cheka Became the NKVD — The Secret Police That Built Stalin's Empire" — 2026-09-06 — o aparato de repressão é o ângulo com melhor desempenho do canal.

## Fome do algoritmo (cluster cross-canal)

Sinal **SIM**: 8 canais distintos com outlier ≥3× nas duas coletas. Em EN e dentro do tópico, dois padrões mostram fome na janela: (a) **documento filmado** (purge de 1979, execução na TV romena) e (b) **família/aparato do ditador** (Uday, NKVD, Mobutu). Fora do tópico, o cluster "secret police documentary" está inflado por bodycam e crime comum, o que mostra que a query mistura "police" com "repressão" e que o cruzamento real é mais estreito do que o termo sugere.

## Convergência de formato (últimos uploads, leitura direta em 2026-09-22)

| Canal | Últimos uploads | Duração | Convergência |
|---|---|---|---|
| History Unveiled | 12/12 long-form de regime (Saddam, Uday, Taliban, Kim, Hitler, Amin, Gaddafi, Stalin) | 14:51–40:34 | total no tópico; cadência de 1–2/semana; queda de views após o flare |
| Dictators Files | 12/12 long-form de regime (Hoxha, Mao, Franco, Mussolini, Hitler, Cheka, Coreia do Norte) | 16:25–25:23 | total; cerca de 1 vídeo a cada 2 dias |
| Untold war Story | 12/12 long-form de execuções/Segunda Guerra | 12:08–15:52 | adjacente; formato "Warning Real Footage" (risco de advertiser) |
| MILO | 12/12 long-form, mas biografias variadas (ditador é episódio ocasional) | 22:00–36:17 | parcial |
| COSMO FILE | 6 uploads, POV/explainer | 6:01–15:09 | baixa |
| Cold Line | 6/6 long-form de bodycam | 19:57–44:07 | fora do tópico |
| Battlefield History | 10/10 Shorts de história militar | 0:05–0:08 | formato incompatível |
| zolma1400 | long-form de drama com narração IA | 37:52–55:52 | formato incompatível |
| The African Reporter | long-form de política/crime do Quênia + 2 Shorts de 0:44–0:48 | 0:44–45:58 | fora do tópico (polícia/política queniana) |
| Forbidden Mysteries | misto (long de 44 min + Shorts) | 0:44–44:23 | sem convergência |

Conclusão de formato: o cruzamento "long-form EN de regimes/repressão" converge em **dois** canais (History Unveiled e Dictators Files), ambos voiceover + arquivo, 15–40 min, com temas de aparato, família e documento filmado. É pouco para os gates, mas é o formato que o recomendador lê; os Shorts do cluster são outro negócio.

## Demanda (autocomplete — top termos)

- "dictatorship documentary" (81): dictatorship in brazil · portugal · venezuela · chile · syria · iran · turkmenistan · korea · dictators of africa · dictator documentary netflix · dw
- "stalin documentary" (220, com ruído de um filme telugu): history channel · bbc · english · timeline · death · daughter · dacha
- "north korea documentary" (240): vice · inside · escape · defector · camp 22 · daily life · dictator documentary
- O espaço de perguntas é profundo e organizado por país/regime, o que sustenta uma série evergreen (um regime por episódio).

## Trends (YouTube 12m)

- "dictatorship documentary": **ALTA** (recente 37 vs anterior 0) — leitura frágil por volume baixo.
- Tentativas extras de Trends ("stalin documentary", "north korea documentary") retornaram **HTTP 429** (rate limit do Google) — sem leitura; fica como pendência para a próxima coleta.

## Comentários (demanda explícita)

API bloqueada: `--comments` retorna `insufficientPermissions` (escopo `youtube.force-ssl` ausente; rodar `python scripts/yt_auth.py`). Proxies usados:

- Contagens reais: 467 comentários no flare da Romênia (140.841 views), 1.689 no bodycam da Cold Line (982.915 views), 72 no vídeo do Uday (202.285 views).
- Reddit: pedido explícito de ditadores menos óbvios (Berdymukhamedov, Déby) no r/DocumentaryReviews; thread do The Dictator's Playbook pede material sobre "como ditadores tomam o poder"; comentários do How to Become a Tyrant reclamam de ausências (Pinochet, Fujimori, Mao) e de imprecisão — demanda e alerta de viés ao mesmo tempo.

## Fontes web

1. https://becomeviral.com/blog/faceless-youtube-case-study-history — case de história faceless a $13k/mês; CPM $8–16; estrutura hook dramático → cronologia → mapas/arquivo; 15–25 min; custo de ~$700/mês para 8 vídeos [ALEGADO].
2. https://becomeviral.com/blog/whatifalthist-case-study — long-form acadêmico de 30–60 min, voiceover + mapas, 2–4 vídeos/mês, catálogo evergreen e Patreon forte; CPM $8–16 [ALEGADO].
3. https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ — tabela de 98 nichos (07/09/2026) com Dark History a $12,2 e Documentary a $12,6 [ALEGADO].
4. https://fluxnote.io/blog/youtube-rpm-by-niche-2026 — History/Documentary com faixa de $6–14 e mediana de $9; limited ads corta de 50% a 80% do RPM [ALEGADO].
5. https://www.learningrevolution.net/youtube-earnings-calculator/ — History & Documentary na casa de $4–6 de RPM com audiência tier 1.
6. https://checktheworth.com/channels/history — CPM de $5–15 e RPM de $2,50–8 no nicho; militar chega a $8–18; nota de que "AI narration over generic images" foi penalizada nos updates de qualidade de 2026.
7. https://support.google.com/youtube/answer/6162278 — diretrizes advertiser-friendly: violência só é elegível com contexto documentário/educativo; "controversial issues" e "sensitive events" podem limitar; documentário sobre evento sensível pode monetizar.
8. https://apnews.com/article/youtube-monetization-update-policy-controversial-issues-545e27e27e26e0baefb937c86620b676 + https://techcrunch.com/2026/01/16/youtube-relaxes-monetization-guidelines-for-some-controversial-topics/ — em 16/01/2026 o YouTube afrouxou diretrizes para conteúdo não gráfico ou dramatizado de temas sensíveis (não cobre abuso infantil nem transtornos alimentares).
9. https://www.reddit.com/r/DocumentaryReviews/comments/mmcayq/documentaries_about_authoritarian_dictators/ — demanda por ditadores menos conhecidos (2021; demanda durável do tema).
10. https://www.reddit.com/r/NetflixBestOf/comments/olxqtg/ — reação a How to Become a Tyrant: público cobra rigor e cobertura fora do eixo EUA-Europa.
11. https://notablepeopleproject.org/stsiapan_putsila — caso NEXTA/Belarus: jornalista condenado à revelia por reportagem sobre regime vivo. Contexto de risco político extremo, não modelo de canal.

## Saturação e riscos observados

- O cruzamento long-form EN de regimes **não tem gigante dark dominando** na amostra: o canal mais convergente tem 18,2 mil inscritos (Dictators Files) e o emergente tem 481 (History Unveiled). Mas também **não há 3 canais pequenos passando os gates** — o nicho ainda não deu o rompimento que a regra exige.
- A query "secret police documentary" é poluída: 4 dos 8 canais analisados são claramente fora do tópico (bodycam, crime comum, drama IA, Shorts militares) e outros 2 (política queniana, mistérios gerais) não fazem long-form de regime; só 2 canais são de regime. Para re-scan, preferir termos de mecanismo ou de caso.
- Risco de advertiser: "execution" e "real footage" (Untold war Story) atraem limited ads; o formato do modelo evita imagem gráfica e trata violência em contexto documental com fontes.
- Risco político/viés: regimes vivos e comparações políticas atuais. Regra do modelo: foco histórico (regimes até cerca de 1990/2000), pessoas vivas como "alleged", nada de propaganda ou equivalência moral.
- Risco de inautenticidade: o cluster mostra Shorts de 5–8s e canais de drama com narração IA; o modelo exige 1 peça primária por episódio e variação de estrutura.

## Queries mais estreitas (para re-scan)

- "stasi documentary" — arquivo, delação e o aparato como protagonista.
- "north korea documentary" — 240 termos de autocomplete, a maior base de demanda medida.
- "saddam purge documentary" — documento filmado; outlier de 20,2×.
- "ceausescu documentary" — execução na TV; flare de 341,8×.
- "cold war secret police documentary" — mantém "secret police" com o recorte long-form.
- Pendência: revalidar em 2–4 semanas se History Unveiled cruza o gate de idade. Cold Line segue como evidência apenas de formato, porque é off-topic.
