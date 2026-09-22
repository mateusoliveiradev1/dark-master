# Evidência — Heists e roubos históricos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "heist documentary" --max 8` + 1 busca estreita (`--cluster "museum heist documentary"`) + 3 checagens de canal (`--channel`) + websearch.
> Brief completo: `data/briefs/heist-documentary.md` · JSON: `data/briefs/heist-documentary.json`
> A saída do `--cluster` não foi salva em artefato (rodou sem `--out`); os números estão transcritos abaixo.
> Quota usada: ~320 unidades de ~10.000/dia (2 buscas de ~150 + 3 checagens de ~5–10).

## Veredito: **REPROVA** (gate estrito)

- Canais pequenos analisados: **16** (8 na busca ampla + 8 na estreita; elegíveis: 14 e 24 — quota cortou a amostra) | passam os 3 gates: **1** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **7 canais** (5 na ampla + 2 na estreita) — sinal: **SIM**
- Autocomplete: **156 termos** (meta ≥15) | Trends: **ESTÁVEL** no geral (59 vs 58), com picos fortes em sub-temas
- Quase-passer: **Thinking. While it's legal.** (15d) está a 717 views do gate de 5 primeiros (9.283/10.000 = 93%), crescendo a 1.799 views/dia

> Leitura honesta: o que reprova é o **gate de quantidade** (≥3 canais), não o cruzamento. No exato cruzamento do modelo — documentário EN de heists históricos, long-form — há **1 canal rompendo de verdade** (Heists and Capers, 41 dias de vida, PASSA os 3 gates, 4 outliers de 4,4×–7,1× em 3 semanas) e **1 quase-passer** que deve cruzar o gate de 10k em dias. A busca ampla está poluída por canais de **movie-recap em hindi** (formato ≠ documentário; "heist movie explained"), o que derruba a idade/aderência dos candidatos. Fome ativa nos dois formatos (long e Short) e nos dois idiomas. **Não escalar como validado**: revalidar com as queries estreitas abaixo e amostra maior antes de lançar.

## Canais-evidência — busca 1: `heist documentary` (2026-09-22)

Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha). 39 canais encontrados · 14 pequenos ≤365d · 8 analisados (quota) · **0/8 passam**.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| VeloCine | 68.300 | 156d | 64.497.577 | 2.203.279 | 011 | 0 |
| Filmexa Official | 6.660 | 107d | 63.594 | 27.784 | 011 | **35,7×** — 638.674 — "Gold Ke Liye Bank Me Hui Duniya Ki Sabse Badi Chori! INSIDE MAN 2019 Movie Explained In Hindi" (2026-07-24) |
| ALPHA DECODES | 13.300 | 184d | 596.683 | 14.110 | 011 | **3,9×** — 616.494 — "Brazil's Most Perfect Bank Robbery" (2026-07-15) |
| Movique Pro | 10.500 | 313d | 581.801 | 13.158 | 011 | 0 |
| Beta Decodes | 4.410 | 86d | 218.926 | 11.588 | 011 | **10,1×** — 379.552 — "The Blue Diamond Heist" (2026-07-15) · **5,7×** — 214.332 — "James Bong Robbery Gang" (2026-07-29) |
| Real Decodes | 2.740 | 229d | 8.510 | 2.450 | 001 | **328,5×** — 446.407 — "Dubai Bank Heist की पूरी कहानी" (2026-08-09) |
| All Crime | 22.400 | 223d | 3.213 | 24.835 | 001 | 0 |
| Life Truth Story | 1.520 | 137d | 709.879 | 5.358 | 011 | **65,8×** — 338.665 — "The Great Train Robbery" (2026-07-12) · **70,8×** — 364.084 — "Gohana Bank Robbery" (2026-07-28) |

> Todos falham na **idade** (86–313 dias). O tema "heist" pulsa nesses canais, mas em formato recap/explained majoritariamente hindi.

## Canais-evidência — busca 2 (estreita): `museum heist documentary` (2026-09-22)

47 canais encontrados · 24 pequenos ≤365d · 8 analisados (quota) · **1/8 passa** (meta ≥3).

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| **Heists and Capers** | 119 | **41d** | **25.683** | **1.341** | **111 PASSA** | **4,4×** — 7.547 — "St. Patrick's Day 1990: Fake Cops and the Gardner Museum Hei…" (2026-08-30) |
| Thinking. While it's legal. | 78 | 15d | 9.283 | 1.799 | 101 (falta 717 views) | 0 |
| CaseLab | 303 | 192d | 17.300 | 570 | 010 | 0 |
| Meta Decodes | 1.360 | 52d | 5.731 | 110 | 000 | 0 |
| سوالف Ai | 380 | 60d | 1.010 | 3.469 | 001 | 0 |
| Ratri Kathalu | 5.280 | 71d | 3.286.316 | 57.015 | 011 | 0 |
| CRIME HQ | 1.120 | 323d | 2.619 | 293 | 000 | 0 |
| POV World17 | 1.820 | 160d | 4.287 | 1.050 | 001 | **19,1×** — 1.737 — "TWO MEN STOLE $500 MILLION IN ART… AND NEVER GOT CAUGHT" (2026-09-05) — Short |

## Verificação individual (convergência de formato)

- **Heists and Capers** (`--channel`, 2026-09-22): PASSA os 3 gates (119 subs · 41d · 5 primeiros 25.692 · 1.341/dia · mediana 1.728). **4 outliers em 3 semanas**: 7,1× "Nice 1976: The Sewer Heist of the Century at Société Générale" (12.279 · 28/08) · 6,1× "Patty Mitchell's 90-Second San Diego Heist" (10.620 · 09/09) · 4,9× "Inside the 1978 Lufthansa Heist at JFK – Jimmy Burke" (8.456 · 16/09) · 4,4× "Gardner Museum" (7.556 · 30/08). Cadência ~2 uploads/semana, 100% heists históricos EN — **formato convergente = documentário narrado de caso histórico**. É o único gate-passer da coleta.
- **Thinking. While it's legal.**: 78 subs · 15d · 5 primeiros 9.283 (93% do gate) · 1.799/dia · mediana 1.219. Falha **só** o gate de 5 primeiros, por 717 views — candidato a gate-passer em dias (rechecar no re-scan).
- **POV World17**: falha idade e gates; outlier 19,1× num **Short** de arte ("$500 million in art", 1.737 views vs mediana 91) — corrobora o tema em Shorts, sem força estatística própria (canal pequeno e heterogêneo).

## Outliers (janela de 2–6 semanas)

- Real Decodes — **328,5× (flare nominal)** — 446.407 views — "Dubai Bank Heist" — 2026-08-09 — padrão: país + banco + cifra (funciona em recap; mediana do canal é 1.359).
- Life Truth Story — **70,8×** — 364.084 — "Gohana Bank Robbery" — 2026-07-28 — padrão: caso local + cifra + "True Crime Documentry".
- Life Truth Story — **65,8×** — 338.665 — "The Great Train Robbery" — 2026-07-12 — padrão: roubo histórico famoso em 15 min.
- Filmexa Official — **35,7×** — 638.674 — "Bank heist / Inside Man recap" — 2026-07-24 — padrão: heist de cinema (fora do formato documentário).
- POV World17 — **19,1×** — 1.737 — Short de roubo de arte — 2026-09-05.
- Beta Decodes — **10,1×** — 379.552 — "The Blue Diamond Heist" — 2026-07-15 — padrão: joia/coleção real + "maior da história".
- Heists and Capers — **7,1×** — 12.279 — "Nice 1976: Société Générale" — 2026-08-28 (e 4,4×–6,1× nos outros 3 uploads) — padrão: documentário EN de heist histórico, lugar + ano no título.
- ALPHA DECODES — **3,9×** — 616.494 — "Brazil's Most Perfect Bank Robbery" — 2026-07-15 — tema: banco sem sangue.

## Fome do algoritmo (cluster cross-canal)

- Busca ampla: **5 canais diferentes** com outlier ≥3× (Filmexa, ALPHA DECODES, Beta Decodes, Real Decodes, Life Truth Story) — sinal aberto no tema "bank heist/roubo famoso".
- Busca estreita: **2 canais** com outlier ≥3× (Heists and Capers, POV World17) — sinal aberto no tema "arte/museu".
- Leitura: fome em **dois idiomas e dois formatos** (recap massivo + documentário EN emergente); a janela de 2–6 semanas está aberta no cruzamento EN documentário — mas a oferta de canais pequenos EN ainda é rasa (1 rompendo de verdade).

## Demanda (autocomplete — 156 termos; top relevantes)

- `heist documentary` (raiz) + variações: `2025`, `uk`, `netflix`, `south africa`, `usa`, `hindi`, `trailer`
- `bank heist documentary` · `art heist documentary` · `louvre heist documentary` · `lufthansa heist documentary` · `diamond heist documentary` · `casino heist documentary` · `crypto heist documentary` · `bitcoin heist documentary`
- `biggest heist documentary` · `best heist documentary` · `big heist documentary` · `british heist documentary` · `brazil heist documentary` · `bangladesh heist documentary` · `bloemfontein heist documentary` · `bank heist documentary uk`
- `robbery crime documentary` · `crime heist documentary` · `history's greatest heists`
- Ruído relevante: ~40 termos de "heist movie explained/full" (cinema) puxam o termo para ficção — separar no metadata (sempre "documentary"/"true story").

## Trends (YouTube 12m)

- Busca do brief: falhou (429). Retry manual (`--trends "heist documentary"`): interesse **ESTÁVEL** (recente 59 vs anterior 58).
- Queries em alta: **`louvre heist documentary` (+266.100%)** · `holy heist documentary` (+26.900%) · **`boston art heist documentary` (+19.650%)** · `isabella stewart gardner museum heist documentary` (+300%) · `hatton garden heist documentary` (+60%) · `gardner museum heist documentary` (+60%).
- Contexto real por trás: assalto ao Louvre em 19/10/2025 (joias napoleônicas; ~US$140M Cdn; a maioria nunca recuperada) + onda de roubos "inspirados" em 2026 (Renoir/Cagnes-sur-Mer em set/2026; Magnani Rocca em mar/2026; Messina em ago/2026) — o tema se renova a cada poucas semanas (CBC, 09/09/2026).

## Comentários (demanda explícita)

- Não coletado via Data API: o scan não expõe video IDs e o orçamento foi limitado às duas buscas autorizadas. Sinais qualitativos de comunidades:
  - r/DocuJunkies: "I'm craving something about heists… famous heists, daring robberies, complex plans that actually worked — or failed spectacularly" (thread com recomendações recorrentes: "This Is a Robbery" (Gardner), "Billion Dollar Heist", doc do Louvre).
  - r/MovieSuggestions: pedidos de docs de £53M (Securitas) e do Antwerp Diamond Heist — "feels like a crime thriller".
  - r/DocumentaryReviews: divulgação de canal novo pequeno "like fern" com doc 3D de bank heist — entrada barata no cruzamento.
- Rodar `--comments` em 1 vídeo do Heists and Capers no piloto para ler pedidos recorrentes (exige `youtube.force-ssl`).

## Fontes web (2+)

- https://www.cbc.ca/news/entertainment/renoir-theft-louvre-copycats-9.7336447 — CBC (09/09/2026): onda de roubos de arte "inspirada" no Louvre; valores; Europol: método mais violento/smash-and-grab.
- https://www.bostonglobe.com/2025/10/21/arts/louvre-heist-gardner-heist/ — Boston Globe (21/10/2025): FBI do caso Gardner sobre o Louvre; livro "Thirteen Perfect Fugitives" (mar/2026); "We know who did it, but the artwork never came back".
- https://www.tvcentral.com.au/free-to-air/sbs-news/the-heist-sbs-louvre-crown-jewels-theft/ — SBS (28/06/2026): documentário "The Heist: The Louvre's Stolen Crown Jewels"; raid de sete minutos; demanda mainstream.
- https://www.youtube.com/watch?v=NIGbQ9NHFEg — Hank Green (11/2025): 2,7M views em 44 min analisando o Louvre — apetite por "como foi" sem gore.
- https://www.youtube.com/shorts/Ws8Xeg5ONck · https://www.youtube.com/shorts/EciUt37Px8Q · https://www.youtube.com/shorts/rF5CcSW-i58 — Shorts de arte/heist em 2026 ("$500M Stolen, Still Unsolved"; "Tiny Detail in Security Footage") — o tema roda em Shorts também.
- https://longformstudio.app/articles/true-crime-youtube-channel (11/08/2026) — formato true crime; RPM reportado $6–9 (não gráfico); guidelines: framing documentário monetiza, gráfico em thumb/15s = Limited Ads; flags de inautenticidade em doc roteirizado; YPP dobra em 01/02/2027 (8.000h/20M).
- https://virvid.ai/blog/faceless-content-rpm-by-niche-real-earnings-data-2026 (20/01/2026) — True Crime/Mystery long RPM $5–10 [ALEGADO]; FilmRise True Crime (1,38M subs) est. $21–64k/mês com vídeos de 27 min; exige "genuine human creative input".
- https://fluxnote.io/blog/youtube-rpm-by-niche-2026 — True Crime $5–12 (mediana $8); History/Documentary $6–14 (mediana $9) [ALEGADO].
- https://www.earngenix.com/blog/most-profitable-youtube-niches-in-2026 (05/01/2026) — "True Crime Documentary" $8–12, ad-heavy, evergreen [ALEGADO].
- https://ytdark.com/en/blog/cpm-nicho-dark-youtube — CPM true crime $8–22, RPM est. $5,40–9,90; membership/merch convertem bem [ALEGADO].
- https://reelpilot.app/blog/best-faceless-youtube-niches-2026 (21/06/2026) — True Crime & Mystery $3–7; history/doc $4–9 com saturação baixa [ALEGADO].
- https://www.reddit.com/r/DocuJunkies/comments/1krvtz3/heist_documentary_suggestions/ · https://www.reddit.com/r/MovieSuggestions/comments/1l0872z/if_you_enjoy_heist_movies_you_should_check_out/ · https://www.reddit.com/r/DocumentaryReviews/comments/1myn0ng/the_most_genius_bank_heist_in_history_short_3d/ — demanda explícita e vitrine de entrantes pequenos.
- https://www.wbur.org/podcasts/lastseen/last-seen-season-one — "Last Seen" (WBUR/Boston Globe): Gardner em 81 minutos, 13 obras, ~$500M, recompensa de $10M — demanda contínua de arte/assalto.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** O tema tem volume massivo, mas concentrado em movie-recap (hindi) e streaming (Netflix/SBS). No EN YouTube long-form documentário, a oferta recente é rasa: 1 gate-passer de 41 dias (Heists and Capers) + 1 quase-passer de 15 dias. Há espaço, mas o gate ≥3 **não fecha** — revalidar.
- **Riscos de advertiser/compliance:** heist é menos gore-prone que homicídio; o risco é enquadramento (gráfico em thumb/15s = Limited Ads) e caso ativo (Louvre 2025 tem presos — "alleged"). Sem sangue, sem arma apontada, sem acusação de pessoa viva.
- **Inautenticidade:** doc narrado com assets sintéticos recebe flag automatizado [ALEGADO — longformstudio] — 1 peça de pesquisa primária por vídeo (linha do tempo, planta, lista do seguro) e variedade de estrutura.
- **Direitos:** obras antigas em domínio público, mas fotos de museu/arquivo podem ter direito; nunca frames de streaming/filmes.

## Queries tentadas e próximas (gate não fechou)

- `heist documentary` — **TENTADA** (busca 1): 0/8 gates; fome 5 canais; poluída por recap hindi.
- `museum heist documentary` — **TENTADA** (estreita): 1/8 gates (Heists and Capers, PASSA) + quase-passer; fome 2 canais.
- `bank robbery documentary` — a alternativa prevista no método, **não rodada** (regra de UMA segunda busca).
- Próximas puxadas por Trends: `louvre heist documentary` (+266.100%), `boston art heist documentary` (+19.650%), `hatton garden heist documentary` (+60%).
- Revalidar: repetir a estreita em 2–4 semanas (janela de fome) com amostra maior (elegíveis 24; analisados 8) e rechecar "Thinking. While it's legal." (deve cruzar o gate de 10k).
