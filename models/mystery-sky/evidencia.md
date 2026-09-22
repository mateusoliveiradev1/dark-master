# Evidência — Fenômenos aéreos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "UFO documentary" --max 8` + 1 busca estreita `python scripts/niche_scan.py --cluster "UAP documentary" --max 8` (defaults do script) + `--suggest "UAP"` + websearch (16+ URLs)
> Brief completo: `data/briefs/ufo-documentary.md` · JSON: `data/briefs/ufo-documentary.json` (gravados automaticamente pelo script)
> A saída do `--cluster` não foi salva em artefato pelo script nesta execução; os números estão transcritos abaixo e são reproduzíveis pelo comando citado.

## Veredito: **REPROVA**

- Canais pequenos analisados: **3 no total** (2 no brief + 1 no cluster; 1 repetido) | passam os 3 gates: **0** (meta ≥3) — RKA Scope e GSP Podcast falham **só na idade**; nenhum ≤45d.
- Emergentes (≤90d + 2/3 gates): **0** — os dois "quase" têm 348d e 168d.
- Fome do algoritmo (outlier ≥3×): **1 canal** (RKA Scope, 14,2×) — sinal: **não** (meta ≥2 canais; e o outlier é **ficção com IA**, não documentário — ver leitura abaixo).
- Autocomplete: **256 termos** no brief + **348 termos** no seed "UAP" (meta ≥15) — profundidade alta, com colisão semântica relevante ("uap" = hardware de rede, jogo e vapor em indonésio).
- Trends: **não coletado** — Google Trends retornou **HTTP 429** em 3 tentativas ("UFO documentary", "UAP sighting", "UAP documentary"); fallback usado: autocomplete.

**Leitura honesta:** a query-mãe ("UFO documentary") é dominada por mídia grande/legacy — de 26 canais encontrados, só **2** são pequenos (≤200k subs) e ≤365d. O cruzamento exato **"documentário de fenômenos aéreos" não mostrou nenhum canal pequeno rompendo na janela** (0/3 gates em 2 scans). O único flare (RKA Scope, 14,2×) é um **mockumentary sci-fi gerado com IA** ("scripted sci-fi mockumentary", na descrição oficial do próprio vídeo) — pede a estética "OVNI recuperado", mas não é o formato do modelo; não conta como fome do crossover documental. Em compensação, a **demanda e a atualidade do tema são excepcionais em 2026** (onda de arquivos oficiais: relatório AARO, releases do PURSUE, emenda Burlison, waiver do Pentágono) e o espaço de perguntas é profundo. Conclusão: **blueprint mantido, produção não autorizada**; re-scan com queries mais estreitas (abaixo) antes de qualquer piloto.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| RKA Scope | 17.100 | 348d | 938.045 | 6.307 | 011 | 14,2× — 776.404 — "Inside A Recovered UFO \| Sci-Fi Short Film" — 23/07/2026 |
| GSP Podcast | 61.400 | 168d | 64.695 | 20.784 | 011 | 0 |
| RKA Scope (cluster, mesmo canal) | — | — | — | — | — | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só o **gate de idade** falha. Brief: 26 canais encontrados → 2 pequenos ≤365d → 2 analisados (quota) → **0 passam**. Cluster "UAP documentary": 26 encontrados → 1 pequeno ≤365d → 1 analisado → **0 passam**. Houve ainda uma execução do cluster com filtro restritivo `--age 90` (0 canais ≤90d; descartada em favor dos defaults do script).

## Outliers (janela de 2–6 semanas)

- **RKA Scope** — **14,2×** — 776.404 views (scan) — "Inside A Recovered UFO | Sci-Fi Short Film" — 23/07/2026 — padrão: **ficção sci-fi em formato mockumentary, com vídeo gerado por IA** (a descrição do vídeo declara: "This is a scripted sci-fi mockumentary created for entertainment purposes... developed using AI-assisted tools"; canais de agregação registram 595.803 views na mesma janela). Não é documentário e não é replicável pelo modelo — mas prova que a **estética "arquivo + objeto recuperado"** tem tração de audiência.
- GSP Podcast — 0 outliers ≥3× (mediana 3.117 views; formato podcast, não documentário).
- Nenhum outro canal pequeno do recorte apresentou outlier ≥3× nos dois scans.

## Fome do algoritmo (cluster cross-canal)

**Não.** Apenas **1 canal** com outlier ≥3× nos 90 dias (RKA Scope) e fora do formato documental (ficção/AI). Não há 2–3 canais diferentes com outlier no mesmo cruzamento — o sinal de "algoritmo com fome" descrito em `23` não se confirmou. O que existe é fome de **tema** (demanda por arquivos/disclosure), demonstrada por: releases oficiais em série (161 arquivos em maio; 222 no segundo lote; 40 arquivos/19 vídeos no quarto lote em julho), audiência de documentários mainstream ("The Age of Disclosure" reportado como recorde de documentário da Amazon Prime) e tráfego de notícia (NewsNation/NewsX com centenas de milhares de views em vídeos sobre os arquivos).

## Demanda (autocomplete — top termos)

**Seed "UFO documentary" (256 termos):** `ufo documentary`, `ufo documentary 2025`, `ufo documentary 2026`, `ufo documentary the age of disclosure`, `ufo documentary jeremy corbell`, `ufo documentary james fox`, `ufo documentary brazil`, `ufo documentary australia`, `ufo documentary history`, `ufo documentary full length`, `ufo documentary disclosure`, `alien autopsy documentary`, `bentwaters ufo documentary`, `calvine ufo documentary`, `ufo conspiracy documentary`, `ufo documentary no ads`.

**Seed "UAP" (348 termos):** `uap news`, `uap footage`, `uap hearing`, `uap congressional hearing`, `uap tic tac`, `uap missile`, `uap hellfire missile`, `uap atc`, `uap briefing`, `uap breaking news`, `uap belgium`, `uap argentina`, `uap compilation`, `uap analysis`, `uap gerb`, `uap are real`.

**Achado de SEO/naming:** "UAP" colide com ruído forte — `uap ac lite`/`uap ac pro` (hardware Ubiquiti), `uapiti rdr2` (Red Dead Redemption 2) e "uap" em indonésio ("vapor", ex.: `uap bayi batuk pilek`). Recomendação: títulos sempre com contexto explícito ("UAP files", "UAP hearing", "UFO sighting"), nunca "UAP" sozinho; o termo de biblioteca é `ufo documentary` + ano.

## Trends (YouTube 12m)

- **Não coletado** — `The request failed: Google returned a response with code 429` em 3 tentativas (brief e retries manuais). Sem direção/rising registrados. Revalidar em outra janela; enquanto isso, usar autocomplete como proxy de demanda (profundidade 256 + 348).

## Comentários (demanda explícita)

Não coletado — `--comments rvaIBNsY35A` retornou `insufficientPermissions` (o `yt_auth` local está sem o escopo `youtube.force-ssl`; mesmo bloqueio registrado nos outros modelos). Proxy qualitativo de demanda: threads do r/UFOs tratando documentários como "most reasonable and least BS-y" (ex.: discussão de "Accidental Truth") — público pedindo abordagem sóbria, não sensacionalista.

## Fontes web (2+)

**Arquivos oficiais / atualidade 2026 (contexto do subnicho):**
- https://www.gillibrand.senate.gov/news/press/release/gillibrand-statement-on-release-of-fy2025-aaro-report — AARO FY2025 (21/07/2026): 319 relatos recebidos, 114 explicados, **205 não resolvidos**; 238 resolvidos como satellite flaring; 1 caso marítimo; 1 jet pack.
- https://burlison.house.gov/media/press-releases/house-adopts-burlison-amendment-establishing-uap-disclosure-framework — Emenda Burlison adotada na NDAA FY2027 (22/07/2026): coleção permanente de registros UAP no National Archives + review board.
- https://thedebrief.org/pentagon-opens-new-pathway-for-government-insiders-to-disclose-uap-information — waiver do Pentágono (16/09/2026) para insiders entregarem informação UAP ao PURSUE.
- https://www.pbs.org/newshour/video/horizons/2026/05/exploring-the-questions-surrounding-uaps-and-the-search-for-extraterrestrial-life — PBS Horizons (22/05/2026): governo dos EUA começou a liberar arquivos desclassificados.
- https://www.thaipbs.or.th/verify/en/content/12637 — checagem (14/05/2026): 161 arquivos foram realmente liberados; vídeo viral "de OVNI gigante" era **gerado por IA** (91,5% de probabilidade) — risco de desinformação no nicho.
- https://www.thenews.com.pk/latest/1408774-ai-enhanced-pentagon-floating-brain-ufo-video-goes-viral-sparks-conspiracy-theories — quarto lote de arquivos (10–11/07/2026): 40 arquivos, 19 vídeos; caso "floating brain" e o problema de enhancements com IA.
- https://oversight.house.gov/release/luna-continues-transparency-investigation-into-uaps — Task Force (01/04/2026) cobrando vídeos UAP do DoD/AARO.
- https://www.prnewswire.com/news-releases/push-for-uap-ufo-transparency-intensifies-as-members-of-congress-and-whistleblowers-call-for-release-of-groundbreaking-conclusive-files-302784861.html — coletiva no Capitólio (09/06/2026) com Grusch, Luna, Burchett, Moskowitz, Kean e James Fox.
- https://www.aaro.mil/UAP-Records — página oficial de registros UAP do AARO (fonte primária para episódios).
- https://disclosure.org/explore — cronologia do disclosure (inclui DefenseScoop: caseload do AARO passa de 2.000 casos, 10/03/2026).

**Casos-âncora do modelo (fontes primárias/reportagem):**
- https://www.archives.gov/research/military/air-force/ufos — National Archives: Blue Book, 12.618 relatos (1947–1969), **701 "unidentified"**.
- https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104590/unidentified-flying-objects-and-air-force-project-blue-book — fact sheet oficial da USAF sobre o Blue Book.
- https://www.theguardian.com/world/2025/feb/11/what-really-happened-in-calvine-the-mystery-behind-the-best-ufo-picture-ever-seen + https://en.wikipedia.org/wiki/Calvine_UFO_photograph — Calvine (agosto/1990): foto real, ficou **32 anos** fora do público (revelada em 2022); nota do MoD "no definite conclusions"; negativos desaparecidos.
- https://abcnews.com/Politics/pentagon-declassifies-navy-videos-purportedly-show-ufos/story?id=70364183 + https://www.mprnews.org/story/2023/07/27/us-recovered-nonhuman-biologics-from-ufo-crash-sites-former-intel-official-says — vídeos Navy (2004/2015) desclassificados em 2020; relato de Fravor (Tic Tac) [REPORTADO].
- https://www.azcentral.com/story/entertainment/life/2025/10/28/phoenix-lights-1997-arizona-lore-aliens-ufo/86934806007 + https://www.phoenixnewtimes.com/arts-culture/the-phoenix-lights-are-no-mystery-6661825 — Phoenix Lights (13/03/1997): dois eventos; o segundo atribuído a **flares LUU-2 de A-10 do Maryland ANG** (22h, Barry Goldwater Range); a formação em V nunca foi oficialmente atribuída.
- https://www.history.com/articles/wwii-ufos-allied-airmen-orange-lights-foo-fighters + https://www.smithsonianmag.com/air-space-magazine/what-were-mysterious-foo-fighters-sighted-ww2-night-flyers-180959847 — Foo Fighters (1944–45): relatos do 415th Night Fighter Squadron; radar não registrava; investigações sem conclusão.

**Canais e formato (referências competitivas):**
- https://ew.com/best-ufo-documentaries-8559858 + https://www.syfy.com/syfy-wire/sleeping-dog-ufo-jeremy-corbell-documentary-interview-with-director-michael-lazovsky — onda mainstream 2026: "The Age of Disclosure" reportado como recorde de documentário da Amazon Prime e "Sleeping Dog" (maio/2026) — demanda de audiência ativa no tema.
- https://realtimesubcount.com/UCIFk2uvCNcEmZ77g0ESKLcQ + https://hypeauditor.com/youtube/UCIFk2uvCNcEmZ77g0ESKLcQ — The Why Files: ~5,9–6M subs, ~1,2B views, engajamento 3,73%, média ~1,1M views/vídeo (set/2026); liderança do gênero "mistério/conspiração" com tom de entretenimento.
- https://gb.youtubers.me/the-why-files/youtuber-stats — estimativa pública de ganhos do Why Files: **$8,44k–$50,6k/mês** [ALEGADO].
- https://www.youtube.com/@DarkDocsSkies — Dark Skies: 675K subs, 544 vídeos, documentários faceless de aviação/militar (rede: Dark Docs 1,19M; Dark Seas 450K; Dark Tech 428K) — formato-análogo mais próximo do modelo.
- https://www.youtube.com/@InterstellarUAP — Interstellar UAP: 4,32K subs, 61 vídeos (canal pequeno real do espaço UAP; mix de entrevistas/clipes).
- https://www.unresolvedsignals.com/ — "Unresolved Signals" (2026): série documental de investigação que cruza arquivos governamentais (9 episódios, 95 fontes primárias, 27 países; pipeline com IA) — referência direta de posicionamento "seguimos os documentos".
- https://vidiq.com/youtube-stats/channel/%40ufonetworkhq — "UFO Network": 618K subs mas **canal legacy convertido em remixes musicais** (22,29M views totais; estimativa de receita $3/mês) — alerta: nome forte de nicho ≠ formato vivo.

**Monetização e compliance:**
- https://support.google.com/youtube/answer/6162278 — guidelines oficiais de advertiser-friendly (aplicam-se a título, thumb, descrição).
- https://www.mediapost.com/publications/article/411997/youtube-opens-ad-rev-monetization-for-dramatized-c.html — jan/2026: temas sensíveis dramatizados/non-graphic ganharam elegibilidade (child abuse e eating disorders excluídos).
- https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline — linha do tempo 2026: onda de enforcement de conteúdo inautêntico (jan/2026); **ago/2026**: conteúdo educacional/documental/news que retrata morte pode monetizar; regra de 6 meses de inatividade.
- https://www.netinfluencer.com/youtube-trust-and-safety-chief-details-three-categories-of-content-barred-from-monetization — Halprin (21/07/2026): 3 categorias barradas do YPP (genérico/template; off-putting; AI personas em temas sensíveis).
- https://engineering.nyu.edu/news/conspiracy-brokers-understanding-monetization-youtube-conspiracy-theories — estudo NYU (2022) [PRATICANTE]: canais de conspiração tinham ~11× mais anúncios predatórios e 2× mais monetização alternativa (Patreon/doações) — risco reputacional a evitar.
- https://reelpilot.app/blog/faceless-youtube-rpm-by-niche + https://eliro.pro/blog/faceless-vs-personal-brand-youtube-earnings — classes de RPM [ALEGADO]: History & Documentary $4–9; True Crime & Mystery $3–7; CPM faceless de History/Documentary $10–18.

## Saturação e riscos observados

- **O cruzamento formato×tópico admite canal novo?** Hoje: **não comprovado**. A query-mãe entrega mídia grande (26 canais, só 2 pequenos ≤365d) e nenhum canal pequeno no recorte "documentário de arquivo sobre fenômenos aéreos" passou os gates. Onde aparecem canais pequenos com tração é nos formatos **adjacentes**: mockumentary sci-fi com IA (RKA Scope — ficção) e podcast/clipes (GSP Podcast, Interstellar UAP). Hipótese de trabalho (a testar no re-scan): o diferencial "arquivo oficial + teste cético" ainda não tem player pequeno dedicado — ou o recorte de busca não o captura (provável: "UFO documentary" puxa catálogo antigo; termos como "UAP hearing/files" são news-driven e não retornam canais pequenos em search).
- **Riscos de advertiser/compliance:** adjacência a "controversial issues"/conspiração → limited ads; metadata enganosa (thumb "PROOF") derruba monetização; o contexto documental/educacional é favorecido pelas mudanças de jan–ago/2026, mas o nicho exige disciplina editorial (nunca afirmar encobrimento; vivos = alegação atribuída).
- **Riscos de desinformação/IA:** dois fact-checks independentes em 2026 (Thai PBS e Lead Stories/CRBC) derrubaram vídeos virais de "OVNI" gerados por IA ligados aos releases reais do DoD — footage sintético apresentado como registro = risco de política/reputação. Divulgar IA de produção é obrigatório; nunca usar vídeo gerado como "prova".
- **Direitos:** footage do governo dos EUA tende a domínio público, mas cada asset deve ser checado (Crown copyright nos arquivos britânicos; clipes de imprensa; música).
- **Prazo:** YPP dobra em 01/02/2027 para novos inscritos — janela de decisão curta se o re-scan aprovar.
- **Ruído de busca:** "UAP" colide com hardware/jogos/indonésio (ver Demanda) — afeta títulos, tags e a própria query de scan.

## Queries mais estreitas (se REPROVA)

Não executadas (limite de 1 busca extra cumprido). Candidatas para re-scan em 2–4 semanas, em ordem de prioridade:

1. `--brief "sky phenomenon documentary"` (a segunda opção de query original, não usada)
2. `--cluster "UAP hearing documentary"` (news-driven com demanda comprovada no autocomplete)
3. `--cluster "pilot ufo encounter documentary"` (recorte aviação/ATC)
4. `--cluster "radar ufo case documentary"` (recorte dados/radar)
5. `--cluster "declassified uap files"` (recorte arquivo oficial/PURSUE)

Recomendação: rodar com `--age 45`/`--max 8`, salvar os artefatos em `data/briefs/` e só promover o modelo a produção com **≥3 canais pequenos passando os 3 gates**. Se o re-scan reprovar de novo, a alternativa é rebaixar o lane para long-first e testar um único piloto de baixo custo (1 long + 3 shorts) antes de qualquer compromisso de calendário.
