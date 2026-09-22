# Evidência — Vigilância

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "surveillance documentary" --max 8` + 1 busca estreita (`--cluster "privacy documentary"`) + leitura direta dos últimos uploads (Data API: `playlistItems`/`videos`, 4 canais) + websearch (4 buscas)
> Brief completo: `data/briefs/surveillance-documentary.md` · JSON: `data/briefs/surveillance-documentary.json`
> A saída do `--cluster` não foi salva em artefato (rodou sem `--out`); os números estão transcritos abaixo.

## Veredito: **PARCIAL** (com ressalva dura)

- Canais pequenos analisados: **16** (8 no brief + 8 no cluster) | passam os 3 gates: **1** (meta ≥3)
- Emergentes (≤90d + 2/3 gates): **1** — FINAL FRAME CRIME (56d)
- Fome do algoritmo (outlier ≥3×): **5 canais** no brief — FINAL FRAME CRIME 1.866,9×; Detective Diaries TV 387,2×; The Time Empire 107,2×; Crime Watch UK-TV 9,0×; Sketch Itihas 3,3× — **porém 100% fora do cruzamento declarado**: 3 são CCTV/câmeras-como-evidência (adjacente true crime) e 2 são animação hindi de espionagem (fora do alvo EN)
- Cluster `privacy documentary`: **0/8 gates; 0 outliers** (frio; os canais retornados são em maioria fora do tema — History Paradox, Hollywood Yesterday, Crown Whisper etc.)
- Autocomplete: **81 termos únicos** (meta ≥15) — profundidade alta, núcleo forte
- Trends: **não coletado** — Google Trends retornou erro 429 nas duas tentativas ("surveillance documentary" no brief; "mass surveillance" em retry manual); fallback usado: autocomplete
- Comentários: **não coletado** — `--comments FeqhfzeO_L8` retornou `insufficientPermissions` (yt_auth sem escopo `youtube.force-ssl`)

> Leitura honesta:
> 1. **O cruzamento declarado (doc EN de vigilância/privacidade/rastreamento tech) NÃO está validado.** O único canal que passa os 3 gates é um canal de true crime UK baseado em CCTV, e o único emergente também é CCTV.
> 2. **A demanda existe** no ângulo tech/privacidade (autocomplete profundo: mass/china/digital surveillance, police surveillance UK, surveillance capitalism, stingray), mas **não há evidência de canais dark novos rompendo nesse ângulo** nas duas buscas.
> 3. A fome do algoritmo está no subcruzamento **"câmeras como evidência"** (3 canais com outliers grandes na mesma janela; todos long-form 22–35 min, upload quase diário) — que é adjacente true crime, não Tech.
> Estatuto do modelo: **watchlist** (revalidar em 2–4 semanas). Se o operador quiser operar agora, o dado aponta para o pivot CCTV — decisão dele, não deste brief.

## Canais-evidência — brief "surveillance documentary" (gates: idade≤45d · 5primeiros≥10k · views/dia≥1k)

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| AntiGlomar | 19.800 | 310d | 647.298 | 2.074 | 011 | 0 |
| FINAL FRAME CRIME | 522 | 56d | 705.025 | 12.919 | 011 | 1 (1.866,9×) |
| Detective Diaries TV | 4.640 | 352d | 398.307 | 2.502 | 011 | 1 (387,2×) |
| The Gambler's Mind | 910 | 129d | 6.406 | 6.100 | 001 | 0 |
| Crime Watch UK-TV | 1.840 | 24d | 235.091 | 11.323 | **111** | 1 (9,0×) |
| FBI Investigates | 68.300 | 315d | 859.849 | 80.765 | 011 | 0 |
| Sketch Itihas | 3.590 | 160d | 610.735 | 6.204 | 011 | 1 (3,3×) |
| The Time Empire | 1.770 | 215d | 8.235 | 3.066 | 001 | 1 (107,2×) |

> Gates no formato `111`: 1º dígito = idade ≤45d · 2º = 5 primeiros ≥10k · 3º = ≥1k views/dia.
> Nota de método: "5 primeiros" = soma dos 5 vídeos mais antigos entre os 15 uploads recentes analisados (definição do `niche_scan.py`).
> FINAL FRAME CRIME: mediana de 224 views — o first5 (705.025) e o views/dia (12.919) são inflados por **1 flare** de 418.180 views (05/09); é hit isolado, não biblioteca.
> Cluster do brief: 45 canais encontrados; 8 pequenos (≤200k subs) e ≤365d; 8 analisados (cota).

## Canais-evidência — cluster estreito "privacy documentary"

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| History Paradox | 92.300 | 296d | 844.328 | 2.039.017 | 011 | 0 |
| Hollywood Yesterday | 14.600 | 337d | 93.596 | 16.003 | 011 | 0 |
| Crown Whisper | 4.190 | 91d | 2.924 | 60.242 | 001 | 0 |
| StoryMakerEn | 250 | 262d | 9.133 | 221 | 000 | 0 |
| Joe's Space Science | 10.300 | 323d | 49.994 | 3.315 | 011 | 0 |
| Histovex | 263 | 133d | 509 | 695 | 000 | 0 |
| Explainer | 1.840 | 95d | 2.139 | 4.306 | 001 | 0 |
| Letters From Pops | 163 | 61d | 2.556 | 1.267 | 001 | 0 |

> Cluster: 48 canais encontrados; 17 pequenos (≤200k subs) e ≤365d; 8 analisados (cota). Nenhum ≤45d com tração; nenhum outlier ≥3×.
> Leitura: a busca "privacy documentary" não devolveu um cluster de canais de privacidade — devolveu canais de história/filmes/espaço que tangenciam o termo. O nicho tech/privacidade, como categoria nativa no YouTube, não apareceu como feed novo nesta janela.

## Outliers (janela de 2–6 semanas)

- **FINAL FRAME CRIME** — 1.866,9× — 418.180 views — "The Passenger Vanished — Then Airport CCTV Found This 84 KG Suitcase | CCTV" — 2026-09-05 — padrão: CCTV + one-line story; canal de 56d/522 subs; mediana 224 → hit isolado.
- **Detective Diaries TV** — 387,2× — 388.327 views — "Cameras Caught Her Final Moments in a Waikiki Hotel" — 2026-09-02 — padrão: câmeras + caso; canal de 163 vídeos em 352d (quase diário); mediana 1.003.
- **The Time Empire** — 107,2× — 96.148 views — "India's Border Spy Network | The Electrician Exposed a Secret Surveillance Network | 2D Animation" — 2026-09-11 — padrão: animação 2D, espionagem; canal Hindi (fora do alvo EN).
- **Crime Watch UK-TV** — 9,0× — 140.544 views — "The CCTV That Exposed Met Police Constable Wayne Couzens — Kidnapper, Rapist, Murderer" — 2026-09-14 — padrão: CCTV + caso UK + 22–35 min; o único canal passando os 3 gates.
- **Sketch Itihas** — 3,3× — 195.825 views — "Kaise Ajit Doval Ne 3 Pakistani Jasoos Ko Pakda | 2D Animation" — 2026-09-13 — Hindi.

## Fome do algoritmo (cluster cross-canal)

- Padrão 1 (o mais forte): **câmeras/CCTV como evidência** — FINAL FRAME CRIME (05/09), Detective Diaries TV (02/09) e Crime Watch UK-TV (14/09) com outliers ≥3× na mesma janela → 3 canais diferentes = fome cross-canal no subcruzamento adjacente (true crime + câmera).
- Padrão 2: **animação hindi de espionagem** — The Time Empire (107,2×) e Sketch Itihas (3,3×) → fome em outro idioma/mercado; não serve ao modelo EN.
- **No cruzamento declarado (privacidade/tech EN): nenhuma fome** — 0 outliers no cluster `privacy documentary`; AntiGlomar, o canal mais próximo do tema no brief, tem apenas 2 vídeos e 0 outliers.

## Demanda (autocomplete — top termos)

81 termos únicos (meta ≥15). Núcleo útil (o resto é cauda de países, letras, franquias e filmes):

- mass surveillance documentary / government surveillance documentary
- china surveillance documentary / surveillance state
- digital surveillance documentary / surveillance capitalism documentary
- police surveillance documentary uk / uk surveillance documentary
- surveillance technology documentary / stingray surveillance technology documentary
- security camera documentary / cctv crime documentary / cctv documentary english
- surveillance documentary latest / surveillance documentary on youtube / surveillance documentary questions and answers

## Convergência de formato (últimos uploads — leitura direta, Data API)

- **Crime Watch UK-TV:** 8/8 uploads recentes de 22–35 min, todos "UK Murders Documentary" + CCTV; cadência ~2 dias (03–21/09). Convergência 100% no formato CCTV+caso.
- **FINAL FRAME CRIME:** 8/8 dos últimos de 23–29 min, título one-line + sufixo "| CCTV"; views 19–31.082 (mediana baixa; depende de hit).
- **Detective Diaries TV:** 163 vídeos em 352d, quase diário; últimos uploads com 144–5.812 views; mesmo molde de título.
- **AntiGlomar** (o mais "privacidade" do brief): apenas 2 vídeos (3m14s e 11m38s), footage policial de celebridade — não é canal de documentário; não valida o formato do modelo.
- Conclusão: o que converge nos canais com tração é **long-form 22–35 min de câmeras + caso**, com frequência alta e mediana baixa (jogo de volume + hit). O formato tech/privacidade ("sistema por dentro", documento como protagonista) não aparece no feed — é prescrição a validar.

## Trends (YouTube 12m)

- Não coletado: erro 429 em duas tentativas. Fallback: autocomplete (81 termos, acima).
- Sugestão de retry no re-scan: "surveillance", "mass surveillance", "license plate reader" (termos específicos, filtro YouTube).

## Comentários (demanda explícita)

- Não coletado: `--comments` retornou `insufficientPermissions` (escopo `youtube.force-ssl` ausente — 3ª tentativa no projeto). Proxy qualitativo: a pauta 2026 (Flock/LPR, dados de fidelidade, spyware) rende debate público intenso em podcasts, ONGs e reportagens — sinal de audiência, não de canal rompendo.

## Fontes web (2+)

- https://wrmj.com/video/NEJZehrfxcy.html — AJC "Curiosities of the South" (ago/2026): Atlanta é a cidade mais vigiada dos EUA; 60.000+ câmeras (~1 para cada 8 moradores), centro de crime em tempo real de US$ 21 milhões, LPR, drones, robôs e reconhecimento facial; episódio em 2 partes centrado em "a promessa se sustenta?".
- https://hadnews.com/silicon-valley-mastermind-whos-behind-palantirs-gotham-surveillance-software-dw-documentary/ — DW Documentary (fev/2026): doc sobre Palantir/"Gotham" e vigilância de dados; referência de oferta mainstream no tema.
- https://www.krokodil.rs/eng/2026/08/nzz-documentary-film-spyware-against-freedom/ — NZZ (ago/2026): doc sobre spyware contra jornalistas/ativistas; Citizen Lab/Anistia; expressão "surveillance tsunami" — risco geopolítico e ângulo.
- https://meta.mk/en/thousands-of-cameras-documentary-exposes-the-dangers-of-mass-biometric-surveillance-in-serbia/ — documentário sérvio (Safe City/Huawei) com legendas EN; DPIA não cumprido; EDRI — exemplo de doc cívico independente.
- https://www.youtube.com/watch?v=lqVvabllzc0 — "They're Tracking Your Family's Every Move — Flock Safety Is NOT Just a Camera" (mai/2026): debate sobre redes privadas de LPR e acesso por agências.
- https://www.youtube.com/watch?v=EqZOzwVaZp8 — "Privacy People" (B Team Films, doc completo): exemplo de oferta no nicho privacidade.
- https://www.youtube.com/channel/UCi3GRbYZKclbujcR1J601rQ — The Opt Out Project: canal real de privacidade/opt-out (referência de posicionamento).
- https://www.youtube.com/watch?v=2LT9WwEPFcw — KIRO 7 (jan/2026): dados de fidelidade de supermercado; Consumer Reports aponta US$ 527 milhões da Kroger em 2024 e perfis com erros [REPORTADO].
- https://reelforgeai.io/blog/50-profitable-faceless-youtube-channel-ideas-for-2026 — nicho faceless "Cybersecurity & Privacy" com RPM $14–24 e afiliados de VPN $30–120/signup [ALEGADO]: base da classe $15–25 do modelo.
- https://tubelab.net/blog/faceless-youtube-channel-niches — contexto de política 2026: conteúdo inautêntico, remoções de "AI slop" (fev/2026), mudanças de monetização de temas sensíveis (jan/2026), auto-dubbing [PRATICANTE].
- https://www.elysiate.com/blog/how-youtube-monetization-works-for-faceless-channels — camadas de monetização/compliance por vídeo; divulgação de conteúdo alterado; originalidade como critério.
- https://zellahq.com/blog/how-to-start-a-faceless-youtube-channel/ — tabela de CPM 2026: "True crime / documentary" 8–12 RPM [ALEGADO] (piso conservador para o cruzamento adjacente).
- https://privacyscore.dev/blog e https://lunyb.com/blog/how-to-stop-ai-tracking-online-2026-msh9olu0 — insumo técnico do subnicho (fingerprinting/JA4/Topics API; opt-out de 30–90 dias por broker) para pautas evergreen e produto digital.

## Saturação e riscos observados

- **Formato×tópico:** "doc tech/privacidade" tem demanda (81 autocompletes) e oferta de mídia grande (DW, NZZ, AJC — ver fontes); competir com emissora no mesmo ângulo é o risco de saturação. O ângulo não coberto é o **"sistema por dentro"** (contrato/licitação/log/auditoria como protagonista), que nenhum canal do scan opera. No subcruzamento CCTV/câmeras a oferta de canais dark é alta, quase diária e com mediana baixa (jogo de volume + hit).
- **Advertiser/compliance:** temas políticos/estatais e spyware podem limitar ads; jan/2026 mudou a monetização de temas sensíveis [OFICIAL `09`]; nunca rosto/placa de pessoa comum; cuidado com "AI persona" de segurança/política (balde 3 do conteúdo inautêntico [OFICIAL]); footage de CCTV de terceiros exige uso transformativo ou licença.
- **Outros:** difamação — empresas/fornecedores sempre com documento + "alleged/reported"; geopolítica — citar documentos oficiais dos dois lados (não virar propaganda nem campanha); YPP dobra em 01/02/2027 (8.000h/20M) [OFICIAL].

## Queries mais estreitas (re-scan em 2–4 semanas)

Não rodadas nesta coleta (limite de quota/instrução). Ordem de prioridade:

1. `--cluster "police surveillance documentary" --age 45 --max 8` (termo forte no autocomplete)
2. `--cluster "license plate reader documentary" --age 45 --max 8` (Flock/LPR é a pauta quente de 2026 nos EUA)
3. `--cluster "facial recognition documentary" --age 45 --max 8`
4. `--cluster "data broker documentary" --age 45 --max 8`
5. `--cluster "spyware documentary" --age 45 --max 8`
6. `--cluster "cctv crime documentary" --age 45 --max 8` (o único cruzamento com fome comprovada nesta coleta — checar se há canal novo passando gates; pivot só com aprovação do operador)

Promover o modelo a produção **somente** com ≥3 canais pequenos passando os 3 gates no cruzamento declarado. Até lá, piloto controlado (máx. 4–6 vídeos) e re-scan.
