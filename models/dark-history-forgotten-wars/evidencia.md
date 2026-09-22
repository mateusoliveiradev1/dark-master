# Evidência — Guerras esquecidas

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "forgotten war documentary" --max 8` + (após reprovar os gates) `python scripts/niche_scan.py --cluster "military history documentary" --max 8` + websearch
> Brief completo: `data/briefs/forgotten-war-documentary.md` · JSON: `data/briefs/forgotten-war-documentary.json`
> A saída bruta do cluster não foi salva em arquivo (execução manual); é reproduzível pelo comando acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: 16 únicos (8 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3) — nenhum dos dois scans aprovou
- Fome do algoritmo (outlier ≥3×): **3 canais no brief + 1 no cluster** — sinal: **sim** (o próprio scan marcou ">=2 canais diferentes com outlier no mesmo tema → janela de 2–6 semanas aberta")
- Autocomplete: 106 termos (meta ≥15) | Trends: **ALTA** (recente 42,25 vs anterior 0,00)

**Leitura honesta:** o critério rígido — ≥3 canais ≤45d passando os 3 gates — **não foi atingido em nenhum dos dois scans; nos gates, é REPROVA**. O que sustenta o PARCIAL é a taxonomia do `models/README.md`: fome cross-canal real (3 canais com outlier ≥3× no mesmo enquadramento "forgotten", incluindo um de 146,4× e um de 110,8×) e emergentes ≤90d com 2/3 gates (Geo World On Map 81d; Vinu Baloliya 25d; Atlas of Civilizations 68d no cluster). O gargalo é idade/primeiros vídeos: os canais com tração têm 98–355 dias. Revalidar em 2–4 semanas: se um canal ≤45d cruzar os 3 gates, sobe para PASSA; se a fome esfriar sem emergente novo, cai para REPROVA.

## Canais-evidência — scan 1: `--brief "forgotten war documentary"` (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| The Forgotten Empire | 9.460 | 317d | 4.477 | 5.684 | 001 | 110,8× — 184.758 — 2026-08-23 |
| Sahel Chronicles | 25.000 | 316d | 85.068 | 7.898 | 011 | 3,7× — 47.665 — 2026-08-28 |
| Geo World On Map | 1.790 | 81d | 13.870 | 25.110 | 011 (emergente) | — |
| Vinu Baloliya | 588 | 25d | 7.611 | 18.960 | 101 (emergente) | — |
| Remnants of Time | 993 | 154d | 1.839 | 181 | 000 | 146,4× — 16.245 — 2026-07-29 |
| Historical Camp | 409 | 76d | 331 | 5.774 | 001 | — |
| Mundos Reimaginados | 106.000 | 241d | 787.162 | 41.623 | 011 | — |
| History Without Fluff | 870 | 278d | 1.855 | 491 | 000 | — |

> Scan 1: 33 canais encontrados, 14 pequenos (≤200k subs e ≤365d), 8 analisados por quota — **0/8 passaram**. Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). Emergentes (≤90d + 2/3): Geo World On Map, Vinu Baloliya.

## Canais-evidência — scan 2: `--cluster "military history documentary"` (mesma ordem de gates)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| History Paradox | 92.300 | 296d | 839.987 | 2.039.017 | 011 | — |
| Map Warden | 12.400 | 98d | 9.950.237 | 102.871 | 011 | 29,6× — 4.572.087 — 2026-07-27 |
| MaPolitik | 43.600 | 352d | 1.346.846 | 94.094 | 011 | — |
| Events Untold | 30.500 | 272d | 191.914 | 938.362 | 011 | — |
| Military Studio | 6.390 | 139d | 2.278 | 5.978 | 001 | — |
| Bannerlore | 48.900 | 355d | 6.540 | 39.092 | 001 | — |
| Atlas of Civilizations | 21.900 | 68d | 15.197 | 74.113 | 011 (emergente) | — |
| Battlefield History | 12.700 | 123d | 390.142 | 162.446 | 011 | — |

> Scan 2: 39 canais encontrados, 9 pequenos (≤200k subs e ≤365d), 8 analisados por quota — **0/8 passaram**. Emergente: Atlas of Civilizations; fome: 1 canal (Map Warden).

## Outliers (janela de 2–6 semanas)

- **Remnants of Time** — 146,4× — 16.245 views — "The War of 1812: The Forgotten Fight Between America and Britain" — 2026-07-29 — padrão: guerra anglo-americana + enquadramento "The Forgotten Fight"; canal de 993 subs (mediana 111), prova que o enquadramento funciona até sem base de inscritos.
- **The Forgotten Empire** — 110,8× — 184.758 views — "(1899–1913) THE AMERICAN WAR IN THE PHILIPPINES: The Forgotten Conflict of 1899–1913" — 2026-08-23 — padrão: intervalo de anos no título + guerra fora do cânone + "Forgotten Conflict".
- **Map Warden** — 29,6× — 4.572.087 views — "The Falklands: A 300-Year Fight #geography #learn #history" — 2026-07-27 — padrão map-based: disputa de fronteira narrada sobre mapa, hashtags de geography/learn/history.
- **Sahel Chronicles** — 3,7× — 47.665 views — "The Forgotten War That Built Terror In West Africa" — 2026-08-28 — padrão: "Forgotten War" + consequência que chega ao presente.

## Fome do algoritmo (cluster cross-canal)

**Sim, no scan 1.** Três canais diferentes com outlier no **mesmo enquadramento** ("The Forgotten…") na janela de jul–ago/2026: Remnants of Time (29/07), The Forgotten Empire (23/08) e Sahel Chronicles (28/08) — o scan marcou a janela de 2–6 semanas como aberta. No scan 2, a fome aparece em outro recorte: Map Warden (29,6×, 4,57M views, map-based + Falklands, 27/07). Convergência de formato nos dois scans: narrativa de conflito histórico sobre mapa, título com "forgotten" e foco em guerra fora do cânone.

## Demanda (autocomplete — top termos)

106 termos únicos (meta ≥15). Destaques relevantes (filtrados do ruído): `the forgotten war documentary`, `forgotten war documentary bbc`, `forgotten war documentary american experience`, `forgotten war documentary history`, `forgotten war documentary english`, `forgotten war documentary real stories`, `forgotten war documentary ww2`, `forgotten war documentary ww1`, `forgotten war documentary uk`, `forgotten war documentary korean`, `forgotten war documentary japanese`, `forgotten history`. Leitura: demanda de biblioteca ("documentary full", "episode 1", "series") e por região/guerra (uk, korean, japanese, ww1, ww2).

## Trends (YouTube 12m)

- Direção: **ALTA** (média recente 42,25 vs anterior 0,00) · Rising: nenhuma query listada pelo script.
- Leitura: termo em ascensão, mas o script não lista queries em alta — validar de novo na revalidação (o ALTA com base zero indica salto de interesse recente, não volume consolidado).

## Comentários (demanda explícita)

Não coletado — o `--comments` exige `force-ssl` no `yt_auth` e não foi rodado nesta coleta. Repetir depois de `python scripts/yt_auth.py` em um vídeo dos canais-evidência ("which forgotten war should we cover next?" é a pergunta a ler).

## Fontes web (2+)

- https://faceless.my/niches/faceless-history-channel — história como nicho faceless provado; RPM de história $5–15 [ALEGADO]; formatos que performam (battle breakdown, timeline explainer, documentário 20–45 min); gap de história não-ocidental; produção com acervo público (Wikimedia, LoC); riscos de copyright de imagem e precisão histórica.
- https://reelsmakerai.com/blog/how-much-do-faceless-youtube-channels-make — History & Mystery $8–18 RPM, saturação baixa; "History" listado como nicho de alta margem [ALEGADO].
- https://www.doodrio.com/blog/faceless-youtube-channel-earnings-2026 — History/Documentary $5–12 RPM [ALEGADO] — piso conservador da classe.
- https://www.youtube.com/@historyonmaps — History on Maps: 412k subs, formato "Every Day" com mapas animados (Korea 412k views; WWI 346k) — valida o formato map-based e mostra o concorrente consolidado do recorte genérico.
- https://www.youtube.com/@forgottenhistorychannel/videos — FORGOTTEN HISTORY: 916k subs, uploads semanais, enquadramento "forgotten" com demanda alta (470k–580k views em vídeos recentes) — formato com apresentadores (não é o do modelo; mostra a demanda do ângulo).
- https://www.youtube.com/@HistoryinMotion3 — History in Motion: 44,8k subs, animação de fotos históricas com IA ("forgotten stories"; vídeos de 100k–316k) — valida visual histórico animado em 2026.
- https://www.youtube.com/channel/UCZVMeD8GS1UanIvVoxWdhrw — Battlefront History: canal criado em 2026 dedicado a "forgotten conflicts" (War of 1812; 2 vídeos, 12 views) — evidência de entrada nova no recorte, ainda sem tração.
- https://www.youtube.com/channel/UC3fOzMSxcmCXZLmAM9vy1IQ — War Stories (History Hit): 1,29M subs, 907 vídeos — incumbente de milhares de views por episódio; não competir de frente no doc de TV, e sim no "conflito esquecido" narrativo.
- https://www.youtube.com/watch?v=BhsGaR4FSXU — "40 Forgotten Wars and Conflicts America Fought That Schools…" (fev/2026) — demanda do tópico em long-form de lista.
- https://support.google.com/youtube/answer/6162278 — política oficial de advertiser-friendly: contexto documental/educacional pesa para violência; foco em sangue/violência sem contexto = limited/no ads.
- https://support.google.com/youtube/answer/9725604 — atualizações 2026: ago/2026 define monetização de "depictions of death" em conteúdo educacional/documental; set/2026 mexe em violência gráfica de jogos — documentário tem tratamento próprio, mas contexto é obrigatório.
- https://apnews.com/article/youtube-monetization-update-policy-controversial-issues-545e27e27e26e0baefb937c86620b676 — jan/2026: YouTube relaxa monetização de temas sensíveis não gráficos (dramatização/cobertura sem descrição gráfica) — espaço para documentário histórico sóbrio.
- https://www.bbc.com/mediacentre/2026/bbc-world-service-witness-history-ai-animated-video — BBC World Service anunciou versão com vídeo animado por IA para o Witness History (mar/2026) — mainstream validando história animada; aumenta o padrão de qualidade esperado.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalva. O recorte "map-based military history" tem incumbentes (History on Maps 412k; War Stories 1,29M; Kings and Generals) — não competir no "Every Day" genérico nem no doc comprado de TV. O espaço aberto é o cruzamento **"conflito esquecido + documentário narrativo 12–22 min + peça de arquivo própria"**: os 3 outliers de jul–ago/2026 usam o enquadramento "forgotten" e canais novos do tema têm pouquíssima tração (Battlefront History, 2 vídeos) — janela real, mas nenhum canal ≤45d passou os gates ainda.
- **Riscos de advertiser/compliance:** violência/mortes exigem contexto documental; imagem gráfica no thumbnail ou nos primeiros 15s derruba para limited ads; conflitos atuais ficam fora (política de eventos sensíveis cita a Ucrânia); ufanismo/glorificação atrai denúncia e quebra a promessa do canal; precisão histórica é o ativo (público corrige em público); imagens só de domínio público/licenciado; 1 peça de pesquisa primária por vídeo contra a política de conteúdo inautêntico.

## Queries mais estreitas (revalidação em 2–4 semanas)

- **Executadas:** `forgotten war documentary` (brief; 0/8 gates, fome 3, emergentes 2) e `military history documentary` (cluster; 0/8 gates, fome 1, emergente 1).
- **Próxima rodada:** `python scripts/niche_scan.py --brief "forgotten war documentary" --age 45` e/ou `--cluster "forgotten war documentary" --age 45 --window 45` para testar o gate de idade; se continuar sem canal ≤45d, estreitar por subnicho com `--query "philippine american war documentary"` e `--query "war of 1812 documentary"` (os dois enquadramentos com outlier comprovado).
