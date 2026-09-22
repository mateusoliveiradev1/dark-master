# Evidência — Serial killers (bio)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "serial killer documentary" --max 8` + retry estreito `python scripts/niche_scan.py --cluster "serial killer case files" --max 8` (Data API) + websearch
> Brief completo: `data/briefs/serial-killer-documentary.md` · JSON: `data/briefs/serial-killer-documentary.json`
> Quota usada: ~300 unidades de ~10.000/dia (2 buscas).

## Veredito: **REPROVA**

- Canais pequenos analisados: 12 (4 na busca ampla + 8 na estreita) | passam os 3 gates: **1** (meta ≥3)
  - busca ampla: 1/4 (Dellirium 13) · busca estreita: 0/8
- Fome do algoritmo (outlier ≥3×): **2** canais na busca ampla e **3** na estreita — sinal: **SIM** (≥2 canais diferentes com outlier nas duas buscas; 1 flare ≥10×)
- Autocomplete: **298 termos** (meta ≥15) | Trends: **ALTA** (83,5 recente vs 74,3 anterior)

Leitura honesta: o cruzamento formato×tópico tem **demanda alta, fome ativa e formato claro** — o que reprova é o **gate de idade**: quase não existem canais ≤45d no conjunto visível (os canais que rompem têm 86–340 dias e falham só o gate de idade). Nicho quente, porém com topo saturado por catálogos; um canal novo precisa de diferenciação (perícia/arquivo, camada "abaixo" dos casos famosos) e recheque em 2–4 semanas.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Busca | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|---|
| **Dellirium 13** | ampla | 23.600 | **42d** | **9.631.211** | **228.060** | **111** | — |
| Red File | ampla | 97.600 | 208d | 8.486.858 | 171.137 | 011 | **10,5×** — 12.649.042 — "Friendly" Cop Has No Idea Police Already Matched Her DNA After 23 Years (2026-08-12) |
| 7 Movie | ampla | 28.800 | 228d | 315.626 | 41.699 | 011 | — |
| Silver Peak Films | ampla | 8.680 | 314d | 344.305 | 11.003 | 011 | 38,3× — 817.338 — He Escaped Prison To Hunt The Serial Killer Who Murdered His Daughter \| Full Crime Action Movie (2026-09-12) — ficção, fora do formato |
| Red File (2ª coleta) | estreita | 97.600 | 208d | 8.486.906 | 171.137 | 011 | 10,5× — mesmo vídeo |
| Desi Cases | estreita | 56.100 | 235d | 62.891 | 216.920 | 011 | — |
| RA True Crime 72 Hrs | estreita | 2.870 | 86d | 29.916 | 20.113 | 011 | — |
| FBI Investigates | estreita | 68.300 | 315d | 859.329 | 80.765 | 011 | **4,3×** — 359.581 — The Railroad Killer: FBI Manhunt For America's Most Evil Ser… (2026-09-05) |
| Crimewatch Central | estreita | 27.000 | 165d | 236.377 | 12.626 | 011 | **8,4×** — 272.830 — Colorado 1984 Bennett Family Massacre Cold Case SOLVED — Arr… (2026-07-14) |
| Othram Studios | estreita | 58.800 | 208d | 15.261 | 42.397 | 011 | — |
| The Infographics Show - True Crime | estreita | 58.700 | 340d | 723.214 | 20.102 | 011 | — |
| FBI Uncovered | estreita | 10.500 | 179d | 29.907 | 16.986 | 011 | — |

> Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha). Leve variação de 5 primeiros/mediana do Red File entre as duas coletas é refresh natural da API.
> Nota: o cluster analisa vídeos top-50 por views em 90d — canais muito novos só aparecem se um vídeo entrar nesse topo (foi o caso do Dellirium 13).

## Outliers (janela de 2–6 semanas)

- **Red File — 10,5× (FLARE)** — 12.649.042 views — citação + reveal forense (DNA casado depois de 23 anos) — 2026-08-12 — padrão: arco longo + prova de laboratório no título.
- **FBI Investigates — 4,3×** — 359.581 — manhunt federal + apelido do caso ("The Railroad Killer") — 2026-09-05 — padrão: FBI + caçada.
- **Crimewatch Central — 8,4×** — 272.830 — cold case de 1984 resolvido (DNA/aresto) — 2026-07-14 — padrão: caso antigo + "SOLVED".
- **Silver Peak Films — 38,3×** — 817.338 — filme de ação "serial killer" — 2026-09-12 — padrão fora do cruzamento (ficção; não conta como documentário).

## Fome do algoritmo (cluster cross-canal)

- Busca ampla ("serial killer documentary"): 2 canais diferentes com outlier ≥3× (Red File, Silver Peak Films) → sinal aberto.
- Busca estreita ("serial killer case files"): **3 canais** com outlier ≥3× (Red File, FBI Investigates, Crimewatch Central) → sinal aberto.
- On-format (documentário/case-file): Red File + FBI Investigates + Crimewatch Central. O padrão "caso + prova forense (DNA) + desfecho judicial" está quente; o flare do Red File se repete nas duas buscas.

## Demanda (autocomplete — top termos)

- serial killer documentary (raiz)
- serial killer documentary full / full episodes / long
- serial killer documentary fbi files
- serial killer documentary interrogation / interview / police / caught
- serial killer documentary cold case / unsolved
- serial killer documentary psychology
- serial killer documentary edmund / kemper / ramirez / green river / hillside strangler
- serial killer documentary uk / asia / africa / india / japan / russia
- serial killer biography
- unknown serial killer documentary / unidentified serial killer documentary

## Trends (YouTube 12m)

- Direção: **ALTA** (83,5 recente vs 74,3 anterior) · Rising: `gilgo beach serial killer documentary netflix` (+650%), `method of a serial killer documentary` (+350%), `gilgo beach serial killer documentary` (+80%).

## Comentários (demanda explícita)

Não coletado nesta coleta — fora do escopo das duas buscas autorizadas; `--comments` exige escopo `youtube.force-ssl` e um ID de vídeo do cluster. Rodar em 1 vídeo do Red File/FBI Investigates no piloto para ler pedidos recorrentes.

## Fontes web (2+)

- https://support.google.com/youtube/answer/6162278?hl=en — [OFICIAL] advertiser-friendly: foco em sangue/violência/ferimento **sem contexto** restringe anúncios; contexto documentário/educacional conta a favor.
- https://falconvid.ai/blog/true-crime-faceless-youtube-channel — [ALEGADO] "true crime é o nicho que mais coleta yellow icons"; RPM $5–12; 4 regras de monetização (contexto, self-certification, vítimas, footage); topo saturado / camadas abaixo abertas; 8.000h a partir de 02/2027.
- https://becomeviral.com/blog/true-crime-faceless-youtube — [ALEGADO] CPM $5–12; formatos que performam: case deep dive 15–25 min, unsolved, perfil de serial killer com psicologia; diferencial = pesquisa original (court documents).
- https://variety.com/2026/digital/news/dr-insanity-true-crime-youtube-wonderloom-content-partners-1236810322 — 14/07/2026: aquisição do Dr. Insanity (5M+ subs) pela Wonderloom — canal faceless de true crime como ativo financeiro.
- http://drinsanity.com/ — 5,2M+ inscritos, 1,28B+ views; "fact-checked documentaries built from police footage, interrogation clips, 911 audio, court records, and case files" — valida o formato arquivo/perícia.
- https://www.reddit.com/r/Casefile/comments/1pz72mp/any_recommendations_for_true_crime_youtube — demanda por canais no estilo CaseFile (estrutura metódica, ethos) — 30/12/2025.
- https://kineclip.com/blog/how-much-faceless-youtube-channels-make — [ALEGADO] binge de true crime aumenta sessão/tempo de tela.
- https://faceless.my/youtube/how-much-do-faceless-youtube-channels-make — [ALEGADO] history/true crime $4–10 RPM.
- https://www.youtube.com/channel/UC1s9576cQFdQq3QTtTxocmA (Real Crime, 2,17M) e https://www.youtube.com/playlist?list=PLOnBqIDMUw1k9hKQuEYKcCUZcg_YldMzR (True Crime Central) — formato dominante: docs de 40–55 min, catálogos "World's Most Evil Killers"/"FBI Files".
- https://www.youtube.com/channel/UCVp68NDqAm_0s7pbC3XP24w (The Mystery Abyss) — concorrente faceless: "lesser known cases from around the world", docs de 35–72 min, pesquisa própria.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Sim, com ressalvas: o topo é saturado (catálogos de estúdio, Netflix, Dr. Insanity) e os canais que rompem têm 86–340 dias — o gate de idade (≤45d) é o gargalo. A fome ativa em "case files/DNA reveal" mostra janela, mas o novo entrante precisa de ângulo próprio (perícia, camada não-famosa, fora dos EUA).
- **Riscos de advertiser/compliance:** yellow icon é o risco estrutural do nicho [ALEGADO]; mitigação obrigatória = foco perícia (`09`), linguagem factual/passado, nada gráfico na thumb/primeiros 15s, self-certification honesta. Concorrência de laboratórios/players com marca (Othram Studios: 42,4k views/dia) e de canais maduros com catálogo (Red File: 171k views/dia).

## Queries mais estreitas (se REPROVA)

- `serial killer case files` — **TENTADA** (estreita): 0/3 gates; fome 3 canais. Próxima tentativa se revalidar.
- `lesser known serial killers` — opção não tomada nesta rodada.
- `unresolved serial killer documentary` — não rodada.
- `dna cold case serial killer` — não rodada.
- `serial killer interrogation files` — não rodada.
- Reconferência: repetir o brief em ~2–4 semanas (janela de fome 2–6 semanas) ou baixar `--small` para captar canais ainda menores.
