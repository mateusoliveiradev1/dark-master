# Evidência — Espionagem

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "spy documentary" --max 8` + `python scripts/niche_scan.py --cluster "cold war spy documentary" --max 8` + autocomplete (265 termos no brief) + websearch
> Brief completo: `data/briefs/spy-documentary.md` · JSON: `data/briefs/spy-documentary.json`
> A saída bruta do cluster não foi persistida em arquivo (execução manual, limite de uma segunda busca); é reproduzível pelo comando acima.

## Veredito: **PARCIAL** (brief: REPROVA; cluster: 0 gates)

- Canais pequenos analisados: **16** (8 no brief + 8 no cluster; sem repetidos entre os recortes) | passam os 3 gates: **0** (meta ≥3)
- Gates 2 e 3 (5 primeiros ≥10k · ≥1k views/dia): **12 dos 16** passam ambos — e esses 12 falham **só** no gate de idade (≤45d)
- Fome do algoritmo (outlier ≥3×): **6 canais no brief + 1 no cluster** — sinal **sim no brief**, **fraco no cluster EN**
- Emergentes (≤90d + 2/3 gates): **2** — Suspense Stories (47d) e Secret India 2D (65d), ambos no brief
- Autocomplete: **265 termos** no eixo `spy documentary` | Trends: **não coletado** (HTTP 429 em 3 tentativas)
- Comentários: **não coletado** — `--comments` retornou `insufficientPermissions` (yt_auth sem escopo `force-ssl`; tentativa no vídeo `9TSIz1HlHRI`, "KGB vs CIA", do Spy Wars: Declassified)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido em nenhum dos dois recortes** — o brief fecha em REPROVA e o cluster em 0 gates. A classificação PARCIAL segue a legenda do `models/README.md`: há fome (6 canais com outlier ≥3×, fome cross-canal em 5 deles no mesmo tema "espião sul-asiático") e há 2 emergentes ≤90d. O ponto crítico que o número esconde: **os flares do brief são Shorts e animação 2D em hindi** (Índia/Paquistão, ISI/R&AW) — outro mercado, outro formato, outra língua que não a do modelo. No recorte EN (cluster "cold war spy documentary"), a fome é fraca (1 outlier, 3.544 views) e os canais que passam os gates 2–3 têm 131–296 dias. Ou seja: **a demanda EN existe e é durável** (autocomplete `cold war`/`kgb`/`mossad`/`soviet`/WW2; pedidos do r/coldwar por "accurate espionage docs"), mas a evidência de um **canal novo EN ≤45d rompendo** ainda **não apareceu** nas duas coletas. Tratar como PARCIAL limítrofe: pilotar só com o ângulo mais defensável (arquivo declassificado + operação histórica) e **revalidar em 2–4 semanas com `--age 45`**. Se nenhum entrante EN ≤45d cruzar os gates, rebaixar para REPROVA e não escalar.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal (scan) | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|
| Himanshu Uncovers (brief) | 20.600 | 122d | 14.840 | 72.578 | 011 | 1.408,2× — 8.301.553 — "Neera Arya's Untold Story" (Short, hindi) — 2026-08-24 |
| WarVerse (brief) | 3.300 | 180d | 565.697 | 3.121 | 011 | 28,7× — 447.805 — "Indian Army Ke Beech Chhupa Tha Pakistani Spy" — 2026-09-03 |
| Suspense Stories (brief) | 5.230 | 47d | 53.960 | 41.956 | 011 | — |
| 2DDoc (brief) | 9.650 | 227d | 510.861 | 12.520 | 011 | — |
| India Doc (brief) | 15.300 | 265d | 567.137 | 13.176 | 011 | 3,1× — 211.073 — "How 3 Pakistani Women Tricked Ajit Doval" — 2026-06-24 |
| Secret India 2D (brief) | 558 | 65d | 794.531 | 11.479 | 011 | 1.916,6× — 789.654 — "Ajit Doval के वो 24 घंटे…" (2D, hindi) — 2026-07-28 |
| SpyNews UK (brief) | 1.370 | 103d | 309.620 | 2.980 | 011 | 580,5× — 308.557 — "Tommy Robinson exposes a Jihadi spy…" — 2026-09-10 |
| EpicDocx (brief) | 3.710 | 226d | 31.829 | 5.081 | 011 | 100,9× — 322.812 — "Milkman Catches ISI Spy" (2D) — 2026-08-04 |
| History Paradox (cluster) | 92.300 | 296d | 843.878 | 2.039.017 | 011 | — |
| Nitesh Upadhyay (cluster) | 22.500 | 235d | 563.405 | 68.606 | 011 | — |
| Super Transports (cluster) | 4.240 | 214d | 1.824 | 7.326 | 001 | — |
| Green Explains The Military (cluster) | 174 | 131d | 40.300 | 308 | 010 | — |
| Spy Dossier (cluster) | 102 | 192d | 887 | 192 | 000 | 28,1× — 3.544 — "One Tourist Photo Ended the CIA's 20-Year Manhunt" — 2026-08-16 |
| world trend wave news (cluster) | 1.790 | 146d | 61.748 | 84.151 | 011 | — |
| Military Studio (cluster) | 6.390 | 139d | 2.278 | 5.978 | 001 | — |
| Cold War Chronicles (cluster) | 6.680 | 285d | 17.210 | 2.302 | 011 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a idade falha; "001" = só views/dia passa; "010" = só os 5 primeiros passam. Brief: 8 canais pequenos analisados (quota). Cluster: 45 canais encontrados, 22 pequenos/jovens (≤200k subs e ≤365d), 8 analisados (quota). IDs dos canais do brief estão no JSON; a saída do cluster não foi persistida em arquivo.

## Outliers (janela de 2–6 semanas)

- **Secret India 2D** — 1.916,6× — 789.654 views — vídeo 2D animado sobre 24 horas de Ajit Doval (hindi) — 2026-07-28 — padrão: micro-história de agência de inteligência em animação 2D; canal de 558 subs.
- **Himanshu Uncovers** — 1.408,2× — 8.301.553 views — "Real Life Dhurandhar: Neera Arya's Untold Story" (Short, hindi) — 2026-08-24 — maior viewport absoluto da coleta; é **Short**, não long.
- **SpyNews UK** — 580,5× — 308.557 views — "Tommy Robinson exposes a Jihadi spy working inside parliament" — 2026-09-10 — outlier político/ativismo, não documentário de arquivo; risco de sensibilidade alto.
- **EpicDocx** — 100,9× — 322.812 views — "Milkman Catches ISI Spy" (2D) — 2026-08-04.
- **WarVerse** — 28,7× — 447.805 views — "Indian Army Ke Beech Chhupa Tha Pakistani Spy" — 2026-09-03.
- **India Doc** — 3,1× — 211.073 views — Ajit Doval vs 3 women — 2026-06-24.
- **Spy Dossier** — 28,1× — 3.544 views — "One Tourist Photo Ended the CIA's 20-Year Manhunt" — 2026-08-16 — padrão "arquivo da CIA + caçada de 20 anos", mas viewport absoluto baixo; o único sinal EN do cluster.

> Nota metodológica: ratios altos em canais de centenas a milhares de subs vêm de medianas baixas. No brief, o que importa é o viewport absoluto (300k–8,3M) — mas em hindi/2D. No cluster EN, nenhum outlier com viewport relevante.

## Fome do algoritmo (cluster cross-canal)

- **Recorte 1 — "espião sul-asiático" (jul–set/2026, SIM):** Secret India 2D (07/28, 789k), WarVerse (09/03, 447k), EpicDocx (08/04, 322k), SpyNews UK (09/10, 308k) e Himanshu Uncovers (08/24, 8,3M) — 5 canais diferentes no mesmo eixo temático ISI/R&AW/segurança interna. Fome real, mas de mercado regional (hindi/EN-Índia), formato Short/2D — **não do lane EN long-form**.
- **Recorte 2 — "cold war spy documentary" (cluster EN, FRACO):** apenas Spy Dossier (08/16, 3.544 views, 28,1×) — o algoritmo não mostra fome cross-canal relevante no EN histórico dentro da janela.

## Demanda (autocomplete — top termos)

- Eixo `spy documentary`: **265 termos**. Termos de demanda documental: `spy documentary uk`, `spy documentary cold war`, `spy documentary kgb`, `spy documentary mossad`, `spy documentary ww2`, `spy documentary russian`, `spy documentary soviet`, `israeli spy documentary`, `spy documentary 2025`, `spycops documentary`, `spy catcher documentary`, `spy documentaries full episodes`.
- **Ruído dominante:** a maioria dos 265 termos é `spy movie ...` (filmes, trailers, cenas, "explained in hindi") — a query "spy documentary" está diluída; use `cold war`/`kgb`/`mossad`/`declassified` para isolar intenção documental.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` e dois retries (`--trends "cold war spy documentary"`, `--trends "declassified files"`) retornaram **HTTP 429** (rate limit do Google) em 2026-09-22. Fallback usado: profundidade de autocomplete (265 termos). Revalidar em outro horário.

## Comentários (demanda explícita)

- **Não coletado** — `--comments` retornou `insufficientPermissions` (falta o escopo `youtube.force-ssl`). Tentativa registrada no vídeo `9TSIz1HlHRI` (Spy Wars: Declassified). Rodar `python scripts/yt_auth.py` e repetir. Demanda qualitativa via Reddit (ver Fontes): r/coldwar e r/AskHistorians pedem documentários **precisos** de espionagem na Guerra Fria (Ben Macintyre, "The Spy and the Traitor"; série "Cold War: The Spies Among Us") — sinal de público que valoriza rigor, não sensacionalismo.

## Convergência de formato (players EN observados)

- **Spy Wars: Declassified** (Postbox, set/2026: 27,4k seguidores; USA/Education) — documentários cinematográficos de espionagem/Guerra Fria; vídeo "KGB vs CIA" com pergunta de engajamento ("where are you watching from") e CTA de inscrição no corpo.
- **The WAR Room** — "WARNING: How the CIA Actually Stole a Soviet Nuclear Sub" (03/2026) e "The Mole Who Sold America's Deepest Secret" (01/2026): operação como problema de engenharia, ritmo de cronologia.
- **Pure Declassified** — "CIA Secret Wars: The Age of Undercover Operations | FULL DOC" (07/2026): formato documentário inteiro (biblioteca).
- **Eyes Wide Open** — "The CIA's Blond Ghost: Ted Shackley" (10/2025): 235,1k views, 1:21:49, categoria Education — prova de que bio de espião em deep dive longo performa.
- **Real Stories / Witness** — documentários de TV de 52 min republicados (28,7k e 12,2k views nos exemplos) — concorrência de footage licenciado; não copiar.
- **Cauda faceless pequena:** Shadow Files Documentary (377 subs, 49.234 views, 52 vídeos desde ago/2025) e COVERT FILES (160 subs, 22,9k views, 16 vídeos desde jan/2026) — volume alto com tração baixa; sinal de que "spy stories" genérico não basta.
- **Anti-modelo:** War of shadows: Declassified ("The Spies Who Became Ghosts", 02/2026) — narração sintética, filosofia genérica, afirmações sem fonte ("programas experimentaram..."), o padrão que a política de conteúdo inautêntico mira.

## Fontes web (2+)

- https://app.postbox.so/en/explorer/spy-wars-declassified_1199443 — Spy Wars: Declassified: 27,4k seguidores, USA/Education, documentários cinematográficos de espionagem e Guerra Fria (set/2026).
- https://www.linkedin.com/posts/usmannow_if-i-told-you-theres-a-faceless-channel-activity-7409231792462786560-7i2K — case Blackfiles [ALEGADO]: 236k+ inscritos, 20M+ views, +2,6M views e +22k inscritos em 28 dias, est. US$3,3–7,1k/mês de AdSense (dez/2025) — faceless de "segredos da CIA/arquivos vazados".
- https://socialcounts.org/youtube-channel-analytics/UCv5ZE1mpo2-5DSzouV0J8Ng — Shadow Files Documentary: 377 subs, 49.234 views, 52 vídeos desde 02/08/2025; descrição "spy history, secret operations, Cold War".
- https://socialcounts.org/youtube-channel-analytics/UC5WYYWK5O5WIClgkQxKPo0g — COVERT FILES: 160 subs, 22,9k views, 16 vídeos desde 12/01/2026; docs animados em 2D.
- https://faceless.my/niches/us-en/faceless-mystery-channel/ — declassified-document explainers "underserved relative to search demand" (exigem mais pesquisa); RPM do vertical mystery US$5–8 [ALEGADO]; risco central citado: "unsourced claims"/conspiracy framing; recomendação de estreitar sub-nicho.
- https://support.google.com/youtube/answer/6162278 — [OFICIAL] Advertiser-friendly: sensitive events (conteúdo que lucra/explora evento sensível não monetiza); "raw footage of armed conflict without educational context" e referências a FTO = limited/no ads.
- https://support.google.com/youtube/answer/9725604 — [OFICIAL] updates: ago/2026 libera monetização plena de temas controversial não gráficos/dramatizados; mantém inelegível conteúdo que explora/deprecia a guerra da Ucrânia.
- https://apnews.com/article/youtube-monetization-update-policy-controversial-issues-545e27e27e26e0baefb937c86620b676 — AP (jan/2026): mudança que permite monetização plena de conteúdo não gráfico sobre temas sensíveis — contexto documental favorecido.
- https://www.solicitorsjournal.com/sjarticle/rzucek-v-vinnicombe-youtube-conspiracy-videos-about-watts-murders-yield-40000-defamation-award — [REAL] abr/2026: YouTuber de true crime condenado a £40 mil + injunção por difamação no Reino Unido — precedente direto para pessoa viva citada em vídeo.
- https://www.prnewsblog.com/law/27469/former-cia-officer-sues-netflix-over-false-portrayal-in-spy-documentary/ — ação contra docudrama de espionagem (caso Wasp Network); nota de assimetria: ex-oficiais da CIA passam por pre-publication review e têm pouco poder de corrigir o registro.
- https://www.pingnetwork.in/knowledge/war-content-on-youtube/ — guia praticante: conteúdo de guerra é permitido em enquadramento educacional/documental, mas tende a limited ads; evitar thumbnails com injúria/explosão/morte.
- https://www.youtube.com/watch?v=9TSIz1HlHRI — Spy Wars: Declassified, "KGB vs CIA" (11/2025) — formato/CTA observados.
- https://www.youtube.com/watch?v=d7nOnLtqtrI — Pure Declassified, "CIA Secret Wars" (07/2026) — formato full doc.
- https://www.youtube.com/watch?v=-DuVeGlLEjw — War of shadows: Declassified (02/2026) — anti-modelo (narração genérica, sem fonte).
- https://www.youtube.com/watch?v=GCITKTqLDxk — Eyes Wide Open, "The CIA's Blond Ghost: Ted Shackley" — 235,1k views, 1:21:49.
- https://www.youtube.com/watch?v=3Te2o-ZMXfA — The WAR Room, "How the CIA Actually Stole a Soviet Nuclear Sub" (03/2026) — referência de produção.
- https://www.reddit.com/r/coldwar/comments/xxngy7/ + https://www.reddit.com/r/AskHistorians/comments/22tp6e/ — demanda por espionagem da Guerra Fria "accurate", com leitura de Ben Macintyre; público leitor, sensível a sensacionalismo.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Com ressalvas: (a) no EN, o eixo "cold war/KGB/Mossad" tem players grandes e antigos (History Paradox 92,3k subs e 2M views/dia; Nitesh Upadhyay 68,6k views/dia) e o faceless de arquivo ainda é pouco servido — a faceless.my aponta "declassified explainers" como subnicho com menos concorrência que o generic "mystery"; (b) a cauda faceless recente (Shadow Files 377 subs; COVERT FILES 160 subs) mostra que volume sem identidade não rompe; (c) o cluster tem 45 canais encontrados e nenhum entrante ≤45d nos 8 analisados — o gargalo é o gate de idade, e a pergunta da revalidação é se entrantes EN aparecem; (d) o padrão de fome comprovado na coleta é regional (hindi/Índia) e em Short/2D — não transferir para o EN sem medir.
- **Riscos de advertiser/compliance:** sensitive events e conflito (limited ads se o enquadramento não for educacional); FTO em tela limita ads; thumbnails com injúria/morte derrubam; conflitos atuais (Ucrânia/Gaza) = evitados por política e por reputação.
- **Riscos legais:** difamação de pessoa viva (precedente de £40k no UK em abr/2026); "implicação por edição" em docudramas; ex-oficiais de inteligência têm pouco poder de retificação — o ônus de rigor é do canal.
- **Riscos geopolíticos:** a versão "espião sul-asiático" que domina os outliers é sensível (Índia/Paquistão, nome de oficial vivo) e não é o lane do modelo; manter casos históricos consolidados com fonte documental.
- **Risco de inautenticidade:** a onda de canais de "spy stories" sintéticos (anti-modelo acima) é exatamente o alvo da política; a defesa é a peça primária por vídeo + estrutura que varia + posição explícita.

## Queries mais estreitas (para revalidação)

- **Executada:** `cold war spy documentary` (cluster; 45 encontrados → 22 pequenos/jovens → 8 analisados; 0 gates; 1 outlier fraco).
- **Não executadas (limite de 1 segunda busca):** `declassified documentary` (a alternativa oferecida — testar isolando o ângulo "arquivo"), `mossad operation documentary`, `cia declassified files`; e revalidar o brief com `--age 45` para forçar o corte da idade e capturar entrantes EN.
