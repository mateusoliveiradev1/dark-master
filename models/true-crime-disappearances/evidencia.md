# Evidência — Desaparecimentos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "missing person documentary" --max 8` + cluster estreito `--cluster "vanished without a trace documentary" --max 8` + websearch (Data API via OAuth; autocomplete; Trends)
> Brief completo: `data/briefs/missing-person-documentary.md` · JSON: `data/briefs/missing-person-documentary.json`
> Scan 2 (cluster) não foi persistido em arquivo (sem `--out`); números reproduzidos abaixo a partir do output da sessão.

## Veredito: **REPROVA**

- Canais pequenos analisados: 8 + 8 | passam os 3 gates: 1 + 1 (meta ≥3)
- Fome do algoritmo (outlier ≥3×): 2 canais (scan 1) e 4 canais (scan 2) — sinal SIM nos dois
- Autocomplete: 78 termos (meta ≥15) | Trends: ALTA (22,5 recente vs 8,3 anterior)

**Leitura honesta:** o cruzamento tem demanda (Trends em alta, 78 autocompletes, outliers fortes e fome cross-canal), mas **não tem 3 canais pequenos passando os gates**. Os dois únicos canais que passam gate (Curious Lens e leeshi887) têm títulos de clickbait e sinais de produção automatizada — evidência fraca. Os canais de formato documentário que tracionam (DARK LOGS, Crime University, FBI Investigates, True Crime Consequence) são todos >45 dias: falham só o gate de idade, mas falham. Próximo passo: revalidar em ~30 dias ou estreitar mais (queries no fim).

## Scan 1 — brief "missing person documentary"

Cluster: 42 canais encontrados; 10 pequenos (≤200k subs) e ≤365d; 8 analisados.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Othram Studios | 58.800 | 208d | 15.261 | 42.397/dia | 011 | — |
| IT'S CRIMINAL | 21.800 | 286d | 825.850 | 18.237/dia | 011 | 581,6× — Brittney Wood (552.490, 06/07/2026) |
| DARK LOGS | 32.700 | 231d | 45.273 | 51.007/dia | 011 | — |
| Crime University | 6.830 | 91d | 210.236 | 26.518/dia | 011 | — |
| FBI Investigates | 68.300 | 315d | 859.329 | 80.765/dia | 011 | — |
| Red Evidence | 3.840 | 97d | 4.494 | 4.135/dia | 001 | — |
| Curious Lens | 803 | 44d | 22.297 | 11.348/dia | **111** | 317,1× — "Lost in Appalachia…" (282.544, 12/09/2026) |
| hfxwlyw | 2.600 | 57d | 1.151.700 | 108.902/dia | 011 | — |

Gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia (1=ok, 0=falha).

## Scan 2 — cluster estreito "vanished without a trace documentary"

44 canais encontrados; 15 pequenos e ≤365d; 8 analisados.

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| True Crime Retold | 39.100 | 335d | 986.127 | 15.276/dia | 011 | 6,4× — cruzeiro de lua de mel (637.830, 24/08/2026) |
| All Emergency | 14.500 | 223d | 19.628 | 21.178/dia | 011 | — |
| World's Strangest History | 3.830 | 173d | 3.131 | 3.168/dia | 001 | — |
| Prehistoria Hub | 6.710 | 123d | 418.131 | 15.613/dia | 011 | 10,5× — império antigo (137.310, 08/09/2026) — tema adjacente |
| True Crime Consequence | 22.200 | 64d | 156.263 | 47.010/dia | 011 | — |
| Shubh Kaayande | 1.310 | 238d | 160.759 | 1.442/dia | 011 | 16,5× — MH370 (40.501, 04/07/2026) — aviação |
| leeshi887 | 258 | 12d | 116.276 | 22.887/dia | **111** | 18,2× — celebrities missing (49.703, 17/09/2026) |
| ScaryVerse with Shabs | 8.250 | 154d | 583.661 | 10.995/dia | 011 | — |

## Outliers (janela de 2–6 semanas)

- IT'S CRIMINAL — 581,6× — 552.490 — Brittney Wood (repack de *Monster in the Shadows*) — 06/07/2026 — padrão: caso real + título de segredo; o canal repacka doc de TV (não copiar).
- IT'S CRIMINAL — 296,5× — 281.656 — "'She was pure evil' | My Mother the Monster" — 03/09/2026; 182,0× — 172.857 — *Monster in the Shadows* P2 — 13/07/2026; 97,3× — 92.449 — P3 — 20/07/2026 (scan de canal `@ItsCriminalChannel`).
- Curious Lens — 317,1× — 282.544 — "Lost in Appalachia for 3 Years…" — 12/09/2026 — padrão: desaparecimento + clickbait de choque; produção com cara de farm.
- leeshi887 — 18,2× — 49.703 — "celebrities who went missing and have never been found" — 17/09/2026 — padrão: lista de desaparecidos famosos em canal de 12 dias.
- Shubh Kaayande — 16,5× — 40.501 — MH370 — 04/07/2026 — tema adjacente (aviação).
- Prehistoria Hub — 10,5× — 137.310 — império antigo — 08/09/2026 — tema adjacente (história).
- True Crime Retold — 6,4× — 637.830 — "31Y/O Memphis Woman Vanished On Her Honeymoon Cruise…" — 24/08/2026 — padrão: idade + vanished + valor no título; uploads recentes convergem para crime internacional/romance (Dubai), não só desaparecimento.

## Fome do algoritmo (cluster cross-canal)

- Scan 1: 2 canais com outlier ≥3× (IT'S CRIMINAL, Curious Lens) → sinal SIM.
- Scan 2: 4 canais (True Crime Retold, Prehistoria Hub, Shubh Kaayande, leeshi887) → sinal SIM, mas 2 são temas adjacentes (história antiga e aviação); o sinal específico de "pessoa desaparecida" fica em 2–3 canais.
- Nenhum par de canais com outlier no mesmo caso exato; a fome é do formato (desaparecimento documentário), não de um caso específico.

## Demanda (autocomplete — top termos)

- missing person documentary
- missing person documentary uk
- missing person case documentary
- unsolved missing person cases documentary
- true crime missing person documentary
- missing person found alive documentary
- missing persons documentary
- missing person documentary latest
- missing person mystery documentary
- missing person documentary on youtube
- bbc missing person documentary
- missing person documentary part 1
- (78 termos no total; profundidade meta ≥15)

## Trends (YouTube 12m)

- Direção: ALTA (interesse recente 22,5 vs anterior 8,3) · Rising: não retornou queries em alta (vazio).

## Comentários (demanda explícita)

- Não coletado — `--comments` retornou `insufficientPermissions` (o escopo `youtube.force-ssl` não está no token; rodar `python scripts/yt_auth.py`). Tentativa registrada no vídeo `UKcJr5eJxe8` (True Crime Retold, 637.830 views).

## Fontes web (2+)

- https://rookcast.com/niches/true-crime — guia faceless 2026: demanda "muito alta", competição alta, RPM estimado $4–10 [ALEGADO], formatos 10–20 min, séries solved/unsolved.
- https://fluxnote.io/blog/true-crime-youtube-channel-guide-2026 — RPM estimado $5–12 [ALEGADO], watch time 12–22 min e sessão 35–55 min, estrutura de episódio, faixa 10–25 min.
- https://phantomline.xyz/blog/true-crime-channel-monetization-2026 — 30–60% dos uploads limitados/desmonetizados [ALEGADO]; enquadramento reportorial; Patreon como maior fatia em canais mid-tier.
- https://www.auditsocials.com/platforms/youtube-advertiser-friendly-guidelines — gatilhos de yellow icon (violência, linguagem), self-certification.
- https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline — timeline 2026: jan/2026 temas controversos não-gráficos elegíveis; ago/2026 documentário retratando morte monetizável; YPP dobra em 01/02/2027.
- https://deadline.com/2026/08/amy-bradley-is-missing-ample-true-crime-originals-youtube-1237018768 — produtora de true crime (*Amy Bradley Is Missing*) lançando canal no YouTube (ago/2026) — demanda de mercado pelo formato.
- https://longformstudio.app/articles/true-crime-youtube-channel — gatilho de imagem gráfica na thumb/primeiros 15s; flexibilização de 16/01/2026 (trecho via busca; fetch direto retornou 403).
- https://vidpros.com/best-true-crime-youtube-channels — panorama dos canais de true crime que performam em 2026.
- https://www.youtube.com/c/TheMissingEnigma/featured — canal real dedicado a casos de desaparecimento com "journalistic integrity".
- https://missingpeopleinamerica.org/ — ONG com canal de documentários de desaparecidos (10 docs) — fonte de casos e apelos.
- https://camviction.com/blog/category/missing-persons — site/canal "case files" de desaparecimentos (formato arquivo).

## Saturação e riscos observados

- O cruzamento "documentário de desaparecimento long-form EN" ainda admite canal novo: os canais que tracionam no scan são de arquivo/repack, não de pesquisa primária com voz própria; a lacuna é pesquisa original + POV.
- Saturação do lado do "repack de TV" é alta (IT'S CRIMINAL faz disso o motor) — e é justamente o que a política de conteúdo inautêntico pune; não é caminho.
- Gate-pass de baixa qualidade (Curious Lens, leeshi887) sugere que parte do "rompimento" recente é slop automatizado — cuidado ao ler outliers como validação de nicho.
- Riscos de advertiser: tema sensível; 30–60% de uploads limitados [ALEGADO]; imagem gráfica nos primeiros 15s/thumb = gatilho; casos com crianças e casos ativos com suspeito não acusado = risco extra.
- Convergência de formato verificada em 2 canais (IT'S CRIMINAL, True Crime Retold); os demais não verificados upload a upload (handle não localizado sem gastar quota extra).

## Queries mais estreitas (se REPROVA)

- vanished without a trace documentary (rodada — também REPROVA: 1 gate-pass, 4 canais com outlier)
- missing person case files (alternativa não rodada — quota)
- unsolved missing person cases documentary
- missing person case documentary
- missing person documentary uk (mercado UK/BBC)
- disappeared full episode (formato série)
