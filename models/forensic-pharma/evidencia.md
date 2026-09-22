# Evidência — Escândalos farmacêuticos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "pharmaceutical scandal documentary" --max 8` + `python scripts/niche_scan.py --cluster "pharma documentary" --max 8` + websearch (stats de canal, política do YouTube, litígio do setor)
> Brief completo: `data/briefs/pharmaceutical-scandal-documentary.md` · JSON: `data/briefs/pharmaceutical-scandal-documentary.json`
> A saída bruta do cluster não foi salva em arquivo (execução manual); é reproduzível pelo comando acima. Números de canais fora dos scans vêm de fontes web citadas (socialcounts/vidIQ) e estão marcados como tal.

## Veredito: **REPROVA**

- Canais pequenos analisados: **16 linhas** (8 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo: o script marca 3 canais no brief e 1 no cluster com outlier ≥3×, mas **em escala de micro-canal** (maior outlier absoluto: 683 views; medianas de 4–69). Pelo limiar forte do método (≥5×; ≥10× = flare), existe **1** outlier (9,9×) — ainda com 683 views. Sinal: **não** sustenta janela de oportunidade.
- Autocomplete: 107 termos (meta ≥15), porém majoritariamente ruído (ficção/kdrama/dublagem/regiões). Trends: **não coletado** — Google Trends respondeu **429** em três tentativas.
- Emergentes (cluster): 3 canais ≤90d com 2/3 gates — mas todos de conteúdo de **fábrica/processo**, ruído do termo "pharma documentary", fora do subnicho. Não contam como evidência do cruzamento.

**Leitura honesta:** este é o oposto do padrão "falha só a idade" das outras rodadas. Os 8 canais do brief falham os **três** gates: os 5 primeiros vídeos somam de 20 a 6.723 views (gate: ≥10 mil) e o melhor faz 664 views/dia (gate: ≥1 mil/dia). Não existe, na coleta, um único canal pequeno em EN rompendo com documentário de escândalo farmacêutico. O que existe é demanda **sênior** recente e forte: o doc de 44 min da fern sobre a Grünenthal fez 2.926.276 views em ~48 dias (05/08/2026, ~61 mil views/dia) e o de Fen-Phen da Into the Shadows fez 206.844 views em 24:55 (22/05/2026). E o cluster mostrou que "pharma documentary" está colado em conteúdo de **fábrica/processo** (World of Factories: 793.808 views/dia, 59d de idade) — o que não valida o cruzamento "escândalo". Conclusão: **REPROVA** a entrada direta em EN; revalidar um recorte estreito (opioides/Purdue, Vioxx, ensaio clínico) ou tratar como aposta editorial de produção sênior antes de qualquer piloto.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Scan | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|---|
| Notes from the Underground | brief | 76 | 138d | 2.051 | 103 | 000 | — |
| Coffin Ledger | brief | 14 | 107d | 797 | 112 | 000 | 9,9× — 683 — "Inside America's Biggest Pill Mill" — 2026-08-07 |
| Cold Capital | brief | 149 | 119d | 2.526 | 155 | 000 | — |
| Paper Empires | brief | 474 | 102d | 107 | 48 | 000 | 3,2× — 61 — "McKinsey's Deleted Files Exposed: The Opioid Scandal" — 2026-07-31 |
| The Untold Records | brief | 25 | 132d | 6.723 | 664 | 000 | — |
| Suited Criminals | brief | 60 | 178d | 20 | 309 | 000 | 4,8× — 19 — "Allergan's Restasis Patent Thicket and Tribal Immunity Scandal" — 2026-08-01 |
| Compound Lens | brief | 18 | 145d | 120 | 14 | 000 | — |
| The Autopsy Files | brief | 17 | 102d | 60 | 49 | 000 | — |
| World of Factories | cluster | 77.400 | 59d | 14.654.048 | 793.808 | 011 (fora do subnicho) | — |
| Nature Khauf | cluster | 57.500 | 69d | 16.019.848 | 276.918 | 011 (fora do subnicho) | — |
| Factory Stories with AI | cluster | 72.500 | 214d | 580.925 | 122.021 | 011 | — |
| Factory process | cluster | 102.000 | 61d | 1.152.144 | 1.399.107 | 011 (fora do subnicho) | — |
| InfoWars | cluster | 153.000 | 147d | 133.641 | 69.258 | 011 | — |
| FactoryVision UK 24 | cluster | 28.400 | 124d | 207.775 | 147.942 | 011 | — |
| The Blueprint Info | cluster | 4.890 | 200d | 698.952 | 4.766 | 011 | 4,6× — 12.035 — empresa farmacêutica indiana (título em hindi) — 2026-08-24 |
| Sedated History | cluster | 27.200 | 349d | 42.927 | 7.574 | 011 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). Brief: 30 canais encontrados, 17 pequenos ≤365d, 8 analisados, 0 passam, 0 emergentes. Cluster: 42 encontrados, 16 pequenos ≤365d, 8 analisados, 0 passam, 3 emergentes. Nenhuma linha passa os 3 gates (0/16). Os "011" do cluster falham só a idade, mas o conteúdo é de fábrica/processo, agregador ou não é o formato do modelo — não servem como canal-evidência do cruzamento.

## Outliers (janela de 2–6 semanas)

**Sênior (web — socialcounts/vidIQ):**

- **fern** — 2.926.276 views — "Exposing a $1,900,000,000 Pharma Company" — 05/08/2026 — 44:42 — Grünenthal/tramadol/tapentadol, baseado na investigação World of Pain (The Examination); ~61 mil views/dia; 54.858 likes e 4.983 comentários. Canal: 5,5 M subs, 140 vídeos.
- **Into the Shadows** — 206.844 views — "Fen-Phen: The Weight Loss Drug that Destroys Your Heart" — 22/05/2026 — 24:55 — uma droga + um dano + processos; 6.043 likes e 858 comentários. Canal: 1,28 M subs, 566 vídeos; 4,34 M views/30d.
- **DW Documentary** — 3,2 M views — "Big Pharma - How much power do drug companies have?" — 12/09/2021 — 42:26 — documentário institucional evergreen.

**Micro (scans):**

- **Coffin Ledger** — 9,9× — 683 — pill mill short — 07/08/2026 — mediana do canal 69 (ruído de micro-canal).
- **Suited Criminals** — 4,8× — 19 — Restasis/patente — 01/08/2026 — mediana 4.
- **Paper Empires** — 3,2× — 61 — McKinsey/opioides — 31/07/2026 — mediana 19.
- **The Blueprint Info** — 4,6× — 12.035 — empresa farmacêutica indiana (hindi) — 24/08/2026.
- **Promethean Overviews** — 16,5 mil — cadeia do fentanil, parte 1 — 21/03/2026 — 22:15 (web).

## Fome do algoritmo (cluster cross-canal)

O script marca fome (3 canais no brief, 1 no cluster), mas os "outliers" são aritmética de micro-canal: 683, 61 e 19 views contra medianas de 69, 19 e 4. Nenhum canal sério e pequeno aparece com outlier no mesmo tema dentro de 90d. O que existe é **demanda de tema** visível em canais grandes em 2026: fern (ago/2026), Into the Shadows (mai/2026), The Strange History Archive (mar/2026), Creepalachia (jan/2026), Promethean (mar/2026) — casos diferentes (Grünenthal, fen-phen, 3 drogas, Sacklers, fentanil), sem convergência de formato que o recomendador possa ter premiado. Ressalva: o recorte em hindi mostra apetite (The Blueprint Info, 4,6×; e o outlier de 9,9× é um Short sobre pill mill).

## Demanda (autocomplete — top termos)

107 termos únicos (meta ≥15). Termos aproveitáveis:

- `pharmaceutical documentary`
- `pharmaceutical industry documentary`
- `pharmaceutical scandal documentary` (com modificadores reais: `bbc`, `channel 4`, `amazon prime`, `english`, `full`)
- `pharmaceutical industry` / `pharmacist industry`

Ruído dominante: cauda de ficção/coreana (`anime`, `kdrama`, `kiss scene`, `gacha`, `genshin`, `love story`), dublagens (`dubbed in hindi`, `eng sub`) e geografias (`bengali`, `malayalam`, `abs cbn`). Leitura: o autocomplete prova profundidade da **categoria farmacêutica**, não do cruzamento "escândalo" — usar no título junto com o nome do caso (`documentary` + nome próprio), nunca só o termo genérico.

## Trends (YouTube 12m)

Não coletado. Google Trends respondeu **429** (rate limit) em três tentativas (no `--brief` e em `--trends "pharmaceutical documentary"`). Reexecutar em outra janela de horário; fallback do script é `--suggest`. Sem esse dado, a trajetória do termo fica em aberto — mas os uploads sêniores de 2026 (fern, Into the Shadows) dão sinal indireto de demanda alta.

## Comentários (demanda explícita)

Não coletado. `python scripts/niche_scan.py --comments Eo0JQLIG6hA` (vídeo da fern) retornou `insufficientPermissions` — falta o escopo `youtube.force-ssl`; rodar `python scripts/yt_auth.py` e repetir. Proxy disponível: o vídeo da fern tem 4.983 comentários em 2,93 M views; o de Fen-Phen, 858 em 206,8 mil — engajamento saudável para o formato, mas nada foi lido (pedidos recorrentes e perguntas sem resposta ficam para a próxima passada).

## Fontes web (2+)

- https://socialcounts.org/youtube-video-analytics/Eo0JQLIG6hA — fern: 5,5 M subs, 140 vídeos (desde 09/2020); doc Grünenthal 44:42 (05/08/2026) com 2.926.276 views, 54.858 likes, 4.983 comentários.
- https://socialcounts.org/youtube-video-analytics/nQAzH0Ck1jo — Into the Shadows: 1,28 M subs, 566 vídeos; Fen-Phen 24:55 (22/05/2026) com 206.844 views, 6.043 likes, 858 comentários.
- https://vidiq.com/youtube-stats/channel/@intotheshadows/ — 1,24 M subs, 544 vídeos, 4,34 M views/30d e +10 mil subs/30d; AdSense estimado em $12,08 mil/mês [ALEGADO].
- https://socialcounts.org/youtube-video-analytics/Q2HXbwIFgic — The Strange History Archive: 2,33 mil subs, 36 vídeos (desde 01/2025, UK); vídeo de escândalo farmacêutico 9:25 (16/03/2026) com 723 views — o teto do tier micro no tema.
- https://socialcounts.org/youtube-video-analytics/ldiPHdoWp4w — Creepalachia: 27,7 mil subs, 2,04 mil vídeos (desde 11/2024); short Sackler/Purdue 1:14 (18/01/2026) com 1.309 views e 127 likes.
- https://www.theexamination.org/series/world-of-pain — investigação World of Pain (The Examination + The Washington Post + Der Spiegel + The Lancet, entre 10+ parceiros): padrão de pesquisa primária e colaboração para o modelo (foi a base do doc da fern).
- https://www.theexamination.org/articles/gruenenthal-pushed-its-latest-opioid-as-a-safer-option-people-around-the-world-got-hooked — caso Grünenthal/tapentadol: empresa reconheceu que "alguns" documentos exageravam o risco; auditoria de 2019; resposta oficial incorporada (modelo de right of reply).
- https://fluxnote.io/guides/youtube-rpm-health-niche-2026 — RPM de saúde 2026: $3–15 (medical explainer $6–15); anunciantes farmacêuticos pagam $10–25 CPM; YMYL pode gerar yellow icon com RPM 50–70% menor [ALEGADO].
- https://vidiq.com/blog/post/most-profitable-youtube-niches/ — Health Services: CPM $15–40 / RPM $7–22; "limited or no ads" derruba o CPM alto; recomenda evitar comparações de medicamentos e claims clínicos [ALEGADO].
- https://support.google.com/youtube/answer/13813322 — política de desinformação médica (prevenção/tratamento) com exceção EDSA (educacional/documental) — o que o roteiro precisa respeitar.
- https://scroll.in/article/1057317/long-before-liver-doc-this-doctor-fought-defamation-by-a-pharma-company-and-won — Lundbeck vs editor (10 anos de processo criminal) e Himalaya vs "Liver Doc": difamação como ferramenta de silenciamento no setor.
- https://allaboutlawyer.com/jj-talc-scientists-libel-lawsuit-dismissed/ — J&J/Pecos River vs cientistas (decisão de 19/08/2026): trade libel como intimidação; a ciência como alvo.
- https://storage.courtlistener.com/recap/gov.uscourts.nysd.626057/gov.uscourts.nysd.626057.9.0.pdf — ação anti-SLAPP (Cassava Sciences): difamação usada para suprimir críticos; efeito inibidor documentado (publicadora e universidade recuando durante o processo).
- https://www.mayoclinicproceedings.org/article/S0025-6196(23)00604-3/fulltext — Pacira vs ASA: "conclusões científicas são discurso protegido", não libel — mapa dos limites legais.
- https://time.com/6302678/painkiller-review-netflix/ — "explainer dramas" em alta (Painkiller/Dopesick): a audiência já conhece a mecânica — diferenciar com documento primário, não com drama.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Não na entrada direta em EN. Os 16 canais pequenos da coleta não passam nenhum gate; o termo "pharma documentary" está contaminado por conteúdo de fábrica/processo; e o tier sênior (fern, Into the Shadows, DW) opera em 25–45 min com produção pesada. Caminhos menos disputados que a própria coleta sugere: (a) recortes fora dos EUA (Grünenthal/Alemanha, Depakine/França, fator VIII/UK-Canadá); (b) ensaios escondidos e literacia de dados (Study 329/Paxil, Vioxx, Tamiflu) com o documento na tela — sem termo forte no autocomplete, é lacuna; (c) série evergreen "caso + status legal"; (d) patente/preço (Restasis, Daraprim, insulina), que cruza com `finance-fraud`.
- **Riscos:** difamação corporativa é o risco central e está documentado no setor (Lundbeck vs editor por 10 anos; J&J vs cientistas; Cassava vs críticos com efeito inibidor; Pacira vs ASA). Saúde é YMYL: política de desinformação médica (com exceção EDSA), limited ads em conteúdo sensível, proibição de conselho/dose. Conteúdo inautêntico: o nicho já tem oferta de baixa qualidade gerada em massa (resumos de "scam/cover-up" com narração sintética) — o antídoto é a peça primária por vídeo. Direitos: retratos, footage jornalístico e prontuários são armadilhas.
- **Nota de honestidade:** o veredito REPROVA olha os gates (0/16). A leitura de oportunidade acima é editorial, não aprovação — nenhum canal pequeno passou, e o modelo só deve sair do papel depois de um recorte revalidado.

## Queries mais estreitas (se REPROVA)

- **Executada como 2ª busca:** `pharma documentary` (cluster) — 42 canais encontrados, 16 pequenos ≤365d, 8 analisados, 0/8 gates; 3 emergentes de fábrica/processo (ruído) + 1 outlier em hindi (4,6× / 12.035 views).
- **Não executadas (limite de 1 segunda busca):** `opioid crisis documentary`, `Purdue Pharma documentary`, `Vioxx documentary`, `clinical trial scandal documentary`, `FDA failure documentary`, `tramadol documentary` — usar na revalidação.
