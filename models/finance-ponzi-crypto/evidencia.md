# Evidência — Ponzi e cripto

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "crypto scam documentary" --max 8` (REPROVOU) + 1 busca estreita autorizada `--cluster "ponzi scheme documentary"` + 5 checagens de canal (`--channel`, 2 casaram) + websearch.
> Brief completo: `data/briefs/crypto-scam-documentary.md` · JSON: `data/briefs/crypto-scam-documentary.json`
> A saída do `--cluster "ponzi scheme documentary"` **não** foi salva em artefato (rodou sem `--out`); os números estão transcritos abaixo.
> Quota usada: ~310 unidades de ~10.000/dia (2 coletas de ~150 + 5 checagens de ~5).

## Veredito: **PARCIAL** (gate estrito REPROVA)

- Canais pequenos analisados: **16** (8 na busca ampla + 8 na estreita; elegíveis: 16 e 20 — quota cortou a amostra) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **4 canais** (1 na ampla + 3 na estreita) — sinal: **SIM** na busca estreita (`>=2 canais diferentes com outlier no mesmo tema`)
- Emergentes (≤90d + 2/3 gates): **0** — nenhum canal na watchlist cruzou os dois gates (o mais perto: The Collapse Archives, 13d, só 1/3)
- Autocomplete: **111 termos** (meta ≥15) | Trends (YouTube 12m): **ALTA** (recente 25 vs anterior 0)

> Leitura honesta: **o cruzamento não fecha o gate estrito** — nenhum canal pequeno passa idade≤45d + 5 primeiros ≥10k + ≥1k views/dia, e as buscas de validação estão poluídas por formatos vizinhos (recap, commentary, canal de notícia). O que existe de verdade é **fome**: 2 canais diferentes com outlier no **Madoff** (67,3× e 4,0×, um deles em set/2026) dentro da janela de 2–6 semanas, mais 1 outlier de 35,4× num Ponzi indonésio e 1 Short de OneCoin com 17,8×. O problema é a **escala absoluta** dos outliers de título EN: 880–3.030 views (medianas de 45–218) — a fome é de ratio, não de volume. Não escalar como validado: o piloto tem que provar que o cruzamento EN long-form sustenta canal novo, e as queries estreitas abaixo são o próximo passo.

## Canais-evidência — busca 1: `--brief "crypto scam documentary"` (2026-09-22)

48 canais encontrados · 16 pequenos ≤365d · 8 analisados (quota) · **0/8 passam** · emergentes 0 · fome 1.
Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha).

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Findicate | 13.300 | 235d | 264.188 | 3.753 | 011 | 0 |
| world trend wave news | 1.790 | 146d | 61.748 | 84.151 | 011 | 0 |
| FinanceCore | 13.000 | 299d | 168.266 | 111.788 | 011 | 0 |
| Anand case study | 4.660 | 83d | 4.679 | 48.773 | 001 | 0 |
| The Collapse Archives | 19 | 13d | 5.019 | 386 | 100 | 0 |
| Sahil Ansari | 125 | 94d | 67.996 | 1.292 | 011 | 0 |
| The Dossier Files | 213 | 45d | 157 | 259 | 100 | 0 |
| Anatomía del Fraude | 69 | 70d | 122 | 90 | 000 | **17,8×** — 1.013 — "La Estafa de $4 Billones: El Misterio de OneCoin" (2026-07-29) — Short ES |

> Todos os candidatos com gates verdes falham na **idade** (146–299 dias). Os canais ≤45d (The Collapse Archives, The Dossier Files) não somam 10k nos 5 primeiros. Nota: o `vpd` alto de "Anand case study" e "FinanceCore" vem de views totais ÷ idade (inclui Shorts virais), não de consistência por upload — não usar como prova de formato.

## Canais-evidência — busca 2 (estreita e autorizada): `--cluster "ponzi scheme documentary"` (2026-09-22)

45 canais encontrados · 20 pequenos ≤365d · 8 analisados (quota) · **0/8 passam** · **fome 3 · sinal SIM**.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| NET CREATIVE | 2.480 | 113d | 160.245 | 6.784 | 011 | **35,4×** — 537.424 — "Skandal Rp3,2 Triliun Cipaganti" (2026-09-10) — ID |
| Built on Lies | 2.180 | 127d | 335.374 | 3.278 | 011 | 0 |
| Stanisław Wiśniewiecki | 45.800 | 226d | 288.960 | 34.749 | 011 | 0 |
| Nexplainr | 113 | 152d | 1.974 | 72 | 000 | **4,0×** — 880 — "Bernie Madoff's 65 Billion Dollar Lie" (2026-07-22) |
| The Conspiracy Vault | 197 | 179d | 6.466 | 141 | 000 | **67,3×** — 3.030 — "Bernie Madoff: The $50 BILLION Ponzi Scheme" (2026-09-06) |
| The Dark Ledger | 48 | 83d | 4.538 | 222 | 000 | 0 |
| Velvet Bones | 24.400 | 349d | 15.100 | 371 | 000 | 0 |
| The Bankruptcy Files | 34 | 70d | 1.731 | 127 | 000 | 0 |

> Medianas: NET CREATIVE 15.190 · Built on Lies 28.306 · Stanisław 36.008 · Nexplainr 218 · Conspiracy Vault 45. Os maiores "5 primeiros" da amostra estão em canais com 113–226 dias — o gate de idade é o gargalo, não a audiência.

## Outliers (janela de 2–6 semanas)

- **The Conspiracy Vault** — 67,3× — 3.030 views — "Bernie Madoff: The $50 BILLION Ponzi Scheme That Fooled America" — 2026-09-06 — padrão: caso clássico EN + cifra no título + "Ponzi Scheme" na query.
- **NET CREATIVE** — 35,4× — 537.424 views — Ponzi de empresa de viagens (Cipaganti, Rp3,2 trilhões) — 2026-09-10 — padrão: caso nacional + cifra + "dari raja travel jadi penipu"; idioma ID, fora do cruzamento EN.
- **Anatomía del Fraude** — 17,8× — 1.013 views — OneCoin/Ruja Ignatova em Short — 2026-07-29 — padrão: Short ES de caso global com "#documental" (idioma ES; mostra que o tema roda em Short).
- **Nexplainr** — 4,0× — 880 views — Madoff — 2026-07-22 — mesmo tema do Conspiracy Vault.

## Fome do algoritmo (cluster cross-canal)

- **Madoff em 2 canais diferentes** (Nexplainr 4,0× em 22/07 e The Conspiracy Vault 67,3× em 06/09, ambos ≤200k subs) → sinal aberto na janela de 2–6 semanas no tema "maior Ponzi da história".
- **OneCoin** em 1 canal (Anatomía del Fraude, 17,8× em Short ES) e **Ponzi local** em 1 canal (NET CREATIVE, 35,4× em ID) — temas quentes em outros idiomas, sem par EN detectado na amostra.
- Ressalva de método: os ratios altos vêm de **medianas minúsculas** (45–218 views). Cross-channel existe, mas volume absoluto do cruzamento EN é baixo — é sinal de "cabe um entrante", não de "o algoritmo está empurrando o tema".

## Verificação individual (convergência de formato)

- **Nexplainr** (`--channel @Nexplainr`, casou com os números do cluster): 113 subs · 152d · 5 primeiros 1.974 · 72/dia · mediana 218. **4 outliers ≥3× na janela de 90d**: 9,1× (1.977 — "The Kid The FBI Can't Catch", 08/08) · 5,7× (1.250 — "The Lottery Curse", 25/07) · 4,0× (880 — Madoff, 22/07) · 3,2× (704 — "What If Saudi Arabia Ran Out of Oil Tomorrow?", 03/07). Formato: explainer dark narrado, temas **heterogêneos** (crime, loteria, Ponzi, macro) — não há convergência em Ponzi/cripto; o canal é "história sombria com número".
- **Built on Lies** — convergência confirmada pela descrição pública do canal: "uncovers history's greatest con artists, fraudsters, and financial manipulators… New documentaries on the world's most infamous frauds, scams, and financial collapses — every week" (SocialCounts, ago/2026). 2.180 subs · 127d · 5 primeiros 335.374 · 3.278/dia · mediana 28.306. É o canal-evidência mais aderente ao formato do modelo (documentário EN semanal de fraude), **falhando só a idade**.
- **Checagens por handle que não casaram** (registro honesto): `@builtonlies`, `@findicate` e `@thecollapsearchives` resolveram para homônimos antigos/pequenos, e `@TheConspiracyVault` deu `playlistNotFound` — handle ≠ canal do scan. 2 de 5 checagens casaram (Nexplainr; e a leitura do Built on Lies veio de fonte web). Nas próximas rodadas, capturar `channelId` no cluster para checar por ID.

## Demanda (autocomplete — 111 termos; top relevantes)

- Raiz e vizinhança: `crypto scam documentary`, `crypto scam movie`, `cryptocurrency scam documentary`, `crypto scam`, `crypto documentary`, `crypto scam documentary explained`, `crypto scam documentary full`, `crypto scam documentary true crime`, `crypto scam documentary dark web`, `crypto scam documentary crime investigation`.
- Distribuidores de streaming e mídia: `netflix`, `amazon prime`, `bbc`, `national geographic`, `real stories`, `recent`, `latest`, `new`.
- Geografia (cauda global): `australia`, `canada`, `uk`, `usa`, `india`, `korea`, `japan`, `kenya`, `malaysia`, `philippines`, `south africa`, `egypt`, `haiti`, `zimbabwe`.
- Formato: `part 1` / `part 2` / `compilation` / `with subtitles` / `green screen`.
- Ruído de autocomplete (não seguir): `hailey bieber`, `david attenborough`, `joe rogan`, `law of attraction`, `mr beast`, `xbox`, `red bull` — termos colados por sessão, não demanda do nicho.

## Trends (YouTube 12m)

- Direção da busca do brief: **ALTA** (recente 25 vs anterior 0). Queries em alta: nenhuma retornada pelo scan nesta rodada (lista vazia).
- Leitura: a curva estava zerada e subiu no período recente — coerente com o outlier de Madoff em set/2026, mas sem massa histórica (ano-base baixo). Rechecar em 2–4 semanas com `--trends "ponzi scheme documentary"`.

## Comentários (demanda explícita)

- **Não coletado via Data API**: o cluster/brief não expõe `videoId` e `--comments` exige o escopo `youtube.force-ssl` (rodar `python scripts/yt_auth.py` uma vez). Proxy qualitativo por comunidades:
  - r/crimedocumentaries (08/04/2026): thread "Why did the SEC ignore proof of Bernie Madoff's fraud for 8 years?" com gente pedindo o "porquê" e o autor dizendo que fez o vídeo — a pergunta "por que ninguém parou" é o que puxa.
  - r/Documentaries: threads recorrentes de OneCoin (Cryptoqueen BBC, DW) com pedidos de "o que aconteceu com ela" e comentários "there's also a great podcast about this" — o público compara com podcast, não com jornal.
  - r/Documentaries (10/05/2026): pedido de docs "about rich people or companies losing money" com listas colaborativas (Madoff Netflix, Fyre, WeWork, Dirty Money) — apetite evergreen pela queda.

## Fontes web (2+)

- https://en.wikipedia.org/wiki/Coffeezilla — perfil do canal-referência do nicho: 4,69M subs e 591M views (jul/2026); trilogia CryptoZoo (dez/2022); histórico de ameaças e processo de difamação.
- https://storage.courtlistener.com/recap/gov.uscourts.txwd.1172793701/gov.uscourts.txwd.1172793701.1.0.pdf — *Paul v. Findeisen* (W.D. Tex. 5:24-cv-717): a peça acusatória trata "scam/serial scammer" como factoide difamatório — base do risco jurídico do nicho.
- https://openclassactions.com/news/logan-paul-coffeezilla-defamation-lawsuit.php (10/07/2026) — estado do caso: recomendação de Bemporad (mar/2025) de **negar** o motion to dismiss porque acusação de fraude por investigador especializado é **verificável**, não opinião; sem veredito.
- https://bohonews.com/articles/logan-paul-coffeezilla-settlement-videos-unavailable/ (26/08/2026) — desfecho: acordo em jul/2026, dismissão com prejuízo, cada lado com seus custos; **3 publicações ligadas às contagens ficaram indisponíveis** nas URLs, trilogia original de 2022 segue pública.
- https://www.law360.co.uk/articles/2504985/logan-paul-youtube-crypto-critic-end-defamation-dispute (23/07/2026) — confirma o encerramento do litígio por acordo.
- https://www.dehek.com/general/scam-fraud-investigations/response-to-cease-and-desist-letter-goliath-ventures-chris-delgado/ (09/09/2025) — carta de cessar-e-desistir de 10 páginas (Goliath Ventures/Chris Delgado) contra jornalista; resposta pública mantém "alleged Ponzi"; o caso evolui para acusação do DOJ em 2026 (Cointzilla, mai/2026).
- https://www.youtube.com/watch?v=04FRAsU0za0 (mai/2026) — Coffeezilla, "$300,000,000 Scam": o próprio vídeo mostra o modelo de receita ("we don't do sponsorships", Patreon) e a frase "I'm going to go public whether I get sued or not" — o custo jurídico do formato.
- https://outlierkit.com/channel/jamesjani (16/09/2026) — benchmark faceless do nicho: 2,2M subs, 95,3M views, 28 vídeos, média 3,4M/vídeo, 38,5K views/dia de vida, est. $4K–$22K/mês [ALEGADO]; canal **dormente há 367 dias**; risco apontado: expor golpes ativos e nomear organizações poderosas.
- https://socialblade.com/youtube/handle/jamesjani (07/06/2026) — faixa de ganho estimado $1,3K–$21K/mês [ALEGADO — estimativa, não dado do dono].
- https://www.patreon.com/jamesvj — modelo de financiamento declarado: "without relying on brand sponsorships or worrying about demonetisation" — evidência de que o nicho se financia por membros.
- https://faceless.my/youtube/faceless-finance-documentary-channels/ (09/05/2026) — formato faceless de finanças: narração + B-roll/arquivo + gráficos, 10–25 min, RPM estimado $10–$25 [ALEGADO]; shapes recomendados incluem "scam or fraud explainers".
- https://socialcounts.org/youtube-live-subscriber-count/UCvrpitoPwr32TZEJos_e6yQ (ago/2026) — Built on Lies: descrição e cadência semanal (documentário de fraude EN) — base da leitura de convergência.
- https://socialcounts.org/youtube-live-subscriber-count/UCB3l10bl80GEN4-bvu3C6kA (ago/2026) — HiddenEmpires of Corporate Fraud: 1.159 subs, 11 vídeos, 801 views totais, est. $1–2 — mostra que **entrar no formato não garante tração**.
- https://www.reddit.com/r/crimedocumentaries/comments/1sfywzj/ (08/04/2026) · https://www.reddit.com/r/Documentaries/comments/1edprs8/ (OneCoin) · https://www.reddit.com/r/Documentaries/comments/1t9meb3/ (10/05/2026) — demanda explícita de "por que ninguém parou" e de docs de queda financeira.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Em EN long-form documentário de fraude, a oferta recente pequena é rasa e de qualidade variável: Built on Lies (127d, forte, sem outlier de ratio), The Dark Ledger (83d, fraco), The Bankruptcy Files (70d, fraco), HiddenEmpires (11 vídeos, 801 views). O **gate ≥3 não fecha** e o único sinal cross-canal consistente (Madoff) tem volume absoluto baixo. Onde há volume (35,4× / 537k views) está em outro idioma (ID). Conclusão: cruzamento **aberto porém não validado** — revalidar antes de escalar.
- **Difamação (risco central, com precedente):** o tribunal recusou tratar "scam" como opinião e o litígio só terminou 2 anos depois, com publicações removidas de suas URLs. Implicações para o modelo: (1) caso adjudicado ou réu formalmente acusado; (2) "charged/alleged/prosecutors say" sempre; (3) nunca "scammer" para pessoa viva sem condenação; (4) guardar autos/screenshots do que foi publicado + versão datada do roteiro.
- **Compliance/advertiser:** dinheiro + acusação atrai escrutínio; o enquadramento documento/educação é o que sustenta monetização; sem conselho de investimento, sem exposição de vítimas, sem gore.
- **Inautenticidade:** o formato é naturalmente pesquisa-pesada; o risco é produzir "recap de notícia" em série — 1 peça primária por vídeo, estrutura variável, fontes na descrição, ponto de vista próprio (`09`).
- **Caso vivo:** Goliath/Delgado, FTX-residual e memecoins em litígio exigem checagem do estado processual na data de publicação (o vídeo envelhece mal e a atualização vira problema).

## Queries tentadas e próximas (gate não fechou)

- `crypto scam documentary` — **TENTADA** (busca 1 / brief): 0/8 gates; fome 1 (OneCoin Short, ES); autocomplete 111; Trends ALTA.
- `ponzi scheme documentary` — **TENTADA** (estreita autorizada): 0/8 gates; fome 3 (Madoff em 2 canais + Ponzi indonésio 35,4×); sinal SIM.
- **Não rodadas** (regra de UMA segunda busca): `crypto collapse documentary`, `bernie madoff documentary`, `onecoin documentary`, `ftx documentary`, `bitconnect documentary`, `crypto ponzi scheme explained`.
- Revalidar em **2–4 semanas**: (a) repetir a estreita com amostra maior (elegíveis 20; analisados 8) e `--out` para guardar o JSON; (b) checar se Built on Lies cruza/expande e se aparece canal ≤45d no cruzamento; (c) rodar `--trends "bernie madoff documentary"` e `--trends "onecoin documentary"`; (d) `--comments` em 1 vídeo de Built on Lies (precisa de `youtube.force-ssl`) para ler pedidos recorrentes.
