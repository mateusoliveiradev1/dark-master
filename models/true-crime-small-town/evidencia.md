# Evidência — Small town secrets

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "small town mystery documentary" --max 8` (principal) + `--cluster "small town crime documentary" --max 8` (estreita, única permitida) + `--channel` (3 canais) + `--trends` + websearch/webfetch (7 fontes).
> Brief completo: `data/briefs/small-town-mystery-documentary.md` · JSON: `data/briefs/small-town-mystery-documentary.json`
> Quota Data API usada na rodada: ~510 unidades (brief ~150 + cluster ~150 + 2 buscas de ID ~200 + videos.list 1 + channel scans ~10). Sem rodadas extras de `--query`/`--brief`.

## Veredito: **REPROVA**

- Canais pequenos analisados: 8 (principal) + 8 (estreita) | passam os 3 gates: **0** em cada (meta ≥3).
- Fome do algoritmo (outlier ≥3x): 2 canal(is) na principal — Psychic Visions (15,8x) e Traceory Files (5,8x). Sinal: **SIM** (janela 2–6 semanas aberta, mas nenhum passa os gates de canal).
- Autocomplete: **114** termos únicos (meta ≥15) — profundidade de perguntas ok.
- Trends: sem dados para o termo principal; "small town true crime" recente 25 vs anterior 0 → ALTA (base 0, sinal fraco); "small town secrets" falhou (HTTP 429).
- Leitura honesta: o tópico tem sinal de outlier e profundidade de busca, mas **não** tem canal novo (≤45d) rompendo o cruzamento formato×tópico na janela analisada. Não escalar; usar as queries estreitas no fim deste arquivo.

## Canais-evidência — busca principal (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates (idade/5p/vpd) | Outliers |
|---|---|---|---|---|---|---|
| Nostalgic Home Films | 12.600 | 313d | 282.174 | 14.580 | X / ok / ok | 0 (brief) |
| FBI Investigates | 68.300 | 315d | 859.329 | 80.765 | X / ok / ok | 0 |
| Golden Valley Films | 9.160 | 82d | 84.717 | 48.243 | X / ok / ok | 0 (brief); 3 via `--channel` |
| Untold Stories Official | 1.030 | 214d | 34.191 | 310 | X / ok / X | 0 |
| Psychic Visions | 975 | 97d | 14.637 | 1.178 | X / ok / ok | 15,8x |
| Haunted History | 6.670 | 221d | 12.048 | 6.593 | X / ok / ok | 0 |
| True Crime Web | 1.830 | 94d | 1.828 | 1.228 | X / X / ok | 0 |
| Traceory Files | 54 | 53d | 3.510 | 418 | X / X / X | 5,8x |

## Canais-evidência — busca estreita (`--cluster "small town crime documentary"`)

Analisados: 8 | passam os gates: 0. Novos canais desta rodada:

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates (idade/5p/vpd) | Outliers |
|---|---|---|---|---|---|---|
| Call SOLVED | 142 | 139d | 2.772 | 376 | X / X / X | 0 |
| Brittany Barry | 244 | 213d | 4.913 | 281 | X / X / X | 0 |
| Story 7ime | 11 | 135d | 2.315 | 61 | X / X / X | 0 |
| THE REAL CRIMINAL MIND | 1.070 | 155d | 1.083 | 184 | X / X / X | 0 |

(Repetidos com os mesmos números: FBI Investigates, Golden Valley Films, Haunted History, Traceory Files. Só Traceory mantém outlier ≥3x.)

## Outliers (janela de 2–6 semanas)

- **Psychic Visions — 15,8x — 12.910 views** — "Psychic Helps Solve Brutal Small Town Murder - The Betty Cornish Case Uncovered" — 2026-08-02 — 23:02 — padrão: psychic + small town murder (long).
- **Traceory Files — 5,8x — 1.550 views** — "The Circleville Letters: An Unsolved American Mystery #documentary #usa #usashorts #truestory" — 2026-09-07 — 0:46 — padrão: caso não resolvido + hashtag #documentary (short).
- Convergência do Traceory (`--channel`): 4,9x/1.301 (2026-09-10, "The Watcher"), 5,4x/1.430 (09-17, "Three Women Vanished"), 5,8x/1.545 (09-19, "Rabbit Costume Axe Attack"), 6,0x/1.595 (09-20, Amelia Earhart) — 5 uploads seguidos entre 4,9x e 6,0x.
- Golden Valley Films (`--channel`): 5,9x/50.789 (2026-09-13), 3,5x/30.161 (09-11), 3,1x/26.533 (09-12) — padrão: story/drama emocional com emoji, não true crime.
- Nostalgic Home Films (`--channel`): 7,8x/138.980 (2026-09-11, "SHE BECAME A NUN AT 16…"), 4,4x/79.314 (09-08), 4,1x/73.645 (09-16) — mesmo padrão drama/emoji.

## Fome do algoritmo (cluster cross-canal)

- Brief principal: **2 canais diferentes** com outlier ≥3x no mesmo tema (Psychic Visions 15,8x e Traceory Files 5,8x) → sinal SIM; janela 2–6 semanas aberta.
- Caso Betty Cornish rastreado em canais diferentes (busca exata + `videos.list`):
  - Psychic Visions — 12.910 views — 2026-08-02 — 23:02
  - Paranormal Lives — 931 views — 2026-08-06 — 23:02 (mesmo caso)
  - Against All Evidence — 9.540 views — 2026-02-11 — 48:00 (caso diferente, mesmo ângulo "psychic hammer murder")
- Leitura: o apetite atual do cruzamento pende ao ângulo **psychic/paranormal** em small town (não ao documentário sóbrio). O modelo cobre esse material apenas como [REPORTADO], nunca como prova.

## Demanda (autocomplete — top termos)

`--suggest` na busca principal: 114 termos únicos. Destaques:

- small town mystery
- small town documentary
- small town stories
- small town mystery documentary crime / killer / kidnap / lost / solved / scary / ghost
- small town mystery documentary in english (demanda internacional pelo mesmo conteúdo)

## Trends (YouTube 12m)

- "small town mystery documentary": **sem dados**.
- "small town true crime": recente 25 vs anterior 0 → **ALTA** (base 0, sinal fraco; sem queries em alta listadas).
- "small town secrets": falhou (HTTP 429 do Google; fallback sugerido pelo script).

## Comentários (demanda explícita)

Não coletado — `--comments` retornou `insufficientPermissions` nos vídeos `oC7SmdkizBA` (Circleville) e `xqMpB4Rt_-8` (Betty Cornish). Falta o escopo `youtube.force-ssl`: rodar `python scripts/yt_auth.py` e repetir.

## Fontes web

- https://shortsfast.com/blog/best-true-crime-youtube-channels-2026/ (2026-08-02) — mapa de 8 formatos de true crime em 2026; faceless funciona com evidência/estrutura; riscos de violência, reuso de footage, privacidade e alegações imprecisas.
- https://longformstudio.app/articles/true-crime-youtube-channel (2026-08-11) — playbook faceless; risco de yellow icon por formato (case deep-dive médio, cold case alto, forensic/court baixo); RPM reportado $6–9 para true crime não-gráfico [ALEGADO]; YPP sobe para 8.000h/20M em 01/02/2027; reencenação em 1ª pessoa de vítima falecida é banida desde jan/2024.
- https://latenights.live/how-the-new-youtube-rules-affect-documentary-clips-and-true- (2026-03-08) — update de jan/2026 permite monetização cheia para conteúdo sensível não-gráfico; táticas de edição (aviso, capítulos, fontes); splits de receita [ALEGADO].
- https://support.google.com/youtube/answer/6162278 — Advertiser-friendly content guidelines (OFICIAL): violência em contexto documental/jornalístico pode monetizar; foco em sangue/violência sem contexto não.
- https://support.google.com/youtube/answer/9725604 — atualizações de guidelines jan–set/2026 (OFICIAL), incl. temas controversos não-gráficos e carve-out de abuso infantil.
- https://www.tubefilter.com/2026/01/15/youtube-sensitive-content-ad-monetization-guidelines-update/ — cobertura do update de jan/2026.
- https://vidpros.com/best-true-crime-youtube-channels/ (2026-08-26) — panorama de canais e formatos (EWU, Rotten Mango, Lazy Masquerade etc.).
- Canais citados em listas de websearch (sem números usados como gate): youtube.com/@thelocalwhisper347, youtube.com/@HoosierColdCases.

## Saturação e riscos observados

- **Formato×tópico:** a SERP do termo é ocupada por canais de story/drama com emoji (Nostalgic Home Films, Golden Valley Films) usando keywords de "documentary"; o true crime sóbrio de cidade pequena aparece em canais mais velhos (FBI Investigates 315d, Haunted History 221d) ou minúsculos (Traceory Files, 54 subs).
- **Lacuna:** série documental sóbria, com arquivo/mapa e tom contido não foi observada passando os 3 gates na janela. O piloto deve testar exatamente esse cruzamento.
- **Riscos de advertiser/compliance:** violência na thumb e nos primeiros 15s é gatilho próprio de yellow icon (OFICIAL, ver fontes); conteúdo focado em abuso infantil permanece inelegível mesmo não-gráfico (OFICIAL); sensitive events; reuso de footage de terceiros (prática comum do nicho) adiciona risco de review; difamação de pessoas vivas; inautenticidade se faltar pesquisa primária por vídeo.

## Queries mais estreitas (se REPROVA — próxima rodada, não executadas)

- small town cold case documentary
- small town disappearance documentary
- small town murder files
- county road mystery documentary
- unsolved small town secrets
