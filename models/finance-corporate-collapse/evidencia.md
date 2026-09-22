# Evidência — Colapsos corporativos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "corporate collapse documentary" --max 8` + `python scripts/niche_scan.py --cluster "business scandal documentary" --max 8` + websearch
> Brief completo: `data/briefs/corporate-collapse-documentary.md` · JSON: `data/briefs/corporate-collapse-documentary.json`
> A saída bruta do cluster (2ª busca) não foi salva em arquivo; é reproduzível pelo comando acima (janela default de 90d, ratio 3,0×, subs ≤200k, idade ≤365d).

## Veredito: **PARCIAL**

- Canais pequenos analisados: 16 (8 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Emergentes ≤90d com 2/3 gates (watchlist): **2** — Tech Of History (73d) e Animated Archives HQ (57d)
- Fome do algoritmo (outlier ≥3×): **9 canais distintos** (5 no brief + 4 no cluster) — sinal: **sim**
- Autocomplete: 103 termos (meta ≥15; profundidade inflada por sufixos) | Trends: **ALTA** (recente 2 vs anterior 0 — volume absoluto baixo, sinal fraco)

**Leitura honesta:** as duas varreduras deram **REPROVA no critério rígido** (0 canais ≤45d passando os 3 gates, em 0/8 e 0/8). O que sustenta o PARCIAL: (1) **fome cross-canal** em 7 semanas — 9 canais diferentes com outlier ≥3× entre 24/07 e 11/09/2026, com convergência de tema (rise-and-fall, outcome-first); (2) **2 emergentes ≤90d** que falham só a idade e passam os dois gates de conteúdo (Animated Archives HQ com 14.137 views/dia e dois outliers, 24,3× e 8,9×; Tech Of History com 16.815 nos 5 primeiros e 2.864 views/dia); (3) formato convergente e estável no teardown do nicho (9–12 min, narração + filings + motion graphics). O gargalo desta coleta **não é demanda — é a janela de 45 dias**, como nas outras rodadas. Revalidar em 2–4 semanas: se um terceiro canal ≤45d aparecer com os dois gates de conteúdo, o modelo cruza para PASSA.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Tech Of History (brief) | 1.690 | 73d | 16.815 | 2.864 | 011 | — (emergente) |
| Animated Archives HQ (cluster) | 1.650 | 57d | 35.947 | 14.137 | 011 | 24,3× — 27.497 — 2026-08-26 · 8,9× — 10.115 — 2026-09-04 (emergente) |
| NET CREATIVE (cluster, canal em ID) | 2.480 | 113d | 160.245 | 6.784 | 011 | 35,4× — 537.424 — 2026-09-10 |
| Dynasty Undone (cluster) | 1.300 | 105d | 11.217 | 2.047 | 011 | — |
| StoryCo (cluster) | 1.880 | 188d | 49.347 | 3.542 | 011 | — |
| Company Killers (brief) | 967 | 81d | 3.891 | 254 | 000 | 16,3× — 11.365 — 2026-08-21 |
| Read The Boardroom (brief) | 20 | 103d | 1.206 | 12 | 000 | 19,5× — 896 — 2026-07-24 |
| Sector Down (brief) | 63 | 109d | 2.128 | 60 | 000 | 3,8× — 675 — 2026-07-29 |
| The Business Obituary (brief) | 210 | 33d | 941 | 149 | 100 | 4,9× — 570 — 2026-09-08 |
| Business Files Hindi (brief) | 5 | 90d | 1.217 | 12 | 000 | 4,5× — 786 — 2026-08-14 |
| True Doc (cluster) | 106 | 129d | 12.076 | 126 | 010 | 10,4× — 2.417 — 2026-07-28 |
| Doa Fatima (cluster) | 35 | 91d | 5.229 | 1.212 | 001 | 16,3× — 11.981 — 2026-09-11 |
| Just Saying... (cluster) | 636 | 241d | 34.885 | 613 | 010 | — |
| Empire Lane (brief) | 170 | 344d | 606 | 124 | 000 | — |
| The Money Case (cluster) | 89 | 178d | 1.190 | 122 | 000 | — |
| Billion Dollar Mistakes (brief) | 2 | 30d | 975 | 124 | 100 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). No brief, 8 canais analisados (0 passaram); no cluster, 21 canais pequenos ≤365d encontrados e 8 analisados por quota (0 passaram). O cluster analisou canais ≤365d — por isso aparecem canais de 100–240d.

## Outliers (janela de 2–6 semanas)

- **NET CREATIVE** — 35,4× — 537.424 views — "Skandal Rp3,2 Triliun Cipaganti: Dari Raja Travel Jadi Penip..." — 2026-09-10 — canal em indonésio (fora do recorte EN); padrão: escândalo local de escala bilionária + cronologia. Prova que a fome atravessa geografia, não serve como evidência direta do recorte EN.
- **Animated Archives HQ** — 24,3× — 27.497 views — "How America's 7th Largest Company Vanished in 24 Days | Corp..." — 2026-08-26 — padrão: pergunta "how + vanished + N days" + colapso de empresa conhecida; segundo outlier no mesmo canal 8,9× — "The Biggest Corporate Fraud in Human History - EAST INDIA CO..." (2026-09-04).
- **Read The Boardroom** — 19,5× — 896 views — "Lehman Brothers' Fatal Flaw | The $50 Billion Cover-Up" — 2026-07-24 — canal de 20 subs: padrão de título "empresa + fatal flaw + número", prova que o padrão funciona mesmo em canal praticamente sem audiência.
- **Company Killers** — 16,3× — 11.365 views — "How to Destroy a Billion-Dollar Empire (Corporate Fails Compilation)" — 2026-08-21 — padrão: destruição como promessa + compilação de falhas.
- **Doa Fatima** — 16,3× — 11.981 views — "Joe Rogan Breaks Down the New Elizabeth Holmes Scandal | T..." — 2026-09-11 — padrão reativo (react/clip) ao escândalo Theranos; fora do formato documentário — **anti-modelo** por depender de terceiros.
- **True Doc** — 10,4× — 2.417 views — "The ABG Shipyard Scam: 22,842 Crore... GONE? India's Biggest..." — 2026-07-28 — padrão: colapso não-americano com número gigante e cifra em moeda local; chance de "traduzir" casos globais para EN.
- **The Business Obituary** — 4,9× — 570 views — "Why Reliance Communications Failed | Anil Ambani's Telecom Collapse" — 2026-09-08 — padrão "Why [company] failed" + dinastia (nome do fundador no título; atenção a alleged).
- **Business Files Hindi** — 4,5× — 786 views — "The Shocking Truth Behind Wirecard's Collapse" — 2026-08-14 — Wirecard funciona em qualquer idioma; tema de escândalo contábil com demanda multi-mercado.
- **Sector Down** — 3,8× — 675 views — "Circuit City Cut Its Experts. Then It Collapsed." — 2026-07-29 — padrão: a decisão única no título, sem número; formato "one decision" que o teardown recomenda.

## Fome do algoritmo (cluster cross-canal)

**Sim.** Nove canais distintos com outlier ≥3× em sete semanas (24/07 a 11/09/2026), sendo 3 no mesmo padrão de título "how [company] vanished/lost X" (Animated Archives HQ, Company Killers, Read The Boardroom) e 4 casos globais (Reliance, ABG, Cipaganti, Wirecard). Nenhum canal repete sozinho o padrão dominante — é fome de tema em canais diferentes, não um canal viral isolado. A janela de 2–6 semanas segue aberta para o recorte "outcome-first autópsia de colapso".

## Demanda (autocomplete — top termos)

103 termos únicos (meta ≥15), profundidade inflada por permutações de sufixo (`...australia`, `...bbc`, `...netflix`, `...explained`), mas com termos reais: `corporations documentary`, `collapse documentary`, `corporate consolidation`, `corporate state`, `corporate collapse documentary full movie`, `corporate collapse documentary debt`, `corporate collapse documentary china/canada/japan/korea`, `corporate collapse documentary dw/cnn/channel 4`. Leitura: intenção de "documentário de colapso" existe e tem cauda longa geográfica — o caso não precisa ser americano.

## Trends (YouTube 12m)

- Direção: **ALTA** (média recente 2 vs anterior 0) · Rising: nenhuma query listada pelo script.
- Leitura: classificação "ALTA" sobre volume absoluto baixíssimo (2 vs 0) — sinal fraco, não apostar tendência; o nicho se sustenta por **busca durável** ("por que [empresa] faliu"), não por pico.

## Comentários (demanda explícita)

Não coletado — `--comments` exige o escopo `youtube.force-ssl` (pendente de re-auth). Nota: o padrão dos outliers sugere demanda explícita do tipo "do [company] next", que deve ser confirmada na Analytics quando o canal existir.

## Fontes web (2+)

- https://outlierkit.com/resources/faceless-business-documentary-channels/ — teardown do formato (27/07/2026): 9–12 min; CPM $10–25; "real RPM is about half the gross CPM"; 16–28h por vídeo; clipe de broadcast é a maior fonte de claim; 4 modos de falha (resumir em vez de sequenciar, intro no lugar da história, footage sem licença, empresa que ninguém conhece); stats dos exemplares: MagnatesMedia 1,9M subs, ColdFusion 5,2M, Company Man 1,8M, How Money Works 1,7M, Business Casual 1,1M, Logically Answered 912k, Modern MBA 801k, Wall Street Millennial 366k.
- https://faceless.my/youtube/faceless-finance-documentary-channels/ (09/05/2026) — finance documental estimado em $10–25 RPM [ALEGADO]; formatos 10–25 min; "company collapse" listado como topic shape de demanda comprovada; path de monetização (ads + sponsors + produto).
- https://fluxnote.io/blog/business-scandals-youtube-channel-guide-2026-start-and-monetize (01/05/2026) — guia do subnicho "business scandals" faceless em 2026; CPM estimado $5–15 [ALEGADO]; arco narrativo recomendado (hook, rising action, climax, aftermath, lesson); cita MagnatesMedia (2,1M subs) e Plainly Difficult (1,3M).
- https://somethingthisweek.substack.com/p/i-went-looking-for-brand-decay-i (01/09/2026) — crítica de campo ao formato: dezenas de documentários faceless quase idênticos sobre Sears/Craftsman publicados em 8 meses, sem crédito de fonte, com erros factuais verificáveis (data da Western Forge, contagem de catracas vendidas, lenda dos $500 sem fonte primária) — o **anti-padrão** que o modelo precisa evitar para não cair em conteúdo inautêntico.
- https://www.solicitorsjournal.com/sjarticle/rzucek-v-vinnicombe-youtube-conspiracy-videos-about-watts-murders-yield-40000-defamation-award (23/04/2026) — condenação de £40.000 + injunção contra canal de YouTube por vídeos difamatórios sobre pessoa ligada a caso; prova que difamação online gera condenação real e alcança publisher no exterior.
- https://www.gibsondunn.com/gibson-dunn-secures-precedential-dismissal-of-defamation-lawsuit-for-warner-bros-sony-and-documentary-filmmakers/ e https://www.latimes.com/entertainment-arts/story/2026-09-11/dan-schneider-quiet-on-set-defamation-suit-thrown-out (set/2026) — ação por "defamation by implication" contra documentário: mesmo com vitória final em anti-SLAPP após ~2 anos, o custo do processo é real; a decisão mostra que separar conduta de crime no roteiro é o que protege.
- https://www.lawcommentary.com/articles/kalshi-threatens-netflix-with-defamation-suit-over-prediction-markets-documentary-trailer (27/07/2026) — cessar-e-desistir por causa do trailer: enquadramento/edição podem criar a implicação difamatória mesmo quando o conteúdo não é falso; cuidado com o que o corte sugere.
- https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm (01/07/2026) — dados reais de 300 canais: Business & Finance mediana de **$2,01 RPM** (amostra pequena, direcional) contra mediana geral de $2,30; longo-form creator fica com 55%; leitura: a classe $18–25 [ALEGADO] é teto de faixa alta, não piso — o resultado depende de geo Tier-1 e formato.
- https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ (07/09/2026) — 98 nichos faceless: Finance $23,10 e Documentary $12,6 em médias estimadas [ALEGADO/estimativas]; saturação "Medium" em ambos; lembra que RPM estimado é direcional e contestável.
- https://vidiq.com/blog/post/most-profitable-youtube-niches/ (20/04/2026) — finance CPM $15–50 / RPM $5–17 [ALEGADO]; longo-form ~20× mais por view que Short; Q4 eleva CPM de finanças.
- https://www.youtube.com/watch?v=Fh9M6FP4ksA — Collapse Archive, "The Handshake That Destroyed America's Biggest Oil Company" (11/05/2026): exemplo real de canal do nicho em 2026, formato outcome-first + cronologia documental (Texaco/Getty/Pennzoil).
- https://www.youtube.com/watch?v=tYNdSGqTAbo — Business Unmasked, "The $74 Billion Lie: How Enron Fooled America" (28/02/2026): mostra que o caso Enron segue sendo recontado em 2026 com demanda.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Sim, com ressalva: os exemplares gigantes (MagnatesMedia 1,9M, Company Man 1,8M, ColdFusion 5,2M) dominam a prateleira aspiracional, mas a fome recente está em canais minúsculos (20–1.700 subs) que publicam casos específicos com título outcome-first — e ninguém domina o recorte "autópsia com documento primário + caso global". O risco de saturação imediata é do formato "resumo de colapso" genérico (onda de Sears/Craftsman documentada pelo Something This Week); o espaço aberto é **mecânica** (o que o balanço escondia), **documento primário** e **casos fora do eixo EUA**.
- **Riscos de advertiser/compliance:** difamação é o risco número 1 (casos de 2026: £40k no UK; anti-SLAPP de 2 anos; C&D por trailer) — nunca afirmar fraude sem sentença, sempre "alleged"/"prosecutors said"; clipes de jornal são a maior fonte de copyright claim (usar licenciado/público/próprio); conteúdo financeiro exige precisão (sem conselho, sem promessa); inautenticidade por documentário genérico sem fonte (política de conteúdo inautêntico + erro replicado entre canais).

## Queries mais estreitas (se REPROVA)

- **Executada:** `--cluster "business scandal documentary"` (21 canais pequenos ≤365d; 8 analisados; 0 gates; 1 emergente com 2 outliers; fome em 4).
- **Não executadas (limite de 1 segunda busca):** `--cluster "company collapse documentary" --age 45` (fecha o cerco no recorte exato); `--cluster "bank collapse documentary"`; `--cluster "corporate fraud documentary"`; `--cluster "retail collapse documentary"`. Manter para a revalidação de 2–4 semanas, junto com o brief `--brief "corporate collapse documentary"`.
