# Evidência — Assassinos não identificados

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "unidentified killer documentary" --max 8` + 1 busca estreita (`--cluster "john doe identified documentary" --max 8`) + websearch
> Brief completo: `data/briefs/unidentified-killer-documentary.md` · JSON: `data/briefs/unidentified-killer-documentary.json`
> A saída do `--cluster` não foi salva em artefato (rodou sem `--out`); os números estão transcritos abaixo.

## Veredito: **REPROVA**

- Canais pequenos analisados: **16** no total (8 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Canais que passam **2/3** gates (falham só a idade ≤45d): **4** — ZDF True Crime, Cold Case Reopened, The Living Archive, Othram Studios
- Fome do algoritmo (outlier ≥3×): **2** canais no brief (ZDF True Crime 3,5×; Cold Case Reopened 4,8×) → sinal: **sim** para o tema "identificação de Doe"; **0** outliers no cluster estreito
- Autocomplete: **111 termos únicos** (meta ≥15) — mas a maior parte é cauda gerada por sufixos (a–z, países, "full episode"); núcleo útil ≈15–20 termos
- Trends: **BAIXA** (recente 0 vs anterior 8,3; sem queries em alta)

> Reprovou nas **duas** queries permitidas. O modelo existe como blueprint, mas produção em escala fica condicionada a re-scan que passe os gates (ver "Queries mais estreitas"). Leitura central: há demanda de audiência no tema (autocomplete profundo + 2 outliers cross-canal + Othram Studios com 42.397 views/dia), mas **nenhum canal dark novo (≤45d) rompendo** apareceu nas buscas — os canais com tração são mídia estabelecida (ZDF, braço de mídia da Othram) ou canais de 100–300 dias.

## Canais-evidência — brief "unidentified killer documentary" (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| ZDF True Crime | 97.900 | 333d | 1.281.534 | 106.974 | 011 | 3,5× |
| Cold Case Reopened | 12.600 | 146d | 452.673 | 13.574 | 011 | 4,8× |
| The Investigation Room | 20.800 | 257d | 8.855 | 6.608 | 001 | 0 |
| The Living Archive | 273 | 113d | 16.429 | 2.436 | 011 | 0 |
| I'm Stickmen | 65 | 56d | 2.888 | 367 | 000 | 0 |
| Before the 90s | 445 | 250d | 5.138 | 632 | 000 | 0 |
| CRIME HQ | 1.120 | 323d | 2.619 | 293 | 000 | 0 |
| الراوي - قصص حقيقية | 225 | 69d | 5.204 | 557 | 000 | 0 |

Cluster: 47 canais encontrados; 25 pequenos (≤200k subs) e ≤365d; 8 analisados (quota). Nenhum ≤45d entre os analisados.

## Canais-evidência — cluster estreito "john doe identified documentary"

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Othram Studios | 58.800 | 208d | 15.261 | 42.397 | 011 | 0 |
| World's Greatest Investigations | 173 | 67d | 3.642 | 885 | 000 | 0 |
| The Last Mile Documentary | 92 | 216d | 3.488 | 176 | 000 | 0 |
| VeriXa True CRIME Mysteries | 7 | 48d | 1.462 | 77 | 000 | 0 |
| TrendyVault | 135 | 150d | 3.733 | 211 | 000 | 0 |
| Harlan Files | 1 | 76d | 204 | 4 | 000 | 0 |
| Alex Mervit | 42 | 132d | 252 | 168 | 000 | 0 |
| Dark Secrets | 4 | 27d | 1.037 | 57 | 000 | 0 |

Cluster: 27 canais encontrados; 12 pequenos (≤200k subs) e ≤365d; 8 analisados (quota). Nenhum ≤45d; nenhum outlier ≥3×.

> Gates no formato `011`: 1º dígito = idade≤45d · 2º = 5 primeiros ≥10k · 3º = ≥1k views/dia.

Leitura honesta: o padrão que se repete nas duas buscas é **falha só na idade** — os canais com números fortes têm 100–333 dias. Os poucos canais dentro da janela de 45d encontrados (Dark Secrets 27d/4 subs; VeriXa 48d/7 subs; I'm Stickmen 56d/65 subs) não têm tração. Não há evidência de feed novo no cruzamento pesquisado.

## Outliers (janela de 2–6 semanas)

- **ZDF True Crime** — 3,5× — 570.768 views — "Die unbekannte Tote: Polizei sucht verzweifelt ihre Identität | ZDF True Crime" — 2026-08-21 — padrão: arquivo + apelo público de identificação de Doe; canal é emissora alemã (não dark) e o vídeo é em alemão.
- **Cold Case Reopened** — 4,8× — 118.791 views — "NEW HAMPSHIRE 1985 Cold Case Solved After 32 Years — Justice for the Bear Brook" — 2026-09-11 — padrão: caso resolvido por DNA + enquadramento "justice"; long-form EN, canal de 146d.
- Demais 14 canais analisados: 0 outliers ≥3×.

## Fome do algoritmo (cluster cross-canal)

2 canais diferentes com outlier ≥3× no mesmo tema (identificação de Doe) na janela de 90 dias — **sinal de fome presente** no brief. Porém o cluster estreito não achou nenhum outlier ≥3×, e os dois outliers do brief estão em canais que não são dark/novos (emissora + canal de 146d). Conclusão: o algoritmo mostra interesse no tema, mas não há evidência de que ele esteja empurrando **canais novos** nesse cruzamento agora.

## Demanda (autocomplete — top termos)

Termos úteis extraídos dos 111 (o restante é cauda com sufixos de letras, países e variações "full episode/movie"):

- unidentified serial killer documentary / unidentified serial killer / unidentified doe
- unidentified killer documentary australia / uk / usa / canada / latest
- unidentified killer documentary full episode / compilation / real stories / documentary
- unsolved murders documentary
- unidentified killer documentary podcast / netflix / reaction / review

Profundidade real: o núcleo semântico é forte (Doe, unidentified, unsolved, serial killer), mas a demanda é dominada por conteúdo já existente de terceiros (Netflix, A&E, BBC, Channel 4/5, ITV) — busca de catálogo, não necessariamente de canal novo.

## Trends (YouTube 12m)

- Direção: **BAIXA** (interesse recente 0 vs anterior 8,33) · Rising: nenhuma query em alta.
- Nota de método: termo de cauda longa em EN; vale monitorar termos irmãos no re-scan ("john doe identified", "genetic genealogy", "forensic genetic genealogy").

## Comentários (demanda explícita)

Não coletado direto: `--comments` retornou `insufficientPermissions` (yt_auth sem escopo `youtube.force-ssl`) em 2 tentativas (Othram Studios `qB9582qdrVo`; gabulosis `qCLorjKzs5k`). Proxy qualitativo: gabulosis mantém canal de pedidos de caso (`gabulosiscaserequests@gmail.com`) e a DNA Doe Project pede uploads de DNA e dicas (`case-tips@dnadoeproject.org`) — há demanda explícita de cobertura e participação do público, mas é sinal de audiência, não de canal rompendo.

## Fontes web (2+)

- https://www.prweb.com/releases/othram-launches-othram-studios-to-bring-real-forensic-investigations-to-a-global-audience-302748147.html — Othram Studios (abr/2026): iniciativa de mídia de "long-form, science-driven storytelling"; 2 episódios no 1º mês → 750 mil espectadores e 100 mil horas de watch time; formato: caso real do vestígio à identificação.
- https://www.youtube.com/@OthramStudios — canal real do espaço (58.800 subs no scan; 42.397 views/dia).
- https://www.youtube.com/channel/UCjUE921QWnbDWuMeg8aMa3g — DNA Doe Project (organização; canal de casos e identificações; >150 identificações desde 2017).
- https://www.youtube.com/watch?v=qCLorjKzs5k — gabulosis: Ventura County Jane Doe identificada como Maricela Rocha Parga (fev/2026) após árvore de 125 mil pessoas; exemplo de demanda e formato do subnicho.
- https://www.youtube.com/watch?v=ZGEzc4OdyAY — WQAD News 8: Jane Clinton Doe identificada como Cheryl Lynn Edwards (jun/2026, DNA Doe Project; caso de 51 anos).
- https://www.youtube.com/watch?v=jfnxMgek4Tk — National Geographic: "Texas Jane Doe Identified after 38 Years" (mai/2026) — long-form mainstream do tema.
- https://www.youtube.com/@NamelessFaces — canal real focado em casos sem nome (referência de posicionamento).
- https://longformstudio.app/articles/true-crime-youtube-channel — playbook faceless 2026: formatos (case deep-dive, cold case, forensic-focus, courtroom) e risco de yellow icon por formato (forensic-focus = menor); RPM reportado $6–9 para true crime educacional non-graphic [ALEGADO]; proibição de simular vítimas (jan/2024); YPP dobra em 01/02/2027.
- https://fluxnote.io/blog/is-unsolved-cases-a-good-youtube-niche-in-2026-rpm-and-growth-data — "unsolved cases" em 2026: RPM US/Tier 1 $6,50–12,00 e misto $4,00–7,50 [ALEGADO]; audiência do gênero +18% a/a desde 2023; nicho considerado não saturado para quem traz perspectiva própria.
- https://support.google.com/youtube/answer/6162278 — diretrizes oficiais de advertiser: contexto documentário/educativo pesa; thumbnail/primeiros 15s gráficos e corpos com ferimento visível em contexto educativo = limited ads; gore = no ads.
- https://www.tubefilter.com/2026/01/15/youtube-sensitive-content-ad-monetization-guidelines-update/ — jan/2026: YouTube libera monetização plena para temas sensíveis discutidos de forma não gráfica/dramatizada.
- https://www.auditsocials.com/blog/youtube-2026-advertiser-friendly-update-controversial-issues-monetizable-brand-safety — detalha a mudança de jan/2026; "child abuse" e "eating disorders" seguem excluídos; clarificação de mar/2026 sobre jovens em sofrimento e shock/gore.
- https://latenights.live/how-the-new-youtube-rules-affect-documentary-clips-and-true- — checklist editorial para qualificar documentário/true crime à monetização plena (contexto, fontes, sem gráfico) [PRATICANTE/ALEGADO].

## Saturação e riscos observados

- **Formato×tópico:** o cruzamento long-form documental + casos sem autor tem demanda (111 autocompletes; 2 outliers cross-canal; Othram Studios com 750 mil espectadores em 1 mês [PR]) mas **nenhuma evidência de canal dark ≤45d rompendo** nas duas buscas. Os números de gate dos canais de maior tração são inflados por mídia estabelecida (ZDF = emissora; Othram Studios = braço de mídia da Othram), o que não prova espaço para canal novo. Reprovado para lançamento imediato; re-testar em 30 dias com queries mais estreitas (abaixo).
- **Advertiser/compliance:** thumbnail/primeiros 15s gráficos = limited ads [OFICIAL]; corpos com ferimento em contexto educativo = limited ads [OFICIAL]; "child abuse" e "eating disorders" fora de full monetização [OFICIAL jan/2026]; jovens em sofrimento/gore = inelegível [OFICIAL mar/2026]; reencenar fala de vítima morta = proibido desde 16/01/2024 [OFICIAL]. O subnicho "forensic-focus" (DNA/perícia) é o de menor risco de yellow icon.
- **Outros:** difamação (pessoa viva = "alleged/reported"); direitos de imagem em fotos de arquivo e reconstruções (creditar artista); exploração da dor da família é o maior risco reputacional do nicho.

## Queries mais estreitas (se REPROVA)

Testada nesta coleta (a única busca extra permitida):

1. `--cluster "john doe identified documentary"` — 0/8 gates, 0 outliers (27 canais; 12 pequenos ≤365d).

Não testadas (candidatas para re-scan em 30 dias, em ordem de prioridade):

2. `--cluster "unsolved murder documentary" --max 8` (a outra opção da instrução; não rodada por limite de quota)
3. `--cluster "forensic genetic genealogy documentary" --max 8`
4. `--cluster "unidentified remains identified documentary" --max 8`
5. `--cluster "namus unidentified documentary" --max 8`
6. `--cluster "unknown offender documentary" --max 8`

Recomendação de re-scan: usar `--cluster "<query>" --age 45 --max 8` para forçar o corte de idade ≤45d e salvar com `--out data/briefs/<query>.md`; só promover o modelo a produção com **≥3 canais pequenos passando os 3 gates**. Atualizar este arquivo com o resultado e o `data/nichos.md` quando houver veredito novo.
