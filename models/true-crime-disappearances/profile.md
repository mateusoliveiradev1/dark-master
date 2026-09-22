# Modelo — Desaparecimentos

> Categoria: True crime · Subnicho: pessoas desaparecidas (casos arquivados e recentes) · Slug: `true-crime-disappearances`
> Lane: mixed · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md`) — os 3 gates rígidos não foram batidos (1 canal pequeno por scan, meta ≥3). Sinais adjacentes: fome do algoritmo (outlier ≥3×) em 2 e 4 canais, Trends ALTA, 78 autocompletes.

## 1. Posicionamento (1 frase)

Documentário de desaparecimento que reconstrói o último dia com linha do tempo e registro — para o espectador de true crime que já cansou de teoria e quer ver o que o arquivo realmente mostra.

## 2. Público e promessa

- **Público:** adultos 25–54 em mercados EN (US/UK/CA/AU) que já consomem true crime long-form e séries de desaparecimento; sessões longas de binge (12–22 min por vídeo, 35–55 min de sessão) [ALEGADO — fontes web em `evidencia.md`].
- **Promessa do canal:** em todo vídeo, a linha do tempo do último dia + o que a investigação e os registros mostram + o estado atual do caso, com fontes citadas.
- **Inimigo da promessa:** gore, reconstituição dramática, teoria apresentada como fato, "eu resolvi o caso", contato com famílias sem consentimento, clickbait que o vídeo não entrega.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Casos arquivados (cold missing) | alta — "unsolved missing person cases documentary", "missing person case documentary" | média | Linha do tempo + arquivo primário (NamUs/Charley Project/DOE); até 3 teorias, sem afirmar |
| Desaparecimentos recentes / em curso | alta — Trends ALTA (22,5 vs 8,3) | média-baixa | "O que se sabe até agora": foco em apelo por informação; suspeito vivo = alleged; zero especulação |
| Contextos específicos (cruzeiro, parques, rotas) | média-alta — "missing person documentary lost", "missing person documentary ocean" | baixa-média | Contexto sistêmico: jurisdição, busca, lacunas de protocolo (evidência: outlier de cruzeiro 6,4×; parques com 335K views) |

## 4. Lane e formato

- **Lane:** mixed — justificativa: os outliers do scan são long-form (581,6×; 317,1×; 6,4×) e há um outlier short de lista ("celebrities who went missing", 18,2×, 49.703 views). Hipótese de trabalho: Short = aquisição, long = receita. **Não confirmado pelos gates** (ver `evidencia.md`) — validar com piloto antes de manter os dois.
- **Duração alvo:** long 12–20 min · short 20–28s (faixa doce de retenção).
- **Cadência:** 2 longs + 1 short por semana; ratio 0,5 → se o RPM do canal cair, descer para 1 short a cada 2–3 longs (0,28–0,40) [PRATICANTE — ref `10`].
- **Mix:** Short aponta para o long do dia (Related Video + comentário fixado); long carrega o produto. Medir a conversão antes de aumentar o volume de Shorts.

## 5. Fingerprint de formato (o que o recomendador lê)

Long 12–20 min, 16:9, voz de documentário contida (passado, reportorial), b-roll de arquivo público + mapas + documentos na tela, capítulos escritos como resposta de busca. Thumb dessaturada com 1 objeto/1 número. Cadência de 2 longs/semana.

Convergência observada nos canais-evidência (verificação parcial — 2 canais checados upload a upload): títulos com idade + "vanished/disappeared" (True Crime Retold), casos de arquivo/repack com nome de procedimento (IT'S CRIMINAL, FBI Investigates, Crime University, DARK LOGS). O que **não** copiar: IT'S CRIMINAL cresce repackando documentário de TV (Monster in the Shadows) — reused content, risco de inautenticidade; os canais que passam gate nos dois scans (Curious Lens, leeshi887) têm títulos de clickbait e sinais de produção automatizada. O cruzamento ainda não tem fingerprint limpo — a lacuna é "documentário de desaparecimento com pesquisa primária e voz própria".

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-disappearances/beats.json` (gênero `true-crime-disappearances`) — usar com `--beats-file`.
- **Porte padrão:** FINO→PADRÃO (12–20 min; ~1.900–3.300 palavras) [ref `30`].
- **Dispositivos:** rehook a cada 2–4 min; re-engage em ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central resolvida só no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — linha do tempo oficial (polícia/NamUs), documento (FOIA/PACER/DOE) ou compilação própria (tabela de chamadas, pings, buscas).

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** objeto-símbolo + micro-história verificada (ref `31`, #7 e #13); contradição entre o que o registro mostra e o que a narrativa popular repete.
- **Exemplos:**
  1. "The car was still running. Her purse was on the passenger seat. She was gone."
  2. "He left a voicemail saying he could see the town lights. Search teams never found the road he described."
  3. "One shoe. That's what the searchers logged — half a mile from where she was last seen."
- **Proibido:** abstração, data/local antes do gancho, meta-linguagem, gore, promessa de resolução.

## 8. Thumbnail

- **Composição:** 1 ponto focal (objeto, documento, mapa ou silhueta) + 1 número-âncora (ano, km, dias) + 3–4 palavras que o título não diz; sujeito fora do centro, texto no lado oposto.
- **Paleta:** dessaturada (azul-noite/cinza) com 1 acento âmbar ou vermelho; fundo escuro para saltar da UI.
- **Fonte:** sans bold pesada com contorno/sombra — tem que ler a 120px.
- **Nunca:** foto de cena de crime, gore, rosto de familiar sem consentimento, repetir palavras do título, imagem gráfica (yellow icon).

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — classe de true crime não-gráfico em `10` ($8–15; documentary $12,6); fontes web divergem para baixo ($4–10 rookcast; $5–12 fluxnote/viralhq) — todas [ALEGADO]; RPM real só no Analytics do canal.
- **Produto digital:** tripwire $7–27 — "case file pack" (dossiê do caso: linha do tempo, documentos, fontes) [ref `19`].
- **Patreon/membros:** sim — early access, versão ad-free, case files e votações de casos. Em canais mid-tier do nicho, Patreon/membros são relatados como a maior fatia da receita [ALEGADO — phantomline].
- **Afiliado/brand:** audiobooks, plataformas de podcast, segurança doméstica — patrocínio mid-tier pode pagar mais que o AdSense no mesmo volume [ALEGADO — phantomline].
- **Rota no funil (`21`):** short → inscrito → long → produto; comentário fixado com o link do long do dia.

## 10. Produção

- **Custo/tempo por vídeo (estimativa de operação solo) [ALEGADO]:** 8–12 h por long (pesquisa 40–50%, roteiro 20%, montagem 25%, publicação 10%); 2–4 h por short.
- **Assets:** arquivo público (Wikimedia Commons, Library of Congress, National Archives), jornais (Google News Archive), registros (PACER, FOIA, NamUs, Charley Project, DOE), stock (Pexels/Pixabay), mapas (Datawrapper/Canva).
- **Voz:** TTS contido, registro documental (edge-tts en-US como base; ElevenLabs para premium), ~150–160 palavras/min [ref `30`].

## 11. Riscos

- **Compliance/advertiser:** true crime é o território mais sensível das diretrizes; imagem gráfica na thumb ou nos primeiros 15s é gatilho próprio, separado do tema. Relatos de 30–60% de uploads limitados/desmonetizados no nicho [ALEGADO — phantomline]. Em jan/2026 temas controversos não-gráficos voltaram a ser elegíveis e em ago/2026 conteúdo educacional/documentário retratando morte também [air.io]. Mitigação: enquadramento reportorial, verbos no passado, sem método gráfico, self-certification conservadora.
- **Inautenticidade:** risco existencial — o maior outlier do scan (581,6×) é repack de documentário de TV; não repetir. 1 peça primária por vídeo, POV e estrutura variando, voz/roteiro próprios (enforcement de conteúdo inautêntico em 2026).
- **Outros:** pessoas vivas → "alleged/suspect"; direitos de imagem; nunca contatar famílias sem consentimento; casos com crianças = risco extra; evitar caso ativo com suspeito não acusado.

## 12. 10 ideias-semente (títulos)

1. Maura Murray: The Crash That Ended With an Empty Road
2. Brian Shaffer: He Walked Into a Bar on Camera. He Never Walked Out.
3. Lars Mittank: The Tourist Who Ran From the Airport and Into the Forest
4. Amy Bradley: The Cruise Disappearance That Changed Maritime Law
5. Brandon Swanson: "I Can See the Lights" — Then the Line Went Dead
6. Jason Jolkowski: He Left for His Shift and Never Arrived
7. Steven Koecher: His Car Was Found Parked. His Phone Was Off. He Was Gone.
8. The Yuba County Five: Five Men, One Car, and a Winter Nobody Explains
9. Jodi Huisentruit: The Anchor Who Never Made It to the Morning Show
10. The Missing on America's Roads: Five Cases, One Pattern (compilação própria — a peça primária do canal)

## 13. Métricas de sucesso

- **D+2:** CTR vs mediana do canal (alvo inicial ≥4% [ALEGADO]); AVP ≥40% em 12–20 min [ALEGADO]; retenção 30s ≥70% [ALEGADO]; queda do 1º minuto ≤55% [PRATICANTE — ref `01`].
- **D+7:** views, inscritos, conversão short→long (cliques no Related/comentário fixado).
- **Meta de validação:** em 30 dias, ≥1 long com 10k+ views e AVP ≥40% e ≥2 shorts com loop >100% → rodar novo `niche_scan --brief` e reavaliar os gates antes de escalar cadência.
