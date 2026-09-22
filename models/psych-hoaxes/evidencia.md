# Evidência — Hoaxes e enganos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "hoax documentary" --max 8` + `python scripts/niche_scan.py --cluster "famous hoaxes documentary"` (segunda busca permitida) + autocomplete + websearch
> Brief completo: `data/briefs/hoax-documentary.md` · JSON: `data/briefs/hoax-documentary.json` (a saída bruta do cluster não é persistida pelo script; é reproduzível pelo comando acima)

## Veredito: **PARCIAL**

- Canais pequenos analisados: **16 únicos** (8 no brief + 8 no cluster; sem repetição) | passam os 3 gates: **1** (meta ≥3) — só `Web Crime`
- Fome do algoritmo (outlier ≥3×): **3 canais** — Uncanny (15,3×), CURIVIOS (239,6×) e Reality Broke Archive (6,3×) | sinal: **sim, mas em 3 sub-temas diferentes**
- Emergentes (≤90d + 2/3 gates): **2** — 晚松講故事 (88d) e CURIVIOS (28d)
- Autocomplete: **36 termos** (meta ≥15; com ruído de ARG e celebridade) | Trends: **não coletado** (HTTP 429 no brief)

**Leitura honesta:** o gate rígido **não foi atingido** — o brief marcou `REPROVA` (1/3 canais; só `Web Crime` cruza os três gates) e o cluster `famous hoaxes documentary` marcou **0/3**. Pela régua de modelo (`models/README.md`: PARCIAL = <3 gates, mas com fome ≥2 canais e/ou emergentes), fica **PARCIAL**: há 3 canais com outlier ≥3× em três recortes (**paranormal em disputa** — Enfield, jul/2026; **vídeo viral falso** — Argentina, ago/2026; **fraude científica** — Piltdown, jul/2026) e 2 emergentes ≤90d. Os outliers mais valiosos em viewport absoluto são o de Uncanny (118.719 views) e o de CURIVIOS (18.927 views, ratio inflado por mediana de 79). Não é PASSA, não é REPROVA: revalidar em 2–4 semanas, procurando entrantes ≤45d — e atenção: `hoax documentary` é termo guarda-chuva que puxa true crime e paranormal; o cruzamento com cara de canal é **caso específico + pergunta de veracidade** ("Haunting or Hoax?", "Fake Fossil", "The Video That Wasn't").

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| The Orbitarium (brief) | 2.960 | 206d | 1.172.983 | 14.771 | 011 | — |
| 晚松講故事 (brief) | 6.570 | 88d | 37.524 | 179.650 | 011 | — |
| Uncanny (brief) | 45.900 | 180d | 157.831 | 11.103 | 011 | 15,3× — 118.719 — "The Enfield Poltergeist: Haunting or Hoax? \| Live - Crossed Wires" — 2026-07-16 |
| **Web Crime (brief)** | **2.440** | **38d** | **85.825** | **21.385** | **111** | — |
| Shubh Kaayande (brief) | 1.310 | 238d | 160.759 | 1.442 | 011 | — |
| Архив Мортимера Холмса (brief) | 5.460 | 196d | 33.671 | 17.409 | 011 | — |
| CURIVIOS (brief) | 9 | 28d | 19.227 | 794 | 110 | 239,6× — 18.927 — "The Sea Vanished in Argentina? The Viral Video That Wasn't #shorts" — 2026-08-30 |
| Reactify (brief) | 177 | 93d | 2.181 | 556 | 000 | — |
| Forbidden Mysteries (cluster) | 34.800 | 363d | 12.283 | 17.063 | 011 | — |
| Real Scottish Facts (cluster) | 345 | 138d | 4.451 | 1.121 | 001 | — |
| DarkCaseFiles (cluster) | 196 | 44d | 5.497 | 450 | 100 | — |
| Reality Broke Archive (cluster) | 130 | 87d | 3.152 | 281 | 000 | 6,3× — 545 — "Piltdown Man: 40 year Fake Fossil (1912)" — 2026-07-29 |
| Explore with Ryan (cluster) | 23 | 80d | 2.187 | 139 | 000 | — |
| The Unknown Files (cluster) | 128 | 360d | 3.346 | 168 | 000 | — |
| BigFactsUSA (cluster) | 87 | 52d | 1.366 | 501 | 000 | — |
| Gravity of Mysteries (cluster) | 8 | 88d | 1.225 | 59 | 000 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). Brief: 49 canais encontrados, 12 pequenos ≤365d, 8 analisados (quota). Cluster: 32 encontrados, 16 pequenos ≤365d, 8 analisados (quota). IDs no JSON do brief; o cluster não é persistido.
> Nota de idioma: 晚松講故事 (nome em zh — direção de idioma não confirmada no scan, 179,6k views/dia) e Архив Мортимера Холмса (ru) mostram a demanda internacional do tema; a versão-alvo do modelo é EN.

## Outliers (janela de 2–6 semanas)

- **CURIVIOS** — 239,6× — 18.927 views — "The Sea Vanished in Argentina? The Viral Video That Wasn't #shorts #viralshorts" — 2026-08-30 — padrão: Short que desmonta um vídeo viral ("o vídeo que não era"), ratio inflado por mediana de 79 views; o viewport absoluto é modesto — sinal de formato, não de escala.
- **Uncanny** — 15,3× — 118.719 views — "The Enfield Poltergeist: Haunting or Hoax? | Live - Crossed Wires" — 2026-07-16 — padrão: pergunta de veracidade no título + caso famoso em disputa; único outlier da coleta com viewport de seis dígitos.
- **Reality Broke Archive** — 6,3× — 545 views — "Piltdown Man: 40 year Fake Fossil (1912)" — 2026-07-29 — padrão: fraude científica histórica no formato arquivo; viewport pequeno, mas ratio acima do bracket 5× e tema exatamente no subnicho de fraude científica.

> Nota metodológica: ratios de canais minúsculos (9, 130 subs) vêm de medianas baixas. O que sustenta o sinal aqui é a **coincidência de três recortes de hoax em três canais diferentes em jul–ago/2026** mais o viewport real de 118,7k da Uncanny.

## Fome do algoritmo (cluster cross-canal)

**Sim, em três sub-temas (jul–ago/2026):**

1. **Paranormal em disputa:** Uncanny (15,3×, jul/2026, Enfield "Haunting or Hoax?") — o caso tem 250h de fita e veredito em aberto, o que combina com o ângulo calibrado do modelo.
2. **Vídeo viral falso:** CURIVIOS (239,6×, ago/2026, Short sobre o mar que "sumiu" na Argentina) — o recorte mais fresco da coleta (≈3 semanas).
3. **Fraude científica:** Reality Broke Archive (6,3×, jul/2026, Piltdown Man) — ratio em viewport pequeno; tema quente fora do YouTube: a BBC reacendeu Piltdown em fev/2026 e há paper de 2016 confirmando Dawson como autor.

Janela: 2 dos 3 outliers têm 7–8 semanas (fora da janela ideal de 2–6); só o de CURIVIOS está fresco. Leitura: fome real, mas nenhum recorte com 2–3 canais convergindo na mesma quinzena — por isso PARCIAL e não PASSA.

## Demanda (autocomplete — top termos)

- `hoax documentary` → **36 termos únicos** (meta ≥15). Termos com intenção real: `fake influencer documentary`, `fake baby documentary`, `fake birds documentary`, `fake dollars documentary`, `deception island documentary`, `fake documentary iceberg`, `fake id documentary`, `fake rich documentary`, `fake lawyer documentary`, `fake judge documentary`, `fake jury documentary`.
- Ruído alto no lote: `fake documentary q` + variações (ARG/série, ~12 termos), `harvey weinstein`, `james holmes`, `jfk family`, `harun farocki` — o seed puxa celebridade e ficção. Implicação: usar seeds específicos de caso na revalidação (ex.: `Piltdown`, `Enfield`, `internet hoax`), não só o guarda-chuva.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` retornou HTTP 429 (rate limit do Google) em 2026-09-22. Sem retry extra (limite de 1 segunda busca na rodada). Fallback usado: autocomplete (profundidade 36) + fome cross-canal. Revalidar com `--trends "famous hoaxes"` em outro horário.

## Comentários (demanda explícita)

Não coletado nesta rodada — fora do escopo do run pedido. `--comments` depende do escopo `youtube.force-ssl` no `yt_auth.py` (`references/23`). Sugestão de alvo na revalidação: comentários do outlier da Uncanny (Enfield) e do Short da CURIVIOS, onde a discussão "real ou falso" tende a concentrar pedidos de casos.

## Convergência de formato (últimos uploads)

- **Uncanny:** o outlier é um formato "Live - Crossed Wires" com pergunta de veracidade no título; canal de 45,9k subs com mediana de 7,7k e outliers de 15,3× — perfil de exploração temática (paranormal/mistério) que pode ser copiado como **pergunta + arquivo**, não como set.
- **Reality Broke Archive:** título "Piltdown Man: 40 year Fake Fossil (1912)" — direção "arquivo + ano" para fraude histórica; mediana 86, ou seja, o formato ainda não escalou nem saturou ali.
- **CURIVIOS:** `#shorts #viralshorts` com o formato "o vídeo viral que não era" — conversão direta do tema hoax em Short de desmonte.
- **The Orbitarium:** 5 primeiros somando 1,17M com mediana de 57,7k — perfil de biblioteca de docs; mostra teto do recorte documental no mesmo seed.
- **Web Crime:** único canal que passa os 3 gates (2,4k subs, 38d, 21,4k views/dia). O scan não expôs o conteúdo dos uploads — confirmar o formato real no revalidate antes de tratar como espelho de formato (honestidade metodológica: gate numérico, formato não verificado).

## Fontes web (2+)

- https://longformstudio.app/articles/youtube-documentary-channel — ago/2026: retenção saudável 30–45% (15–30 min); CPM de documentário/educação $10–25 (~$2,75–6,88 RPM) contra $2–8 de entretenimento; caso Fern com estimativa de $19k–43k/mês em 18,06M views [ALEGADO — screen recording]; YPP novo (8.000h/20M) a partir de 01/02/2027.
- https://fluxnote.io/blog/conspiracy-debunking-youtube-channel-guide-2026-start-and-monetize — guia 2026 do recorte debunking/misinformation: estrutura introduzir→"evidência"→contra-evidência→falhas→conclusão; evergreen; monetização por AdSense + afiliado + patrocínio.
- https://www.thataintnoplane.com/index.php/2026/05/31/yesterday-i-uploaded-a-documentary-in-which-i-exposed-blake-and-brent-cousins-thirdphaseofmoon-long-history-of-fabricating-fake-ufo-stories-and-videos-they-took-down-my-video-with-a-copyright-strike-3/ — mai/2026: documentário "The Hoax Files Episode 1 – Thirdphaseofmoon Exposed" removido por copyright strike do próprio acusado — retaliação documentada contra canal de exposé.
- https://www.gadgetreview.com/weaponizing-copyright-how-fake-gurus-are-using-legal-censorship-to-silence-critics — set/2026: strikes fabricados (incl. claim musical falso) para derrubar exposés de golpe; supressão custa $2k–5k ao fraudador; YouTube só checa formalidade do filing.
- https://www.contentremoval.com/remove-youtube-expose-video — set/2026: como vídeos de exposé são removidos (difamação por país, privacidade); opinião/crítica é protegida, declarações falsas de fato não; resposta do acusado alimenta o algoritmo — o canal precisa narrar com documento, não com adjetivo.
- https://lunoo.com/item/captain-disillusion — jun/2026: formato "explain the fake" com análise frame a frame e explicação de VFX em vez de veredito seco — referência de teto e de profundidade técnica do recorte "internet hoax".
- https://ytubeinfluencers.com/category/horror/country/united-states/ — 2026: players adjacentes do recorte internet mysteries — Nick Crowley 3,11M subs; Barely Sociable 1,4M subs e ~100M views com 35 vídeos em 5 anos (20–80 min, narração contida); Nexpo com episódios de hora inteira — mostra o teto do formato e a expectativa de produção.
- https://currentuk.co.uk/tech/jessica-radcliffe-orca-attack-hoax/ — jun/2026: hoax de IA da "treinadora" Jessica Radcliffe/Pacific Blue Marine Park — vídeo passou de 87M views antes do debunk; caso-âncora do subnicho "hoaxes virais".
- https://theconspiratory.com/theory/enfield-poltergeist — jul/2026: Enfield — 250 horas de fita, admissão de fakes pelas irmãs, câmera flagrando truque, e veredito que não fecha para nenhum lado; guia do "veredito calibrado" (o outlier da Uncanny é esse caso).
- https://www.bbc.co.uk/news/articles/ce3gvpz427po + https://en.wikipedia.org/wiki/Piltdown_Man — fev/2026 + contínuo: Piltdown Man — 41 anos da descoberta (1912) à exposição (1953); paper de 2016 com DNA aponta Charles Dawson (morto em 1916) como autor; segue como o caso canônico de fraude científica.
- https://www.tubefilter.com/2025/05/01/20-years-of-youtube-2006-lonelygirl15-jessica-rose/ — 2025: lonelygirl15 — o reveal tornou o canal mais popular; precedente histórico do hoax como formato (e da audiência que gosta do desmonte).
- https://socialblade.com/youtube/handle/thehoaxhotel — jun/2026: The Hoax Hotel, 220K subs e 54,5M views — nome/recorte "hoax" já ocupado por formatos de scambaiting; não é a mesma lane, mas é o que o público associa ao termo.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalvas: (a) o seed `hoax documentary` é guarda-chuva e mistura true crime (Web Crime), paranormal (Uncanny) e mistério viral (CURIVIOS) — a entrada deve ser por **caso + pergunta de veracidade**, não pelo termo; (b) o recorte "fraude científica" está pouco servido no formato dark (o outlier de Piltdown é de um canal de 130 subs) — melhor aposta de diferenciação; (c) o recorte "paranormal em disputa" tem players de horror maiores e exige veredito calibrado para não virar mais um canal de assombração; (d) players estabelecidos (Nexpo, Barely Sociable, Nick Crowley, Captain Disillusion) definem a expectativa de qualidade do recorte internet mysteries — um canal commodity de slideshow não compete.
- **Gargalo real:** nenhum canal ≤45d passou os três gates além do `Web Crime` (gate numérico; formato não verificado). O tier emergente atual (88d e 28d) precisa cruzar o gate de idade em 2–4 semanas para o veredito subir.
- **Riscos de advertiser/compliance:** acusação contra pessoa viva (difamação) é o risco nº 1 — sempre "alleged/reported"; strikes de retaliação são documentados em 2026 (Thirdphaseofmoon; censura via DMCA contra exposés); casos com mortes (curas milagrosas) exigem enquadramento educacional; conteúdo "respeitoso e documental" protege a monetização, thumbnail de pessoa acusada derruba.
- **Inautenticidade:** "debunk" mass-produzido é um dos perfis que a política de conteúdo inautêntico mais pega [TNW, jan/2026: 16 canais terminados]. O modelo exige 1 peça primária por vídeo e estrutura variável por caso — nunca a mesma fórmula de 3 atos com TTS sobre imagens de banco.

## Queries mais estreitas (se REPROVA)

- **Executada (2ª busca permitida):** `famous hoaxes documentary` (cluster) — 32 encontrados → 16 pequenos/jovens → 8 analisados; **0 gates**; 1 outlier (Reality Broke Archive, 6,3×, Piltdown).
- **Não executadas (limite de 1 segunda busca na rodada):** `fake viral video documentary`, `scientific fraud documentary`, `internet hoax documentary` — usar na revalidação de 2–4 semanas, com `--age 45` para forçar o corte de idade, e seeds de caso (`Piltdown`, `Enfield`) no `--suggest` para medir profundidade limpa.
