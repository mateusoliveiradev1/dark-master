# Evidência — Fraudes e golpes

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "fraud documentary" --max 8` + `python scripts/niche_scan.py --cluster "scam documentary"` + websearch
> Brief completo: `data/briefs/fraud-documentary.md` · JSON: `data/briefs/fraud-documentary.json`
> A saída bruta do cluster não foi salva em arquivo (execução manual); é reproduzível pelo comando acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: 8 únicos (9 linhas: 5 no brief + 4 no cluster; ALPHA DECODES repetiu) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **5 canais** nos dois scans, com **2 flares** (86,0× e 1.104,5×) — sinal: **sim**
- Autocomplete: 155 termos (meta ≥15) | Trends: **ALTA** (recente 60,25 vs anterior 49,0)

**Leitura honesta:** o scan bruto marca REPROVA porque nenhum canal pequeno tem ≤45 dias. Os 9 canais analisados falham a idade (57–297d); 8 deles passam os outros dois gates e falham **apenas a idade** (011). Há 5 canais com outlier ≥3× em dois scans, dois deles flares (>10×), e 1 emergente (57d, 2/3 gates). Isso não é PASSA (zero canais elegíveis pelos gates) e não é REPROVA (fome + emergente presentes na coleta). É PARCIAL: o formato×tópico mostra performance real, mas a janela de canal novo em EN ainda não está confirmada. Revalidar em 2–4 semanas com `--cluster "scam documentary" --age 45`.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Scan | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|---|
| Bodycam Exposed TV | brief | 13.900 | 190d | 1.803.050 | 42.552 | 011 | 86,0× — 1.640.052 — 2026-08-29 |
| ALPHA DECODES | brief+cluster | 13.300 | 184d | 596.683 | 14.110 | 011 | 3,9× — 616.524 — 2026-07-15 |
| Raaz Codex | brief | 3.150 | 139d | 520.424 | 5.680 | 011 | 31,5× — 171.454 — 2026-07-12 |
| **Animated Archives HQ** | brief | **1.650** | **57d** | **35.947** | **14.137** | 011 (emergente) | — |
| World's Greatest Heists | brief | 13.500 | 126d | 22.421 | 27.043 | 011 | — |
| Hidden Ops India | cluster | 71.300 | 184d | 2.407.736 | 102.709 | 011 | 12,8× — 4.201.123 — 2026-08-27 |
| Upscaled Documentry | cluster | 7.930 | 297d | 50.398 | 7.982 | 011 | 1.104,5× — 2.233.271 — 2026-08-29 |
| StoryFlix Studio | cluster | 1.140 | 190d | 1.165 | 1.583 | 001 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a idade falha; "001" = idade e 5 primeiros falham. Scan 1 (brief): 47 canais encontrados, 5 pequenos ≤365d analisados, 0/5 passaram. Scan 2 (cluster): 44 encontrados, 4 pequenos analisados, 0/4 passaram. Nenhum canal passa os 3 gates (0/9 linhas).

## Outliers (janela de 2–6 semanas)

- **Upscaled Documentry** — 1.104,5× — 2.233.271 views — "Vijay Mallya Story" — 2026-08-29 — padrão: documentário da queda de um tycoon endividado (canal de 7.930 subs, mediana 2.022) — flare; o eixo "o dinheiro que sumiu" com cifras explícitas.
- **Bodycam Exposed TV** — 86,0× — 1.640.052 views — "Nursing Student Tries to Deposit a $400K Stolen Check… Police Were Already Waiting | Legal Analysis" — 2026-08-29 — padrão: fraude do cotidiano (check fraud) + footage bodycam + análise legal — flare; golpe do dia a dia tem apetite próprio.
- **Raaz Codex** — 31,5× — 171.454 views — "Sukesh Chandrasekhar 215 Crore Scam | 2D Animated True Crime Documentary" — 2026-07-12 — padrão: golpe de alto valor + true crime em animação 2D.
- **Hidden Ops India** — 12,8× — 4.201.123 views — "Tukaram Mundhe ने कैसे खोली Food Mafia की पोल? | Asli Singha" — 2026-08-27 — padrão: exposé investigativo de rede de corrupção.
- **ALPHA DECODES** — 3,9× — 616.524 views — "Brazil's Most Perfect Bank Robbery…" — 2026-07-15 — padrão: análise de heist/assalto de alto valor.

## Fome do algoritmo (cluster cross-canal)

Sim. Cinco canais distintos com outlier ≥3× em duas coletas no mesmo mês, quatro deles com outlier em agosto/2026 (janela de 2–6 semanas aberta). Os formatos variam (bodycam + legal analysis, 2D animado, doc de tycoon, exposé, análise de heist), o que indica fome no **formato documentário de crime financeiro**, não em um caso único. No topo do mercado EN a demanda é visível em escala: Coffeezilla (4,71M subs; uploads recentes de 2,4–8,3M views) e Fern (5,22M subs; ~$19k–43k/mês estimados com 18,06M views [ALEGADO]). Ressalva importante: os canais pequenos dos dois scans são majoritariamente de língua hindi/índia ou bodycam EN. O recorte EN "fraud documentary" não entregou 3 canais jovens passando os gates.

## Demanda (autocomplete — top termos)

155 termos únicos (meta ≥15). Recorte aproveitável: `fraud documentary`, `fraud documentary uk`, `fraud documentary 2025`, `major fraud documentary`, `art fraud documentary`, `fyre fraud documentary`, `fraud cases documentary`, `crypto fraud documentary`, `mortgage fraud documentary`, `bank fraud documentary`, `medical fraud documentary`, `accounting fraud documentary`, `business fraud documentary`, `corporate fraud documentary`, `financial fraud documentary`, `insurance fraud documentary`, `online fraud documentary`, `money fraud documentary`, `fraud scandal documentary`, `fraud investigation documentary`, `check fraud documentary`, `wine fraud documentary`, `food fraud documentary`, `benefit fraud documentary`.

Ruído alto: ~metade da lista é filme indiano (`fraud movie …`) e há termos de grafia corrompida (`fraud documentary xbox`). Usar modificadores (`documentary`, `case`, `scheme`, cifra) em título e miniatura para desambiguar.

## Trends (YouTube 12m)

- Direção: **ALTA** (média recente 60,25 vs anterior 49,0) · Rising: nenhuma query listada pelo script.
- Leitura: interesse subindo no termo, sem breakout específico — combina com biblioteca evergreen + picos quando um caso novo estoura.

## Comentários (demanda explícita)

Não coletado nesta coleta — `--comments` exige o escopo `youtube.force-ssl` (pendente de re-auth, conforme rodada 1) e a passada foi limitada às duas buscas de dados. Repetir depois de `python scripts/yt_auth.py` em um vídeo-outlier (ex.: "Vijay Mallya Story").

## Fontes web (2+)

- https://www.youtube.com/@Coffeezilla — canal real: 4,71M subs, 537 vídeos, 566,7M views; long-form investigativo de 16–55 min; "Exposing a $300,000,000 Scam" 4,4M (3 meses), "I Found The $200,000 Missing Lego" 8,3M (2 meses); mantém disclaimer de hipérbole retórica e Patreon.
- https://www.youtube.com/channel/UCODHrzPMGbNv67e84WDZhQQ/about — Fern: 5,22M subs, 135 vídeos, "armchair documentaries" quase semanais, faceless (por @Simplicissimus).
- https://longformstudio.app/articles/youtube-documentary-channel — Fern estimada em $19k–43k/mês com 18,06M views (ViewStats) [ALEGADO]; CPM de documentário/educação $10–25 [ALEGADO]; retenção saudável 30–45% (15–30 min); requisito YPP sobe para 8.000h em fev/2027.
- https://sigmastory.in/fern-proves-high-end-3d-animation-and-documentaries-are-the-future-of-youtube — Fern: 4M+ subs em pouco mais de 2 anos, faceless; Electrify Video Partners adquiriu participação majoritária (50–80%) em 2025 — canal tratado como ativo.
- https://www.newyorker.com/news/letter-from-the-southwest/coffeezilla-the-youtuber-exposing-crypto-scams — perfil do Coffeezilla: campanhas de assédio, identidade oculta por anos, contato com os investigados para comentário antes de publicar.
- https://www.iheart.com/podcast/269-danny-de-hek-53194510/episode/coffeezilla-exposes-a-300m-scam-333529623/ — caso Goliath Ventures (alegado Ponzi de $328M): processo judicial, pressão jurídica sobre quem publica investigações e a regra prática de só repetir o que o autos já sustentam.
- https://storage.courtlistener.com/recap/gov.uscourts.txwd.1172793701/gov.uscourts.txwd.1172793701.140.1.pdf — docket real (exhibit em processo) que evidencia litígio em torno de conteúdo de exposição do nicho.
- https://www.overseeros.com/blog/successful-faceless-finance-youtube-channels — guia 2026 de canais faceless de finanças: "scam investigations" entre os subnichos de maior probabilidade de sucesso e maior carga legal; sponsor fit (identity protection, VPN); regras de confiança; disclosure FTC; política de conteúdo inautêntico.
- https://support.google.com/youtube/answer/1311392 — política oficial de monetização (conteúdo inautêntico/repetitivo), citada pela fonte acima.
- https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers — guia FTC de disclosure para afiliados e patrocinados, citado pela fonte acima.
- https://medium.com/@anirbanmukherjee1311/how-people-are-making-10-000-month-on-youtube-without-showing-their-face-complete-2025-a90be3e35d3c — estimativa [ALEGADO] de receita para canais faceless (Fern $80k/mês); divergente do ViewStats ($19k–43k) — registrar só como camada fraca de mercado.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Em tese, sim, com ressalva. A demanda sênior está comprovada (Coffeezilla e Fern em escala, Trends ALTA, 155 autocompletes, fome cross-canal em 5 canais), mas o tier pequeno EN não aparece nos scans — o que admite duas leituras: (a) o cruzamento "documentário EN de fraude" é mais duro para canal novo do que os recortes em hindi; (b) ruído de idioma da coleta. Caminhos menos disputados que a evidência aponta: queda de tycoon (flare 1.104,5×), check fraud/legal analysis (flare 86×), fraude de arte/vinho/luxo e fraude corporativa com documentos primários. Evitar entrar de frente no espaço "crypto scam commentary": Coffeezilla domina e o tema envelhece rápido.
- **Riscos:** difamação é o risco central — pessoa viva só como alleged/charged, com autos e direito de resposta (o próprio Coffeezilla já respondeu a processo e mantém disclaimer de hipérbole retórica); advertiser limitado em conteúdo controverso sem contexto documental; conteúdo inautêntico se o formato virar template sem pesquisa primária; direitos de footage jornalístico e de retratos; assédio/doxxing contra o criador (caso real no nicho); nenhum episódio pode virar conselho de investimento.

## Queries mais estreitas (se REPROVA)

- **Executada:** `scam documentary` (cluster, 44 canais encontrados, 4 pequenos analisados, 0/4 gates, fome em 2 canais).
- **Não executadas (limite de 1 segunda busca):** `ponzi scheme documentary`, `corporate fraud documentary`, `insurance fraud documentary`, `vijay mallya story` — usar na revalidação de 2–4 semanas, junto com `--age 45`.
