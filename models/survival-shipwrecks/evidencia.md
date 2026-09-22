# Evidência — Naufrágios

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "shipwreck documentary" --max 8` + segunda busca `python scripts/niche_scan.py --cluster "lost ship documentary" --max 8` (a segunda opção do método era `shipwreck mystery documentary`; a escolha daqui cobre a metade "desaparecimento/achado de casco" do subnicho, distinta do genérico já testado) + checagem de âncoras `--channel @OceanlinerDesigns` e `--channel @parttimeexplorer` + websearch (autocomplete e Trends vêm embutidos no brief).
> Brief completo: `data/briefs/shipwreck-documentary.md` · JSON: `data/briefs/shipwreck-documentary.json` (o cluster imprime em tela, não salva arquivo; saída capturada no temp da sessão).
> Quota: ~310 unidades (estimativa) de ~10.000/dia — 2 buscas pesadas (~150 cada) + 2 checagens de canal (~5 cada); autocomplete é HTTP livre.

## Veredito: **PARCIAL**

> Nota: o brief automático retornou **REPROVA** (1/8 gates) e o cluster **REPROVA** (0/8). A classificação **PARCIAL** segue a legenda do `models/README.md`: menos de 3 gates, **com fome do algoritmo (≥2 canais com outlier ≥3×) e emergentes ≤90d** — as duas condições estão presentes e verificadas abaixo. Não é PASSA (nenhum conjunto de 3 canais ≤45d cruzou os 3 gates) e não é REPROVA pura (o formato está performando com sobra nos gates 2–3 e há fome recente em set/2026).

- Canais pequenos analisados: **15 únicos** (8 no brief + 8 no cluster, 1 repetido) | passam os 3 gates: **1** (meta ≥3) — Buried Frequencys (111)
- Emergentes (≤90d + 2/3 gates): **4** — Atlas One (66d), FunWorldFun (56d), Lifelog Tales (62d), Beyond Bharat (64d)
- Fome do algoritmo (outlier ≥3×): **6 canais** (3 no brief + 3 no cluster); **4 deles são de naufrágio/mar** — sinal: **sim**, com flare de 1.169,7× (Atlas One) e outliers frescos de set/2026
- Autocomplete: **72 termos** (meta ≥15), com eixos fortes em Great Lakes, Titanic, Fitzgerald, Endurance, Antikythera, Uluburun, Atocha e San José | Trends: **429** (rate limit do Google — sem leitura própria; fallback autocomplete)
- Âncoras do segmento (fora dos gates, evidência de teto): Oceanliner Designs 969 mil subs; Part-Time Explorer 492 mil subs (números Data API, 2026-09-22)

**Leitura honesta:** o cruzamento **não fecha os 3 gates** — 1 canal em 15 passa (Buried Frequencys, 15 dias, flare de 15,4× checando o que os filmes de Titanic erram), e o gargalo é o mesmo do resto da biblioteca: **o gate de idade**. Dos 15 canais analisados, 13 passam os gates 2 e 3 (5 primeiros ≥10k e ≥1k views/dia) — 12 deles falham só a idade; apenas 2 canais falham um gate adicional (Cine Addict em views/dia; The Hidden World Hindi nos 5 primeiros). A fome é real e recente: entre jul e set/2026, quatro canais diferentes fizeram outlier em naufrágio/mar — Lifelog Tales (04/09), Atlas One (08/09), Buried Frequencys (16/09) e The Hidden World Hindi (06/08) — e as âncoras provam o teto (Edmund Fitzgerald: 2,5M views; série semanal de 41–44 min com 184k no primeiro episódio). O recorte tem sobreposição com o modelo `mystery-ocean` (coletado no mesmo dia; Atlas One aparece nos dois) — a diferenciação está na seção de saturação. **Não escalar ainda**; revalidar em 2–4 semanas olhando por entrantes ≤45d.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

### Busca 1 — `--brief "shipwreck documentary"` (8 pequenos analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| **Buried Frequencys** | **162** | **15d** | **16.640** | **15.620** | **111** | **15,4× — 42.050 — "Why Every Titanic Movie Gets This Wrong 🌑" — 2026-09-16** |
| Atlas One | 3.670 | 66d | 138.751 | 32.060 | 011 | 1.169,7× — 1.594.246 — "They Were Left On An Island For 15 Years: True Survival Story" — 2026-09-08 |
| FunWorldFun | 1.460 | 56d | 178.905 | 30.642 | 011 | — (mediana 30; quase todo o volume em um upload — formato a confirmar) |
| New Discovery | 49.400 | 215d | 81.984 | 57.182 | 011 | — |
| Día 0 | 11.500 | 203d | 45.973 | 52.122 | 011 | — |
| Forbidden Mysteries | 34.800 | 363d | 12.283 | 17.063 | 011 | — (fora da amostra do scan; web mostra a série `Shipwreck Secrets` com 184.247 views no E1) |
| Before Us | 6.260 | 287d | 14.583 | 1.411 | 011 | — |
| Cine Addict | 53 | 297d | 16.459 | 55 | 010 | 164,2× — 16.259 — "Shipwrecked,Nightmare At Sea Full Hd Movie." — 2026-07-10 (upload de filme pronto; **fora da evidência**) |

### Busca 2 — `--cluster "lost ship documentary"` (46 canais achados; 17 pequenos ≤365d; 8 analisados por quota)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| ExplainFlix | 67.900 | 168d | 3.044.472 | 620.970 | 011 | — |
| Ashes & Steel | 22.800 | 239d | 389.512 | 738.176 | 011 | — |
| Nostalgic War Stories Official | 9.100 | 303d | 334.227 | 3.448 | 011 | 16,5× — 180.602 — "What Happened to the Mother Who Lost All Five Sons?" — 2026-07-21 (guerra; naufrágio **não confirmado** no título) |
| CosmoMyst | 895 | 139d | 76.655 | 5.259 | 011 | — |
| **Lifelog Tales** | 744 | **62d** | 55.146 | 3.673 | 011 | 12,8× — 38.709 — "THE SHIP WAS FOUND… BUT ALL 25 PEOPLE WERE GONE 😱" — 2026-09-04 |
| Beyond Bharat | 469 | 64d | 16.544 | 5.082 | 011 | — |
| The Hidden World Hindi | 2.210 | 215d | 6.024 | 1.690 | 001 | 24,6× — 72.660 — USS Cyclops Mystery (hindi) — 2026-08-06 |
| Forbidden Mysteries (dup.) | 34.800 | 363d | 12.283 | 17.063 | 011 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "111" = passa os 3. "011" = só a idade falha. O cluster ranqueia os top-50 vídeos do tema em 90 dias e analisa os canais pequenos (≤200k subs) e ≤365d que aparecem ali — canais muito novos só entram se um vídeo já estiver nesse topo. Únicos: 8 + 8 − 1 (Forbidden Mysteries em ambas) = 15.

## Outliers (janela de 2–6 semanas; oportunidade quando fresco)

- **Buried Frequencys — 15,4×** — 42.050 views — "Why Every Titanic Movie Gets This Wrong 🌑" — 2026-09-16 — canal de 15 dias e 162 subs; padrão: **checagem mito vs registro** (o que os filmes erram) — o ângulo mais fresco do recorte e o único gate-passer.
- **Atlas One — 1.169,7× (FLARE)** — 1.594.246 views — "They Were Left On An Island For 15 Years: True Survival Story" — 2026-09-08 — sobrevivência no mar com "true story" no título; canal de 3,7k subs e 66 dias. O ratio é inflado por mediana baixa; o que vale é o viewport absoluto (1,59M) em canal pequeno.
- **The Hidden World Hindi — 24,6×** — 72.660 views — USS Cyclops (desaparecimento de 1918) em hindi — 2026-08-06 — demanda global pelo caso clássico.
- **Lifelog Tales — 12,8×** — 38.709 views — "THE SHIP WAS FOUND… BUT ALL 25 PEOPLE WERE GONE 😱" (caso Joyita) — 2026-09-04 — canal de 62 dias e 744 subs; padrão: **casco achado + tripulação sumida**.
- **Cine Addict — 164,2×** — 16.259 views — upload de filme "Shipwrecked" — 2026-07-10 — **excluído da evidência** (não é documentário; canal de 53 subs e 55 views/dia).
- **Nostalgic War Stories Official — 16,5×** — 180.602 views — "What Happened to the Mother Who Lost All Five Sons?" — 2026-07-21 — tema de guerra; possível ligação naval (irmãos Sullivan?), **não confirmada no título** — não conta como fome de naufrágio.

## Fome do algoritmo (cluster cross-canal)

**Sim, em dois cortes, com 4 canais de naufrágio/mar na janela jul–set/2026:**

1. **"Casco achado / tripulação sumida"** — Lifelog Tales (04/09, 38,7k) e The Hidden World Hindi (06/08, 72,6k; caso Cyclops) + Buried Frequencys (16/09, 42k; mito do Titanic). Três casos diferentes, dois idiomas, todos em set–ago/2026 — janela de 2–6 semanas viva.
2. **"Sobrevivência no mar"** — Atlas One (08/09, 1,59M) — o flare da coleta; mesmo recorte que o `mystery-ocean` registrou em jul–set/2026 (Atlas One, Hidden Earth, THE GEO VIBE). Sobreposição reconhecida e endereçada na seção de saturação.
3. **Sinal de teto:** Part-Time Explorer fez 783.004 views (14,2×) com "The Wreck of the Andrea Doria" em 17/07/2026 e 2,5M (45,4×) com o Edmund Fitzgerald em nov/2025; Forbidden Mysteries mantém série semanal de 41–44 min (Shipwreck Secrets, E1 com 184.247 views em 21/07/2026). O tema sustenta viewport de sete dígitos em canais estabelecidos e de cinco a seis dígitos em canais pequenos.

## Demanda (autocomplete — top termos)

72 termos únicos. Eixos com demanda real:

- **Grandes Lagos:** `shipwreck documentary great lakes` (2º termo geral), `fitzgerald`, `shipwreck edmund fitzgerald documentary`.
- **Casos clássicos:** `titanic`, `batavia`, `atocha`, `san jose`, `bom jesus`, `ww2 shipwreck documentary`.
- **Achados/expedições:** `endurance shipwreck documentary`, `antikythera shipwreck documentary`, `uluburun shipwreck documentary`, `shipwreck discovery documentary`, `shipwrecks found`.
- **Investigação:** `shipwreck investigation`, `shipwreck detectives`, `shipwreck tomb`.
- **Idiomas:** hindi, urdu, tamil, kannada, malayalam (demanda global pelo tema).
- **Ruído (não é demanda do nicho):** `minecraft`, `kobe bryant`, `kyoto`, `qatar`, `philippines`, `xbox`, `zemtv`, `reaction`, `netflix trailer`, `part 1/2`.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` retornou **HTTP 429** (rate limit do Google) em 2026-09-22, como no restante da rodada. Fallback: autocomplete (72 termos, três eixos densos). Revalidar `--trends "shipwreck documentary"` e `--trends "great lakes shipwreck"` em outro horário.

## Comentários (demanda explícita)

Não coletado — `--comments` exige o escopo `youtube.force-ssl` (a tentativa da sessão de coleta de 22/09 retornou `insufficientPermissions`; rodar `python scripts/yt_auth.py` uma vez). Sugestão para a revalidação: ler os comentários dos episódios de `Shipwreck Secrets` (Forbidden Mysteries) e do outlier de Lifelog Tales — os pedidos recorrentes tendem a apontar os próximos cascos (Great Lakes, frota japonesa, U-boats).

## Convergência de formato (últimos uploads)

- **Forbidden Mysteries:** série `Shipwreck Secrets` quase semanal (E1 21/07 — 184.247 views; E4 31/07 — 23.717; E5 04/08 — 11.434; E6 07/08 — 70.960; snapshots de espelho), 41–44 min por episódio, temporada numerada — formato de biblioteca por série. O canal é maior que o recorte do scan sugere (27,5k → 34,8k subs entre jul e set/2026 pela comparação espelho × Data API).
- **Part-Time Explorer:** um navio por episódio, nome no título, 20–90 min; convergência total na promessa "o que aconteceu com este casco".
- **Oceanliner Designs:** setembro/2026 com outlier de 6,3× (1.338.141 views, "Soviet Cruises Were Actually Pretty Good", 02/09) — cobre o tema marítimo amplo com rosto e equipe; mediana altíssima (210.911). Teto do segmento, não molde faceless.
- **Buried Frequencys:** 15 dias de canal, quase todo o volume em um vídeo de checagem de Titanic — formato a confirmar com `--channel` na revalidação.

## Fontes web (2+)

- https://www.oceanlinerdesigns.com/about — o maior canal de história marítima do YouTube: ~1M de inscritos, 5–10M de espectadores/mês, 200M+ views; produção com equipe (roteiristas, modeladores 3D, animadores) e apresentador com rosto — teto e contraexemplo do faceless.
- https://www.youtube.com/@OceanlinerDesigns — snapshot público: 917K subs e 539 vídeos; ecossistema de canais parceiros (Warship Designs 58,6K; Airliner Designs 61,6K; Brick Immortar 391K) — mostra a segmentação que o nicho já tem.
- https://divert.stream/watch/7O2cE8KcUNw — Forbidden Mysteries, `Shipwreck Secrets` E1 (Bermuda Triangle): 184.247 views · 21/07/2026, 41–44 min — prova do formato de série semanal no recorte.
- https://divert.stream/watch/up2aVnu0rBw — `Shipwreck Secrets` E6 (Lake Erie / Lake Serpent): 70.960 views · 07/08/2026 — Great Lakes como pauta quente.
- https://www.netflix.com/tudum/articles/shipwrecked-nightmare-at-sea-release-date-news — documentário de streaming em jul/2026 sobre o desastre marítimo de 2012 (32 mortes, pena de 16 anos): atenção mainstream ao tema **e** zona de risco (tragédia recente, famílias ativas) — fora do escopo do canal.
- https://www.abc.net.au/news/2026-09-05/documentary-tells-story-of-geltwood-shipwreck-south-australia/107058110 — doc comunitário do naufrágio Geltwood (150 anos) repercutindo em set/2026 — apetite local/regional por história de casco.
- https://faceless.my/youtube/how-much-do-faceless-youtube-channels-make — faixas faceless 2026: history/true crime $4–10 RPM; business documentaries $8–18 [ALEGADO] — âncora baixa da classe.
- https://reelsmakerai.com/blog/how-much-do-faceless-youtube-channels-make — History & Mystery $8–18 RPM, saturação "baixa" [ALEGADO] — âncora alta da classe.
- https://flippa.com/12813083-faceless-documentary-youtube-channel-with-11m-views-235k-revenue-98-profit-margin-and-20-rpm-in-a-premium-history-niche — listagem de canal faceless de documentary history (94.680 subs, 11M views, +$235k de receita, RPM $20+ reportado, 77,2% US, 83% em 45+) [ALEGADO — dados do vendedor; útil como sinal de que documentary faceless é ativo vendável].
- https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos — [OFICIAL reportado] atualização de jul/2026: 3 categorias de conteúdo inautêntico não monetizável (genérico/repetitivo/template; off-putting/emocionalmente manipulador; AI personas em temas sensíveis) — regra de desenho do canal.
- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage — jun/2026: 16 canais terminados em jan/2026 (35M de inscritos, ~$10M/ano); enforcement no nível do canal (um padrão nos últimos 30 uploads pode derrubar a monetização inteira) — risco central do modelo.
- https://gizmodo.com/youtube-cracks-down-on-off-putting-content-and-ai-slop-2000787956 — leitura da categoria "off-putting": conteúdo feito para angustiar ou manipular emoção é o que derruba — o oposto do tom documental proposto.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Com ressalvas. (a) O ângulo "contar a história" está saturado por âncoras com rosto (Oceanliner Designs 969k; Part-Time Explorer 492k) — competir no mesmo enquadramento é perder. (b) O que está aberto no faceless EN é o **dossiê do casco**: checagem de mito (Buried Frequencys), desaparecimento sem traço (Cyclops/Joyita), achado recente e ciência de expedição — os outliers de jul–set/2026 mostram fome exatamente aí, e nos canais pequenos que fizeram outlier a produção é contida. (c) Great Lakes é o eixo de autocomplete mais forte depois do genérico e tem caso quente (Lake Serpent/Erie em ago/2026) com players regionais, não nacionais. (d) O lado "tesouro" (Atocha, San José) tem demanda (`shipwreck treasure documentary`) mas puxa o canal para clickbait e para litígios ativos — usar como tema, nunca como promessa.
- **Sobreposição com `mystery-ocean`:** o modelo irmão (coletado no mesmo dia) cobre oceano profundo, abismo e "lost at sea survival" — e Atlas One aparece nas duas evidências. Não operar os dois canais com a mesma promessa: aqui o protagonista é **o navio e o dossiê do casco** (viagem, perda, busca, descoberta, inquérito); lá é **o oceano e o que ele esconde**. Se rodar só um, este modelo é o mais "arquivo" (evergreen) e o outro é o mais "mistério".
- **Gargalo real:** o gate de idade — 13 de 15 canais passam os gates 2 e 3; 4 emergentes de 56–66 dias estão a 1–3 semanas de cruzar a janela. A revalidação responde à pergunta: os emergentes mantêm o ritmo quando cruzarem 45 dias, e aparecem novos entrantes ≤45d?
- **Riscos de advertiser/compliance:** mortes em naufrágios (enquadramento documental e sem imagem gráfica tende a monetizar; thumbnails de tragédia e tom "chocante" caem em limited ads/"off-putting"); naufrágios de guerra são túmulos legais e simbólicos (sem restos, sem coordenadas sensíveis); precisão (casos com teoria conspiratória precisam de rótulo explícito, e contradições entre fontes viram camada [REPORTADO]); direito de footage (a concorrência do recorte usa conteúdo empacotado de TV — não replicar sem licença); tragédias recentes com famílias ativas ficam fora.

## Queries mais estreitas (não executadas — para a revalidação)

- `great lakes shipwreck documentary` (2º termo do autocomplete; eixo mais forte não testado).
- `shipwreck investigation` e `found shipwreck documentary` (foco em caso + inquérito, não em história marítima ampla).
- Checar entrantes ≤45d com `--age 45` e acompanhar Buried Frequencys, Atlas One, FunWorldFun, Lifelog Tales e Beyond Bharat quanto cruzarem a idade; confirmar o formato de Buried Frequencys com `--channel`.
