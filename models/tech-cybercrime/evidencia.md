# Evidência — Cybercrime (hackers, vazamentos, dark web e crimes digitais)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "cybercrime documentary" --max 8` (Data API) → REPROVA → segunda busca permitida: `python scripts/niche_scan.py --cluster "hacker documentary" --max 8` (Data API) + `--suggest` (via brief) + `--trends` (falhou) + `--comments` (falhou) + websearch/webfetch.
> Brief completo: `data/briefs/cybercrime-documentary.md` · JSON: `data/briefs/cybercrime-documentary.json` (o cluster imprime em tela e não salva JSON — números transcritos abaixo).
> Quota: ~300 unidades de ~10.000/dia — 1 brief + 1 cluster; autocomplete/Trends não consomem quota da API do YouTube.

## Veredito: **PARCIAL**

- Busca 1 (`--brief "cybercrime documentary"`): 49 canais encontrados, 20 pequenos ≤365d, 8 analisados | passam os 3 gates: **0** | emergente (≤90d + 2/3): 1 (`Suspense Stories`) | fome (outlier ≥3×): 1 (`The Time Empire`, 22,0×).
- Busca 2 (`--cluster "hacker documentary"`, janela 90d): 40 canais encontrados, 9 pequenos ≤365d, 8 analisados | passam os 3 gates: **0** | emergentes: **3** (`Beta Decodes`, `El Agente Infiltrado`, `Kesit`) | fome: **5** (`Quin`, `Beta Decodes`, `REDACT`, `Kesit`, `SiliconUnbound`). Sinal cross-canal: **SIM** (≥2 canais diferentes com outlier no mesmo tema).
- Autocomplete: **67 termos** (meta ≥15) | Trends: **não lido** (Google retornou 429 em todas as tentativas) | Comentários: **não coletados** (`insufficientPermissions`; falta escopo `youtube.force-ssl`).

Leitura honesta: a busca ampla reprova (0/8, fome fraca e poluída por true crime non-EN). O estreitamento para **"hacker documentary"** muda o quadro: 5 canais com outlier ≥3× e 3 emergentes, todos operando em vídeo longo. Nenhum canal ≤45 dias passa os 3 gates — o mesmo padrão estrutural do lane long-first já registrado em `finance-offshore` e `true-crime-organized-crime`: documentário publica ~1 vídeo/semana, então a soma dos 5 primeiros só se completa depois de ~5 semanas. O detalhe novo aqui: **3 dos 5 canais com fome são non-EN** (ES, HI, TR) e o único EN na fome é o `REDACT` (332 subs, 67d, outlier de 58,1×). O formato está quente e viaja entre idiomas; o que falta é canal EN ≤45d convergente com os gates completos. PARCIAL — revalidar em 2–4 semanas.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia · 1 = ok / 0 = falha)

### Busca 1 — `--brief "cybercrime documentary" --max 8`

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| The Time Empire | 1.770 | 215d | 8.235 | 3.066 | 001 | **22,0×** — 19.764 — "India's Border Spy Network \| The Electrician Exposed a Secret Surveillance Network Part-2" (2026-09-13) |
| Inqalaab | 72.500 | 340d | 58.938 | 24.515 | 011 | — |
| Midnight Crime Vault | 5.000 | 112d | 14.539 | 4.112 | 011 | — |
| Temné stránky světa | 2.140 | 221d | 11.641 | 3.091 | 011 | — |
| RAUD Crime Files India | 3.520 | 99d | 57.774 | 20.634 | 011 | — |
| The Record | 4 | 24d | 3.994 | 166 | 100 | — |
| Suspense Stories | 5.230 | 47d | 53.960 | 41.956 | 011 | — (**emergente**; tema do vídeo não verificado) |
| BAD FILES. | 40 | 333d | 4.947 | 46 | 000 | — |

### Busca 2 — `--cluster "hacker documentary"` (janela 90d)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Movie Zilla - Hindi Movies | 170.000 | 318d | 2.316.374 | 344.895 | 011 | — (canal de filmes dublados; fora do formato) |
| Bharat Cinema | 8.800 | 155d | 149.184 | 23.952 | 011 | — (filmes; fora do formato) |
| Quin | 17.600 | 206d | 2.320.237 | 11.738 | 011 | **14,2×** — 560.839 — "El Hacker que Apagó Corea del Norte" (2026-07-10); **13,1×** — 517.571 — "El Hacker Más Peligroso del Mundo (sigue libre)" (2026-06-26) |
| Beta Decodes | 4.410 | 86d | 218.926 | 11.588 | 011 | 3,1× — 116.919 — "American Most Wanted Hacker \| …" (2026-06-28) — **emergente** |
| REDACT | 332 | 67d | 65.539 | 966 | 010 | **58,1×** — 61.442 — "Why The FBI Can't Find The World's Most Wanted Hacker" (2026-08-25) |
| El Agente Infiltrado | 18.100 | 59d | 265.621 | 34.071 | 011 | — (**emergente**) |
| Kesit | 1.210 | 49d | 101.084 | 9.894 | 011 | **37,1×** — 25.533 — "Rusya'nın Gizli Hacker Şirketi - Belgesel (Evil Corp)" (2026-09-08) — **emergente** |
| SiliconUnbound | 32 | 50d | 3.908 | 797 | 000 | 5,0× — 9.125 — "The First Computer Virus Was Just a Prank #techdocumentary" (2026-08-19) |

Leitura honesta dos quase:

- **REDACT** é o achado central: 332 inscritos, 67 dias, um long de ~11:07 que fez 61.442 views (58,1× a mediana de ~1.057). Falha a idade (67d) e **por 3,4% o gate de views/dia** (966 vs 1.000). É o único canal EN com fome na coleta inteira.
- **Kesit** (49d, TR) e **El Agente Infiltrado** (59d, ES) passam os dois gates "de sustentação" com folga (101 mil e 265 mil nos 5 primeiros; 9,9 mil e 34 mil views/dia). **Beta Decodes** (86d, HI) idem (218,9 mil; 11,6 mil/dia). Os três falham só a idade — e nenhum deles pode mais "envelhecer para dentro" do gate de 45d; a leitura correta é que o formato sustenta tração, não que esses canais sejam elegíveis.
- **Quin** (206d, ES) é o maior flare da coleta: dois longs de 517–560 mil views em 13–14× a mediana. O canal é de 2026 e cresce em vídeo longo.
- Dois dos 8 canais analisados no cluster são **canais de filmes dublados** (Movie Zilla, Bharat Cinema) que entraram na busca de vídeo por causa da palavra "hacker" — poluição de formato que o `--cluster` (busca por vídeo) tende a trazer. Não contam como evidência.
- Na busca 1, o cluster é dominado por true crime non-EN e por um canal de filme (BAD FILES). O único sinal on-topic é o `The Time Empire` (rede de vigilância/eletricista, série em 2 partes), adjacente ao subnicho de vazamentos/vigilância.

## Outliers (janela de 2–6 semanas)

- **REDACT — 58,1×** — 61.442 views — "Why The FBI Can't Find The World's Most Wanted Hacker" — 2026-08-25 — EN; long de ~11:07 (confirmado em listagem pública de snapshot). Padrão: perfil de hacker procurado + pergunta de impossibilidade no título. Ratio inflado por mediana mínima (~1.057), mas são 61 mil views num canal de 332 subs.
- **Kesit — 37,1×** — 25.533 views — "Rusya'nın Gizli Hacker Şirketi - Belgesel (Evil Corp)" — 2026-09-08 — TR. Padrão: **organização criminosa nomeada** (Evil Corp) + formato "Belgesel" no título.
- **The Time Empire — 22,0×** — 19.764 views — "India's Border Spy Network… Part-2" — 2026-09-13 — EN com contexto indiano. Padrão: **série em 2 partes** + rede de vigilância secreta; mesmo ratio inflado por mediana pequena (897).
- **Quin — 14,2× / 13,1×** — 560.839 e 517.571 views — "El Hacker que Apagó Corea del Norte" (2026-07-10) e "El Hacker Más Peligroso del Mundo (sigue libre)" (2026-06-26) — ES. Padrão: perfil de hacker associado a Estado + promessa "sigue libre" (o não capturado).
- **SiliconUnbound — 5,0×** — 9.125 views — "The First Computer Virus Was Just a Prank #techdocumentary" — 2026-08-19 — EN. Padrão: **curiosidade histórica de tech** (origem do primeiro vírus) com hashtag de documentário; escala micro (32 subs), mas on-topic.
- **Beta Decodes — 3,1×** — 116.919 views — "American Most Wanted Hacker" — 2026-06-28 — HI. Padrão: mesmo tema "most wanted hacker", em hindi, com 117 mil views.

## Fome do algoritmo (cluster cross-canal)

Sinal **SIM** (5 canais no cluster + 1 no brief). Três padrões:

1. **"Most wanted hacker / o que o FBI não pega"** — REDACT (58,1×), Quin (14,2×, "sigue libre"), Beta Decodes (3,1× "American Most Wanted Hacker") = **3 canais diferentes, 3 idiomas, mesmo ângulo**. Confirmado em incumbentes (Blackfiles com Mitnick/Gonzalez; Hacker Group Machina "FBI's Most Wanted Hacker" 69 mil views em 3 semanas). É a interseção mais quente da coleta.
2. **"Grupo/organização nomeada"** — Kesit (Evil Corp, 37,1×); Cybernews dedica long de 38:47 ao Conti; John Hammond ao submundo do dark web. Funciona como série: nome próprio no título.
3. **"Marco histórico da internet"** — SiliconUnbound (primeiro vírus, 5,0×), tema de baixa concorrência e escala ainda micro.

Fora do EN, o formato já rompe com força (ES/HI/TR). No EN, a fome é visível (REDACT + incumbentes publicando semanalmente), mas nenhum canal ≤45d fechou os 3 gates na amostra.

## Convergência de formato (últimos uploads, leitura de 2026-09-22)

| Canal | O que foi lido | Formato | Convergência |
|---|---|---|---|
| Blackfiles (incumbente, ~392K subs) | 6 uploads recentes: 22:38–30:51, 46K–379K views, 1–14 dias | long faceless de caso, capítulos, fontes no descritivo, ~semanal | convergente em long; deriva parcial para crime geral ("Cartel", "KKK"), hacker histories na origem |
| Cybernews (incumbente, 910K subs) | "The Internet Group That Changed Hacking Forever" (38:47, 12,4 mil views/14h, patrocínio Incogni) e "CONTI" (38:47) | long documental com capítulos (Baseline/Trigger/Execution/Post Mortem) | convergente; duração maior (38–41 min) e peça recorrente de grupo nomeado |
| REDACT (332 subs) | outlier "Why The FBI Can't Find…" ~11:07; recentes não listados na leitura | long EN de perfil investigativo | sinal único de long EN jovem; sem janela para confirmar os 5 últimos (limitação da leitura) |
| Quin / Beta Decodes / Kesit / El Agente Infiltrado | títulos dos outliers (ES/HI/TR) e médias | long de documentário/perfil | convergem no formato long; listas completas não lidas (canais non-EN, handles não resolvidos) |
| John Hammond (referência, 1M+ views no outlier) | série "Dark Web Documentary" (17:30–43:28) | long de explorador técnico (hands-on) | formato NÃO replicável: conteúdo hands-on de pesquisador; o canal dark deve ficar na reconstrução documental |

Conclusão de formato: o cruzamento **long-form de caso cyber com narração faceless** é o que converge entre fome e incumbentes; duração de entrada razoável entre 15 e 25 min. Nenhum Short no topo da amostra.

## Demanda (autocomplete — top termos)

67 termos únicos (meta ≥15). Blocos mais úteis:

- **Geografias:** philippines · india · in hindi · arabic · ghana · china · canada · nepal · pakistan · qatar · uk · gujarat/gujarati · kannada · marathi · tamil — demanda fortemente non-EN (bate com a fome em ES/HI/TR).
- **Formato/intenção de documentário:** "and investigation" · "report" · "episode 1/2" · "questions and answers" · "latest" · "national geographic" · "channel 4" · "netflix" — busca por investigação aprofundada.
- **Temas:** "cyber crime documentary dark web" · "cybersecurity documentary" · "cyber attacks documentary" · "cyber war" · "cybercrime investigator" · "cybercriminals".
- **Contaminação de intenção:** família de filme domina parte dos termos ("cyber crime best movie", "full movie", "jamatra movie", "movie in hindi/kannada/marathi/tamil"). O canal deve disputar as queries "documentary/explained/investigation", não as de filme.

## Trends (YouTube 12m)

- **Não lido:** Google retornou **429 (rate limit)** na tentativa automática do brief e em duas tentativas próprias (`--trends "hacker documentary"` e `--trends "dark web documentary"`). Proxy de trajetória: a janela de fome está quente (5 canais cross-canal com outlier ≥3× em 90 dias) e há incumbentes publicando semanalmente, mas sem leitura direta de Trends nesta rodada.

## Comentários (demanda explícita)

Não coletado via API: `--comments edZhyTpFZ1Q` (John Hammond, "The Hacker's Playbook in 2026") retornou `insufficientPermissions` — falta o escopo `youtube.force-ssl`; rodar `python scripts/yt_auth.py` para habilitar. Proxies observados:

- Engajamento nos incumbentes: 4,7 mil likes em 378.791 views no vídeo do Gonzalez (Blackfiles) e 590 likes em 12.361 views em 14h no doc do Cybernews (~4,8%) — interesse acima do casual.
- Proxy de demanda de linguagem: o fandom de **Darknet Diaries** (podcast: 22,9 mi de downloads em 2022, ~400 mil ouvintes) mostra apetite por "true crime meets cybercrime" com história fechada, não notícia quente. A autocomplete "cybercrime documentary questions and answers" indica demanda por investigação em profundidade.
- Recomenda-se minerar comentários (quando o escopo for ligado) de: 1 vídeo do Blackfiles, 1 do Cybernews, 1 do REDACT — os três públicos mais próximos do modelo.

## Referências de formato (fora dos gates — não contam como evidência de entrada)

- **Blackfiles** (~392 mil subs; snapshots de set/2026 variam 295–453 mil): "hacker histories" semanais de 22–31 min; recentes com 46 mil–379 mil views; vídeo de 4 meses com 1,1M; produto próprio (**Blackfiles Academy**) com link no descritivo — prova de formato e de monetização por produto no nicho.
- **Cybernews** (910 mil subs): docs de 38–41 min com capítulos e patrocínio de privacidade; "The Internet Group That Changed Hacking Forever" a 12,4 mil views em 14h de publicação.
- **Cryton** — "The Hunt for Lux: The Internet's Most Disturbed User" (36:15) com 1M de views em 2 semanas; **Lume** — "The Man Who Printed $250,000,000 and Fooled the FBI" (28:23, 39 mil views em 2 dias); **Hacker Group Machina** — "FBI's Most Wanted Hacker Revealed" (69 mil em 3 semanas). O tema performa em EN com múltiplos canais médios.
- **John Hammond** (pesquisador de segurança): série "Dark Web Documentary"; topo "Exploring the Latest Dark Web Onion Sites" com 1,2M de views. Referência de demanda — e anti-referência de produção (hands-on não replicável por canal dark).
- **Darknet Diaries**: padrão narrativo "espera a história envelhecer 3–5 anos para ter o desfecho"; modelo de receita com assinatura (Plus a $7,49/mês). Formato-âncora do nicho.
- Validação mainstream do tema: HBO Max "Most Wanted: Teen Hacker" (4 episódios, set/2025) sobre Aleksanteri Kivimäki. O tema tem apetite de plataforma.

## Fontes web

1. https://support.google.com/youtube/answer/2801964 — política de conteúdo perigoso: "Hacking: Demonstrating how to use computers or information technology with the intent to steal credentials, compromise personal data, or cause serious harm" é proibido; exceções EDSA existem, mas exigem contexto.
2. https://support.google.com/youtube/answer/6345162 — como o YouTube avalia EDSA: contexto precisa estar no vídeo/áudio (não só na descrição); exige fato, contraditório e desencorajamento quando aplicável.
3. https://blog.youtube/inside-youtube/look-how-we-treat-educational-documentary-scientific-and-artistic-content-youtube — nota oficial sobre EDSA e categorias de barra mais alta.
4. https://www.theverge.com/2019/7/3/20681586/youtube-ban-instructional-hacking-phishing-videos-cyber-weapons-lab-strike — histórico do ban a "instructional hacking/phishing" e o efeito em canais de educação em segurança (risco de moderação ainda ambíguo para conteúdo técnico).
5. https://www.zdnet.com/article/youtube-ban-on-instructional-hacking-causes-infosec-community-outrage — strikes revertidos após recurso; lição de compliance: nunca flertar com tutorial.
6. https://www.opus.pro/blog/faceless-youtube-niches-2026 (2026-05-12) — nicho cybersecurity com "CPM: $20–30, among the highest on the platform" [ALEGADO].
7. https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ (2026-09-07) — Technology avg RPM $21,2 [ALEGADO — auditorias de canais públicos].
8. https://reelpilot.app/blog/faceless-youtube-rpm-by-niche (2026-06-21) — Tech & AI $7–15; History & Documentary $4–9 [ALEGADO] (contraponto conservador para a classe do modelo).
9. https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm (2026-07-01) — 300 canais reais: mediana global ~$2,30; dispersão dentro do nicho maior que entre nichos [PRATICANTE].
10. https://www.youtube.com/@Blackfiles-HD — canal real do nicho: "I make videos on Hacker histories", uploads semanais 22–31 min, produto Academy; snapshots com contagens divergentes (295K/443K/453K) — a divergência entre estimadores/páginas é o dado, não o número.
11. https://www.youtube.com/watch?v=y_RirGTqnlM — Cybernews: doc de 38:47 com capítulos e patrocínio; confirma formato de 30–40 min no incumbente.
12. https://divert.stream/watch/QlZgsplS0ig — listagem pública que confirma o vídeo do REDACT ("Why The FBI Can't Find The World's Most Wanted Hacker", ~11:07) entre conteúdos de Bloomberg/VICE — evidência de formato long do outlier EN.
13. https://darknetdiaries.com/ + https://cybersecurityventures.com/jack-rhysiders-darknet-diaries-delivers-true-cybercrime-stories — formato "true crime meets cybercrime", 22,9 mi de downloads/2022 e ~400 mil ouvintes; referência de narrativa e de assinatura.
14. https://www.youtube.com/playlist?list=PL1H1sBF1VAKU8aP5FC-makTTBknb1EWYC — John Hammond "Dark Web Documentary" (21 vídeos, 175,5 mil views na playlist; topo de 1,2M) — demanda e anti-referência de produção.
15. https://vault.fbi.gov/view — FBI Vault como fonte primária de pesquisa (arquivos históricos) para a peça obrigatória por vídeo.
16. https://press.wbd.com/na/media-release/hbo-max/hbo-max-releases-official-trailer-max-original-documentary-series-most-wanted-teen + https://www.imdb.com/news/ni65455664 — "Most Wanted: Teen Hacker" (HBO Max, set/2025): validação mainstream do tema hacker/cybercrime.

## Saturação e riscos observados

- **Saturação:** o cruzamento EN long-form "hacker histories" tem incumbentes ativos e semanais (Blackfiles, Cybernews, Cryton, Lume, Machina) — é concorrido, mas o feed segue surfando canais novos (REDACT a 332 subs fez 61 mil views). O ângulo menos disputado é o **caso nomeado com documento primário** (o que Blackfiles e Cybernews fazem bem; a maioria dos novos entrantes ainda é genérica). O espaço non-EN (ES/HI/TR) está em rompimento visível — útil como watchlist, fora do idioma do modelo.
- **Advertiser:** hacking não é gore, mas é tema sensível. Enquadramento documental e forense, zero instrução operacional, zero glorificação; capture flag sem tela de tutorial. Sem isso, o risco de limited ads/yellow icon e de strike por "hacking" é o maior do nicho.
- **Jurídico:** difamação continua sendo o risco central — pessoas vivas implicadas = "charged/alleged/prosecutors say"; não afirmar autoria sem documento oficial; não expor vítimas nem republicar dados vazados; não publicar credenciais nem links.
- **Inautenticidade:** enforcement de 2026 continua; a defesa é 1 peça primária por vídeo (docket, advisory, release) e ângulo próprio — o "explainer de arquivo" com narração genérica e sem documento cai fácil na política.

## Queries mais estreitas (próximo re-scan, uma por vez)

- "ransomware documentary" — o sub-tema com mais casos recentes e cifras verificáveis (Colonial, Change Healthcare, MOVEit).
- "dark web documentary" — a alternativa de cluster não escolhida nesta rodada; alta intenção de busca.
- "data breach documentary" — interseção vazamentos + vítimas em escala.
- "cyber attack documentary" — termo presente na autocomplete; checar espaço de resposta em EN.
- "silk road documentary" — caso âncora de dark web com desfecho judicial completo.
- "wannacry documentary" — caso mais buscado da história do ransomware; medir saturação real.
