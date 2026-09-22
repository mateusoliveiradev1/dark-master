# Evidência — Arqueologia e artefatos

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "archaeology mystery documentary" --max 8` (1ª passada, REPROVA nos gates) + segunda busca permitida `python scripts/niche_scan.py --cluster "ancient artifact documentary" --max 8` + `--suggest "ancient artifacts"` (226 termos) + websearch (fontes abaixo)
> Brief completo: `data/briefs/archaeology-mystery-documentary.md` · JSON: `data/briefs/archaeology-mystery-documentary.json`
> A saída bruta do cluster `ancient artifact documentary` não foi persistida em arquivo (execução manual, limite de 1 segunda busca); é reproduzível pelo comando acima. O feed RSS dos canais (últimos uploads) respondeu **404** em 2026-09-22 — a convergência de formato foi lida pela assinatura dos outliers e pelas fontes web.

## Veredito: **PARCIAL**

- Canais pequenos analisados: **14 únicos** (8 no brief + 7 no cluster; Atlas of Civilizations aparece nos dois) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **6 canais únicos** (3 no brief + 3 no cluster) — sinal: **sim**, com flare de **631,9×** e outlier de **1,61M views**
- Emergentes (≤90d + 2/3 gates): **6 canais** — Last Cartographer, ThePastBlueprints, Aicontentcreator, DocuAI, Atlas of Civilizations, Podcast Gold
- Autocomplete: **117 termos** (brief) + **226** (`ancient artifacts`) | Trends: **não coletado** (429 nas duas tentativas)

**Leitura honesta:** o critério rígido (≥3 canais ≤45d passando os 3 gates) **não foi atingido**. Mas **11 dos 14 canais falham apenas o gate de idade** e passam os outros dois (5 primeiros ≥10k e ≥1k views/dia); o mais novo da coleta tem 52 dias (Ozil Hub) e três emergentes estão a uma semana do corte de 90d (89d). A fome cross-canal é **fresca e clara**: três canais diferentes (Hidden History, DarkOrbit Files, Primitive Minds) fizeram outlier no eixo "artefato antigo + o que a ciência não explica" entre 20/08 e 02/09/2026, e o maior outlier do brief (Last Cartographer, 403,1×) tem 1,61M views. Não é PASSA (nenhum canal ≤45d cruzou os 3 gates) e não é REPROVA (fome + 6 emergentes + profundidade de busca alta). Revalidar em 2–4 semanas com foco em entrantes ≤45d.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

| Canal | Scan | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers (janela 90d) |
|---|---|---|---|---|---|---|---|
| Khush ki Kahaniya | brief | 51.900 | 98d | 5.025.899 | 198.907 | 011 | — |
| Last Cartographer | brief | 18.800 | 89d | 74.424 | 20.614 | 011 | 403,1× — 1.612.231 — Grand Canyon/Hopi — 2026-07-06 |
| ThePastBlueprints | brief | 7.230 | 89d | 1.435.901 | 21.302 | 011 | — |
| Aicontentcreator | brief | 12.300 | 71d | 79.823 | 87.499 | 011 | 53,4× — 435.238 — Kailash (09-03) · 24,3× — 197.842 — templo/Shivaji (09-13) · 10,1× — 82.111 (09-07) · 7,4× — 60.107 (08-31) |
| DocuAI | brief | 4.860 | 72d | 983.940 | 35.277 | 011 | — |
| Atlas of Civilizations | brief + cluster | 21.900 | 68d | 15.197 | 74.113 | 011 | — |
| Podcast Gold | brief | 5.140 | 89d | 408.306 | 44.142 | 011 | — |
| MovieMithra | brief | 10.900 | 249d | 126.633 | 12.848 | 011 | 64,4× — 89.695 — Treasure Mystery (Telugu) — 2026-08-26 |
| Primitive Minds | cluster | 9.190 | 116d | 2.127.335 | 59.349 | 011 | 8,5× — 1.031.165 — Andean mummies / AI reconstruction — 2026-08-20 |
| DarkOrbit Files | cluster | 2.170 | 103d | 5.954 | 11.110 | 001 | 74,6× — 403.215 — "7 ancient discoveries…" — 2026-08-27 |
| The Hidden Place 4U | cluster | 45.200 | 155d | 349.109 | 364.982 | 011 | — |
| Hidden History – Official | cluster | 7.460 | 237d | 824 | 1.285 | 001 | 631,9× — 79.624 — "most mysterious ancient artifacts" — 2026-09-02 |
| Olive Télé | cluster | 29.000 | 280d | 65.318 | 27.462 | 011 | — |
| Ozil Hub | cluster | 892 | 52d | 9.663 | 8.631 | 001 | — |

> Gates na ordem (idade≤45d, 5primeiros≥10k, views/dia≥1k). "011" = só a **idade** falha; "001" = idade + 5 primeiros falham, views/dia passa. Brief: 34 canais encontrados, 9 pequenos ≤365d, 8 analisados (quota); 6 emergentes ≤90d. Cluster: 38 encontrados, 7 pequenos/jovens, 7 analisados (quota); 1 emergente. IDs dos canais do brief estão no JSON; a saída do cluster não foi persistida.

## Outliers (janela de 2–6 semanas)

- **Last Cartographer** — 403,1× — **1.612.231 views** — "What the Hopi Said Was Living Beneath the Grand Canyon" — 2026-07-06 — padrão: "o que está sob [lugar conhecido]" + tradição oral; canal de 18,8k subs e 89 dias.
- **Hidden History – Official** — **631,9×** — 79.624 views — "The Truth Behind The World's Most Mysterious Ancient Artifacts" — 2026-09-02 — maior ratio da coleta (mediana de 126 views); padrão: lista de artefatos + promessa de "verdade por trás".
- **Aicontentcreator** — 53,4× / 24,3× / 10,1× / 7,4× — 435.238 / 197.842 / 82.111 / 60.107 views — 31/08 a 13/09/2026 — quatro outliers em 2 semanas no eixo templo/achado/geografia indiana (títulos-hashtag, canal 71d).
- **DarkOrbit Files** — 74,6× — 403.215 views — "7 ancient discoveries that science still can't explain…" — 2026-08-27 — canal de 2,2k subs; padrão: número + "ciência não explica" + emoji (framing sensacionalista).
- **MovieMithra** — 64,4× — 89.695 views — "230 ఏళ్లుగా ఎవరూ ఛేదించలేని Treasure Mystery!" (Telugu) — 2026-08-26 — padrão: enigma de tesouro há 230 anos.
- **Primitive Minds** — 8,5× — **1.031.165 views** — "The Real Face of an Ancient Andean Mummies | AI Reconstruction" — 2026-08-20 — padrão: múmia + reconstrução facial por IA (exige disclosure no upload).

> Nota metodológica: ratios altos vêm de medianas baixas em canais minúsculos. O que sustenta a leitura é o **viewport absoluto** (79k–1,6M em canais de 2–19k subs) e a **convergência de tema em canais diferentes** na última semana de agosto e primeira de setembro.

## Fome do algoritmo (cluster cross-canal)

**Sim, em três recortes:**

1. **"Artefato + o que a ciência não explica" (20/08–02/09/2026):** Primitive Minds (20/08, 1,03M), DarkOrbit Files (27/08, 403k), Hidden History (02/09, 79k) — 3 canais diferentes em 2 semanas. É a fome mais recente e a mais alinhada ao subnicho de artefatos; parte dela com framing sensacionalista, que o modelo **não** copia (copia a curiosidade, entrega o método).
2. **"O que está sob [lugar]" (jul/2026):** Last Cartographer (06/07, 1,61M) isolado, mas com o maior viewport da coleta; ângulo replicável com contexto arqueológico real.
3. **Templo/achado e enigma regional (31/08–13/09/2026):** Aicontentcreator (4 outliers, EN/Hindi) e MovieMithra (26/08, Telugu) mostram demanda fora do eixo anglófono — sinal de que a versão EN tem espaço, desde que com pesquisa primária (não template de hashtags).

## Demanda (autocomplete — top termos)

- `archaeology mystery documentary` (brief): **117 termos**. Destaques: `archaeology mysteries documentary`, `archaeology documentary`, `archeology discoveries`, `archaeology mystery documentary egypt`, `… gold`, `… lost`, `… real stories`, `… explained`, `… series`, `… youtube channel`.
- `ancient artifacts` (`--suggest`): **226 termos**. Destaques de demanda real: `ancient artifacts that cannot be explained`, `ancient artifacts explained`, `ancient artifacts discovered`, `ancient artifacts recently discovered`, `ancient artifacts found in america`, `ancient artifacts documentary`, `oldest archeological artifacts`, `ancient relics`, `ancient biblical artifacts`, `ancient artifacts auction`, `buying ancient artifacts`, `ancient artifacts destroyed`. Ruído relevante: termos de jogos (Indiana Jones, Diablo) — filtrar.

## Trends (YouTube 12m)

- **Não coletado.** `--brief` e retry de `--trends "ancient artifacts"` retornaram **HTTP 429** (rate limit do Google) em 2026-09-22. Fallback usado: autocomplete (117 + 226 termos). Revalidar com `--trends "ancient artifacts"` e `--trends "archaeology documentary"` em outro horário.

## Comentários (demanda explícita)

Não coletado — `--comments` exige o escopo `youtube.force-ssl` (ver `references/24`); o autocomplete `ancient artifacts that cannot be explained` e `recently discovered` sugere demanda explícita por (a) explicação e (b) achados novos. Rodar `python scripts/yt_auth.py` e depois `--comments` no vídeo de maior outlier (Last Cartographer, `data/briefs/archaeology-mystery-documentary.json`).

## Convergência de formato (últimos uploads)

- **Limitação:** o feed RSS dos canais respondeu 404 e a coleta não persiste duração dos vídeos. O que dá para afirmar: os outliers dos 6 canais "hungry" são todos do mesmo tipo de embalagem (artefato/achado + promessa de explicação), em canais com biblioteca curta e recente (52–237d). Revalidar com `--channel` (últimos 5 uploads) na próxima rodada.
- **Back to Ancient** (fonte web): canal pequeno (4,8k subs, 1,74M views) publicando compilações "1 HOUR OF…" quase diárias em ago/2026 com 627–19.590 views por vídeo — evidência de que a **versão commodity do nicho não performa**; o que performa é o achado com narrativa única.

## Fontes web (2+)

- https://becomeviral.com/blog/origins-explained-case-study — caso Origins Explained (mai/2026): canal voice-only de história antiga com ~3M subs; formato 15–25 min, arquivo + imagens de artefatos, cadência alta; CPM estimado $5–12 para history/antiguidades [ALEGADO]; lição "biblioteca + voz consistente".
- https://www.inverse.com/input/culture/alternative-historians-youtube-who-built-pyramids-not-aliens — risco central do nicho: pseudoarqueologia (Bright Insight, UnchartedX) com centenas de milhares de views por vídeo; ligação documentada com misinformation e conspiração; caso de vandalismo na Grande Pirâmide (2013); alerta de que o vácuo deixado pela academia é ocupado por pseudo-história.
- https://en.wikipedia.org/wiki/Ancient_Aliens — [REFERÊNCIA] descrição do formato "Gish gallop" pseudocientífico: o que o modelo **não** pode reproduzir (perguntas retóricas + afirmação sem evidência).
- https://www.youtube.com/watch?v=4uvD30xw_ZY — World of Antiquity, "Fantasy Archaeology is a Dead End" (mar/2026): crítica pública ao eixo "civilização avançada perdida"; mostra que a audiência de arqueologia real existe e consome o contra-ângulo.
- https://videos.feedspot.com/archaeology_youtube_channels/ — lista 2026 com 40 canais de arqueologia: quase todos institucionais ou com especialista na tela (Penn Museum, Jamestown Rediscovery, DigVentures, Ancient Americas, Ancient Architects) — a lacuna **faceless com método** segue aberta no EN.
- https://www.showmeyourchannel.com/youtuber/backtoancientyt — Back to Ancient (2026): compilações "1 HOUR OF…" de mistérios arqueológicos quase diárias, 627–19,59k views — a versão commodity do formato.
- https://support.google.com/youtube/answer/14328491 — [OFICIAL] disclosure obrigatório de conteúdo realista gerado/alterado por IA (relevante para reconstruções faciais de múmias, formato que fez 1,03M views na coleta).
- https://pocketmags.com/skeptical-inquirer-magazine/marapr-2023/articles/apocalyptic-pseudoarchaeology — análise do fenômeno Ancient Apocalypse (Skeptical Inquirer): por que o formato pseudodocumental convence e quais red flags usar contra ele.

## Saturação e riscos observados

- **Formato×tópico ainda admite canal novo?** Sim, com ressalvas: (a) o recorte "artefato + ciência não explica" já tem 3 outliers recentes e tende a saturar em semanas — a diferenciação é método, não o framing; (b) "o que está sob [lugar]" tem só um flare (jul) e segue aberto; (c) parte da fome é alimentada por sensacionalismo (títulos com emoji e "can't explain") que o modelo não pode copiar sem perder advertiser-safety e credibilidade; (d) a versão commodity (compilações de 1h) está servida e não performa.
- **Gargalo real:** o gate de idade. 11/14 passam os gates 2–3; nenhum ≤45d. A pergunta da revalidação é se entrantes ≤45d aparecem. Três emergentes (Last Cartographer, ThePastBlueprints, Podcast Gold, 89d) cruzam o corte de 90d na próxima semana — revalidar em 2–4 semanas.
- **Riscos de advertiser/compliance:** restos humanos (múmias) exigem framing educacional e sem close gráfico; pseudoarqueologia como fato é risco de política de misinformation e de credibilidade; "supressão pela ciência" e "forbidden knowledge" proibidos; saque/treasure hunting não pode ser glamourizado; reconstruções fotorrealistas por IA exigem label [OFICIAL]; imagens de museu têm licença peça por peça (Met/Smithsonian Open Access e Wikimedia são as bases seguras); precisão histórica exige [FATO]/[REPORTADO]/[LENDA] e correção pública.

## Queries mais estreitas (revalidação 2–4 semanas)

- **Executadas:** `archaeology mystery documentary` (brief; 34→8 canais; 0 gates; 6 emergentes; 3 com fome) e `ancient artifact documentary` (cluster; 38→7 canais; 0 gates; 1 emergente; 3 com fome).
- **Próximas (limite de 1 segunda busca por rodada):** `antikythera mechanism documentary` e `voynich manuscript documentary` (subnichos de artefato único, alta intenção de busca); rodar com `--age 45` para forçar o corte de idade. Se ambos reprovarem de novo nos gates, manter PARCIAL e considerar o piloto mesmo assim, com validação de 30 dias do `profile.md` §13.
