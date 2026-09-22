# Modelo — Ponzi e cripto

> Categoria: Finanças · Subnicho: esquemas Ponzi e golpes de criptomoedas · Slug: `finance-ponzi-crypto`
> Lane: mixed · Idioma: en (docs PT-BR, exemplos em EN) · RPM (classe): $18–25 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 — 0/16 canais passam os 3 gates (meta ≥3), mas há **fome do algoritmo em 4 canais** (outliers 4,0×–67,3×, com o tema Madoff em 2 canais diferentes) e **0 emergentes ≤90d com 2/3 gates**; revalidar com as queries estreitas antes de escalar (ver `evidencia.md`)

## 1. Posicionamento (1 frase)

Reconstrução de caso para quem quer entender o mecanismo: cada episódio abre o extrato de um Ponzi ou golpe cripto real, mostra de onde vinha o dinheiro que pagava os investidores antigos e onde o rastro parou, a partir de autos de tribunal, ações da SEC/DOJ/CFTC e dados de blockchain.

## 2. Público e promessa

- **Público:** 28–50 anos, US/Canadá/UK/Austrália no núcleo, com cauda global (o autocomplete puxa `india`, `kenya`, `philippines`, `malaysia`, `south africa`, `korea`); já consome Coffeezilla, James Jani, "Madoff: The Monster of Wall Street" (Netflix), "The Missing Cryptoqueen" (BBC/podcast) e a categoria finance do r/Documentaries e r/crimedocumentaries. Sabe o que é um Ponzi; quer o mecanismo, não o susto.
- **Promessa do canal:** em todo vídeo o espectador entende *por que o esquema pagava*, *por que durou tanto* e *por que caiu*, com pelo menos um documento verificável no vídeo (auto, ordem da SEC, release do DOJ, carteira na blockchain) e uma regra prática para o próximo "investimento" que aparecer.
- **Inimigo da promessa:** chamar alguém de "scammer" sem condenação ou acusação formal, expor vítimas, repetir narrativa de mídia sem citar fonte, especular sobre paradeiro de foragidos, sensacionalismo de "você foi enganado".

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete/trends) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Ponzi clássicos EN (Madoff, Stanford, Charles Ponzi 1920) | **alta** — fome real: 2 canais diferentes com outlier no **Madoff** (The Conspiracy Vault 67,3×; Nexplainr 4,0×); Threads r/crimedocumentaries | **média** — muitos vídeos soltos, mas nenhum canal EN ≤45d passando os gates; o espaço é de *documentário de caso*, não de recap | O extrato que não fechava: 4 minutos de matemática vs 8 anos de SEC |
| Colapsos cripto (FTX, Celsius, Terra/Luna, Voyager) | **alta** — `crypto scam documentary` com Trends em ALTA (25 vs 0 na busca do brief); autocomplete `crypto documentary`, `crypto scam movie` | **média-alta** — cobertura jornalística saturada em 2022–24; ângulo documento+blockchain ainda abre | A contabilidade impossível: dinheiro de cliente usado como capital de giro |
| Golpes cripto por mecanismo (BitConnect, OneCoin, rug pulls, memecoins) | **alta** — OneCoin puxa 2 outliers de canais diferentes (17,8× em Short; 67,3× era Madoff — OneCoin tem outlier próprio em Anatomía del Fraude); autocomplete `onecoin`-adjacente via `crypto scam documentary` | **média** — OneCoin já tem BBC/podcast; o ângulo "não havia blockchain" é pouco explorado em EN no YouTube | O mecanismo puro: o que o produto prometia e o que existia de fato |
| Pirâmides/MLM e esquemas locais fora dos EUA (Bulgária, Quênia, Indonésia, Brasil, Índia) | **média-alta** — autocomplete `crypto scam documentary india / kenya / malaysia / philippines / south africa`; outlier de 35,4× num Ponzi indonésio (NET CREATIVE) | **baixa-média** em EN — o material local está quase todo em idioma nativo | A mesma máquina, outro país: o Ponzi que virou marca nacional |
| Fraudes corporativas com mecânica Ponzi (Wirecard, Enron, Theranos) | **média** — canal MKT Glory Story publicando Wirecard em 2026; sobrepõe com `finance-fraud`/`finance-corporate-collapse` | **média** | Fronteira com o modelo irmão; usar quando o mecanismo de pagamento for o elo Ponzi |

## 4. Lane e formato

- **Lane:** mixed — justificativa: o short curto é onde apareceu o outlier isolado de canal pequeno (Anatomía del Fraude, 17,8× num Short de OneCoin) e o formato explicado/recap é onde os ratios maiores aparecem (NET CREATIVE 35,4×; The Conspiracy Vault 67,3×; Nexplainr 4,0×). O long-form é o que carrega a classe de RPM finance e o watch time (`10`). Sem gate-passer em nenhum dos dois formatos, o mixed só se mantém **com o funil medido** (`30`); se o Short não converter inscrito→long em 30 dias, cair para long-first.
- **Duração alvo:** long 14–22 min (padrão ~18) · short 20–28s · **Cadência:** 1 long/semana + 1 short a cada 2–3 longs (ratio 0,28–0,40 — `10`).
- **Mix:** ~75% long / ~25% short; Short como aquisição com Related Video apontando para o long do dia (`21`).

## 5. Fingerprint de formato (o que o recomendador lê)

Long 16:9 de 14–22 min, 1/semana, narração EN única (~150–160 palavras/min), zero rosto, zero webcam; short 9:16 de 20–28s recortando **um número** do caso. Assets: autos de tribunal e PDFs (SEC litigation releases, DOJ, CFTC, tribunal), manchetes de época, gráficos de preço e de fluxo de dinheiro, timelapses de capturas de tela de sites/promessas arquivadas (Wayback), visualizações de blockchain. Estilo visual: documento em tela + zoom em trecho sublinhado + cifra grande no centro-alto. Thumb: 1 objeto-documento (extrato, auto, gráfico caindo) + cifra + 3–5 palavras que não repetem o título. Convergência observada nos canais-evidência do cruzamento (Built on Lies, HiddenEmpires, Nexplainr): título-caso no padrão `[Nome/Esquema]: [cifra] [promessa/queda]` e cadência semanal declarada; a exceção (Foragidos/commentary) é o território do Coffeezilla, que é persona, não formato dark.

## 6. Estrutura de roteiro

- **Beats:** `models/finance-ponzi-crypto/beats.json` (gênero `finance-ponzi-crypto`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); FINO (12–15 min, ~1.900–2.400) para esquemas com pouca fonte primária; RICO (24–27 min) para FTX/Madoff. Short: ~60–70 palavras.
- **Dispositivos:** rehook a cada 2–4 min (novo documento, nova camada do mecanismo); re-engage ~3 e ~6 min; 3–5 open loops no hook (a promessa, o mecanismo, o documento que derruba, o dinheiro); pattern interrupt a cada 30–90s (documento → gráfico → blockchain → manchete); pergunta central ("de onde vinha o pagamento") que só fecha no fim.
- **Pesquisa obrigatória (1 peça primária por vídeo):** ação/auto da SEC ou CFTC, release do DOJ, ordem de tribunal, demonstrativo/relatório do síndico (recovery report), depoimento, dado de blockchain; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[ALEGADO]. Sem peça primária o vídeo não entra em produção — é o que separa este modelo de recap de notícia.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** número + stake (a cifra que não existia) e contradição verificada (o que o documento dizia vs o que o dinheiro fazia).
- **Exemplos:**
  1. "Every dollar of return came from the next investor who signed. For years, that was enough."
  2. "He proved the numbers were impossible in four minutes. It took the regulators eight years."
  3. "The coin had no blockchain. It still sold four billion dollars' worth."
- **Proibido:** abstração/filosofia ("no mundo das finanças…"); data ou local antes do gancho; meta-linguagem ("in this video"); acusar pessoa viva sem "alleged/charged"; prometer recuperação de dinheiro ou culpado que o vídeo não comprova.

## 8. Thumbnail

- **Composição:** 1 objeto-documento (extrato com linha circulada, auto judicial, gráfico em queda, cold wallet) + 1 cifra grande + 3–5 palavras que não repetem o título.
- **Paleta:** preto/grafite + verde-terminal ou vermelho-alerta, alto contraste · **Fonte:** sans bold, legível a 120px.
- **Nunca:** rosto de pessoa viva como culpada, algemas genéricas sem relação com o caso, logos de exchange/marca sem necessidade, gore, cifra maior do que a documentada no vídeo.

## 9. Monetização

- **AdSense (classe):** $18–25 [ALEGADO] — vem do índice da biblioteca (modelo `finance-ponzi-crypto`); a classe de referência em `10` é Finance/Investing $12–23 e Investing/Economics $17–21, e o gênero "documentary" aparece a $12,6 na mesma tabela. Trate $18–25 como **hipótese de classe**, não como fato: confirma-se só na Analytics. Conteúdo financeiro é sensível a advertiser de marca em quadro de acusação; o enquadramento documento+educação é o que sustenta a faixa alta.
- **Produto digital (tripwire $7–27):** "case file" por episódio (linha do tempo, links dos autos, extrato do mecanismo, checklist anti-Ponzi) e bundle de temporada $19–27; serve também como isca de e-mail para auditar a série.
- **Patreon/membros:** sim — é o padrão do gênero: James Jani declara financiar o canal "without relying on brand sponsorships or worrying about demonetisation"; Coffeezilla não faz sponsorship e roda em Patreon. Libera faixa de entrada a partir de 500 inscritos (`21`).
- **Afiliado/brand:** livros de caso (Amazon Associates; "Easy Money" de Ben McKenzie, "The Missing Cryptoqueen"), Audible; **não** aceitar afiliado de corretora/exchange (conflito direto com a promessa e com o tema).
- **Rota no funil (`21`):** Short (1 número do caso) → inscrito → long do dia → case file.

## 10. Produção

- **Custo/tempo por vídeo (estimativa operacional do modelo):** long 12–18 h — pesquisa em autos 5–8 h (a etapa mais pesada), roteiro 2–3 h, assets/gráficos 2–3 h, voz + edição 3–4 h; short 1–2 h (recorte do long). Sem locação, sem equipe, sem gravar em rua.
- **Assets:** PDFs públicos (SEC, DOJ, CFTC, tribunal, relatórios de síndico), Wayback Machine para páginas de venda e promessas, capturas de blockchain explorer, gráficos próprios de fluxo do dinheiro, manchetes com crédito. Nada de footage de streaming nem de frames de documentário de terceiro.
- **Voz:** narrador EN consistente (edge-tts ou ElevenLabs; ~150–160 palavras/min, pausado) ou locução própria; voz única = marca (`14`). Divulgar voz/imagem sintética no pacote quando aplicável.

## 11. Riscos

- **Difamação (risco nº 1 deste nicho, com precedente):** no caso *Paul v. Findeisen* o tribunal americano recusou tratar "scam/serial scammer" como opinião — em maio/2025 a corte entendeu que acusações de fraude feitas por um investigador especializado são **verificáveis** e o caso seguiu; terminou em acordo com dismissão em julho/2026 e as três publicações ligadas às contagens ficaram indisponíveis nas URLs conhecidas (a trilogia original de dez/2022 segue pública). Lição operacional: **disclaimer em descrição não cura acusação factual**. Regras do canal: usar apenas casos adjudicados (condenação, guilty plea, ordem da SEC, prisão) ou pessoas já acusadas formalmente e descritas como "charged/alleged"; para o resto, "prosecutors allege" + documento; nunca "scammer" como rótulo de pessoa viva sem condenação.
- **Compliance/advertiser:** dinheiro e acusação atraem revisão; enquadrar como educação/consumidor final e manter ausência de conselho de investimento ("this is not financial advice" só como marcador de escopo, não como escudo legal). Sem gore; sem exposição de vítimas identificáveis.
- **Inautenticidade:** tema com risco de flag por "recap de notícia" massificado (`09`) — 1 peça primária por vídeo, estrutura variável, fontes na descrição, ponto de vista próprio; sem template com 50 Shorts idênticos.
- **Foragidos e casos abertos:** Ruja Ignatova (OneCoin) está na lista dos mais procurados do FBI e há especulação sobre paradeiro; nunca afirmar que está morta ou localizada. Chris Delgado/Goliath Ventures: caso com acusação do DOJ e cessar-e-desistir contra jornalista — usar "alleged/charged" e autos, nunca veredito próprio.
- **Direitos:** PDFs públicos e citações curtas com crédito; capturas de reportagem só com citação; nunca trecho longo de streaming/podcast de terceiro.

## 12. 10 ideias-semente (títulos)

1. Madoff: The $65 Billion Statement That Never Existed
2. Four Minutes of Math: The Analyst Who Broke Madoff's Returns
3. OneCoin: The $4 Billion Currency With No Blockchain
4. BitConnect: One Percent a Day, Paid by the Next Deposit
5. FTX: The $8 Billion Hole in the Customer Accounts
6. Celsius: The Withdrawal Button That Stopped Working
7. Terra/Luna: The $40 Billion Algorithm That Ate Itself
8. Stanford: The $8 Billion Certificates Nobody Audited
9. Ponzi's Own Scheme: 50% in 45 Days, 1920
10. The SEC Walked Into the Office Three Times. The Fraud Kept Paying.

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção de 30s ≥70%; AVD ≥30% em longs de 14–22 min; Short: swipe-away no 1º segundo <25% e AVP 50–65% na faixa de 20–28s (`02`).
- **D+7:** views e watch time do long; inscritos por vídeo; conversão Short→long medida (cliques no Related/comentário fixado ≥2%); 1 vídeo ≥3× a mediana do canal.
- **Meta de validação (30 dias):** 4–5 longs + 1–2 shorts publicados; ≥1 long com outlier ≥5×; **nenhuma reclamação/notificação jurídica** e nenhum vídeo limitado; funil Short→long medido. Como o gate de nicho não fechou na coleta (0/16), o piloto precisa ainda provar em 30 dias que existe canal novo sustentável no cruzamento — se as views medianas ficarem abaixo do gate de 10k nos 5 primeiros, o modelo volta para revalidação com as queries estreitas do `evidencia.md`.
