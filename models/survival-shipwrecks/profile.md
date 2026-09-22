# Modelo — Naufrágios

> Categoria: Sobrevivência · Subnicho: naufrágios, desaparecimentos no mar e achados de casco · Slug: `survival-shipwrecks`
> Lane: long-first · Idioma: en (docs PT-BR, exemplos em EN) · RPM (classe): $8–14 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — brief automático deu REPROVA com 1/8 canais nos 3 gates; cluster 0/8; a classificação PARCIAL segue a legenda do README: fome cross-canal em 4+ canais de naufrágio e 4 emergentes ≤90d falhando só o gate de idade)

## 1. Posicionamento (1 frase)

Documentário de investigação sobre naufrágios para espectadores 30–60 no mercado EN que querem o dossiê completo de um navio — a viagem, o minuto da perda, a busca, o achado do casco e o que o inquérito concluiu — com registro público, respeito às vítimas e sem caça ao tesouro sensacionalista. O navio é o personagem; o oceano em si (abismo, mistérios do fundo) fica no modelo `mystery-ocean`.

## 2. Público e promessa

- **Público:** EUA/Reino Unido/Canadá/Austrália (EN), 30–60, peso masculino. Consome Oceanliner Designs (969 mil subs), Part-Time Explorer (492 mil), Brick Immortar (391 mil) e documentários de TV do segmento; assiste 20–45 min por episódio, muito em TV (um canal faceless de documentary history à venda reporta 77,2% das views nos EUA e 83% da audiência em 45+ [ALEGADO — Flippa, 2026]).
- **Promessa do canal:** todo episódio reconstrói um naufrágio ou desaparecimento com fontes públicas — linha do tempo, busca, descoberta do casco e causa provável — mostrando o que foi provado e o que segue aberto.
- **Inimigo da promessa:** sensacionalismo de tragédia; tesouro como isca de clique; teoria conspiratória apresentada como fato; gore e restos humanos; explorar famílias de vítimas; footage de documentário de terceiros sem licença.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Naufrágios de linha e desastres famosos (Titanic, Lusitania, Fitzgerald, Gustloff, Empress of Ireland) | alta — `titanic shipwreck documentary`, `fitzgerald` e `ww2 shipwreck documentary` entre os 72 termos | alta — âncoras com rosto (Oceanliner Designs 969k; Part-Time Explorer 492k) e TV saturam o ângulo "contar a história" | Forense do naufrágio: o que o inquérito concluiu, o que a descoberta do casco mostrou, o que o mito errou (Buried Frequencys fez flare de 15,4× checando filmes de Titanic) |
| Desaparecimentos sem traço (USS Cyclops, Joyita, SS Pacific, Mary Celeste) | alta — `shipwreck investigation`, `shipwrecks found`, `shipwreck detectives`; fome em 4 canais (jul–set/2026) | média — lacuna faceless EN: os outliers recentes do recorte estão em canais pequenos e em hindi, não nas âncoras | Reconstrução a partir do último sinal + busca + teorias rotuladas [FATO]/[REPORTADO]/[LENDA]; a pergunta "o que a evidência permite afirmar" |
| Achados e arqueologia subaquática (Endurance, Antikythera, Uluburun, Batavia, Atocha) | média-alta — `endurance`, `antikythera`, `uluburun`, `atocha`, `bom jesus` | baixa-média — ciência de expedição é rara no faceless EN | A expedição como narrativa: o que o casco e o carregamento revelam sobre a época; ciência acima de tesouro |
| Grandes Lagos (Edmund Fitzgerald, Lake Erie / Lake Serpent, `great lakes`) | alta — `shipwreck documentary great lakes` é o 2º termo do autocomplete; doc regional do Geltwood repercutiu em set/2026 (ABC) | média — história regional forte, mas poucos canais faceless dedicados | Série regional: água doce e fria preserva os cascos; arquivo + batimetria + memória das comunidades |
| Naufrágios de guerra (Jutland, frota japonesa, U-boats, SS Justicia) | média — `ww2 shipwreck documentary`; série semanal de TV (Shipwreck Secrets) com 184.247 views no episódio 1 | média — canais de história de guerra; risco alto de túmulo/restos | Arqueologia de campo de batalha subaquático com respeito a túmulos de guerra; zero restos humanos, zero coordenadas sensíveis |

## 4. Lane e formato

- **Lane:** long-first — justificativa: os outliers do recorte são longos (Part-Time Explorer: "Edmund Fitzgerald: The Full Story" 2.498.360 views, 45,4×; "The Wreck of the Andrea Doria", 783.004, 14,2× em jul/2026; Forbidden Mysteries: série `Shipwreck Secrets` de 41–44 min com 184.247 views no E1); a classe de RPM documentary [ALEGADO] paga ordens de magnitude acima de Shorts ($0.03–0.10, `references/10`); Shorts ≤20% apenas como teaser medido.
- **Duração alvo:** long 18–28 min (PADRÃO–RICO; compilações de biblioteca de 45–90 min ocasionais) · short 20–28s · **Cadência:** 2 long/semana + 1 short.
- **Mix:** ~85% long / ~15% short; o Short é teaser do arquivo da semana com Related Video apontando para o long.

## 5. Fingerprint de formato (o que o recomendador lê)

18–28 min, 16:9, 2 uploads/semana; título com nome do navio ou número (ano, tripulação); cold open de registro (último sinal de rádio, foto do casco, objeto recuperado); thumbnail com 1 objeto/casco + número + 3–5 palavras; voz única contida (voice-only brand); mapas, batimetria e diagramas no lugar de reenactment; série recorrente ("Wreck File") com numeração. Convergência observada na coleta: **Forbidden Mysteries** publica a série `Shipwreck Secrets` quase semanalmente (S1 E1–E6 entre jul e ago/2026, 41–44 min, E1 com 184.247 views); **Part-Time Explorer** converge em "um navio por episódio" com o nome no título (Andrea Doria, jul/2026, 783k; Edmund Fitzgerald, nov/2025, 2,5M); o emergente **Buried Frequencys** (15 dias, 162 subs) fez flare checando o que os filmes de Titanic erram — o ângulo "mito vs registro" é o mais fresco do recorte.

## 6. Estrutura de roteiro

- **Beats:** `models/survival-shipwrecks/beats.json` (gênero `survival-shipwrecks`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); RICO (24–27 min, ~3.400–3.800) para biblioteca; FINO (12–15 min, ~1.900–2.400) para casos com pouca fonte.
- **Dispositivos:** rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central (por que o navio se perdeu) fechada no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — inquérito oficial (Marine Casualty Investigation Branch, US Coast Guard, Wreck Commissioner, relatório de comissão), relatório de expedição (NOAA, Ocean Exploration Trust, Schmidt Ocean Institute), registro de bordo/jornal da época ou levantamento batimétrico (GEBCO); 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** último sinal verificado + escala/silêncio (navio que segue navegando vazio; SOS que não chegou; profundidade em metros; número de tripulantes).
- **Exemplos:**
  1. "The last words from the Edmund Fitzgerald were 'We are holding our own.' All 29 men were gone before the next check-in."
  2. "More than three hundred men left Barbados on a clear morning in 1918. No distress call was ever heard."
  3. "The Joyita was found five weeks late, half-submerged, with a working radio. All twenty-five people were gone."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); teoria como fato; prometer achado ou tesouro que o episódio não entrega.

## 8. Thumbnail

- **Composição:** 1 sujeito (casco em ângulo, navio visto de cima, ROV, objeto recuperado) + 1 elemento de escala ou mistério (número de tripulantes, profundidade em metros, X no mapa) + 3–5 palavras que não repetem o título.
- **Paleta:** azul-petróleo/verde-água com 1 cor de sinal (âmbar) · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** corpos, sangue, restos humanos, imagem de tragédia recente, familiares enlutados; seta/círculo de clickbait; primeiro frame escuro.

## 9. Monetização

- **AdSense (classe):** $8–14 [ALEGADO] — documentary/"dark history" em `references/10`; estimativas de mercado 2026 divergem para history/mystery: $4–10 (faceless.my), $8–18 (reelsmakerai) e $20+ reivindicado numa listagem de venda de canal faceless de documentary history (Flippa) [ALEGADO]; a classe só se confirma na Analytics do canal.
- **Produto digital:** pack "Wreck File" ($7–27) com linha do tempo, mapas, glossário (sonar, batimetria, inquérito) e o guia "how a shipwreck gets investigated".
- **Patreon/membros:** sim — early access, mapas em alta resolução, Q&A de casos, versão sem trilha.
- **Afiliado/brand:** livros de história marítima e arqueologia subaquática; museus e memoriais; modelos e jogos (o jogo Ship Explorer, da Oceanliner Designs, mostra a extensão de marca possível no nicho — referência de teto, não de clone).
- **Rota no funil (`references/21`):** short (teaser do arquivo) → inscrito → long (o dossiê completo) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 8–12h (pesquisa 4–6h; roteiro 2–3h; montagem 2–3h) + TTS; sem locução humana, locação ou equipe.
- **Assets:** domínio público e oficial (Library of Congress, National Archives, US Navy, NOAA Photo Library, Wikimedia Commons), batimetria GEBCO, releases de expedição, mapas e diagramas próprios; nunca footage de TV/documentário de terceiros sem licença (a série concorrente do recorte é conteúdo empacotado — não reproduzir).
- **Voz:** TTS edge-tts (en-US, voz contida) ou ElevenLabs; ritmo 150–160 palavras/min; voz única e consistente = marca; legendas revisadas.

## 11. Riscos

- **Compliance/advertiser:** naufrágios com morte são material sensível — enquadramento documental/educacional, sem imagem gráfica e sem close de vítima; thumbnails com objeto/mapa. A categoria "off-putting" (atualização de jul/2026) derruba conteúdo desenhado para angustiar ou manipular emoção; tragédia recente com famílias em luto (o documentário de streaming de jul/2026 sobre o desastre de 2012 é o exemplo vivo) fica fora do escopo do canal.
- **Inautenticidade:** em jan/2026 o YouTube terminou 16 canais (35M de inscritos somados; ~US$10M/ano estimados) sob a política de conteúdo inautêntico, e a fiscalização é no nível do canal (um padrão nos últimos 30 uploads pode derrubar a monetização inteira) [TNW, 2026]; a atualização de jul/2026 dividiu o alvo em 3 categorias (genérico/repetitivo/template; off-putting; AI personas em temas sensíveis) [TechCrunch, 2026]. Mitigação: 1 peça primária por vídeo, estrutura que varia, série e voz próprias — nunca "slideshow com TTS".
- **Outros:** direitos de footage jornalístico; naufrágios de guerra são túmulos (sem restos humanos nem coordenadas sensíveis); precisão (contradições entre fontes viram camada rotulada, não afirmação); pessoas vivas e famílias ("reported missing", sem especular); tesouros com litígio ativo (ex.: San José, disputado por três países) — reportar o litígio, nunca o direito.

## 12. 10 ideias-semente (títulos)

1. Edmund Fitzgerald: 29 Men, One Last Check-In
2. The USS Cyclops: 306 Men and No Distress Call
3. The Joyita: Found Adrift, Twenty-Five Gone
4. The Sultana: The Wreck Lincoln's Death Erased
5. Endurance: Found 107 Years After She Went Down
6. Andrea Doria: Two Ships, One Fog Bank
7. Batavia: The Mutiny That Started With a Wreck
8. 6,895 Meters Down: The Deepest Wreck Ever Surveyed
9. Scapa Flow: The Fleet That Scuttled Itself
10. Why Lake Superior Keeps Its Wrecks

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 30–100 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; ≥500 inscritos; nenhum vídeo limitado por advertiser/compliance.
