# Evidência — Aviação e acidentes

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "aviation disaster documentary" --max 8` + retry `python scripts/niche_scan.py --cluster "plane crash documentary"` (Data API) + `--suggest` (HTTP livre) + tentativa de convergência `--channel` (handles não resolvidos) + websearch.
> Brief completo: `data/briefs/aviation-disaster-documentary.md` · JSON: `data/briefs/aviation-disaster-documentary.json` (o cluster imprime em tela e não salva JSON).
> Quota: ~300 unidades (estimativa) de ~10.000/dia — 2 buscas pesadas (brief + cluster) + resolução de handles; autocomplete é HTTP livre. Trends falhou (429).

## Veredito: **PARCIAL**

- Scan bruto da ferramenta: **REPROVA** (1/8 gates no brief; 1/5 no cluster — o mesmo canal). A leitura do método (`23`) sustenta **PARCIAL**: fome em 3 canais (outlier ≥3×) + 3 emergentes ≤90d com 2/3 gates. Não é PASSA.
- Canais pequenos analisados: 8 (brief) + 5 (cluster, 4 repetidos) = **9 canais únicos** | passam os 3 gates: **1** (meta ≥3) — Koda Aviation, 42d.
- Emergentes (≤90d + 2/3 gates): **3** — Video Gallery 238 (89d), Austrian Aviation (84d), Beyond The Unknown (79d) — watchlist, não aprovam sozinhos.
- Fome do algoritmo (outlier ≥3×): **3** canais no brief (Koda 33,9×; Prime Action Films 18,8×; Iqbal Production 6,1×) e **1** no cluster (Koda) — sinal: SIM, mas estreito.
- Autocomplete: **102** termos (meta ≥15) | Trends: **429** (rate limit do Google; sem leitura de direção — fallback autocomplete).

Leitura honesta: só **1 canal ≤45 dias** passa os três gates, e ele é pequeno e provavelmente short-form (outlier de 4,7M views com título de emoji). O que sustenta o PARCIAL é a combinação **fome (3 canais com outlier ≥3×, dois deles fora do short: um documentário de sobrevivência e um caso VARIG em hindi) + 3 emergentes de 79–89 dias que falham apenas o gate de idade**. O gargalo é o mesmo do resto da biblioteca: idade ≤45d. O lane long-first não se apoia nos rompimentos pequenos — apoia-se nas âncoras seniores de long-form (Mentour Pilot, Green Dot, Mayday) e num entrante novo declarado em 2026 (Planes Gone Wrong). Revalidar em 2–4 semanas; se um emergente cruzar 45 dias mantendo o desempenho, o modelo sobe para PASSA.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

### Busca 1 — `--brief "aviation disaster documentary"` (42 canais achados; 8 pequenos ≤365d analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Koda Aviation (UCdCIIEObdwIlbIXIEAhfSvg) | 8.000 | **42d** | 706.363 | 185.118 | **111** | **33,9× — 4.717.882 — "When The Rudder Stops Working... 😳✈️" (2026-08-20)** |
| It's Aviation (UCqITpJ_xP_p-_JX_tv5W9bw) | 29.400 | 260d | 24.760.882 | 95.233 | 011 | — (mediana ~9,9M/vídeo; formato não inspecionado) |
| Video Gallery 238 (UC4Ytu1VuuuQWEKmxIeXMZyg) | 47.600 | 89d | 11.038 | 212.492 | 011 | — (**emergente**) |
| Austrian Aviation (UCBlon5PgVO4XunNqaQExI9A) | 9.270 | 84d | 561.588 | 94.573 | 011 | — (**emergente**) |
| Beyond The Unknown (UC1ZKLArCqTFVkYv_Z8VlQ8w) | 9.040 | 79d | 308.133 | 91.585 | 011 | — (**emergente**) |
| NextGen Briefs (UCz8vzTNYdEFLeqwQGmN5kXw) | 8.520 | 96d | 2.531.936 | 45.125 | 011 | — |
| Prime Action Films (UCFIdF_lbrW92svslsths7Xg) | 106.000 | 238d | 1.370.693 | 78.374 | 011 | 18,8× — 940.180 — "He Survived a Plane Crash… Then Faced the Canadian Wilderness Alone" (2026-09-13) |
| Iqbal Production (UCDSPS5K0K_aP-wM38s4cVrg) | 54.400 | 298d | 737.407 | 17.400 | 011 | 6,1× — 531.786 — "PILOT की एक गलती और Boeing 737 Amazon में खो गया! \| VARIG Flight 254" (2026-07-09) |

### Busca 2 — `--cluster "plane crash documentary"` (40 canais achados; 5 pequenos analisados; 4 sobrepõem a busca 1)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Koda Aviation | 8.000 | 42d | 706.363 | 185.118 | **111** | 33,9× (mesmo outlier) |
| ZN Explain | 36.600 | 147d | 1.492.785 | 105.780 | 011 | — |
| It's Aviation | 29.400 | 260d | 24.760.882 | 95.233 | 011 | — |
| Video Gallery 238 | 47.600 | 89d | 11.038 | 212.492 | 011 | — (**emergente**) |
| Austrian Aviation | 9.270 | 84d | 561.588 | 94.573 | 011 | — (**emergente**) |

> Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha). 7 dos 8 canais da busca 1 falham **apenas** o gate de idade.

## Outliers (janela de 90 dias; oportunidade de 2–6 semanas quando recente)

- **Koda Aviation — 33,9× (FLARE)** — 4.717.882 views — "When The Rudder Stops Working... 😳✈️" — 2026-08-20 — canal de 42d, mediana 139.224. Padrão: falha de controle em voo + promessa de emergência. Formato provavelmente curto (emoji no título); convergência não inspecionada (handle não resolveu no `--channel`).
- **Prime Action Films — 18,8× (FLARE)** — 940.180 — "He Survived a Plane Crash… Then Faced the Canadian Wilderness Alone" — 2026-09-13 — padrão: sobrevivência depois do acidente (o ângulo "e depois?"), exatamente o subnicho de sobrevivência.
- **Iqbal Production — 6,1×** — 531.786 — VARIG Flight 254 (Boeing 737 na Amazônia) — 2026-07-09 — hindi; padrão: caso nomeado + erro de pilotagem no título.
- **It's Aviation — não é outlier contra a própria mediana, mas é anomalia de volume** — 24,7M views nos 5 primeiros, 95.233 views/dia, mediana ~9,9M/vídeo — provável short/compilação; formato não inspecionado.

## Fome do algoritmo (cluster cross-canal)

- 3 canais com outlier ≥3× (Koda, Prime Action, Iqbal) em temas diferentes do mesmo pai: falha de controle, sobrevivência pós-queda e erro de pilotagem em caso nomeado. Não é o mesmo tema em canais diferentes (fome mais fraca que a de vulcões/desastres), mas há dois padrões replicáveis: **"o sistema/controle falhou"** e **"ele sobreviveu e…"**.
- No cluster `plane crash documentary`, só Koda repete como outlier — a fome no corte exato é fraca (1 canal). Honestidade: a janela de 2–6 semanas existe, mas é estreita.

## Convergência de formato (âncoras, via web)

- **Mentour Pilot** (@MentourPilot): 2,2–2,5M inscritos · 692–797 vídeos; uploads de 25–51 min, com documentários "quase de uma hora" anunciados semanalmente; casos recentes: Jeju Air 1,4–1,7M; Tenerife 850 mil em 1 mês; FedEx 80 990 mil em 1 mês; MH370 6,4–6,8M; Concorde 14–15M. Monetização: patrocínio (NordVPN), merch próprio, Amazon, canais em outros idiomas. [REPORTADO]
- **Green Dot Aviation** (@GreenDotAviation): 574–613K inscritos · 92–97 vídeos; 14–43 min; piloto de Airbus com formação em Psicologia; animações de sistema (comentários elogiam "as representações gráficas de slats/flaps"); Patreon com níveis; patrocínio (Odoo). Casos: JAL 123 3,4M; Qantas 32 3,2M; USAir 405 353K (jul/2026). Cadência lenta. [REPORTADO]
- **Mayday: Air Disaster** (oficial): 1,06–1,07M · 1,3–1,4 mil vídeos; episódios de 44:33; formato de reencenação + testemunhos. Reposts de terceiros (Documentary Central, 1,05M; Machina) rodam o mesmo episódio: "Ghost Plane" 4,6M; outros 92–213K. [REPORTADO]
- **Documentary Central** (repost): ~909 uploads longos; ~45 min; 6,1 uploads/semana; mediana 3K views; topo = 1.352,9× a mediana; receita estimada $135–539/mês [ALEGADO — TubeHunter]. Evidência de saturação por repost e de variância altíssima.
- **Planes Gone Wrong**: canal novo anunciado em jul/2026 — documentário long-form cinematográfico + tese "a segurança de hoje foi construída pelos desastres de ontem" + produto físico (pôsteres/art prints) + público 25–55. [REPORTADO — press release]
- **Canais pequenos da coleta (Koda Aviation, Austrian Aviation, Beyond The Unknown, Video Gallery 238):** convergência **não inspecionada** — os handles não resolveram no `--channel` e as páginas do YouTube não renderizam sem JS; revalidar quando o handle aparecer (ou medir no piloto).

## Demanda (autocomplete — top termos)

- Termos úteis: "air crash investigation", "aviation incidents", "aviation accident news", "aviation disasters documentary", "air disaster documentary", "flight disaster documentary", "aviation crash documentary", "part 1/2/3" (séries), "with subtitles".
- Ruído/adjacência: "national geographic", "netflix", "bbc", "dw" (demanda por acervo de TV), dublagens ("hindi", "russian", "korean", "japanese", "tamil dubbed") e filmes de desastre ("airline disaster full movie").
- Leitura: a profundidade vem de **variantes do mesmo tema + traduções/dublagens**; não apareceram termos de cauda longa de casos específicos (MH370 etc.) a partir desta seed — bom para o canal (menos disputa de busca) e ruim (mais dependência de feed/sugestão).

## Trends (YouTube 12m)

- 429 (rate limit do Google) na consulta do brief — sem leitura de direção. Fallback: autocomplete (102 termos) + fome (3 canais) como proxy. Reexecutar `--trends "aviation disaster documentary"` em outro horário.

## Comentários (demanda explícita)

- Coleta via API não rodada (falta escopo `force-ssl` no `yt_auth.py`).
- Leitura qualitativa da web (comentários públicos do Green Dot no vídeo USAir 405, jul/2026): pedidos recorrentes de (a) **explicações visuais de sistemas** ("as representações gráficas de slats e flaps foram mais informativas que qualquer coisa que já vi"); (b) **mais frequência de uploads** (membro pede "more frequent videos"); (c) vínculo afetivo com a narração calma ("plane crash videos viraram meu comfort show"). Orientação: diagrama animado é o diferencial pedido, cadência é a dor, tom contido é o ativo.

## Fontes web (2+)

- https://www.youtube.com/@mentourpilot + https://www.youtube.com/channel/UCwpHKudUkP5tNgmMdexB3ow — [REPORTADO] 2,2–2,5M inscritos, 692–797 vídeos, 25–51 min; MH370 6,4–6,8M; Concorde 14–15M; Tenerife 850K/1 mês; patrocínio NordVPN, merch, canais multi-idioma.
- https://www.youtube.com/@GreenDotAviation + https://www.youtube.com/c/greendotaviation/videos + https://divert.stream/watch/yG3NIaZT7YM — [REPORTADO] 574–613K, 92–97 vídeos, 14–43 min, Patreon, Odoo; comentários com demanda por animação de sistema e cadência.
- https://www.youtube.com/c/MaydayAirDisaster + https://divert.stream/watch/-iVestIZ-fs — [REPORTADO] canal oficial 1,06–1,07M, 1,3–1,4 mil vídeos, episódios de 44:33; "Ghost Plane" 4,6M.
- https://tubehunter.app/channel/documentary-central-od4grw — [ALEGADO] repost de Mayday: 909 longos, ~45 min, 6,1/semana, mediana 3K, topo 1.352,9× a mediana, receita estimada $135–539/mês.
- https://www.somdnews.com/online_features/press_releases/planes-gone-wrong-documentary-channel-argues-modern-aviation-s-one-in-eleven-million-safety-record/article_2a61cda4-e5b9-5057-90b2-247eb3d70101.html — [REPORTADO] canal novo long-form (mid-2026) + art prints; tese do arco de segurança; público 25–55.
- https://admiralcloudberg.medium.com/failures-of-technique-the-crash-of-air-new-zealand-dc-8-zk-nzb-5bf5263a4b23 — [REPORTADO] Kyra Dempsey (Admiral Cloudberg), analista de acidentes e roteirista do Mentour Pilot, 75K seguidores; modelo de pesquisa escrita como fosso.
- https://www.mediapost.com/publications/article/411997/youtube-opens-ad-rev-monetization-for-dramatized-c.html — [REPORTADO] jan/2026: YouTube abre monetização para conteúdo controverso dramatizado.
- https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline — [REPORTADO] ago/2026: conteúdo educacional/documentário/jornalístico retratando morte passa a ser monetizável.
- https://support.google.com/youtube/answer/6162278 + https://support.google.com/youtube/answer/9348366 — [OFICIAL] diretrizes advertiser-friendly; contexto documentário é fator explícito.
- https://milx.app/en/trends/what-shanges-in-youtube-monetization-policy-can-creators-expect-in-2026 — [ALEGADO/REPORTADO] elegibilidade mais estrita para faceless/copy-paste; granularidade de brand safety.

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Em parte. O formato **repost de Mayday** está saturado (Documentary Central/Machina) e o **slideshow TTS genérico** é o alvo da política de conteúdo inautêntico. O espaço aberto é o **long-form de investigação com animação própria de sistemas + arco de segurança** — o que Mentour e Green Dot provam e o que Planes Gone Wrong tenta ocupar agora. No lado pequeno, os rompimentos da coleta são short-form, o que não valida o lane long-first por si.
- **Riscos de advertiser:** morte no centro do tema; sem gore, sem imagem de impacto na thumb/15s; a política de ago/2026 favorece contexto documentário, mas a autoclassificação e a thumb decidem a faixa.
- **Riscos de sensibilidade:** vítimas e famílias; acidentes recentes precisam de distância; casos com suicídio/terrorismo são alto risco; nada de especulação como fato (MH370 é o teste).
- **Direitos:** reencenação de TV, áudio de ATC de terceiros e imagens de radar/ADS-B têm licença restrita; a base segura é relatório/docket público + arte própria + mídia com licença checada.
- **Gargalo de validação:** 1/9 canais passa os 3 gates; o modelo é PARCIAL e depende de revalidação — não escalar antes.

## Queries mais estreitas (próxima rodada)

- `aviation mystery documentary` — não rodada (era a segunda opção do método; cobre desaparecimentos/MH370).
- `air crash investigation documentary` — não rodada (termo de maior demanda no autocomplete).
- `MH370 documentary` — não rodada (desaparecimento; checar fome própria).
- `aviation safety documentary` — não rodada (subnicho de segurança moderna).
- `air disaster documentary` / `flight disaster documentary` — variantes do brief; só revalidar se a idade dos emergentes amadurecer.
- Nota de captação: `--channel` não resolveu handle de Koda Aviation/Austrian Aviation; `--cluster` não salva JSON; habilitar `force-ssl` no `yt_auth.py` para `--comments`.
