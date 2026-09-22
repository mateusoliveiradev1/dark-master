# Evidência — Ataques de animais

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "animal attack documentary" --max 8` + retry estreito `python scripts/niche_scan.py --cluster "wild animal attacks documentary" --max 8` (Data API) + `--suggest` (HTTP livre, 5 seeds de subnicho) + checagem de convergência `--channel` em 5 canais (últimos uploads, com duração) + resolução de handle + tentativa de `--comments` + websearch.
> Brief completo: `data/briefs/animal-attack-documentary.md` · JSON: `data/briefs/animal-attack-documentary.json` (o cluster estreito imprime em tela, não salva JSON).
> Quota: ~550 unidades (estimativa) de ~10.000/dia — 2 buscas pesadas (brief + cluster), 5 checagens de canal, resolução de handles (1 search de 100 un), 2 tentativas de comentário; autocomplete/Trends são HTTP livre. O cluster estreito foi escolhido entre as duas opções do método porque o próprio autocomplete do brief já traz "wild animal attack documentary" e o maior flare da coleta ampla é um ataque nomeado (crocodilo, 19,9×); "deadly animals documentary" desloca o eixo para espécies perigosas, não para encontros.

## Veredito: **PARCIAL**

- Scan (gates): **REPROVA** — 0/8 na busca ampla + 0/8 no corte estreito (meta ≥3). Total 0/16.
- Emergentes (≤90d + 2/3 gates): **2 + 2 = 4** — watchlist, não aprovam sozinhos (WildLife Tv 77d; Animal Zone TV 26d; Wild zora 66d; Animal Zone TV repete no segundo corte).
- Fome do algoritmo (outlier ≥3×): **7 canais** no total — 2 na busca ampla e 5 no corte estreito (com sobreposição; Animal Zone TV e WildLife Tv foram flagrados no check de canal). Sinal: SIM nos dois cortes, com flares de 169,9× / 107,6× / 32,9× / 20,5× / 19,9× / 10,3×.
- Autocomplete: **84 termos** no seed principal (meta ≥15; metade é ruído de filme) e **246–364 termos** nos seeds de subnicho (shark 364, snake bite 346, bear 336, crocodile 308, orca 246).
- Trends: **429 nas duas consultas** (rate limit do Google; sem leitura de direção — fallback autocomplete).

Leitura honesta: o cruzamento **não fecha os 3 gates** em nenhum dos cortes (o gargalo continua sendo idade ≤45d — o mesmo padrão da biblioteca), mas a fome é forte e a demanda é profunda: 7 canais com outlier ≥3×, 4 emergentes (três deles ≤77 dias, falhando só a idade ou só os 5 primeiros) e 246–364 termos de autocomplete por subnicho. O detalhe que muda a decisão: **quase todo o rompimento atual está em Shorts de luta/especulação** (Wild zora, 169,9×, 11s; Animal Zone TV, 107,6×, 24s; Info Wild News, 19,9×, 34s) — exatamente a categoria que a política de monetização trata como risco quando vira série repetitiva de "animais em perigo/angústia". O lane de documentário longo em EN está jovem (GaiaDocs, 272d, flare 10,3× em ago) e é o menos ocupado. **Não escalar ainda**; revalidar em 2–4 semanas. O modelo entrega o tema pelo formato de menor risco (documentário com fonte e prevenção), não pelo formato que está pegando fogo.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

### Busca 1 — `--brief "animal attack documentary"` (37 canais achados; 10 pequenos e ≤365d; 8 analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| WildLife Tv (@wildlifetvanimal) | 59.500 | 77d | 20.640 | 501.150 | 011 | 4 flares no check de canal (5,7× / 5,1× / 4,3× / 3,1× — 12,7k–16,7k views) (**emergente**) |
| manishpedia | 163.000 | 101d | 33.220.396 | 2.190.526 | 011 | — |
| GaiaDocs (@gaiadocsen) | 56.000 | 272d | 4.556.597 | 97.898 | 011 | 10,3× — 2.379.933 — WILD AMAZON (2026-08-19) |
| Decode Universe | 116.000 | 157d | 490.461 | 826.902 | 011 | — |
| Creature Science Hub | 6.920 | 138d | 26.863 | 26.735 | 011 | — |
| Animal Zone TV (@animalzonetv-n8u) | 3.960 | **26d** | 6.864 | 339.317 | 101 | 107,6× — 182.428 (2026-09-20); 49,3× — 83.588 (2026-09-20) (**emergente**) |
| Info Wild News (@infowildnews) | 27.100 | 347d | 575.875 | 114.289 | 011 | 19,9× — 1.749.394 — crocodilo (2026-09-08) |
| JUNGLE x science | 1.600 | 111d | 323 | 29.344 | 001 | — |

### Busca 2 — `--cluster "wild animal attacks documentary"` (29 canais achados; 9 pequenos e ≤365d; 8 analisados)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| GaiaDocs (@gaiadocsen) | 56.000 | 272d | 4.556.597 | 97.898 | 011 | 10,3× — 2.379.933 (2026-08-19); 3,0× — 702.169 (2026-09-16); 6,9× — 1.587.379 (2026-08-24, check de canal) |
| Fact D. Man (@factdman) | 8.870 | 332d | 284.677 | 31.232 | 011 | 32,9× — 2.156.670 — "Most Incredible Animal Moments" (2026-08-09) |
| Decode Universe | 116.000 | 157d | 490.461 | 826.902 | 011 | — |
| Animal Zone TV (@animalzonetv-n8u) | 3.960 | 26d | 6.864 | 339.317 | 101 | 107,6× / 49,3× (2026-09-20) (**emergente**) |
| Info Wild News (@infowildnews) | 27.100 | 347d | 575.875 | 114.289 | 011 | 19,9× — 1.749.394 (2026-09-08); 4,0× — 348.098 (2026-08-20) |
| HSD CineFlix BD | 168.000 | 286d | 1.917.766 | 540.785 | 011 | 20,5× — 1.272.737 — short em bengali (2026-09-18) |
| HermeX Vision | 1.370 | 231d | 1.336 | 13.592 | 001 | — |
| Wild zora (@wildzora-c8u) | 1.920 | **66d** | 231.217 | 50.556 | 011 | **169,9× — 594.718** (2026-08-24) (**emergente**) |

> Gates em ordem: idade≤45d / 5primeiros≥10k / ≥1k views/dia (1 = ok, 0 = falha).
> Nota de método: o campo "5 primeiros" do scan é a soma dos **5 mais antigos entre os 15 uploads mais recentes** (convenção do script), não dos 5 primeiros da história do canal — por isso canais antigos com hit histórico (WildLife Tv, 38,5M views totais em 82 vídeos) podem ter "5 primeiros" baixo. O gate de views/dia usa total de views ÷ idade.

## Outliers (janela de 90 dias; oportunidade de 2–6 semanas quando recente)

- **Wild zora — 169,9× (FLARE)** — 594.718 views — "🐾 Tiny Terror Attacks Giant Hippo! 😱 | Unbelievable Wildlife Fight" (2026-08-24, 11s) — canal de 66 dias; série "Mother Honey Badger vs X" com picos de 1.131.322 (07/09), 691.456 (27/08) e 601.679 (08/09) alternando com vídeos de 840 e 97 views. Formato de luta/especulação (possivelmente sintético) — maior flare da coleta e o mais próximo do risco de política.
- **Animal Zone TV — 107,6× (FLARE)** — 182.428 views — "The Lion Walked In… and Took Their Entire Meal!" (2026-09-20, 24s) — canal de 26 dias; segundo flare no mesmo dia (83.588, 27s). Shorts de leão/búfalo, quase diário.
- **Fact D. Man — 32,9× (FLARE)** — 2.156.670 views — "The Most Incredible Animal Moments Ever Recorded" (2026-08-09, 2m20) — compilação "caught on camera"; canal sem upload desde 23/08.
- **HSD CineFlix BD — 20,5× (FLARE)** — 1.272.737 views — short em bengali de leões e javali selvagem (2026-09-18).
- **Info Wild News — 19,9× (FLARE)** — 1.749.394 views — "Why Animal Not Servive Crocodile Attack" (2026-09-08, 34s) — maior outlier em views absolutas entre os Shorts EN; template de título com erro proposital/gramatical.
- **GaiaDocs — 10,3× / 6,9× / 3,0× (FLARE + fortes)** — 2.379.933 (WILD AMAZON, 19/08) / 1.587.379 (WILD COLOMBIA, 24/08) / 702.197 (WILD PACIFIC, 16/09) — documentário longo (1h03–1h46) por região, o formato menos saturado do cruzamento.
- **WildLife Tv — 5,7× / 5,1× / 4,3× / 3,1×** — 16.692 / 14.907 / 12.697 / 9.000 views — shorts de 13–27s "Educational Wildlife Story" (set/2026); números pequenos em absoluto.

## Fome do algoritmo (cluster cross-canal)

- **Ampla (`animal attack documentary`):** 2 canais com outlier ≥3× — GaiaDocs (documentário longo de predadores) e Info Wild News (short de crocodilo). Padrão: **ataque nomeado no título** (crocodilo, leão) + bicho não-leão no pacote.
- **Estreita (`wild animal attacks documentary`):** 5 canais com outlier ≥3× — GaiaDocs, Fact D. Man, Info Wild News, HSD CineFlix BD e Wild zora. Padrão cross-canal: **predador em ação + linguagem de conflito** ("attack", "vs", "fight", "survive") em Shorts, e **compilação "caught on camera"** no médio (1–2 min); apenas GaiaDocs opera no formato documentário longo.
- Ressalva honesta: o cluster ranqueia os top-50 vídeos do tema por views em 90 dias, então os ratios medem o contraste contra a mediana de cada canal, não a saúde média do canal. WildLife Tv (501 mil views/dia) tem esse número puxado por hit histórico e uploads recentes de três dígitos — prova de que o gate de views/dia premia biblioteca, não momentum.

## Convergência de formato observada (últimos uploads, com duração)

- **GaiaDocs** (@gaiadocsen, EN): 10 vídeos analisados entre 31/08 e 21/09; **1h03–1h46**; série "WILD [REGIÃO] | [hook] | Nature Animal Documentary"; cadência de 2–4 dias; flares em ago; os dois uploads mais recentes ficaram em 137.360 e 69.121 — abaixo da mediana (231.271). É a âncora EN de documentário longo do cruzamento.
- **Info Wild News** (@infowildnews, EN): **29–45s**; template "Why/Will ... By info wild news" com erro gramatical; crocodilo, leopardo, lobo; cadência ~2–3/semana; 10 vídeos entre 15/08 e 19/09.
- **WildLife Tv** (@wildlifetvanimal, EN): 82 vídeos em 77 dias (38,5M views totais); mistura **shorts de 13–27s** e "Educational Wildlife Story" de **4–6 min**; uploads recentes em 143, 165 e 193 views — volume alto com hit histórico carregando o total.
- **Animal Zone TV** (@animalzonetv-n8u, EN): 39 vídeos em 26 dias (até 2/dia); **shorts de 8–49s** de leão/búfalo com emoji no título; flares em 20/09 e depois 28 e 8 views em 21–22/09 — volatilidade típica de feed de Short.
- **Fact D. Man** (@factdman, EN): 140 vídeos; **compilações de 1m19–2m20** ("Most Incredible / Unbelievable Animal Moments Caught on Camera"); sem upload desde 23/08; flare de 32,9× em 09/08.
- **Wild zora** (@wildzora-c8u, EN): 27 vídeos desde 17/07; **shorts de 11s** (alguns 17–38s); série "Mother Honey Badger vs [predador]" com maiúsculas e emoji; alternância extrema entre hit e zero — formato de aposta, não de biblioteca.
- **Não inspecionados:** HSD CineFlix BD (bengali) e manishpedia — sem handle resolvido nesta rodada.

## Demanda (autocomplete — top termos)

- **Seed principal (84 termos):** metade é ruído de filme (`animal attack movie`, `in hindi dubbed`, `tamil`, `sinhala`). Termos úteis para o modelo: `wild animal attack documentary`, `animal attack human documentary`, `animal attack documentary jungle`, `animal attack documentary predator`, `animal planet hindi documentary lion attack`.
- **Subnichos (246–364 termos cada):**
  - `shark attack` — 364: australia, sydney, dee why, israel, 2025, animation (ruído).
  - `snake bite` — 346: first aid, treatment, caught on camera, lion (conteúdo animal).
  - `bear attack` — 336: japan, dog, hunter, climber, greece, movie (ruído).
  - `crocodile attack` — 308: lion, zebra, hyena, boat, australia, animals compilation.
  - `orca attack` — 246: boat, yacht, portugal, seal, great white shark drone.
- Leitura: a demanda do público é **por conflito e encontro** (contra-ataque, captura, sobrevivência), não por "espécie perigosa" genérica — o título do episódio deve carregar o encontro, e o corpo entrega a ciência.

## Trends (YouTube 12m)

- **429 nas duas consultas** (brief e `--trends "animal attack documentary"`) — rate limit do Google no mesmo dia; sem leitura de direção. Fallback: autocomplete (84 + 1.600+ termos nos 5 subnichos) + janela de fome (7 canais). Reexecutar em outro horário.

## Comentários (demanda explícita)

Não coletado nesta rodada — `--comments` retornou `insufficientPermissions` nos dois testes: E20q1JmDvJo (Info Wild News, 1.749.394 views) e p15gr8nhfns (GaiaDocs, 702.197 views). O escopo `youtube.force-ssl` precisa ser habilitado com `python scripts/yt_auth.py`. Próximo passo do piloto: minerar comentários de 1 vídeo do Info Wild News, 1 do GaiaDocs e 1 do Animal Zone TV.

## Fontes web (2+)

- https://support.google.com/youtubecreatorstudio/answer/1311392 — [OFICIAL] política de monetização lista como inelegível "channels that heavily rely on generic templates or emotionally manipulative themes, like a series showing repetitive scenarios of animals in exaggerated distress or peril" — é a descrição do anti-modelo deste nicho.
- https://support.google.com/youtube/answer/6162278 — [OFICIAL] advertiser-friendly: "non-graphic depictions of animal violence in the natural world" é elegível; ferimento gráfico focal, sofrimento prolongado e caça com gore focal = limited/no ads; sofrimento induzido por humanos (resgate encenado etc.) = sem ads.
- https://support.google.com/youtube/answer/2802008 — [OFICIAL] política de conteúdo violento/gráfico: exceções para contexto documental, educacional ou científico; regras de abuso animal.
- https://www.auditsocials.com/blog/youtube-2026-advertiser-friendly-update-controversial-issues-monetizable-brand-safety — [REPORTADO] atualização 2026: temas controversos monetizáveis quando não gráficos e dramatizados; clarificação de março/2026: sujeito que parece jovem (humano ou não) em sofrimento, ougore/repulsa, não é elegível.
- https://youtubecreator.online/en/articles/youtube-updated-monetization-rules-for-controversial-and-shocking-content — [REPORTADO] mesma atualização, com a leitura de "restraint vs sensationalism".
- https://outlierkit.com/channel/wildus-x7s — [REPORTADO] análise de canal real do subnicho ("Wild Us", 47K subs, 22,3M views, est. $4–12K/mês incl. patrocínio): modelo de compilação de footage de terceiros com risco severo de demonetização e copyright; breakouts em predadores não-leão (orca, cão selvagem, águia, hiena, honey badger); recomenda narração estruturada e Shorts de 30s como funil.
- https://www.noodletomato.com/niches/science-nature/animal-attacks-caught-on-camera — [ALEGADO] estimativas do subnicho: vídeo típico 19–33 min, $265–796 por vídeo, canal médio acumula $524–1,6K, melhor vídeo ~$11,3K, cadência a cada 4 dias; vizinhos: crocodilo $1,5–4K, big cats $1,3–3,5K, ursos $597–1,6K por canal.
- https://www.noodletomato.com/niches/science-nature/crocodile-and-alligator-attack-footage — [ALEGADO] crocodilo: $359–958 por vídeo; melhor vídeo 8,4M views; canal "Scary Animal Attacks" (28,4K subs, ~4 uploads/mês, ~$22,6K acumulado est.).
- https://fluxnote.io/guides/faceless-youtube-animal-nature-niche-guide — [ALEGADO] guia 2026: RPM $3–6 em animal/natureza; 100k views/mês ≈ $300–600; afiliados de fauna ($30–200/venda); patrocínio $500–2.000/vídeo a partir de 50K subs; footage Artgrid $15–25/mês; subniche "dangerous animals" com engajamento alto; narração documental.
- https://www.linkedin.com/posts/usmannow_faceless-animal-attack-channels-are-blowing-activity-7269350077796675584-VVBS — [ALEGADO] caso publicado de canal de 108 dias: 538.658 views/mês e $4.309,26/mês a $8 de RPM, vídeos de 30+ min.
- https://longformstudio.app/articles/youtube-documentary-channel — [ALEGADO] documentário/educação: CPM $10–25 (≈$2,75–6,88 de RPM); retenção saudável 30–45% em vídeos de 15–30 min; YPP 1.000 subs + 4.000h hoje, com piso dobrado a partir de 01/02/2027 (8.000h/20M Shorts).
- Reddit (demanda): https://www.reddit.com/r/Documentaries/comments/1t6otir/maneating_prides_nature_shock_2008_5001/ (2026-05-07, leões que passaram a caçar humanos na Tanzânia); https://www.reddit.com/r/sciencedocumentaries/comments/2cufer/ (estratégias de caça de orcas); https://www.reddit.com/r/Documentaries/comments/45kj1e/ (grande branco) — o público de documentário pede predador + comportamento, não só o ataque.
- Nat Geo (demanda de marca, 2026): https://www.youtube.com/watch?v=XWywpARYgmA ("Human-Animal Encounters in the Wild", 03/06/2026, 75,9K views) e https://www.youtube.com/watch?v=vilevuVVjho ("Deadly Encounters", 2026) — séries ativas de encontros reais no mesmo ano.
- Canais verificados por URL: https://www.youtube.com/@gaiadocsen · https://www.youtube.com/@infowildnews · https://www.youtube.com/@wildlifetvanimal · https://www.youtube.com/@animalzonetv-n8u · https://www.youtube.com/@factdman · https://www.youtube.com/@wildzora-c8u

## Saturação e riscos observados

- **O cruzamento ainda admite canal novo?** Sim, com ressalva. O feed de Shorts está quente mas é o campo mais perigoso (luta, especulação, "fight", títulos de angústia — exatamente o que a política cita como inelegível quando vira série repetitiva). O documentário longo em EN está quase vazio (GaiaDocs é o único com formato sério, e seus dois últimos uploads ficaram abaixo da mediana). **Núcleo não coberto na coleta:** o encontro com fonte primária, ciência do comportamento e prevenção — ninguém no feed faz isso com estrutura de série.
- **O que está saturado:** compilação "caught on camera" (Fact D. Man; Wild Us), shorts de 11s de luta de animais (Wild zora) e template de 30–45s de ataque com bicho grande (Info Wild News) — modelos baratos de copiar e com risco de reused content/demonetização [REPORTADO — OutlierKit].
- **Gargalo real:** idade ≤45d falha em 16 de 16 canais dos dois cortes. Emergentes de 26–77 dias estão a 1–3 semanas de cruzar o gate — revalidar em 2–4 semanas.
- **Riscos de advertiser:** violência animal não gráfica é elegível [OFICIAL], mas o formato deste nicho encosta na linha em três pontos: ferimento gráfico focal, sofrimento prolongado e angústia repetitiva. Mitigação: foco em biologia, cronologia sem gore, resposta e prevenção; autoclassificação honesta; zero "momento do ataque".
- **Direitos:** footage de vida selvagem de broadcast (BBC/NatGeo/Discovery) é copyright; footage de caçadores/criadores tem licença restrita. Base segura: licenciado (Artgrid/Storyblocks/Pond5) + institucional/público (USGS, NPS, NOAA, Wikimedia, Internet Archive) + mapas e diagramas próprios.
- **Sensibilidade:** sem imagem de vítima, sem áudio de gritos/sofrimento, sem reconstituição da morte; contagem de mortos só com fonte primária; nomes de vítimas apenas quando já são registro público e necessários ao caso — dados e respeito às famílias.
- **Diferenciação:** `nature-extreme` cobre desastre geológico/climático (terremoto, tsunami, vulcão, enchente); este modelo cobre o animal como agente (ataque, defesa, veneno, manejo). `mystery-ocean` cobre o oceano como mistério; aqui o predador marinho aparece pelo ataque e pelo comportamento. Não sobrepor.

## Queries mais estreitas (próxima rodada)

- `shark attack documentary` — maior profundidade de autocomplete (364 termos) e demanda evergreen.
- `snake bite documentary` — 346 termos; ângulo saúde/antiveneno (CPM potencialmente mais alto que o resto do modelo).
- `bear attack documentary` — 336 termos; subnicho com estimativas publicadas [ALEGADO].
- `crocodile attack documentary` — 308 termos; âncora Info Wild News (flare 19,9×) e subnicho vizinho com estimativas [ALEGADO].
- `man eating lions documentary` — casos históricos com registro de museu e livro (Tsavo, Njombe); público de documentário ativo no Reddit em 2026.
- `orca attack documentary` — 246 termos; fenômeno em curso desde 2020 na Península Ibérica.
- Testada nesta rodada: `wild animal attacks documentary` (cluster) — 0/9 gates, 5 canais com fome, 2 emergentes; revalidar em 2–4 semanas. `deadly animals documentary` não foi rodada (preterida na escolha do cluster).
- Nota de captação: `--cluster` não salva JSON (imprime em tela) — se quiser registro, capturar a saída; habilitar `force-ssl` no `yt_auth.py` para `--comments`.
