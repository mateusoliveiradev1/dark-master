# Evidência — Lendas urbanas

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "urban legend documentary" --max 8` + segunda busca `python scripts/niche_scan.py --cluster "folklore documentary"` + autocomplete + websearch + verificação de convergência (últimos uploads de canais com ID conhecido)
> Brief completo: `data/briefs/urban-legend-documentary.md` · JSON: `data/briefs/urban-legend-documentary.json` (o cluster não é persistido pelo script; é reproduzível pelo comando acima)

## Veredito: **PARCIAL**

- Canais pequenos analisados: **16 únicos** (8 no brief + 8 no cluster; sem repetição) | passam os 3 gates: **1** (meta ≥3) — só `Otis Boone`
- Emergentes (≤90d + 2/3 gates): **2** — Magic Toon Nepal (70d) e Myth After Dark (36d)
- Fome do algoritmo (outlier ≥3×): **10 canais únicos** (5 no brief + 5 no cluster) — sinal: **sim**
- Autocomplete: **85 termos** (meta ≥15; com ruído alto do filme `Urban Legend` de 1998) | Trends: **não coletado** (HTTP 429 em 3 tentativas: brief + 2 retries)

**Leitura honesta:** o brief `urban legend documentary` **REPROVOU nos gates** (0/3) — o seed é guarda-chuva e puxa o filme de 1998 no autocomplete, além de canais de horror asiático fora do EN. A segunda busca, `folklore documentary`, **melhorou o cruzamento**: 1 canal passando os 3 gates (`Otis Boone`, 35d, 7,1k subs, 37.968 views/dia — outlier de 4,1× há 9 dias), 2 emergentes ≤90d e 5 canais em fome, dois deles com flares extremos (`Myth After Dark`, 162× em 36d, e `Magic Toon Nepal`, 267,9× em 70d). Pela régua de modelo (`models/README.md`: PARCIAL = <3 gates, mas com fome ≥2 canais e/ou emergentes), fica **PARCIAL** — não PASSA (falta o terceiro canal cruzando os gates), não REPROVA (a fome é ampla e fresca). O gargalo não é demanda: **todos os 8 canais do brief passam 2/3 gates** (só falham idade, 121–282d) e a janela de entrantes ≤45d existe em `folklore documentary`. O cruzamento com cara de canal é **lenda específica + região/cultura + arquivo** (não "urban legend" genérico).

## Canais-evidência (gates: idade≤45d · 5 primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| Paint Maniac (brief) | 41.600 | 121d | 1.494.789 | 35.570 | 011 | 3,1× — 658.971 — "The Disturbing Audio Recordings Explained" — 2026-08-06 |
| Yogiesh (brief) | 13.600 | 199d | 839.449 | 12.983 | 011 | 8,3× — 463.621 — "Teke Teke \| Japan-oda Bayangaramaana Ghost Legend" — 2026-08-02 |
| RickFrame (brief) | 14.300 | 282d | 404.193 | 17.340 | 011 | 19,6× — 232.992 — "Film Horor Jepang Ini Membuat Saya Mimpi Buruk" — 2026-07-12 |
| The Dark Logs (brief) | 5.150 | 263d | 204.627 | 3.145 | 011 | 3,5× — 170.521 — "Sinister Secrets of New Orleans: Ghosts, Voodoo & Haunted Streets" — 2026-06-30 |
| Horror Glimpse (brief) | 18.600 | 213d | 886.485 | 22.826 | 011 | — |
| Nightmare Tv (brief) | 1.500 | 149d | 58.558 | 1.370 | 011 | 15,8× — 72.941 — "FILE 1 \| Japanese Horror Mocumentary…" — 2026-07-14 |
| Sleepy Mystery Channel (brief) | 12.800 | 202d | 190.125 | 7.910 | 011 | — |
| DARK LOGS (brief) | 32.700 | 231d | 45.276 | 51.007 | 011 | — |
| Magic Toon Nepal (cluster) | 1.230 | **70d** | 357.536 | 5.898 | 011 | 267,9× — 342.973 — "मजिपा लाखे: The Demon Among The Gods \| Nepali Mythology Story" — 2026-07-22 |
| **Otis Boone (cluster)** | **7.120** | **35d** | **475.683** | **37.968** | **111** | 4,1× — 111.059 — "I'm From Appalachia. Here's the Truth About Bigfoot." — 2026-09-13 |
| Myth After Dark (cluster) | 190 | **36d** | 6.777 | 3.354 | 101 | 162,0× — 99.324 — "Aswang: The Terrifying Shapeshifter of Philippine Folklore" — 2026-09-06 |
| Euphy Empire of stories (cluster) | 188 | 65d | 5.240 | 557 | 000 | 14,2× — 16.764 — "The Fisherman And The Misty River" — 2026-08-19 |
| Seven Sisters (cluster) | 22.000 | 154d | 9.943 | 14.531 | 001 | — |
| Hollow Hills (cluster) | 4.940 | 116d | 175.085 | 2.520 | 011 | — |
| guythatlikeshistory (cluster) | 123 | 46d | 3.410 | 73 | 000 | 5,9× — 2.571 — "Following Folkscapes: Corpse Roads & British Folklore" — 2026-08-06 |
| Nature's Armory (cluster) | 6.590 | 206d | 1.991 | 4.731 | 001 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). Brief: 41 canais encontrados, 13 pequenos ≤365d, 8 analisados (quota). Cluster: 45 encontrados, 8 pequenos ≤365d, 8 analisados. IDs dos canais do brief no JSON persistido; o cluster não é persistido.
> Nota de idioma: Yogiesh (indiano), RickFrame (indonésio) e Magic Toon Nepal (nepalês) mostram a demanda internacional do tema; a versão-alvo do modelo é **EN**.
> Nota metodológica: o scan busca os **15 uploads mais recentes** e trata os 5 mais antigos desse lote como "5 primeiros" — para canais com ≤15 uploads é o primeiro lote real; nos demais, é aproximação do lote inicial. Para os canais jovens do cluster (35d, 36d, 70d) a leitura é confiável; para os canais de 121–282d do brief, os gates de idade já reprovam de qualquer forma.

## Outliers (janela de 2–6 semanas)

- **Otis Boone** — **4,1×** — 111.059 views — "I'm From Appalachia. Here's the Truth About Bigfoot." — 2026-09-13 (9 dias) — padrão: **primeira pessoa regional + "a verdade sobre"**, no único canal que passa os 3 gates; é o outlier mais fresco e mais limpo da coleta.
- **Myth After Dark** — **162,0×** — 99.324 views — "Aswang: The Terrifying Shapeshifter of Philippine Folklore" — 2026-09-06 (16 dias) — padrão: **uma lenda por vídeo, título `Nome: o adjetivo da cultura`**, num canal de 190 subs e 36 dias; ratio inflado pela mediana de 613, mas o viewport absoluto é real.
- **Magic Toon Nepal** — 267,9× — 342.973 views — "मजिपा लाखे: The Demon Among The Gods" — 2026-07-22 — padrão: mitologia narrada como história (nepalês); maior viewport do cluster.
- **Paint Maniac** — 3,1× — 658.971 views — "The Disturbing Audio Recordings Explained" — 2026-08-06 — maior viewport absoluto da coleta; crossing de **folclore de internet** ("internet horrors explicados", 8–9 min).
- **Yogiesh** — 8,3× — 463.621 views — Teke Teke (lenda japonesa, em indiano) — 2026-08-02 — mostra a lenda urbana japonesa funcionando como conteúdo de massa fora do EN.
- **RickFrame** — 19,6× — 232.992 views — horror japonês (indonésio) — 2026-07-12.
- **The Dark Logs** — 3,5× — 170.521 views — "Sinister Secrets of New Orleans: Ghosts, Voodoo & Haunted Streets" — 2026-06-30 — padrão: **lugar + história documentada**, no formato que o canal repete (ver convergência).
- **Nightmare Tv** — 15,8× — 72.941 views — mockumentary de horror japonês (found footage) — 2026-07-14 — recorte de ficção; fora do ângulo editorial do modelo.
- **Euphy Empire of stories** — 14,2× — 16.764 views — contos africanos em formato de história — 2026-08-19.
- **guythatlikeshistory** — 5,9× — 2.571 views — "Corpse Roads & British Folklore" — 2026-08-06 — viewport minúsculo, mas o tema (folclore britânico documental) é exatamente o subnicho regional do modelo.

## Fome do algoritmo (cluster cross-canal)

**Sim — 5 canais diferentes com outlier ≥3× no cluster `folklore documentary`, em 4 quadrantes:**

1. **Regional EN:** Otis Boone (4,1×, Appalachia/Bigfoot, set/2026) — o mais fresco; `guythatlikeshistory` (5,9×, corpse roads britânicas, ago/2026) no mesmo quadrante.
2. **Lenda internacional com contexto cultural:** Myth After Dark (162×, Aswang filipino, set/2026); Magic Toon Nepal (267,9×, mitologia nepalesa, jul/2026).
3. **Storytelling de tradição oral:** Euphy Empire of stories (14,2×, contos africanos, ago/2026).
4. **Lugar/cultura documentada (vestígio no brief):** The Dark Logs (3,5×, New Orleans, jun/2026) — fora do cluster, mas no mesmo guarda-chuva de folclore local.

Janela: Otis Boone (9 dias) e Myth After Dark (16 dias) estão **fresquíssimos**; dois outliers têm 7–10 semanas (limítrofes). Leitura: fome real e diversificada, com entrada recente de canais ≤45d — por isso PARCIAL com watchlist, não REPROVA.

## Demanda (autocomplete — top termos)

- `urban legend documentary` → **85 termos únicos** (meta ≥15), mas **ruído dominante do filme de 1998** (`urban legend movie explained in hindi`, `urban legend movie recap`, `urban legend 1998 movie clips`…). Termos com intenção real de conteúdo: `urban myths`, `urban legends`, `urban legends from around the world`, `urban legend story`, `urban legend documentary national geographic`, `urban legend documentary london`, `urban legend documentary philadelphia`-like (geo), `urban legend documentary netflix`.
- Implicação: o seed "urban legend" puxa cinema; a revalidação deve usar seeds **de caso/região** (`Aswang`, `Woodbooger`, `Teke Teke`, `corpse roads`) no `--suggest`, não o guarda-chuva.
- Sinais de demanda real (web): threads recorrentes pedindo **vídeos individuais por lenda** — "top 10" é exatamente o que o público reclama (r/ifyoulikeblank); threads de recomendação de folclore (r/horror) e de deep dives paranormais (r/Ghosts) com dezenas de respostas apontam canais como Shrouded Hand, Lazy Masquerade, The Why Files, The Lore Lodge, The Tape Library — teto de formato e prova de apetite.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` e duas tentativas manuais de `--trends` retornaram **HTTP 429** em 2026-09-22. Sem retry extra nesta rodada. Fallback usado: autocomplete (85 termos) + fome cross-canal. Revalidar com `--trends "folklore"` em outro horário/dia.

## Comentários (demanda explícita)

Não coletado nesta rodada — `--comments` exige o escopo `youtube.force-ssl` no `yt_auth.py` (`references/23`). Alvos sugeridos na revalidação: o outlier do Otis Boone ("I'm From Appalachia… Bigfoot"), o Aswang da Myth After Dark e o Stanley Hotel do The Dark Logs — onde a discussão "qual versão você ouviu?" tende a concentrar pedidos de região/lenda.

## Convergência de formato (últimos uploads)

- **The Dark Logs** — últimos 5 uploads, todos **35–48 min**, lugar amaldiçoado documentado: Winchester Mystery House (2026-09-21, 255 views, 43:44), Los Feliz Murder House (2026-08-29, **53.241**, 35:14), Salem (2026-08-18, **26.877**, 47:53), cemitérios históricos dos EUA (2026-08-10, 779, 44:16), Stanley Hotel (2026-07-31, **149.677**, 38:17). Convergência clara: formato repetível de long-form documental em **lugares com lenda** — é o espelho mais direto para o fingerprint do modelo.
- **Paint Maniac** — últimos 5: internet lore em 8–9 min (Roblox media 209.052; Every Meme With a Horrific Backstory 405.734; Russian Internet 89.084) + 1 compilação de 1h (407.544) + um desvio de true crime (Epstein, 437.383). Convergência: **folclore de internet explicado** em vídeos curtos e compilações; quadrante secundário do modelo.
- **Canais micro do cluster (Otis Boone, Myth After Dark, Magic Toon Nepal)** — convergência **não verificada** nesta rodada: o cluster não persiste ID/handle e os chutes de `--channel` falharam (sem footprint web — canais de 35d/36d). Verificar na revalidação com `--channel @handle` antes de tratar como espelho de formato (honestidade metodológica: gate numérico, formato não confirmado).
- **Demais canais do brief** — não verificados individualmente (moderação de quota; os 8 já reprovam no gate de idade de qualquer forma).

## Fontes web (2+)

- https://support.google.com/youtube/answer/6162278 — diretrizes oficiais de conteúdo advertiser-friendly: contexto **documentário/educacional** é avaliado melhor; gore e "shocking content" (inclusive conteúdo que pode assustar crianças) limitam ou desligam anúncios.
- https://support.google.com/youtube/answer/1311392 — políticas oficiais de monetização: conteúdo **mass-produced, genérico, repetitivo ou produzido por template** não é elegível (política de conteúdo inautêntico, aplicada ao canal como um todo).
- https://support.google.com/youtube/answer/9725604 — histórico oficial de atualizações das diretrizes (2025–2026): ampliação de monetização para educacional/documentário; regras de linguagem e conteúdo sensível.
- https://www.youtube.com/watch?v=vjX4RqqyCx4 (Creator Insider, jan/2026) — atualização oficial: temas controversos passam a monetizar quando **não gráficos/dramatizados**; criança/abuso e transtornos alimentares seguem excluídos.
- https://www.auditsocials.com/blog/youtube-2026-advertiser-friendly-update-controversial-issues-monetizable-brand-safety (jul/2026) — consolida a mudança de jan/2026 e a **clarificação de março/2026**: conteúdo com sujeitos que aparentam ser jovens em sofrimento, gore/repulsa, fica fora da monetização; resto é "não-gráfico e dramatizado" [PRATICANTE].
- https://www.auditsocials.com/blog/youtube-advertiser-friendly-guidelines-2026-content-categories-self-certification-inventory-modes-brand-suitability (jun/2026) — categorias que limitam anúncios + autoclassificação; o **título/thumb/metadata contam** para a classificação [PRATICANTE].
- https://fluxnote.io/blog/folklore-youtube-channel-guide-2026-start-and-monetize (mai/2026) — guia do nicho folclore: benchmarks de players (Lazy Masquerade 2,05M; MrBallen 8,4M; Nexpo 3,04M); subnichos (lendas urbanas, mitologia, criptídeos, folclore local); YPP; promete "bom RPM" sem número — **[ALEGADO — vendor de ferramenta]**
- https://fluxnote.io/blog/urban-legends-youtube-channel-guide-2026-start-and-monetize (mai/2026) — guia de lendas urbanas faceless; "CPMs mais altos" sem número; alerta de originalidade/reused content — [ALEGADO — vendor]
- https://fluxnote.io/guides/urban-legend-youtube-channel-guide (mar/2026) — números de RPM citados: $3–6 (lenda urbana) e $4–8 (mistério histórico/paranormal) [ALEGADO — vendor]; FAQ recomenda **enquadrar a lenda como fenômeno cultural** ("According to the legend…") para não violar misinformation.
- https://faceless.my/niches/us-en/faceless-mystery-channel/ (ago/2026) — análise do recorte mistério documental: **folclore regional/cryptid tem "mais espaço para canal novo"** que mistério genérico; brand safety trata documentário pesquisado melhor que jump-scare; RPM citado $5–8 [ALEGADO].
- https://vexub.com/blog/urban-legends-faceless-youtube-ai (mar/2026) — defende o ângulo **lendas locais/regionais**; cita CPM $8–15 no cruzamento folclore/true crime e "top creators $15k–50k/mês" [ALEGADO — vendor].
- https://facelesslab.video/blog/en/faceless-horror-story-videos (ago/2026) — storytelling long-form citado em $6–13 RPM [ALEGADO]; alerta de direitos ao narrar histórias de fóruns (reescrever em palavras próprias).
- https://www.reddit.com/r/ifyoulikeblank/comments/mq60gx/im_looking_for_youtube_channels_about_urban/ — demanda explícita: usuário reclama que só encontra "top 10 scariest urban legends" e procura **vídeos individuais por lenda** (a lacuna exata do modelo).
- https://www.reddit.com/r/horror/comments/14ka777/looking_for_creepy_folklore_youtubers/ — thread de recomendação de canais de folclore (Shrouded Hand, Lazy Masquerade, Morbid Midnight, Scary Interesting) — apetite e nomes do teto de formato.
- https://www.reddit.com/r/Ghosts/comments/1nxk7dk/any_recommendations_for_youtube_channels_who_do/ (out/2025) — pedido de "deep dives" em lendas/cryptids; lista The Tape Library, Peter Laws, The Why Files — prova de que o público pede profundidade, não listas.
- https://www.pbs.org/video/life-in-virginias-appalachia-folklore-arpeas/ (jan/2025) — Woodbooger e nomes regionais de Appalachia; mostra o tratamento "folclore como cultura local" que o modelo adota (referência de tom para o subnicho regional).
- https://appalachianhistorian.org/the-yahoo-of-kentucky-daniel-boone-gullivers-travels-and-appalachian-bigfoot-lore/ (jun/2026) — caso modelo do arquivo: a história do "Yahoo" de Daniel Boone **tratada como folclore com paper trail, não como prova** (estudo de Carl Lindahl; a palavra popularizada na biografia de Faragher, 1993) — o arquétipo de roteiro do canal.
- https://www.squatchable.com/article.asp?id=21156 (jul/2026) — nomes regionais ("wood booger") anteriores ao "Bigfoot" mainstream dos anos 1950; formato de storytelling regional (The Holler Files with Buzzard).
- https://wbkr.com/daniel-boone-and-bigfoot/ (jul/2026) — interesse da mídia regional na lenda (demanda evergreen do subnicho local).

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalvas: (a) `urban legend documentary` como seed está **poluído** (filme de 1998 no autocomplete; horror asiático no resultado) — a entrada é por **lenda nomeada + região/cultura**, não pelo termo; (b) o quadrante **regional EN** está aberto (Otis Boone 35d passando gates; guythatlikeshistory 46d com outlier; Hollow Hills 116d crescendo); (c) o quadrante **internacional** tem flares enormes fora do EN (Myth After Dark 162×, Magic Toon Nepal 267,9×) e tradução/versão EN como oportunidade; (d) o quadrante **lugar amaldiçoado long-form** funciona (The Dark Logs, 35–48 min), mas exige produção de pesquisa mais longa; (e) players estabelecidos (MrBallen, Lazy Masquerade, The Why Files, Lore Lodge) definem a expectativa de qualidade — um slideshow TTS de 5 min não compete.
- **Gargalo real:** nenhum canal ≤45d **além do Otis Boone** cruzou os 3 gates nesta coleta; os emergentes (70d e 36d) precisam cruzar a idade em 2–4 semanas para o veredito subir para PASSA.
- **Riscos de advertiser/compliance:** adjacência de horror/paranormal exige enquadramento documental (as diretrizes oficiais tratam documentário melhor que jump scare); a clarificação de março/2026 mantém **gore e sujeitos jovens em sofrimento** fora da monetização — thumb e roteiro nunca podem flertar com isso; título/thumb contam para a classificação.
- **Desinformação:** lenda apresentada como fato = risco de unreliable content; a FAQ do nicho recomenda o enquadramento cultural ("According to the legend…") — é também a promessa editorial do modelo.
- **Inautenticidade:** "lendas em série" com template + TTS é o perfil que a política de conteúdo inautêntico mais pega (mass-produced/template não monetiza). Mitigação do modelo: 1 peça primária por vídeo, estrutura variável, ângulo próprio.
- **Direitos/respeito:** creepypasta e relatos de fórum são obra de terceiros; crenças vivas (Aswang, yokai) entram como cultura, sem deboche e sem afirmar sobrenatural.

## Queries mais estreitas (se REPROVA)

- **Executada (2ª busca permitida):** `folklore documentary` (cluster) — 45 encontrados → 8 pequenos/jovens → 8 analisados; **1 gate** (Otis Boone) + 2 emergentes + 5 outliers ≥3×.
- **Não executadas (limite de 1 segunda busca na rodada):** `regional folklore documentary`, `appalachian folklore documentary`, `haunted places documentary`, `japanese folklore documentary`, `corpse roads documentary` — usar na revalidação de 2–4 semanas, com `--age 45` no cluster e seeds de caso (`Aswang`, `Woodbooger`, `Teke Teke`) no `--suggest`.
