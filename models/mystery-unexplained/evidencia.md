# Evidência — Mistérios inexplicados

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "unexplained mystery documentary" --max 8` + `python scripts/niche_scan.py --cluster "unsolved mystery documentary" --max 8` + `python scripts/niche_scan.py --channel "@TsoTso-z7x"` + websearch
> Brief completo: `data/briefs/unexplained-mystery-documentary.md` · JSON: `data/briefs/unexplained-mystery-documentary.json`
> A saída do cluster e do `--channel` não foi salva em arquivo (execução manual); é reproduzível pelos comandos acima.

## Veredito: **PARCIAL**

- Canais pequenos analisados: 11 únicos (8 no brief + 3 novos no cluster) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **4 canais** no brief e **2** no cluster; pós-flare do Warrior Mind manteve 4 outliers de 16,1× a 148,8× — sinal: **sim**
- Autocomplete: **84 termos** (meta ≥15) | Trends: **bloqueado** (Google 429 em 2 tentativas)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido** — nenhum dos 11 canais tem ≤45 dias. Mas 10 dos 11 falham **apenas a idade** (92–365d) e passam os outros dois gates (5 primeiros ≥10k e ≥1k views/dia), o que indica formato performando numa janela que a coleta não capturou. Não há emergentes ≤90d (os mais próximos, Visual Doc com 92d e HisTora com 98d, estão a dias do corte). A fome existe (4→2 canais com outlier ≥3× nos dois scans e o Warrior Mind sustentando outliers depois do flare), mas é **heterogênea**: 2 dos 4 outliers do brief são em idiomas fora do recorte EN (Tamil, Hindi) e não há um sub-tema EN compartilhado por ≥2 canais — o que converge é o **formato** (long documental narrado com promessa de explicação), não o tópico. Não é REPROVA (há fome e profundidade de demanda) e não é PASSA (falta o 3º canal jovem). Revalidar em 2–4 semanas com `--cluster "unsolved mystery documentary" --age 45`.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Warrior Mind | 14.000 | 287d | 2.011 | 14.992 | 001 | 969,2× — 3.229.402 — 2026-07-21; +4 pós-flare: 16,1× (53.774), 22,2× (74.098), 63,0× (209.819), 148,8× (495.957) |
| Tamil Unmaigal | 57.200 | 307d | 5.230.945 | 67.038 | 011 | 421,3× — 2.785.327 e 318,8× — 2.107.581 — 2026-08-17 (canal em tâmil) |
| Bhakti Sadhna Bharat | 80.700 | 319d | 158.775 | 43.890 | 011 | — |
| Explorer Vault | 5.640 | 154d | 27.442 | 21.902 | 011 | — |
| Chilling Scares Compilations | 44.700 | 105d | 2.744.636 | 73.305 | 011 | — |
| DARK LOGS | 32.700 | 231d | 45.276 | 51.007 | 011 | — |
| Visual Doc | 2.620 | 92d | 541.851 | 7.966 | 011 | 42,4× — 526.679 — 2026-07-16 (vídeo em hindi) |
| HisTora | 4.060 | 98d | 117.218 | 6.088 | 011 | 278,8× — 434.989 — 2026-08-09 |
| New Discovery (cluster) | 49.400 | 215d | 81.983 | 57.182 | 011 | — |
| Mind Unfolded (cluster) | 29.400 | 365d | 656.501 | 18.159 | 011 | — |
| Oldies Radio Station (cluster) | 3.760 | 141d | 158.460 | 10.577 | 011 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a idade falha. O brief encontrou 44 canais, 13 pequenos ≤365d, analisou 8 por quota (0/8 passaram); o cluster encontrou 41, 10 pequenos ≤365d, analisou 8 (0/8 passaram; 5 canais repetidos entre os scans → 11 únicos). Limitação de quota: canais mais jovens podem não ter entrado na amostra — a revalidação deve filtrar por `--age 45`.

## Outliers (janela de 2–6 semanas)

- **Warrior Mind** — 969,2× — 3.229.402 views — "8 Disturbing Paranormal Police Encounters No One Can Explain" — 2026-07-21 — padrão: listicle-documental (8 casos) de relatos policiais paranormais com promessa "No One Can Explain"; o canal **pivotou** de conteúdo de autoajuda (8–9 meses antes, 139–957 views) para documentário paranormal e o flare veio em 2 meses.
- **Warrior Mind (pós-flare, mesmo formato)** — 148,8× — 495.957 — "When Cops WITNESS Paranormal Activity" — 2026-09-04; 63,0× — 209.819 — "15 Disturbing Paranormal Police Encounters…" — 2026-07-29; 22,2× — 74.098 — 2026-08-09; 16,1× — 53.774 — 2026-09-11 — 4 uploads seguidos na mesma fórmula = fome sustentada (não one-hit).
- **Tamil Unmaigal** — 421,3× e 318,8× — 2.785.327 e 2.107.581 — "The Unsolved Mysteries of Amazon Rainforest" — 2026-08-17 — fora do recorte EN (tâmil); mostra apetite do tema.
- **HisTora** — 278,8× — 434.989 — "The Unsolved Mystery of Benazir Bhutto | What Really Happened" — 2026-08-09 — canal de 4.060 subs; EN, mas tema político (não anomalia).
- **Visual Doc** — 42,4× — 526.679 — "भारत के इतिहास की सबसे बड़ी चोरी | The Project Black Ledger Mystery" — 2026-07-16 — vídeo em hindi, tema heist/arquivo.
- Ressalva de medição: a mediana do Warrior Mind (3.332) inclui a era de autoajuda do canal — os ratios ficam inflados; os valores absolutos (53k–3,2M views num canal de 14k subs) seguem fortes.

## Fome do algoritmo (cluster cross-canal)

Sim, com ressalva de heterogeneidade. Brief: 4 canais com outlier ≥3× (Warrior Mind, Tamil Unmaigal, Visual Doc, HisTora); cluster: 2 (Tamil Unmaigal, HisTora) — os mesmos dois aparecem nos dois scans, o que confirma **≥2 canais diferentes com outlier**. Porém os outliers não compartilham um sub-tema EN comum: dois são em idiomas fora do recorte (tâmil, hindi) e os temas variam (paranormal, heist, político). O que converge entre canais é o **formato**: long documental narrado, ≥20 min, com uma pergunta sem resposta e promessa de explicação — e o Warrior Mind mostra a fórmula viva há 5 uploads. Janela de 2–6 semanas considerada **aberta para o cruzamento formato×anomalia técnica**, não para listicles genéricos de compilação.

## Demanda (autocomplete — top termos)

84 termos únicos (meta ≥15). Destaques: `unexplained mystery documentary`, `unsolved mystery documentary`, `strange mystery documentary`, `unexplained mystery`, `unexplained mysteries new`, `unexplained mysteries history`, `unexplained mysteries channel`, `unexplained mystery documentary english`, `unexplained mystery documentary episodes`, `unexplained mystery documentary full`, `unexplained mystery documentary crime`, `unexplained mystery documentary lost media`, `unexplained mystery documentary on the internet`, `unexplained mystery documentary at night`, `unexplained mystery documentary part 2`. Profundidade alta e de busca durável (biblioteca evergreen).

## Trends (YouTube 12m)

- **Bloqueado:** Google Trends retornou 429 em duas tentativas (a do brief e uma manual). Sem direção coletada.
- Proxy usado: 84 termos de autocomplete + fome em dois scans consecutivos. Reexecutar `--trends "unexplained mystery documentary"` na próxima revalidação.

## Comentários (demanda explícita)

Não coletado. `--comments G8FqGh102nc` (outlier do Warrior Mind) retornou `insufficientPermissions` — `yt_auth.py` sem o escopo `youtube.force-ssl`; os scans também não expõem video IDs. Rodar `python scripts/yt_auth.py` e repetir para ler os pedidos recorrentes do público.

## Fontes web (2+)

- https://blog.autonolab.com/niches/2025-12-28-faceless-youtube-unsolved-mysteries — 6 canais faceless de mistério verificados com dados públicos em jul/2026 (Scary Interesting ~1,99M; Barely Sociable ~1,38M; Lazy Masquerade ~1,89M; Bedtime Stories ~1,08M; Nexpo ~3,85M; Shrouded Hand ~990K); taxonomia de lanes (caso não resolvido, true crime resolvido, internet mystery, paranormal/folclore, ficção); "o moat é a qualidade de pesquisa e o julgamento editorial"; não estima RPM.
- https://outlierkit.com/resources/faceless-youtube-channels — CPM/RPM de referência: History Documentaries $5–12, True Crime Narrations $5–12 [ALEGADO]; mystery/solução de caso como formato faceless de alta retenção; exemplos LEMMiNO etc.
- https://faceless.my/youtube/top-faceless-youtube-channels — formato "narração calma sobre footage ilustrativo, feito para ouvir como podcast" no nicho true crime/história/mistério; 8–20h de escrita por vídeo; lane documental "ownable" em 2026 [ALEGADO].
- https://ytvoice.app/blog/faceless-youtube-niches-2026 — "Historical Mysteries and Unexplained Events": CPM $6–14, competição baixa, AI-friendly [ALEGADO].
- https://longformstudio.app/articles/faceless-youtube-channel-ideas — "True crime & mystery": RPM $8–18 [ALEGADO]; "cold cases e mistérios sem solução rendem mais que gore" e AdSense limita conteúdo gráfico.
- https://apnews.com/article/youtube-monetization-update-policy-controversial-issues-545e27e27e26e0baefb937c86620b676 — jan/2026: YouTube libera monetização cheia para temas sensíveis dramatizados/discutidos de forma não gráfica [OFICIAL].
- https://techcrunch.com/2026/01/16/youtube-relaxes-monetization-guidelines-for-some-controversial-topics — mesma atualização; child abuse e eating disorders seguem restritos [OFICIAL].
- https://support.google.com/youtube/answer/10834785 — política de desinformação: exceções para contexto educacional/documentário não protegem falsidade afirmada como fato [OFICIAL].
- https://www.mediamatters.org/google/youtube-keeps-allowing-verified-conspiracy-theory-channel-next-news-network-monetize — caso de canal de conspiração monetizado; referência de risco reputacional/advertiser do nicho.
- https://www.youtube.com/@TheWhyFiles — 5,96M subs, 509 vídeos (snapshot set/2026); descrição tem Patreon + loja = sinais de monetização fora do AdSense [ALEGADO — página pública].
- https://www.youtube.com/@UnexplainedMysteriesOfficial — 2,01M subs, 7,3K vídeos; formato Top5s/listas.
- https://www.youtube.com/channel/UCa5LZlHH637evemqjUnqaTw — Warrior Mind (handle @TsoTso-z7x): descrição "covering the most unexplained encounters and disturbing discoveries ever caught on camera. new uploads every week".

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalva. O ângulo "paranormal police encounters" (Warrior Mind) tem prova de fome e concorrência de compilações de alto volume (Chilling Scares Compilations, 73,3k views/dia) — risco de satu­ração do listicle genérico e de flag de inautenticidade. A abertura está no cruzamento **anomalia com registro técnico + teste de hipóteses** e no **caso único reconstruído** (lane Bedtime Stories/Scary Interesting), onde o moat é proveniência e pesquisa, não volume. Os 10/11 canais passando os gates de performance indicam que o formato longo narrado está distribuindo; falta um canal ≤45d na amostra (limite de quota) — revalidar filtrando por idade.
- **Riscos de advertiser/compliance:** conspiração como fato e desinformação (misinformation policy) → strike/limited ads; recriação apresentada como registro real e footage fabricado → política de inautenticidade e perda de confiança; sensational/clickbait no título/thumb → limited ads; saúde/medicina fora do escopo; vítimas reais exigem respeito e "alleged"/"claimed" para pessoas vivas.

## Queries mais estreitas (se REPROVA)

- **Executada:** `unsolved mystery documentary` (cluster, 8 canais; 0 passam os 3 gates; fome em 2 canais) — a segunda busca permitida.
- **Não executada (limite de 1 segunda busca):** `mysterious events documentary` (cluster) — usar na revalidação.
- **Revalidação (2–4 semanas):** `--cluster "unsolved mystery documentary" --age 45` e `--cluster "mysterious events documentary" --age 45`; rechecar `--channel "@TsoTso-z7x"` (Warrior Mind) e `--channel` de HisTora/Visual Doc se aparecerem novos outliers.
