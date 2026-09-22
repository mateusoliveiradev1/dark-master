# Evidência — Civilizações perdidas

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "lost civilization documentary" --max 8` + `python scripts/niche_scan.py --cluster "lost city documentary" --max 8` + autocomplete (`--suggest "lost city"`; o brief já coletou 107 termos) + websearch
> Brief completo: `data/briefs/lost-civilization-documentary.md` · JSON: `data/briefs/lost-civilization-documentary.json`
> A saída bruta do cluster `lost city documentary` não foi salva em arquivo (execução manual, limite de 1 segunda busca); é reproduzível pelo comando acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: **13 únicos** (8 no brief + 8 no cluster; 3 repetidos: Aiwala, Documentary Empire, Atlas of Civilizations) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **7 canais únicos** (4 no brief + 5 no cluster; 2 repetidos) — sinal: **sim**, com 5 flares ≥10×: 280,6×, 148,5×, 115,5×, 78,6× e 67,2×
- Emergentes (≤90d + 2/3 gates): **4 únicos** — Aiwala (80d), Atlas of Civilizations (68d), The Descent Record (68d), S Rao (90d)
- Autocomplete: **107 termos** no brief + **343** em `lost city` (ruidoso: jogos/filmes) | Trends: **não coletado** (HTTP 429 em duas tentativas)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido** — 0 canais. Mas todos os 4 emergentes falham **apenas o gate de idade** e passam os outros dois, o padrão da rodada 1 de true crime; o nicho tem flares entre os maiores já vistos na biblioteca (280,6× com 4,49M views em um canal de 80 dias e 15,1k subs) e fome cross-canal em **três** recortes (cidade sob a selva/areia, El Dorado em hindi e Atlântida com evidência). Não é PASSA (nenhum canal ≤45d cruzou os 3 gates) e não é REPROVA (o formato performa com sobra nos gates 2–3 e há fome recente). Revalidar em 2–4 semanas, olhando especificamente por entrantes ≤45d.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| **Aiwala** (brief + cluster) | 15.100 | 80d | 1.095.407 | 120.442 | 011 | **280,6× — 4.490.941 — "Dholavira – The Ancient City \| The Lost City of Indus Valley" — 2026-08-18** |
| **Atlas of Civilizations** (brief + cluster) | 21.900 | 68d | 15.197 | 74.113 | 011 | — |
| **The Descent Record** (cluster) | 3.970 | 68d | 109.560 | 9.671 | 011 | — |
| **S Rao** (cluster) | 122 | 90d | 217.599 | 2.458 | 011 | 4,0× — 65.103 — "The Lost City of Atlantis: What Really Happened? \| Evidence, …" — 2026-08-25 |
| Wrongly Assumed (brief) | 6.720 | 133d | 685.151 | 22.541 | 011 | 8,4× — 575.266 — "Easter Island Was Reanalyzed by AI — And the Statues Were Hiding Somet…" — 2026-08-20 |
| Documentary Empire (brief + cluster) | 13.200 | 257d | 1.567.722 | 25.092 | 011 | **115,5× — 615.302 — "Lost Cities Beneath the Jungle \| The Hidden Kingdoms of the Maya" — 2026-07-21** · 18,0× — 96.150 — "The Rise and Fall of Mesopotamia \| How the World's First Gre…" — 2026-08-14 |
| Mr. True States (brief) | 14.600 | 250d | 146.853 | 7.960 | 011 | **78,6× — 443.270 — "Beneath Florida Lies a Lost World Older Than the Pyramids" — 2026-08-17** |
| Nilesh Toppo (cluster) | 1.390 | 93d | 8.035 | 1.928 | 001 | **148,5× — 149.390 — "El Dorado का रहस्यमयी खजाना \| The Lost City of Gold Mystery" — 2026-08-25** |
| Legends Unbound (cluster) | 651 | 288d | 81.830 | 712 | 010 | **67,2× — 69.649 — "El dorado - The lost city of gold \| एल डोराडो का रहस्य" — 2026-07-15** |
| New Cosmic Explorer (brief) | 8.840 | 150d | 24.081 | 16.633 | 011 | — |
| Decode the Past (brief) | 1.350 | 170d | 2.044 | 5.110 | 001 | — |
| Buried Signal (brief) | 5.420 | 128d | 3.787 | 20.581 | 001 | — |
| Beyond Myths (cluster) | 1.030 | 83d | 1.942 | 2.871 | 001 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a **idade** falha. Brief: 41 canais encontrados, 14 pequenos ≤365d, 8 analisados (quota). Cluster: 41 encontrados, 10 pequenos ≤365d, 8 analisados (quota). IDs dos canais do brief estão no JSON; a saída do cluster não foi persistida.

## Outliers (janela de 2–6 semanas)

- **Aiwala** — 280,6× — 4.490.941 views — "Dholavira – The Ancient City | The Lost City of Indus Valley" — 2026-08-18 — padrão: cidade específica do Vale do Indo + "lost city" no título; canal de 15,1k subs e 80 dias. **Nuance honesta:** os uploads recentes do canal estão em hindi (último vídeo conferido por oEmbed em 2026-09-22: aula de história sobre Takshashila); o flare é forte, mas é do mercado hindi — não assumir migração automática para o EN.
- **Nilesh Toppo** — 148,5× — 149.390 views — El Dorado em hindi — 2026-08-25 — padrão: "cidade perdida do ouro" + mistério do tesouro; canal de 1,4k subs.
- **Documentary Empire** — 115,5× — 615.302 views — "Lost Cities Beneath the Jungle | The Hidden Kingdoms of the Maya" — 2026-07-21 — padrão: cidades sob a selva (Maya) + framing de reinos ocultos; o mesmo canal repetiu a fórmula com Mesopotâmia (18,0×, 96.150, 2026-08-14) — convergência clara de formato.
- **Mr. True States** — 78,6× — 443.270 views — "Beneath Florida Lies a Lost World Older Than the Pyramids" — 2026-08-17 — padrão: "mundo perdido sob os pés" + comparação de idade com as pirâmides; canal de 14,6k subs.
- **Legends Unbound** — 67,2× — 69.649 views — El Dorado em hindi — 2026-07-15 — mesmo tema do Nilesh Toppo, 6 semanas antes; canal pequeno (651 subs) e antigo (288d).
- **Wrongly Assumed** — 8,4× — 575.266 views — "Easter Island Was Reanalyzed by AI…" — 2026-08-20 — padrão: reanálise por IA de um caso icônico + "hiding something" no título; risco de sensacionalismo, mas mostra a fome por reinterpretação de sítios conhecidos.
- **S Rao** — 4,0× — 65.103 views — "The Lost City of Atlantis: What Really Happened? | Evidence…" — 2026-08-25 — padrão: Atlântida pelo ângulo de evidência (não de crença); canal de 122 subs (!), primeira leva de vídeos somando 217.599 views.

> Nota metodológica: ratios altos em canais de 122–15k subs vêm de medianas baixas. O que importa é o **viewport absoluto** (65k–4,49M) em canais pequenos e recentes, que sustenta a fome.

## Fome do algoritmo (cluster cross-canal)

**Sim, em três recortes:**

1. **Cidades reveladas sob a selva/areia (jul–ago/2026):** Documentary Empire (07/21, 615k), Aiwala (08/18, 4,49M), Mr. True States (08/17, 443k) e Wrongly Assumed (08/20, 575k) — 4 canais diferentes em 4 semanas com o mesmo ângulo "cidade/mundo perdido revelado". É o recorte mais forte da coleta.
2. **El Dorado / cidade do ouro em hindi (jul–ago/2026):** Legends Unbound (07/15, 69,6k) e Nilesh Toppo (08/25, 149,4k) — fome cross-canal em outro idioma; no EN faceless o tema ainda está raso.
3. **Atlântida com evidência (ago/2026):** S Rao (08/25, 65,1k) — o ângulo "what really happened / evidence" funciona (4,0× em um canal de 122 subs), o que valida o posicionamento anti-pseudociência do modelo.

## Demanda (autocomplete — top termos)

- Brief `lost civilization documentary`: **107 termos**. Destaques: `lost civilization documentary`, `lost civilizations documentary bbc`, `lost history documentary`, `lost civilisations documentary`, `ancient lost civilizations documentary`, `lost ancient civilizations`, `lost civilization documentary explained`, `lost civilization documentary channel 4`, `lost civilization documentary discovery`, `lost civilization documentary compilation`, `lost civilization documentary david attenborough`, e variações de streaming (`netflix`, `amazon prime`) — mostra que a demanda busca docs de TV; a versão faceless EN entra como alternativa de catálogo.
- `lost city`: **343 termos** (ruidoso — jogos, filmes, parques temáticos). Termos de demanda real: `lost city of atlantis`, `lost city colombia` (Ciudad Perdida), `lost city amazon`, `lost city china`, `the lost city of z`, `lost city ambience` (existe demanda de formato de fundo/ambiente para o tema).
- Cruzamento com a evidência: os termos de streaming e "explained" indicam intenção de **entender o caso**, não só consumir mistério — alinhado à promessa "o que foi escavado, como foi datado".

## Trends (YouTube 12m)

- **Não coletado.** `--brief` e o retry `--trends "lost civilization documentary"` retornaram **HTTP 429** em 2026-09-22 (rate limit do Google). Fallback usado: autocomplete (107 + 343 termos). Revalidar em outro horário; o eixo `lost ancient civilizations` é o termo mais promissor para o teste.

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` (yt_auth sem o escopo `youtube.force-ssl`; teste em 2026-09-22 no vídeo `eHeT1G0I2jc`). Além disso, as páginas de canal/RSS do YouTube bloquearam a leitura por bot (só 1–3 vídeos visíveis no HTML). Repetir depois de `python scripts/yt_auth.py`, priorizando o vídeo do Dholavira (Aiwala) e "Lost Cities Beneath the Jungle" (Documentary Empire).

## Convergência de formato (últimos uploads)

- **Aiwala:** último upload confirmado por oEmbed (`QrEAXql1KIc`) é "Class 10 History: Takshashila University", em hindi — o canal convergiu para história educacional no mercado indiano; o Dholavira é o produto de maior alcance dessa linha.
- **Documentary Empire:** dois outliers na mesma janela ("Lost Cities Beneath the Jungle" e "The Rise and Fall of Mesopotamia") — formato "civilização: ascensão e queda/revelação" convergente.
- **Mr. True States / Wrongly Assumed / S Rao:** formato único de caso ("um sítio/um mistério por vídeo") com ângulo de evidência ou reinterpretação.
- **Limitação:** o coletor não mediu duração nem os últimos 5 uploads de cada canal; o HTML do YouTube bloqueou a verificação em massa. Revalidar com `--channel @handle` nos 3–4 canais-alvo.

## Fontes web (2+)

- https://faceless.my/niches/faceless-history-channel/ (13/06/2026) — guia do nicho de história faceless: RPM de história $5–15 [ALEGADO]; formatos 8–20 min (explicador) e 20–45 min (doc); lacuna em história não-ocidental (África, Sudeste Asiático, Mesoamérica); sponsors de livros/audiobooks; evergreen.
- https://www.overseeros.com/blog/faceless-ai-history-channels (02/07/2026) — "ancient civilizations" como subnicho de alta probabilidade; risco de precisão e de "AI slop"; monetização (AdSense, edtech, Patreon, produtos); alerta de que YouTube pune template mass-produzido.
- https://blog.autonolab.com/blog/2026-09-07-youtube-rpm-by-niche-98-faceless-niches-data (07/09/2026) — auditoria de 98 nichos faceless: Documentary $12,6 (31 canais), Dark History $12,2 (8), History $9,9 (50) [ALEGADO]; média geral $11,10 — base da classe $8–14, com confirmação só na Analytics.
- https://reelpilot.app/blog/faceless-youtube-rpm-by-niche (21/06/2026) — History & Documentary $4–9, saturação "low" [ALEGADO] — contraponto honesto à classe do modelo.
- https://support.google.com/youtube/answer/1311392 — [OFICIAL] política de conteúdo inautêntico (renomeada em 15/07/2025; aplicada ao canal como um todo; template/repetição inelegíveis).
- https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline (28/08/2026) — onda de enforcement de jan/2026: 16 canais, 35M de inscritos, 4,7B de views, ~US$10M/ano; detecção em nível de canal; padrão sinalizado: narração sintética + thumbnail em template + estoque sem comentário original.
- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage (15/06/2026) — algoritmo passou a favorecer rostos; criadores faceless humanos penalizados; conteúdo educacional de nicho segurou melhor — risco central do modelo.
- https://doi.org/10.1126/sciadv.adj8096 (Science Advances, 02/08/2023) — análise acadêmica do "counterestablishment archaeology"; a SAA exigiu que Netflix classificasse *Ancient Apocalypse* como ficção científica; Hancock usa a arqueologia "quando convém".
- https://debunked.info/terms/graham-hancock-lost-civilization/ (10/07/2026) — síntese claim-by-claim: o consenso rejeita a "civilização avançada perdida" pela ausência de traços físicos (ferramentas, pedreiras, assentamentos, resíduos); Göbekli Tepe é datado ~9500 BCE e construído por caçadores-coletores sem predecessor avançado.
- https://www.youtube.com/watch?v=4uvD30xw_ZY (World of Antiquity, 09/03/2026) — "fantasy archaeology" como beco sem saída: não corrige erros, não gera descoberta; defende mistério ancorado em evidência ("what does the data actually show?").
- https://www.nature.com/articles/s41586-022-04780-4 (25/05/2022) — Prümers et al.: LiDAR revela urbanismo pré-hispânico de baixa densidade no Amazonas boliviano (cultura Casarabe, ~500–1400 CE): 26 sítios, dois principais (147 ha e 315 ha), pirâmides de até 22 m, 4.500 km² — base factual do pilar "cidade escondida pela floresta".
- https://www.theguardian.com/science/2022/jun/02/amazon-rainforest-archaeology-settlements-bolivia-casarabe (02/06/2022) — cobertura do achado ("Amazonian urbanism") — derruba de vez a tese de floresta intocada.
- https://socialcounts.org/youtube-channel-analytics/UCE-tvt3RXs5LzQWV8UzvYnQ — "Lost Civilizations at Night": criado em 24/11/2025; 1.960 subs; 165.864 views; 52 vídeos (em 20/07/2026) — canal adjacente real do nicho (formato noturno/ambiente) com tração modesta; mostra que "lost civilizations" também existe como formato de fundo.
- https://www.linkedin.com/posts/stephen-ngene-88184431_faceless-youtube-automation-channel-case-activity-7436818094670585857-aZvA (09/03/2026) — case study [ALEGADO]: canal de documentário histórico faceless, 20–30 min, RPM $8–12, 256k inscritos, 25,3M views, 31 uploads (~815k views/vídeo) — referência de teto do gênero.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com qualificadores: (a) os cinco flares vêm de canais pequenos (122–21,9k subs) e recentes (68–288d) — o cruzamento "cidade específica + evidência/datalha LiDAR" está aberto no EN faceless, porque os grandes do tema têm rosto (historiadores) ou são TV (BBC/Discovery/Netflix); (b) "El Dorado" já tem dois outliers em 6 semanas (hindi) e começa a saturar; (c) o maior flare (Aiwala) é do mercado hindi — a versão EN precisa provar a própria tração; (d) a faixa de fundo/ambiente ("lost cities at night") já tem player pequeno, não disputar por lá; (e) o rótulo "lost civilization" sem qualificador atrai o público pseudocientífico — o posicionamento tem de ser de evidência desde o título e a thumbnail.
- **Gargalo real:** o gate de idade é o único que reprova em bloco (13/13 análises falham ≤45d; 4 emergentes passam 2/3). A pergunta da revalidação é se aparecem entrantes ≤45d no recorte "cidade revelada" — em 2–4 semanas os emergentes atuais (68–90d) sairão da janela de 45d, sendo substituídos ou não.
- **Riscos de advertiser/compliance:** (a) adjacência com pseudociência/conspiração derruba monetização mesmo com views — o canal deve ser explicitamente "evidence-based" e rotular [FATO]/[REPORTADO]/[LENDA]; (b) política de conteúdo inautêntico com detecção em nível de canal (jan/2026) exige 1 peça primária por vídeo e variação real de substância; (c) disputas de autoria/patrimônio (Great Zimbabwe) e sítios funerários exigem cuidado e respeito; (d) não publicar coordenadas de sítios não protegidos nem imagens de saque.

## Queries mais estreitas (se REPROVA)

- **Executada:** `lost city documentary` (cluster; 41 encontrados → 10 pequenos/jovens → 8 analisados; 0 gates; 4 emergentes; 5 com fome).
- **Não executadas (limite de 1 segunda busca da coleta):** `ancient civilization documentary` (a alternativa oferecida), `dholavira documentary`, `amazon lost cities documentary` e `el dorado documentary` — usar na revalidação de 2–4 semanas com `--age 45` para forçar o corte de idade e `--channel @handle` para checar os últimos 5 uploads dos canais-alvo.
