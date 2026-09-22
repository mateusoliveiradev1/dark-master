# Evidência — Lavagem e offshore (lavagem de dinheiro, paraísos fiscais e vazamentos)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "money laundering documentary" --max 8` + 1 busca estreita (`--cluster "tax haven documentary" --max 8`) + leitura dos últimos uploads de 4 canais-evidência + websearch (5 consultas)
> Brief completo: `data/briefs/money-laundering-documentary.md` · JSON: `data/briefs/money-laundering-documentary.json`
> A saída do `--cluster` rodou sem `--out`; os números estão transcritos abaixo. `--comments` não coletou (escopo ausente, ver seção própria).

## Veredito: **PARCIAL**

- Canais pequenos analisados: **16 no total** (8 no brief + 8 no cluster, sem repetição) | passam os 3 gates: **1** (meta ≥3) — e o único passer opera em **espanhol**
- Nenhum canal **EN** passou os 3 gates. Dois canais EN ficam em 2/3 falhando só a idade (Old Money Scandals, 134d; Beneath The Code, 68d — este no tier emergente)
- Fome do algoritmo (outlier ≥3×): **5 canais no brief + 5 no cluster** — sinal: **SIM**
- Autocomplete: **78 termos** (meta ≥15) | Trends YouTube 12m: **ALTA** (40,5 recente vs 15,1 anterior; sem queries rising)
- Emergentes (≤90d + 2/3 gates, watchlist): **Beneath The Code** (68d) e **El Legado De Los Imperios** (66d)

> Reprovou nas duas queries permitidas no gate de idade, e só 1 canal passou os 3 gates (em espanhol). O padrão é o mesmo do lane long-first já registrado no modelo `true-crime-organized-crime`: documentário longo publica cerca de 1 vídeo por semana, então os 5 primeiros levam cerca de 5 semanas e o canal raramente é julgado antes dos 45 dias. O sinal de demanda e de outlier é forte; o que falta é canal EN <45d convergente no cruzamento exato (lavagem/offshore). PARCIAL, revalidar em 2–4 semanas.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

Brief "money laundering documentary" (8 pequenos, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| NOIR FILES | 1.060 | 98d | 672.127 | 6.822 | 011 | 2.814× — 671.143 — hawala (2026-08-13) |
| DocSaga | 14.800 | 127d | 249.337 | 24.726 | 011 | 5,6× — 255.526 — Subrat Roy (2026-08-08) |
| World Entertainment Documentaries | 1.430 | 113d | 35.465 | 4.696 | 011 | 0 (ver nota) |
| Raaz Codex | 3.150 | 139d | 520.424 | 5.680 | 011 | 31,5× — 171.454 — Sukesh Chandrasekhar (2026-07-12) |
| Veltrix Bharat | 8.700 | 150d | 89.896 | 6.849 | 011 | 7,2× — 129.367 — Ajit Doval/Hawala (2026-07-26) |
| Making Sense With Shariar | 10.600 | 137d | 1.935 | 3.658 | 001 | 0 |
| Old Money Scandals | 1.560 | 134d | 123.327 | 2.798 | 011 | 8,6× — 86.764 — The Black Hand (2026-08-07) |
| Beneath The Code | 136 | 68d | 80.005 | 1.166 | 011 | 0 |

Cluster "tax haven documentary" (49 canais encontrados, 30 pequenos ≤365d, 8 analisados, 1 passa):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| FD Finance Español | 748 | 40d | 206.866 | 5.033 | 111 | 9,9× — 52.390 — Los Papeles del Paraíso (2026-08-30) |
| El Legado De Los Imperios | 5.570 | 66d | 201.935 | 3.491 | 011 | 0 |
| ECONOMY HISTORIAN | 24.800 | 314d | 175.771 | 6.606 | 011 | 3,6× — 93.965 — Why Ireland Will Soon be Poorer Than The UK (2026-07-21) |
| Europe Beyond Headlines | 1.220 | 113d | 4.966 | 1.901 | 001 | 0 |
| Luxury Insider | 91 | 89d | 9.338 | 290 | 000 | 8,3× — 3.968 — Monaco square mile (2026-07-08) |
| The Business of Places | 10 | 34d | 2.342 | 67 | 100 | 21,7× — 1.696 — Monaco millionaires (2026-08-25) |
| Made IN USA | 73 | 106d | 1.254 | 150 | 000 | 64,8× — 1.231 — Shell Companies Explained (2026-08-05, Short) |
| Prime Stories | 79 | 94d | 2.176 | 129 | 000 | 0 |

Leitura honesta dos quase:

- **FD Finance Español** é o único canal a passar os 3 gates em toda a coleta: 40 dias, 206.866 views nos 5 primeiros, 5.033/dia, outlier de 9,9× sobre o vídeo dos Paradise Papers. É o sinal mais on-topic que existe aqui — e é em espanhol, fora do idioma do modelo.
- **Old Money Scandals** (EN, 134d) e **Beneath The Code** (EN, 68d, emergente) passam 2 de 3 gates e falham só a idade. São os únicos EN convergentes em long-form, mas o tópico deles na amostra é crime organizado (máfia), não offshore.
- O brief é dominado pelo cluster **hindi** de documentário financeiro em animação 2D: NOIR FILES, DocSaga, Raaz Codex, Veltrix Bharat. Fome real, idioma errado para o modelo.
- **World Entertainment Documentaries** é misto (1 long + Shorts diários de crime UK) — formato sem convergência. **Making Sense With Shariar** tem 5 primeiros de 1.935 (entrevista/podcast), fora do formato.
- O cluster de tax haven tem **muitos canais micro em EN** (Luxury Insider 91 subs, The Business of Places 10 subs, Made IN USA 73 subs) com outliers de 1,2k–4k views: interesse existe, escala não.
- **ECONOMY HISTORIAN** (EN, 314d) é macroeconomia; o outlier de 3,6× é sobre Irlanda/UK, tangencial ao subnicho.

Nota sobre "outliers 0": o scan só marca outlier de vídeo que aparece na janela de busca. O World Entertainment Documentaries tem o long de 40:47 "SAM WALKER - Left For Dead In Spain" (2026-09-11) com 87.961 views e 145 comentários — cerca de 31,8× a mediana dos últimos uploads do canal, não detectado pela query. O marcador "0" é artefato de janela, não ausência de outlier.

## Outliers (janela de 2–6 semanas)

- **NOIR FILES** — 2.814× — 671.143 views — "हवाला क्या है? | Hawala Explained" (22:08) — 2026-08-13 — padrão: sistema financeiro sem banco explicado com animação 2D; ratio inflado por mediana minúscula (238), mas são 671k views num canal de 1.060 inscritos.
- **FD Finance Español** — 9,9× — 52.390 — "Los Papeles del Paraíso: El Escándalo Offshore que Sacudió a..." — 2026-08-30 — padrão: vazamento nomeado (Paradise Papers) em canal de 40 dias. **O outlier mais on-topic da coleta.**
- **Raaz Codex** — 31,5× — 171.454 — "Sukesh Chandrasekhar 215 Crore Scam | 2D Animated True Crime" — 2026-07-12 — padrão: golpe específico nomeado + animação 2D.
- **Old Money Scandals** — 8,6× — 86.764 — "The Black Hand: How One Sicilian Immigrant Built an Empire..." — 2026-08-07 — padrão: história de organização criminosa em vídeo longo.
- **Luxury Insider** — 8,3× — 3.968 — "Monaco: Inside the World's Most Expensive Square Mile" — 2026-07-08 · **The Business of Places** — 21,7× — 1.696 — "Why Monaco Is Full of Millionaires" — 2026-08-25 — padrão repetido em 2 canais: paraíso dos ricos como tema.
- **DocSaga** — 5,6× — 255.526 — Subrat Roy — 2026-08-08 · **Veltrix Bharat** — 7,2× — 129.367 — Ajit Doval/Hawala — 2026-07-26 · **ECONOMY HISTORIAN** — 3,6× — 93.965 — Ireland — 2026-07-21 · **Made IN USA** — 64,8× — 1.231 — Shell Companies Explained (Short) — 2026-08-05.

## Fome do algoritmo (cluster cross-canal)

Sinal **SIM** (5 canais no brief + 5 no cluster). Quatro padrões distintos com outlier na janela:

1. **"Explique o sistema sem banco"** — hawala (NOIR FILES 2.814×, Veltrix Bharat 7,2×). O tema que mais rompeu na coleta, em hindi.
2. **"Golpe/vazamento nomeado + forma visual própria"** — Sukesh Chandrasekhar (Raaz Codex), Subrat Roy (DocSaga), Paradise Papers (FD Finance Español, 9,9×).
3. **"Paraíso dos ricos"** — Monaco repetido em dois canais EN diferentes (Luxury Insider, The Business of Places), escala micro.
4. **"História de crime organizado em long"** — Old Money Scandals (8,6×).

Cross-canal EN confirmado em Monaco (2 canais) e shell companies (Made IN USA). É fome de demanda, mas ainda em escala pequena fora do hindi.

## Convergência de formato (últimos uploads, leitura de 2026-09-22)

| Canal | Últimos uploads lidos | Duração | Convergência |
|---|---|---|---|
| Beneath The Code | 2 longs públicos | 12:00–12:55 | convergente em long EN ("how X happened"), tópico mafia; 1 upload/mês |
| Old Money Scandals | 8 longs | 68:05–111:26 | convergente em long EN; crime organizado; durações extremas (68–111 min) |
| World Entertainment Documentaries | 1 long + 9 Shorts | 1:11–40:47 | sem convergência (misto long + Shorts diários) |
| NOIR FILES | 5 longs públicos | 2:23–22:08 | 2D explainer hindi; cadência irregular; outlier de 671k em 6 vídeos |

Conclusão de formato: nos EN, dois canais convergem em long-form, mas o tópico deles é crime organizado. O cruzamento exato do modelo (lavagem/offshore/leaks em EN long-form) **não tem canal convergente abaixo de 45 dias na amostra** — o que é ausência de evidência de rompimento, não prova de espaço aberto. Revalidar com query mais estreita antes de escalar.

## Demanda (autocomplete — top termos)

78 termos únicos (meta ≥15). Blocos mais úteis:

- **Mecânica/explicação:** "money laundering explained" · "money laundering explained documentary" · "money laundering schemes" · "anti money laundering documentary" · "money laundering history".
- **Regiões/jurisdições:** "uk" · "bbc" · "al jazeera" · "dubai" · "london" · "south africa" · "germany" · "kenya" · "philippines" · "pakistan" · "qatar" · "ghana".
- **Casos/vazamentos:** "gold mafia" · "hsbc money laundering documentary" · "dw".
- **Contaminação de intenção:** a família "money laundering movie" domina boa parte dos termos (é demanda de filme, não de documentário). O modelo deve disputar as queries "documentary/explained", não as de filme.

## Trends (YouTube 12m)

- **"money laundering documentary": ALTA** — 40,5 (recente) vs 15,1 (anterior), leitura de volume médio. Nenhuma query rising retornada na coleta.
- Contexto de tópico em 2026: os Panama Papers completaram **10 anos em abril de 2026** (cobertura ICIJ) e a Oxfam publicou em abril/2026 a estimativa de até **US$ 3,55 trilhão** escondidos em offshore. São ganchos de atualidade para a série.

## Comentários (demanda explícita)

Não coletado via API: `--comments` retornou `insufficientPermissions` nos dois vídeos testados (hawala `BJZXodi7NEg`; Sbarro `L1bAwTcqAHE`) — falta o escopo `youtube.force-ssl`; rodar `python scripts/yt_auth.py` para habilitar. Proxies observados:

- Contagens (Data API): 82 comentários no outlier hawala (671k views) · 58 no "Sbarro" do Beneath The Code (78,9k views) · 145 no "SAM WALKER" do World Entertainment (88k views). O long de caso local com narração humana puxa conversa.
- Reddit (demanda de linguagem, não de canal): threads recorrentes pedindo a **mecânica** — "ELI5: What's the concept of money laundering?", "ELI5: money laundering via small high street shops", "How does money laundering work in an age where cash is so rarely used", "ELI5: how does money laundering work through the art world". As séries (Ozark, Breaking Bad) aparecem como porta de entrada e os threads discutem se a ficção acerta. A dor é entender o sistema, e a ficção é a concorrente de atenção.

## Fontes web

1. https://www.icij.org/investigations/panama-papers/ — 11,5 milhões de registros, 214.488 entidades offshore e 140 políticos; cobertura de 10 anos (abril/2026).
2. https://www.icij.org/investigations/paradise-papers — 13,4 milhões de arquivos; desdobramentos (Apple/Irlanda; material novo de cripto em agosto/2026).
3. https://pulitzercenter.org/sites/default/files/paradise_papers_a_global_investigation_pulitzer_center.pdf — resumo oficial da investigação: "there is nothing illegal about doing business offshore" (linha editorial que o canal deve respeitar: legalidade x opacidade).
4. https://www.theguardian.com/world/panama-papers — abril/2026: estimativa da Oxfam (até US$ 3,55 tri fora do alcance do fisco); listas de paraísos fiscais da UE.
5. https://faceless.my/youtube/channels-like-magnatesmedia (2026-05-18) — formato do documentário financeiro faceless: 10–15 min, 1 sujeito por vídeo, narração dramática sobre stock/arquivo, pesquisa de 8–20 h; monetização em CPM de $6–$18 e sponsors a partir de 25k inscritos [ALEGADO].
6. https://faceless.my/niches/faceless-finance-channel-earnings (2026) — RPM de finance faceless $10–25, com tax/retirement em $12–20; audiência US/UK/CA/AU multiplica por 3–5× [ALEGADO].
7. https://glasp.co/youtube/eXk_e63qzS8 (2026-01-16) — economic documentaries $7–12 RPM, luxury/wealth $8–15 [ALEGADO].
8. https://www.houstonpublicmedia.org/npr/2026/09/10/... (NPR, 2026-09-10) — Musk ameaça processar Alex Gibney por documentário sobre pessoas vivas: risco de difamação é real mesmo para produção jornalística.
9. https://www.theguardian.com/media/2026/jun/05/... (2026-06-05) — Trump x BBC, US$ 10 bi por edição de documentário; referência de risco de edição seletiva.
10. https://www.vulture.com/article/dan-schneider-quiet-on-set-defamation-lost.html (2026-09-11) — caso de difamação contra docusérie rejeitado; mesmo vencendo, são anos de litígio.
11. https://www.procapitas.com/news/world/kim-soo-hyun-youtube-channel-deletion-after-ceo-arrest (2026-06-02) — CEO de canal preso por evidência fabricada com IA em caso de difamação: o pior cenário para quem mistura síntese e acusação.
12. https://support.google.com/youtube/answer/9725604 e política de conteúdo inautêntico (enforcement alto em 2026 — vídeos de referência: Creator Insider "YouTube's Inauthentic Content Policy - Explained!" e a cobertura de julho/2026 sobre nova categoria de desmonetização) — forma e substância precisam variar por episódio.
13. Snapshots de busca (set/2026), para leitura de concorrência: "Banksters: HSBC" (49k views, 1 mês) · "UBS - The Bank of Dirty Money" (2025-07) · Real Stories "Money Laundering: How the World's Richest Families Really Hide Their Money" (295k views, 3 meses) · FT Film "Chinese brokers launder hundreds of millions" (1,9M views) · Moconomy "The Paradise Papers: Secrets of Offshore Schemes" (89k views, 1 ano). Os incumbentes são jornalismo com equipe; o canal dark compete por mecanismo + documento + especificidade.

## Saturação e riscos observados

- **Saturação:** o cruzamento hindi 2D (dinheiro/golpe) está quente e povoado. O cruzamento EN long-form lavagem/offshore está **sem evidência de rompimento** na amostra (nenhum canal <45d), com incumbentes grandes de jornalismo ocupando o tópico. Isso abre uma escolha honesta: ou entrar por um ângulo mais estreito (shell companies, hawala, Monaco/paraísos dos ricos) com pesquisa primária, ou tratar o modelo como watchlist até aparecer canal EN jovem passando os gates.
- **Advertiser:** crime financeiro não é gore, mas exige enquadramento educacional; nada de instrução operacional, nada de glorificação; multas e casos públicos são o material seguro.
- **Jurídico:** difamação é o risco central (pessoas e empresas vivas): "alleged", fonte dupla, sem afirmar crime sem condenação, sem republicar documento vazado não público; crédito ao ICIJ.
- **Inautenticidade:** enforcement de 2026; a defesa é 1 peça primária por vídeo e ângulo próprio — o oposto do template reciclado.

## Queries mais estreitas (próximo re-scan, uma por vez)

- "panama papers documentary" — a segunda opção permitida nesta rodada; **não foi rodada** (a escolhida foi "tax haven documentary"). Candidata natural.
- "shell company documentary" — dor de mecanismo com evidência micro em EN (Made IN USA 64,8× em Short) e base documental forte (ICIJ/OpenCorporates).
- "hawala documentary" — maior flare da coleta (671k views) e demanda de mecanismo; checar quanto existe em EN.
- "monaco documentary" — padrão repetido em 2 canais EN; escala pequena, mas tópico de "paraíso dos ricos" com demanda de lifestyle.
- "gold mafia documentary" — termo que aparece no autocomplete; série investigativa da Al Jazeera, checar espaço de resposta em EN.
- "tax evasion documentary" — variação de intenção mais próxima de search intent durável.
