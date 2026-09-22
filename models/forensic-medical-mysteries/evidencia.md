# Evidência — Mistérios médicos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "medical mystery documentary" --max 8` + `python scripts/niche_scan.py --cluster "medical case documentary" --max 8` + verificação de canais (Data API, metadados/uploads) + websearch + tentativa de `--comments`
> Brief completo: `data/briefs/medical-mystery-documentary.md` · JSON: `data/briefs/medical-mystery-documentary.json`
> Custo: ~300 unidades de quota (2 scans) + ~15 em verificação de canais. `--trends` retornou HTTP 429 em 3 tentativas (brief + 2 retries) — não coletado.

## Veredito: **REPROVA**

- Canais pequenos analisados: **14** (6 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **2 canais, em escala trivial** (Body Mechanics Lab 6,0× = 60 views; TIME HISTORY FILES 3,6× = 1.223 views) — **não é fome utilizável**
- Emergentes (≤90d + 2/3 gates): **3** (Blue Tundra 52d, Declassified Real 88d, REAL CRIME VAULT 70d) — mas a verificação de canais mostrou que **2 dos 3 estão fora do cruzamento** (canal de filmes licenciados; canal de shorts de sobrevivência)
- Autocomplete: **99 termos** (meta ≥15) | Trends: sem dados (429)

**Leitura honesta:** a demanda de busca existe (99 termos de autocomplete; threads no Reddit pedindo exatamente "YouTube channels about medical mysteries"), mas **nenhum canal dedicado pequeno foi encontrado rompendo no cruzamento em nenhum dos dois scans**. O termo `medical mystery documentary` tem **intenção mista**: retorna ficção (clipes de House M.D., filmes licenciados) e catálogo de streaming (Netflix/Amazon), além de conteúdo real. Os canais que aparecem e crescem são generalistas ("real stories that feel impossible", compilações de TV). O espaço tem marcas de TV (Mystery Diagnosis, 2005–2011) e um player dominante de formato próprio (Chubbyemu, ~3,9–4,0M subs em ago–set/2026), mas a lacuna do documentário faceless dedicado **não está comprovada com canal jovem**. Não é PASSA nem PARCIAL por evidência de canal; é REPROVA com caminho de revalidação claro (abaixo).

## Busca 1 — brief `medical mystery documentary` (--max 8)

30 canais encontrados · 6 pequenos (≤365d) analisados. **0 passam os 3 gates.**

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Blue Tundra | 16.900 | 52d | 201.245 | 146.283 | 011 | 0 — **EMERGENTE** |
| Vanta Meraki | 29 | 176d | 119.007 | 892 | 010 | 0 |
| NOFiCTiON | 16.000 | 152d | 113.189 | 132.512 | 011 | 0 |
| Declassified Real | 748 | 88d | 260.292 | 57.590 | 011 | 0 — **EMERGENTE** |
| Do Geese See God | 9.910 | 227d | 17.330 | 1.129 | 011 | 0 |
| Instant Medical | 51.700 | 322d | 8.932 | 26.069 | 001 | 0 |

> Gates na ordem (idade≤45d, 5 primeiros≥10k, views/dia≥1k). "011" = só a idade falha.

## Busca 2 — cluster `medical case documentary` (única segunda busca permitida)

30 canais encontrados · 8 pequenos (≤365d) analisados. **0 passam os 3 gates.** 2 outliers (micro).

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| REAL CRIME VAULT | 1.240 | 70d | 41.957 | 4.465 | 011 | 0 — **EMERGENTE** |
| Body Mechanics Lab | 3 | 84d | 80 | 4 | 000 | **6,0× — 60 views — 2026-07-29** |
| Zalfar Files | 118 | 145d | 2.825 | 174 | 000 | 0 |
| Viral Insight | 946 | 141d | 3.568 | 677 | 000 | 0 |
| TIME HISTORY FILES | 40 | 60d | 3.026 | 220 | 000 | **3,6× — 1.223 views — 2026-08-09** |
| Raja Gupta | 21 | 88d | 1.778 | 26 | 000 | 0 |
| Global Community | 66 | 56d | 6.293 | 591 | 000 | 0 |
| Traceory Files | 54 | 53d | 3.510 | 418 | 000 | 0 |

## Verificação de canais (o que os candidatos realmente são)

Checagem de metadados e últimos uploads via Data API (não é nova busca):

| Canal | Handle | O que é (descrição/últimos uploads) |
|---|---|---|
| Blue Tundra | @bluetundra-film (AR; 22 vídeos; 7.606.728 views) | **Canal de filmes licenciados** em inglês (drama/thriller). Uploads: "This Movie Will Shock You! \| LOCKED AWAY \| Drama Thriller" (17/09), "Dangerous Traps Lead Detectives Closer to a Shocking Truth" (20/09). Fora do cruzamento. |
| Vanta Meraki | @thihiepnguyen-o8x (29 subs; 7 vídeos; 157.011 views) | **Clipes de House M.D.** ("House M.D. S02E09..."). Ficção — explica os 119k dos 5 primeiros. Fora do cruzamento. |
| NOFiCTiON | @nofiction.2d (US; 12 vídeos; 20.141.802 views) | Generalista de "real events that feel impossible" (animais, sobrevivência, mortes estranhas). **2 Shorts de mistério médico**: "He Was Always Drunk But Never Drank #autobrewerysyndrome" (17/07/2026 — **41.186 views, 848 likes**) e "She Couldn't Explain The Smell #medicalmystery" (12/07/2026 — **20.385 views, 497 likes**; trimetilaminúria). Sinal de tópico em Shorts, não prova de canal dedicado; os ratios vs mediana do canal (36.732) são 1,1× e 0,55×. |
| Declassified Real | @declassifiedreal (IN; 163 vídeos; 5.067.896 views) | Shorts diários de sobrevivência ("They Lifted the SUV Off His Chest"); descrição cita "extraordinary medical cases" entre os temas. Alta cadência, não é documentário médico. |
| Do Geese See God | @dogeeseseegodpod (US; 70 vídeos; 256.315 views) | Clipes de podcast (bizarro/folclore); episódio "They Called Her a 'Chemical Weapon.' No One Could Explain It." (15/09/2026) = mistério médico. |
| Instant Medical | @instantmedicall (IN; 89 vídeos; 8.394.087 views) | História médica sombria em long: série "The Experimental Trap" (Unit 731), Mengele (Ep. 2), "How Did Ireland Lose 1 Million People?". Adjacente ao cruzamento (dark medical), origem IN, cadência irregular. |
| REAL CRIME VAULT | — (cluster; sem metadados coletados) | Emergente do cluster (70d; 41.957; 4.465/dia); nome sugere crime — cruzamento com o tema médico **não verificado**. |

## Outliers (janela de 2–6 semanas)

- **Body Mechanics Lab** — **6,0×** — **60 views** — "He Drank Homemade Moonshine... Then He Went Blind \| True Med" — 2026-07-29 — ratio alto, escala irrelevante (canal de 3 subs, mediana 10).
- **TIME HISTORY FILES** — **3,6×** — **1.223 views** — \#shorts sobre Lindsay Clancy/psicose pós-parto — 2026-08-09 — segundo micro-outlier do cluster.
- Sem outros outliers ≥3× na coleta (brief: 0 em 6 canais).
- **Não-outliers com valor de sinal:** os dois Shorts médicos do NOFiCTiON (41,2k e 20,4k views) mostram que tópicos de mistério médico (auto-brewery, trimetilaminúria) performam dentro de canal generalista — mas não são outliers vs a própria mediana.

## Fome do algoritmo (cluster cross-canal)

**Não.** O script marcou "SINAL: sim" por 2 canais com outlier ≥3×, mas ambos estão em escala trivial (60 e 1.223 views). Não há 2 canais diferentes com outlier **utilizável** no mesmo tema na janela de 90 dias.

## Demanda (autocomplete — 99 termos)

Termos relevantes: `medical mystery documentary`, `medical mysteries`, `medical mysteries solved`, `medical mystery documentary full episodes`, `medical mystery documentary real stories`, `medical mystery documentary series`, `medical mystery documentary crime investigation`, `medical mystery documentary youtube`.
Contaminação (intenção mista): `black metal`, `black hole`, `amazon prime`, `netflix`, `david attenborough` — o termo puxa ficção/streaming, não só documentário real.
Leitura: profundidade alta (99 ≥ 15) e cauda longa pede **série/full episodes** — bom para long-form, mas exige desambiguar o posicionamento (caso real documentado + fontes).

## Trends (YouTube 12m)

- `medical mystery documentary` e `medical mystery`: **HTTP 429 nas 3 tentativas** (rate limit do Google na coleta). Pendente — repetir na próxima rodada. Fallback usado: autocomplete (99 termos).

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` nos 2 vídeos testados (escopo `youtube.force-ssl` ausente no `yt_auth.py`; rodar `python scripts/yt_auth.py` uma vez). Sinal indireto (Reddit): thread "I'm really into the whole medical mystery thing. If anyone has suggestions on similar pods or YouTube channels please lmk" com recomendações de Chubbyemu, Sawbones, Dark History (Bailey Sarian), `Diagnosis` (Netflix) e `Medical Mysteries` (MrBallen) — demanda por conteúdo, mas boa parte do público já é servida por podcast/TV/streaming.

## Fontes web (2+)

- https://en.wikipedia.org/wiki/Mystery_Diagnosis — formato canônico do subnicho (docudrama, 2+ pacientes/episódio, 43 min, Discovery Health/OWN 2005–2011); também documenta o risco de simplificação/inexatidão pela estrutura dramática.
- https://www.reddit.com/r/mrballen/comments/1kov1g5/im_really_into_the_whole_medical_mystery_thing_if/ — demanda explícita por canais de mistério médico; lista do que o público já consome.
- https://www.reddit.com/r/tipofmytongue/comments/1npkmjp/ — Chubbyemu identificado como o formato "pessoa fez X, isso aconteceu" (case study storytelling).
- https://socialblade.com/youtube/handle/chubbyemu — Chubbyemu ~3,71M subs em jun/2026, 436–438 vídeos, ~612M views acumulados.
- https://hypeauditor.com/youtube/UCKOvOaJv4GK-oDqx-sj7VVg/ — Chubbyemu ~4,0M subs em set/2026; descrição oficial: "These videos are not medical advice" (benchmark de disclaimer no nicho).
- https://outlierkit.com/channel/chubbyemu — "Medical Case Study Storytelling"; média ~1,5M views/vídeo; receita estimada $5–16k/mês [ALEGADO]; upload de baixa frequência.
- https://fluxnote.io/guides/faceless-youtube-health-wellness-niche-2026 — faceless health/wellness 2026: RPM $8–15 [ALEGADO]; YMYL; disclaimer obrigatório em todo vídeo; formato case study performa; evitar claims e temas que contrariem consenso.
- https://support.google.com/youtube/answer/13813322 — política de desinformação médica: proibição + exceção para contexto educacional/documentário/científico (EDSA).
- https://support.google.com/youtube/answer/1311392 — políticas de monetização: "AI personas related to sensitive topics" (ex.: "AI doctor" dando diagnóstico/conselho) **não monetizam**.
- https://healths.live/creators-and-controversy-how-youtube-s-monetization-shift-af — jan/2026: monetização cheia para conteúdo não gráfico de temas sensíveis; exigências de evidência, disclosure e proibição de claims médicos.
- https://www.youtube.com/watch?v=CmyKsgfZQrI ("2 Hours Of Medical Mysteries That Stumped Doctors" — Real Responders) — formato compilação long de casos médicos com audiência evergreen.
- https://outlierkit.com/resources/faceless-youtube-channels/ — classes de CPM faceless 2026 [ALEGADO].
- https://blog.kliptory.com/how-to-make-faceless-youtube-documentaries/ — formato documentário faceless; acervos públicos (Library of Congress, Internet Archive, Wikimedia).

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Não comprovado. O termo é disputado por ficção (House M.D.), filmes licenciados, streaming e compilações de TV; nenhum canal pequeno dedicado aparece rompendo. Sinais a favor (não aprovação): autocomplete profundo (99), lacuna de catálogo (Mystery Diagnosis saiu do ar em 2011 e não está em streaming), demanda comunitária explícita e tópicos médicos performando em Shorts de canais generalistas.
- **Riscos de advertiser/compliance:** medical misinformation policy (contexto EDSA é o escudo — fontes e disclaimer obrigatórios); **AI persona de médico proibida de monetizar** (nunca narrar como especialista); gore/procedimento em thumb/first frames = limited ads; YMYL exige citação de fontes; sensacionalismo com paciente derruba confiança e pode atrair reclassificação.
- **Recomendação:** **não lançar** como canal dedicado sem revalidação; se lançar como teste, tratar como piloto barato (FINO) com queries de recheque agendadas.

## Revalidação (2–4 semanas)

- **Queries mais estreitas (não executadas — quota):** `mystery diagnosis documentary`, `bizarre medical cases documentary`, `rare disease documentary`, `medical case files documentary`, `medical mysteries solved documentary`.
- **Watchlist:** Declassified Real (88d, 2/3 gates — formato fora do cruzamento), REAL CRIME VAULT (70d, 2/3 — verificar tema), NOFiCTiON (tópico médico em Shorts; medir se vira série), Instant Medical (322d, dark medical, 26k views/dia), Do Geese See God (episódio médico 15/09).
- **Critério de aprovação:** ≥3 canais pequenos passando os 3 gates no cruzamento OU o tier PARCIAL do README (fome ≥2 canais **utilizável** ou múltiplos emergentes ≤90d dentro do cruzamento).
- Repetir `--trends "medical mystery documentary"` (429 na coleta) e rodar `python scripts/yt_auth.py` para habilitar `--comments`.
