# Evidência — Espaço e astronomia

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "space mystery documentary" --max 8` + `python scripts/niche_scan.py --cluster "astronomy documentary" --max 8` + autocomplete (`--suggest "space mystery"`) + websearch
> Brief completo: `data/briefs/space-mystery-documentary.md` · JSON: `data/briefs/space-mystery-documentary.json`
> A saída bruta do cluster `astronomy documentary` não foi persistida no repo (execução manual, limite de 1 segunda busca); é reproduzível pelo comando acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: **10 únicos** (7 no brief + 6 no cluster, 3 repetidos entre scans) | passam os 3 gates: **0** (meta ≥3) → o critério rígido **REPROVA** nas duas buscas
- Fome do algoritmo (outlier ≥3×): **7 canais únicos** (5 no brief + Orvexa e Sleepy Space Science novos no cluster) — sinal: **sim**, com flares de **421,3×**, **162,4×** e **29,8×**
- Emergentes (≤90d + 2/3 gates): **1** — Gupt vigyan (74d); quase: Orvexa (92d, fora da janela por 2 dias)
- Autocomplete: **103 termos** no brief + 38 termos extras (`space mystery`) — 141 no total | Trends: **não coletado** (HTTP 429 em 3 tentativas)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido em nenhuma das duas buscas** — e o padrão é idêntico ao das rodadas anteriores: **10 de 10 análises falham apenas o gate de idade** e passam os outros dois (5 primeiros ≥10k e ≥1k views/dia). Há fome cross-canal fresca em dois recortes (pergunta científica de espaço em ago–set/2026; cosmologia/escala em ago/2026), flares fortes em canais pequenos (535.488 views em 13 dias no `Calm Space`; 207.963 no `Sleepy Space Science`) e profundidade de busca alta (141 termos). Não é PASSA (nenhum canal ≤45d cruzou os 3 gates) e não é REPROVA puro (o formato performa com sobra nos gates 2–3 e há fome recente) — é **PARCIAL**, com revalidação em 2–4 semanas focada em entrantes ≤45d.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Fonte | Subs | Idade | 5 primeiros | Views/dia* | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|---|
| Calm Space | brief + cluster | 106.000 | 276d | 962.900 | 61.744 | 011 | **29,8× — 535.488 — "Why Voyager 1 Still Hasn't Hit a Single Thing After 49 Years in Space" — 2026-09-09** |
| Sleepy Space Science | brief + cluster | 15.000 | 158d | 391.763 | 10.754 | 011 | 5,8× — 207.963 — "Why Does Everything In The Universe Spin?" — 2026-08-05 |
| Magnetic Space | brief + cluster | 9.760 | 143d | 131.074 | 13.380 | 011 | 4,2× — 51.149 — "Spacetime\| The 4-Dimensional Mystery We Still Can't Explain \| 100 Years Later" — 2026-09-10 |
| Cosmic Door | brief | 22.300 | 169d | 131.569 | 32.193 | 011 | 7,2× — 145.582 — Laniakea Supercluster (Hindi) — 2026-08-30 |
| Sleepy Mystery Channel | brief | 12.800 | 202d | 190.041 | 7.910 | 011 | — |
| What Happens If? | cluster | 134.000 | 135d | 97.232 | 474.272 | 011 | — |
| Talk Mode | cluster | 4.500 | 197d | 53.702 | 8.301 | 011 | — |
| Orvexa | cluster | 208 | 92d | 698.430 | 9.994 | 011 | **162,4× — 667.132 — "Miller's Planet #interstellar #spaceexploration #spacex" — 2026-08-02** (formato Short/movie-adjacent — não usar como evidência de long) |
| Gupt vigyan | brief | 44.200 | 74d | 466.178 | 274.841 | 011 | 13,9× — 526.939 — sapos na chuva (Hindi; fora do espaço) — 2026-08-24 |
| Tamil Unmaigal | brief | 57.200 | 307d | 5.231.226 | 67.038 | 011 | **421,3× — 2.785.390** — segredos da Amazônia (Tâmil; fora do espaço) — 2026-08-17 |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a **idade** falha. *Views/dia = views totais do canal ÷ idade (definição do `niche_scan.py`). Brief: 7 pequenos analisados (quota); cluster: 37 encontrados → 6 pequenos ≤365d analisados (quota). IDs dos canais do brief estão no JSON (ex.: Calm Space `UCXyJmt3PKv0fbsU9DtcreEw`).

## Outliers (janela de 2–6 semanas)

- **Calm Space** — 29,8× — 535.488 views — "Why Voyager 1 Still Hasn't Hit a Single Thing After 49 Years in Space" — 2026-09-09 — padrão: pergunta "why" sobre missão icônica + escala interestelar (canal de 106k subs; ~13 dias desde a publicação na coleta).
- **Orvexa** — 162,4× — 667.132 views — "Miller's Planet #interstellar #spaceexploration #spacex" — 2026-08-02 — padrão: espaço-cinema em formato curto (208 subs, 92d). Ratio inflado pela mediana baixa; conteúdo movie-adjacent, não documentário.
- **Sleepy Space Science** — 5,8× — 207.963 views — "Why Does Everything In The Universe Spin?" — 2026-08-05 — pergunta de física fundamental em tom calmo.
- **Cosmic Door** — 7,2× — 145.582 views — Laniakea Supercluster (Hindi) — 2026-08-30 — cosmologia de escala; mesmo tema do topo global em outro idioma.
- **Magnetic Space** — 4,2× — 51.149 views — Spacetime / 4 dimensões / "100 Years Later" — 2026-09-10 — física fundamental com gancho de aniversário.
- **Tamil Unmaigal** — 421,3× — 2.785.390 views — mistério geral (Tâmil) — 2026-08-17 — fora do recorte de espaço; mostra a força do "mystery documentary" regional.
- **Gupt vigyan** — 13,9× — 526.939 views — mistério de ciência natural (Hindi) — 2026-08-24 — fora do recorte de espaço; canal de 74d com tração altíssima.

> Nota metodológica: ratios muito altos (162×, 421×) vêm de medianas baixas em canais novos/pequenos. O que sustenta a leitura aqui é o **viewport absoluto** (51k–2,8M) e a **convergência de tema** entre canais diferentes na mesma janela.

## Fome do algoritmo (cluster cross-canal)

**Sim, em dois recortes:**

1. **Pergunta científica de espaço (ago–set/2026):** Calm Space (09/09, 535k, Voyager), Sleepy Space Science (08/05, 208k, rotação cósmica) e Magnetic Space (09/10, 51k, spacetime) — 3 canais diferentes em ~5 semanas, todos no formato "pergunta 'why' + mistério científico + narração documental". Fome **fresca** (o flare principal é de 2 semanas atrás).
2. **Cosmologia de escala (ago/2026):** Cosmic Door (08/30, 146k, Laniakea, Hindi) — eco do topo global de "tamanho do universo" em outro idioma; mostra a demanda do tema em múltiplos mercados.

A busca `--cluster "astronomy documentary"` (37 canais encontrados, 6 analisados) reportou fome em 3 canais e **0 gates**; a busca `--brief "space mystery documentary"` reportou fome em 5 canais e **0 gates** — convergente, sem contradição.

## Demanda (autocomplete — top termos)

- Brief `space mystery documentary`: **103 termos**. Destaques de demanda real (o resto é ruído de filmes/streaming): `space mysteries`, `space secrets`, `space exploration documentary`, `space documentary 2023`, `space mystery documentary nasa`, `space mystery documentary latest`, `space mystery documentary discovery`.
- `space mystery` (suggest extra): **38 termos**. Destaques: `space anomalies`, `space theories`, `space biggest mysteries`, `space mysteries explained`, `mysterious space facts`, `mysterious space facts hindi/tamil`, `deep space mystery`, `space mysteries for sleep`, `space curiosities`.
- Sinal de profundidade: o tema tem 3 eixos de pergunta vivos (missão/sonda, física fundamental, escala/cosmologia) + trilha sleep, o que dá pauta para 50+ episódios sem repetir.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` e retry de `--trends "astronomy documentary"` retornaram **HTTP 429** (rate limit do Google) em 2026-09-22. Fallback usado: autocomplete (profundidade alta) + evidência de API (outliers recentes). Revalidar com `--trends "astronomy documentary"` em outro horário.

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` (yt_auth sem o escopo `youtube.force-ssl`; tentativa em 2026-09-22 no vídeo `ulMzHpL2wGE`, NSN Space News). Repetir depois de `python scripts/yt_auth.py`. O autocomplete `space mysteries explained` e `space theories` sugere demanda explícita por "explicação", não por "mais um mistério".

## Convergência de formato (últimos uploads)

- **Calm Space / Sleepy Space Science / Magnetic Space:** outliers recentes (ago–set/2026) no formato "título-pergunta + narração documental + mistério científico ainda aberto". Convergência clara em torno de "why/what".
- **Onda sleep-space (adjacente):** The Sleepy Space Channel ("The Most Extreme Exoplanets Ever Found | Space Documentary 2026") e "101 Sleepy Facts" (docs de 3h quase diários, narração a ~100 palavras/min, fontes NASA/ESA declaradas) mostram a versão commodity do tema: longuíssimos, calmos, de baixa densidade — o oposto do posicionamento do modelo (episódio denso de 12–22 min com fonte primária).
- **Estabelecidos (teto do nicho):** Astrum (2,85M subs, 479 vídeos, space discovery documentary), John Michael Godier (493K, 698 vídeos, voice-first) [autonolab 02/2026] — o entrante faceless compete por **ângulo e rigor**, não por tópico.
- Limitação: a página de vídeos do YouTube não é raspável (JS); a convergência foi inferida da janela da API + títulos + fontes web.

## Fontes web (2+)

- https://blog.autonolab.com/niches/2026-02-08-faceless-youtube-science/ — 7 canais faceless de ciência verificados até jul/2026: Astrum 2,85M/479 (space discovery documentary), John Michael Godier 493K/698 (voice-first), Branch Education, Real Engineering; lição: ancorar episódio em uma descoberta concreta e construir famílias de temas recorrentes.
- https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm — AIR 2026 (300 canais reais, 3.595 meses monetizados, mai/2025–mai/2026): Education & Science é o maior RPM mediano (**$10,22**; P25–P75 $2,31–$19,50), com **77%** das views monetizadas e 1,84 anúncios/sessão — base real da classe de RPM do modelo.
- https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data/ — RPM médio por nicho faceless (dados públicos/modelagem): Astronomy $14,0 (5 canais), Space $10,1 (8), Space Exploration $9,8 (5), Physics $19,1 [ALEGADO].
- https://fluxnote.io/guides/how-much-space-astronomy-channel-makes — [ALEGADO] space RPM $5–11 (tech angle $9–11); "faceless são o formato dominante"; sponsors Brilliant.org $300–2.500/vídeo; eventos (JWST, lançamentos) geram 3–5× de tráfego; busca "how big is the universe" 500 mil+/mês.
- https://clippie.ai/blog/faceless-ai-explainer-channel-youtube-science-tech-2026 — [ALEGADO] Space & astronomy CPM $8–15; formatos vencedores ("What [mission] Just Discovered"); 8–12 min para mid-rolls; entry tier "quase vazio".
- https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ — [OFICIAL/REPORTADO] atualização de 16/07/2026 define 3 categorias de conteúdo inautêntico inelegível (genérico/repetitivo/template; off-putting; AI personas em temas sensíveis); enforcement no nível do canal.
- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage — jan/2026: 16 canais, 35M de inscritos, 4,7B de views terminados; algoritmo passou a favorecer rostos; conteúdo educacional de nicho segurou melhor; risco central do modelo faceless.
- https://outlierkit.com/resources/youtube-ai-slop-crackdown-2026/ — critérios de detecção: upload velocity, script fingerprinting, interchangeability; 21% dos Shorts para novos usuários classificados como slop; 278 canais sob investigação.
- https://www.youtube.com/watch?v=bFrYnjIoWzw — The Sleepy Space Channel, "The Most Extreme Exoplanets Ever Found | Space Documentary 2026": exemplo da onda sleep-space (narração lenta, catálogo de exoplanetas) em convergência com o tema.
- https://podcasts.apple.com/pg/podcast/101-sleepy-facts/id1895888068 — "101 Sleepy Space Facts": docs de ~3h com fontes NASA/ESA publicados quase diariamente — evidência da versão commodity/alta-cadência do subnicho.
- https://www.youtube.com/shorts/qF7pm_h7DpQ — SpaceVrse: panorama do topo estabelecido (Dr. Becky, Scott Manley, PBS Spacetime, Cool Worlds, MelodySheep) — o diferencial do entrante é formato/ângulo/rigor, não o tópico.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalvas: (a) o recorte EN de "documentário de mistério científico com fonte primária" tem entrantes crescendo (Calm Space 106k em 276d; Sleepy Space Science 15k em 158d; Magnetic Space 9,8k em 143d) e nenhum deles é commodity de sleep; (b) a onda sleep-space (1–3h, ~100 wpm, cadência quase diária) **já saturou o ângulo "relaxar ouvindo o cosmos"** — copiar esse formato é anti-modelo (e flerta com inautenticidade por template); (c) canais Hindi/Tâmil/Bengali escalam o "space mystery" genérico globalmente — o entrante EN deve vencer por rigor + método (paper, telemetria, dado), não por "mais um vídeo de buraco negro"; (d) o título-pergunta "Why [mission]…" já tem flare recente — usar o arquétipo com ângulo próprio, nunca clone de título.
- **Gargalo real:** o gate de idade é o único que reprova (10/10 análises passam os gates 2 e 3). A pergunta da revalidação é se **novos entrantes ≤45d** aparecem — o tier emergente atual (74–92d) estará fora da janela em 2–4 semanas, sendo substituído ou não.
- **Riscos de advertiser/compliance:** pseudociência e doom derrubam para limited ads; imagens NASA/ESA em geral liberam com créditos, mas footage de terceiros não; tragédias humanas espaciais exigem tratamento histórico (sem espetáculo); precisão numérica é não-negociável (unidade + fonte); autores de papers não podem ser acusados de erro sem documentação.
- **Risco de inautenticidade (o maior):** enforcement por canal (últimos 30 uploads) + detecção por padrão (velocidade de upload, script fingerprinting, interchangeability) [TechCrunch/OutlierKit/TNW 2026] — mitigação no `profile.md` §11 (1 peça primária por vídeo, estrutura variada, voz própria, cadência humana, comentário editorial).

## Queries mais estreitas (se REPROVA)

- **Executada:** `astronomy documentary` (cluster; 37 encontrados → 6 pequenos analisados; 0 gates; 3 com fome; escolhida em vez de "cosmos documentary" por ser mais científica e menos poluída por filmes/sleep).
- **Não executadas (limite de 1 segunda busca):** `voyager documentary`, `black hole documentary` e `space discovery documentary` — usar na revalidação de 2–4 semanas, idealmente com `--age 45` no cluster para forçar o corte da idade, junto com `--trends "astronomy documentary"` e `--comments` (após reautenticar com force-ssl).
