# Evidência — Cultos e seitas criminosas

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "cult documentary" --max 8` + 1 busca estreita (`python scripts/niche_scan.py --cluster "cult survivor documentary" --max 8`) + websearch
> Brief completo: `data/briefs/cult-documentary.md` · JSON: `data/briefs/cult-documentary.json`
> A saída do `--cluster` não foi salva em artefato (rodou sem `--out`); os números estão transcritos abaixo.

## Veredito: **REPROVA**

- Canais pequenos analisados: **9** no total (1 no brief + 8 no cluster) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **1** canal (namthos, 3,9× com 213 views) — sinal: **não** (meta ≥2 canais)
- Autocomplete: **225 termos únicos** (meta ≥15) — porém só **40** são de documentário; **183** citam "movie/film" (cinema indiano/Kannada), ruído
- Trends: **ESTÁVEL** (recente 52,5 vs anterior 56,6) · rising: "cult of personality" (+150%)

> Reprovou nas **duas** queries permitidas. O modelo existe como blueprint, mas produção em escala fica condicionada a re-scan que passe os gates (ver "Queries mais estreitas").

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Bubble Talks Movies | 14.700 | 57d | 922.592 | 320.923 | 011 | 0 |
| Trial & Crime | 1.160 | 61d | 50.957 | 3.608 | 011 | 0 |
| USA Crime Evidence | 917 | 41d | 3.045 | 5.991 | 101 | 0 |
| Real Archives | 577 | 84d | 8.143 | 557 | 000 | 0 |
| MN Fifty Fifty One | 2.190 | 292d | 3.064 | 291 | 000 | 0 |
| The Cold Case Desk | 113 | 61d | 1.960 | 305 | 000 | 0 |
| The Real NIFB Parody | 470 | 361d | 818 | 1.664 | 001 | 0 |
| Cult Files | 32 | 125d | 189 | 62 | 000 | 0 |
| namthos | 9 | 52d | 626 | 37 | 000 | 3,9× |

Leitura honesta: os três "quase" não são do subnicho. **Bubble Talks Movies** (14,7k subs) é um canal de cinema/entretenimento capturado pelo termo "cult documentary"; **Trial & Crime** e **USA Crime Evidence** são true crime geral (não cultos). Nenhum canal de culto long-form puro apareceu rompendo na janela. O único canal diretamente de culto (**namthos**, 9 subs) não é evidência de nada em escala.

## Outliers (janela de 2–6 semanas)

- **namthos** — 3,9× (213 views vs mediana 55) — "The Cult That Branded Its Own Members.. #CultDocumentary #Tr" — 2026-08-17 — padrão: Short de culto com gancho de objeto (marca/ferro). Base minúscula (9 subs) → flare fraco, não replicável como sinal.
- Demais canais analisados: 0 outliers ≥3×. Mediana de exemplo: Trial & Crime 1.806 views (sem vídeo ≥3×); Real Archives 1.728 (sem ≥3×).

## Fome do algoritmo (cluster cross-canal)

1 canal com outlier ≥3× em 90 dias (namthos) — **não há 2 canais diferentes com outlier no mesmo tema**. Sem fome detectável no cruzamento.

## Demanda (autocomplete — top termos)

Termos úteis extraídos dos 225 (o restante é "cult movie" — cinema indiano):

- cult documentary / cult documentary 2026 / cult documentary netflix / cult documentary trailer / cult documentaries full length
- documentary about cult / documentary on cult / worst cult documentary
- cult survivor documentary (tema do cluster) / cult escape documentary / leaving cult documentary / cult deprogramming documentary
- cult leaders documentary / cult leader film / cult of mother god documentary / cult next door
- cult crime documentary / cult religion documentary / aum cult documentary / nuwaubian cult documentary / oregon cult documentary / australian cult documentary / cult documentaries rotten mango / cult documentaries kallmekris

Profundidade real do espaço de perguntas (sistema, saída, líder, financiamento) é consistente — mas a demanda de busca é dominada por títulos de streaming (Netflix) e criadores grandes.

## Trends (YouTube 12m)

- Direção: **ESTÁVEL** (sem aceleração).
- Rising: **"cult of personality" (+150%)** — única query em alta; encaixa no subnicho "cultos de personalidade/poder".

## Comentários (demanda explícita)

Não coletado em vídeo específico: o brief/cluster não expõem VIDEOID e `--comments` exige escopo `youtube.force-ssl`. Proxy qualitativo: thread do r/cults "I've seen every documentary about cults – these are the eight best" (abr/2026, 52 up / 33 comentários) — público ativamente pedindo **mais** listas e títulos além do catálogo Netflix. Sinal de demanda de audiência, não de canal rompendo.

## Fontes web (2+)

- https://www.youtube.com/watch?v=QNX6UNyA90w — Visual Venture, "Secret Cults Hiding in Plain Sight Today" (jan/2026): exemplo real de canal faceless de cultos em long-form narrado (casos: Happy Science, Love Has Won).
- https://facelesslab.video/blog/en/faceless-true-crime-videos — formatos faceless de true crime em 2026; RPM "mid-double digits" [ALEGADO]; regra de tom contido para manter monetização.
- https://longformstudio.app/articles/true-crime-youtube-channel — risco de yellow icon por formato; RPM reportado $6–9 em true crime educacional non-graphic [ALEGADO]; YPP sobe para 8.000h/20M em 01/02/2027; proibição de simular vítimas (jan/2024).
- https://podcastor.ai/blog/how-to-start-a-true-crime-youtube-channel — sub-nicho "Cult, Conspiracy & Hidden History" = público large, monetização "very high", ideal para long-form binge; RPM $4–12 [ALEGADO].
- https://support.google.com/youtube/answer/6162278 — diretrizes de advertiser: contexto documentário/educacional pesa; gore/imagens gráficas no thumbnail ou primeiros 15s derrubam para limited/no ads.
- https://www.youtube.com/watch?v=vjX4RqqyCx4 (Creator Insider) + https://www.tubefilter.com/2026/01/15/youtube-sensitive-content-ad-monetization-guidelines-update/ — jan/2026: temas sensíveis (abuso, autoagressão etc.) monetizam pleno se dramatizados/non-graphic; **child abuse e eating disorders seguem excluídos**.
- https://www.auditsocials.com/blog/youtube-2026-advertiser-friendly-update-controversial-issues-monetizable-brand-safety — detalha a mudança de jan/2026 e a clarificação de mar/2026 (jovens em sofrimento, shock/gore = inelegível).
- https://www.mirror.co.uk/tv/tv-news/trust-me-false-prophet-netflix-36908684 + https://www.reddit.com/r/cults/comments/1s11vw2/ — "Trust Me: The False Prophet" (Netflix, abr/2026): demanda mainstream de cultos ativa em 2026.
- https://rephonic.com/podcasts/the-cult-vault — The Cult Vault: formato survivor-first (entrevistas + deep dives) com YouTube; referência de voz e posicionamento do subnicho.
- https://www.youtube.com/c/CultVault + https://www.youtube.com/@cultcoffin — canais reais do espaço "cult" (tom sombrio; evitar conflito de nome no branding).

## Saturação e riscos observados

- **Formato×tópico:** a busca geral está poluída (183 de 225 termos citam "movie/film") e o topo é ocupado por docs de streaming e canais grandes de true crime; no recorte "survivor", 34 canais mapeados, 14 pequenos, mas nenhum passando os 3 gates. O espaço admite canal novo **somente** se o re-scan confirmar um cruzamento mais estreito (ex.: estrutura de controle/exit story com peça primária) — hoje: não validado.
- **Advertiser/compliance:** conteúdo gráfico, thumbnail com cena de crime e detalhes de abuso sexual/child abuse são o maior risco de yellow icon; documentário contextualizado e non-graphic é o que monetiza (jan/2026). Publicar sem gore é pré-requisito do modelo.
- **Outros:** difamação (vivos = reported/alleged); exploração de sobreviventes; proibição de síntese de fala de vítimas; YPP mais duro a partir de 01/02/2027 (8.000h/20M).

## Queries mais estreitas (se REPROVA)

Não rodadas nesta coleta (limite de 1 busca extra cumprido). Candidatas para re-scan em 30 dias, em ordem de prioridade:

1. `--cluster "cult escape documentary"`
2. `--cluster "cult deprogramming documentary"`
3. `--cluster "leaving cult documentary"`
4. `--cluster "cult leaders documentary"`
5. `--cluster "cult next door"`
6. `--cluster "nuwaubian cult documentary"`

Recomendação: salvar os artefatos do re-scan em `data/briefs/` (o `--brief` já grava sozinho) e atualizar este arquivo com o resultado. Só promover o modelo a produção com **≥3 canais pequenos passando os 3 gates**.
