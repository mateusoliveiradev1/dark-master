# Modelo — Heists e roubos históricos

> Categoria: True crime · Subnicho: assaltos a banco/museu, roubos históricos e o dinheiro que sumiu · Slug: `true-crime-heists`
> Lane: mixed · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA no gate estrito** em 2026-09-22 — 1 canal passa os 3 gates (meta ≥3) + 1 quase-passer a 93% do gate; fome de algoritmo **SIM**; revalidar antes de escalar (ver `evidencia.md`)

## 1. Posicionamento (1 frase)

Documentário de assalto para quem prefere o plano ao sangue: cada episódio reconstrói um roubo famoso (museu, banco, cofre, trem) minuto a minuto e segue o rastro do dinheiro que sumiu.

## 2. Público e promessa

- **Público:** 25–45 anos, EUA/Canadá/UK/Austrália (idioma EN); já consome heist docs em streaming (Netflix: "This Is a Robbery", "Biggest Heist Ever"), podcasts de arte/assalto ("Last Seen" do WBUR + Boston Globe, "Crime & Canvas") e threads no r/DocuJunkies e r/MovieSuggestions — em set/2026 o tema está aquecido pela onda de roubos de museu (Louvre out/2025 + episódios "inspirados" em 2026). Gosta de true crime, mas prefere o quebra-cabeça do golpe ao gore.
- **Promessa do canal:** em todo vídeo o espectador entende o plano melhor do que a polícia da época entendeu, e sai com um detalhe verificável sobre para onde o dinheiro foi (ou por que nunca apareceu).
- **Inimigo da promessa:** sensacionalismo sanguinolento, acusação de pessoa viva, teoria sem fonte, "mistério" quando existe documento; reencenação gráfica.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete/trends) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Museus e arte (Gardner 1990, Louvre 2025, Antwerp 2003, onda de 2026) | **alta** — `art heist documentary`, `louvre heist documentary`, `boston art heist documentary`; Trends: louvre +266.100%, boston art +19.650%, gardner +300%/+60% | **baixa-média** no cruzamento EN long-form: só 1 canal small ≤45d encontrado (Heists and Capers, outlier 4.4× no caso Gardner) | O objeto que não dá para vender: 81 minutos, molduras vazias, recompensa de $10M |
| Bancos e cofres (Lufthansa 1978, Société Générale 1976, Hatton Garden 2015, Fortaleza 2005) | **alta** — `bank heist documentary` + `hatton garden heist documentary` (+60%); outliers de recap em hindi (35,7× / 328,5×) mostram volume do tema | **média** — volume grande, mas em formato movie-recap/explained (hindi); documentário EN é espaço distinto | A engenharia do golpe: túnel de 78 m, esgoto, parede do cofre; onde o dinheiro parou |
| Trens e transporte de valores (Great Train Robbery 1963, Securitas 2006) | **média** — outlier 65,8× em "Great Train Robbery"; Reddit pede docs de £53M (Securitas) | **baixa** | A fortuna em notas: o dinheiro que envelheceu e os erros depois do golpe |
| Joalherias e diamantes (Antwerp, Hatton Garden, Pink Panthers) | **média-alta** — `diamond heist documentary`; hatton garden +60% | **média** | O detalhe pequeno que derruba: uma impressão digital, uma fita, um cofre aberto |
| O rastro do dinheiro / cripto (Bitfinex, "Billion Dollar Heist") | **média** — `crypto heist documentary`, `bitcoin heist documentary` | **média** | Resgate, seguro, lavagem e o que "sumiu" — ponte com o nicho finance ($21–23 de classe) |

## 4. Lane e formato

- **Lane:** mixed — justificativa: há outlier long-form EN em canal de 41 dias (Heists and Capers, 4.4×–7.1× em 3 semanas; ALPHA DECODES 3,9× com 616 mil views) e outlier Short no mesmo tema (POV World17, art heist 19,1×) — o núcleo é long (receita/watch time), o Short é aquisição (`evidencia.md`).
- **Duração alvo:** long 12–20 min (padrão ~18) · short 20–28s · **Cadência:** 1 long/semana + 1 short a cada 2–3 long (ratio 0,28–0,40 — `10`).
- **Mix:** ~75% long / ~25% short (ratio de Shorts 0,28–0,40 — `10`); manter o Short só se o funil Short→long for medido (cliques no Related/comentário ≥2% em 30 dias; senão virar long-first — `30`).

## 5. Fingerprint de formato (o que o recomendador lê)

Long 16:9, 12–20 min, 1 long/semana + shorts 9:16 de 20–28s; narração EN contida (~150–160 palavras/min), voz única (voice-only brand — `14`); imagens de acervo público (NARA, Library of Congress, Wikimedia, Europeana — padrão do nicho em `14`) + mapas e timelines procedurais (planta do museu, túnel, rota da fuga, fluxo do dinheiro); sem rosto, sem reencenação gráfica. Thumb: 1 objeto-símbolo (moldura vazia, porta de cofre, joia, pilha de notas) + 3–5 palavras que não repetem o título. Convergência observada no canal-evidência: série de casos históricos nomeada por lugar + ano ("Nice 1976", "Inside the 1978 Lufthansa Heist at JFK") — o recomendador lê documentário criminal histórico em EN.

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-heists/beats.json` (gênero `true-crime-heists`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); RICO (24–27 min) para casos densos (Gardner, Louvre 2025); FINO (12–15 min) para roubos com pouca fonte. Short: ~60–70 palavras.
- **Dispositivos:** rehook a cada 2–4 min (nova peça do plano, dado do dinheiro); re-engage ~3 e ~6 min; 3–5 open loops no hook (o plano, o dinheiro, a pista); pattern interrupt a cada 30–90s (diagrama/mapa novo); pergunta central ("onde foi parar") que só fecha no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — linha do tempo oficial, autos de tribunal, registro do museu/FBI, lista do seguro, matéria de época; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[LENDA]. "O dinheiro que sumiu" é o ângulo, nunca a acusação sem fonte.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** relógio/contagem + contradição verificada (o número exato do golpe e o detalhe que não fecha).
- **Exemplos:**
  1. "Eighty-one minutes inside. A half-billion dollars out. The frames are still empty."
  2. "The cameras recorded everything. The thieves left with the tape."
  3. "They didn't break into the bank. They dug to it from the city sewers."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); gore; prometer o que o episódio não entrega.

## 8. Thumbnail

- **Composição:** 1 sujeito/objeto-símbolo (moldura vazia, porta de cofre, joia sob vidro, notas empilhadas) + 1 elemento de escala (cifra/contagem) + 3–5 palavras que não repetem o título.
- **Paleta:** preto/âmbar/dourado envelhecido, alto contraste; nada de sangue · **Fonte:** sans bold, legível a 120px.
- **Nunca:** gore, corpo, arma apontada, rosto de suspeito vivo como culpado, frame de streaming (Netflix/SBS/BBC) ou de filme (o tema atrai heist movies — não reciclar Hollywood).

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — classe do índice (`10`: true crime não gráfico $8–15). Fontes web 2026 divergem para baixo no gênero: $5–12 (fluxnote, mediana $8), $5–10 (virvid), $8–12 (earngenix, "True Crime Documentary"), $6–9 (Longform Studio, não gráfico), CPM $8–22 → RPM est. $5,40–9,90 (ytdark). A classe alta só se sustenta com enquadramento documentário, long 15+ min com mid-rolls e audiência US/UK — confirmar na Analytics, nunca projetar como fato.
- **Produto digital (tripwire $7–27):** "Heist Files" — dossiê por caso (mapa do túnel/planta, linha do tempo, o que nunca foi recuperado); bundle de temporada $19–27.
- **Patreon/membros:** sim — acesso antecipado + arquivo de fontes/mapas; true crime tem conversão de membership acima da média (`14`, ytdark).
- **Afiliado/brand:** livros de caso (Amazon Associates; ex.: "Thirteen Perfect Fugitives", de Geoffrey Kelly, mar/2026) e Audible; VPN/audiobook/podcast é o patrocínio padrão do gênero [ALEGADO — kineclip, 2026].
- **Rota no funil (`21`):** Short (1 detalhe do caso) → inscrito → long do dia → dossiê.

## 10. Produção

- **Custo/tempo por vídeo (estimativa operacional do modelo):** long 8–14 h (pesquisa 3–5 h; roteiro 2–3 h; assets/mapas 2–3 h; voz + edição 2–3 h); short 1–2 h (recorte do long). Sem locação, sem equipe.
- **Assets:** acervo público (NARA, Library of Congress, Wikimedia Commons, Europeana, arquivos de polícia/museu), mapas/timelines próprios, arte procedural para planta de túnel/cofre; nunca footage de terceiros sem licença.
- **Voz:** narrador EN (TTS edge-tts ou ElevenLabs; ~150–160 palavras/min, pausado) ou locução própria; voz consistente = marca (`14`). Divulgar voz/imagem sintética no pacote quando aplicável.

## 11. Riscos

- **Compliance/advertiser:** o subnicho é menos gore-prone que homicídio — o risco é enquadramento. Regra de 2026: framing documentário/educacional monetiza; imagem gráfica em thumb ou nos primeiros 15s derruba para Limited Ads mesmo com tema coberto (`longformstudio`, 2026). Foco em plano, engenharia e dinheiro; nada de violência, sangue ou corpo.
- **Pessoas vivas / casos abertos:** suspeitos presos (Louvre 2025) = "alleged/presumed innocent"; caso Gardner (não resolvido) = nunca afirmar culpa; recompensa e dados oficiais sempre com fonte.
- **Inautenticidade:** documentário narrado com assets sintéticos é alvo de flag automatizado (`longformstudio`, 2026) — 1 peça de pesquisa primária por vídeo, estrutura que varia, fontes na descrição, roteiro com ponto de vista próprio; sem template massificado (`09`).
- **Direitos:** obras de arte antigas em domínio público, mas fotografias de museu podem ter direito; surveillance e fotos de caso com copyright incerto; créditos no descritivo; nunca frames de streaming.
- **Dinheiro:** alegações de lavagem/desvio exigem [REPORTADO] e 2+ fontes; a pergunta central é "para onde foi", não "quem é culpado".

## 12. 10 ideias-semente (títulos)

1. 81 Minutes at the Gardner: The $500 Million Heist That's Still Open
2. The Sewer Heist of Nice: They Robbed a Bank From Under the Street
3. Lufthansa 1978: $5 Million in Cargo and a Trail That Went Cold
4. Hatton Garden: The £14 Million Hole in the Vault Wall
5. Seven Minutes at the Louvre: The Jewels That Never Came Back
6. The Day the Mona Lisa Walked Out of the Louvre
7. Brazil's $70 Million Tunnel Job
8. The Great Train Robbery: £2.6 Million and the Mistake After
9. Antwerp: The Fingerprint That Cracked a $100 Million Vault
10. The Empty Frames: 36 Years of the FBI's Biggest Art Hunt

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção de 30s ≥70%; AVD ≥30% em vídeos de 12–20 min (faixa saudável 30–45% em 15–30 min [PRATICANTE]); Short: swipe-away no 1º segundo <25% e AVP 50–65% (20–28s — `02`).
- **D+7:** views e watch time do long; inscritos por vídeo; conversão Short→long (cliques no Related/comentário fixado ≥2%); 1 outlier ≥3× a mediana do canal.
- **Meta de validação (30 dias):** 4–5 longs + 1–2 shorts publicados (ratio ~0,3 — `10`); ≥1 long com outlier ≥5×; funil Short→long medido; ≥500 inscritos; nenhum vídeo limitado por conteúdo gráfico. Se o funil não medir, cortar Shorts e manter long-first (`30`).
