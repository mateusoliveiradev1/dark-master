# Modelo — Hoaxes e enganos

> Categoria: Psicologia · Subnicho: grandes farsas, fraudes científicas e enganos em massa · Slug: `psych-hoaxes`
> Lane: mixed · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–15 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — 1/3 gates no brief `hoax documentary`; 0/3 no cluster `famous hoaxes documentary`; fome em 3 canais: Uncanny 15,3×, CURIVIOS 239,6×, Reality Broke Archive 6,3×; 2 emergentes ≤90d)

## 1. Posicionamento (1 frase)

Documentário de arquivo sobre a farsa que enganou o mundo para espectadores 25–55 no mercado EN que querem entender como o engano foi construído, por que gente séria acreditou e o que o desmonte revela sobre quem somos — evidência antes de escândalo, e o caso fechado só até onde os documentos fecham.

## 2. Público e promessa

- **Público:** EUA/Reino Unido/Canadá/Austrália (EN), 25–55; consome Nexpo, Barely Sociable, Nick Crowley (3,11M subs), Captain Disillusion, Fascinating Horror e docs do History/Discovery; gosta de reconstrução em arquivo, análise de "como a fraude funcionou" e veredito calibrado. O tema tem demanda global — a coleta de set/2026 achou canais do recorte em russo (Архив Мортимера Холмса, 17,4k views/dia), chinês (晚松講故事, 179,6k views/dia) e hindi (Shubh Kaayande), o que sustenta uma versão EN com produção contida.
- **Promessa do canal:** todo episódio reconstrói uma farsa com registro primário — como foi apresentada, como se espalhou, quem duvidou, o que a derrubou e o que continua sem resposta — e sempre separa fato, versão reportada e lenda.
- **Inimigo da promessa:** chamar de "farsa" o que a evidência não fechou (ou de "mistério" o que já foi provado falso); sensacionalismo de "você não vai acreditar"; acusar pessoa viva sem registro público ("alleged"); debunk de duas frases sem mostrar o método; humilhar quem acreditou.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Fraudes científicas históricas (Piltdown, Archaeoraptor, fósseis e resultados forjados) | média-alta — Piltdown reacende na imprensa em 2026 (BBC, fev/2026); outlier de 6,3× em jul/2026 | baixa-média — pouco servido por canais dark; maioria é canal de ciência com rosto | O método do falsificador (as marcas, a tinta, a cola) + a técnica que desmontou, décadas depois |
| Hoaxes virais da internet (vídeos que não eram reais, deepfakes virais, ARGs de farsa, lonelygirl15) | alta — `fake influencer documentary`, `fake baby documentary`, `deception island documentary` no autocomplete; caso AI da orca com 87M views antes do debunk (ago–set/2025) | média — recorte mais disputado; players de horror/mistério já cobrem parte | Forense digital (o artefato que entrega a montagem) + anatomia da viralização, sem "assustador" gratuito |
| Casos paranormais em disputa (Enfield e afins) | alta — outlier de 15,3× com "Haunting or Hoax?" (jul/2026) | média-alta — horror/paranormal é cheio; lacuna é o veredito calibrado | "Nem debunk limpo, nem provado": evidência lado a lado, o que os fãs e os céticos ignoram |
| Enganos em massa e charlatanismo (curas milagrosas, pânicos morais, impostores históricos) | média — tema clássico e evergreen; sem termo dominante no autocomplete | baixa-média | Psicologia social do engano + quem lucrou; números e registros oficiais |
| Impostores e identidades falsas (falsos médicos, falsos heróis, personas inventadas) | média — `fake lawyer`, `fake judge`, `fake rich` no autocomplete | média | Linha do tempo da persona e o detalhe que a quebrou; pessoa viva = "alleged/charged" sempre |

## 4. Lane e formato

- **Lane:** mixed — justificativa da coleta: o brief tem fome em **long** (Uncanny, 15,3×, mediana de 7,7k, 45,9k subs) e em **Short** (CURIVIOS, 239,6×, vídeo `#shorts` de 28 dias); a classe documentary [ALEGADO] paga long-form ($10–25 CPM no recorte doc/edu, ver `evidencia.md`), e o Short serve como aquisição do caso. O funil Short→long só se mantém se medido (`references/21`).
- **Duração alvo:** long 15–24 min (PADRÃO; FINO para casos com pouca fonte, RICO para casos com arquivo denso) · short 20–28s · **Cadência:** 1–2 long/semana + 2 shorts/semana.
- **Mix:** ~70% long / ~30% short; o Short entrega 1 detalhe do caso e aponta Related Video para o long da semana (nunca CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

15–24 min, 16:9; título de veracidade ("X: Hoax or History?" / "The [fossil/video] That Fooled [quem]"); thumbnail com 1 objeto-símbolo (mandíbula, fita, foto, bilhete, carimbo) + 1 marca de exame (lupa, seta fina, selo REJECTED) + 3–5 palavras; voz única contida (voice-only brand); documentos digitalizados, recortes de jornal, arte procedural e diagramas no lugar de reenactment; sem rosto de suspeito na thumb. Convergência observada na coleta: os outliers recentes repetem a pergunta de veracidade — Uncanny "The Enfield Poltergeist: Haunting or Hoax?" (jul/2026), Reality Broke Archive "Piltdown Man: 40 year Fake Fossil (1912)" (jul/2026), CURIVIOS "The Viral Video That Wasn't" (ago/2026) — e o desmonte por exame (arquivo, teste, câmera) é o segundo ato comum.

## 6. Estrutura de roteiro

- **Beats:** `models/psych-hoaxes/beats.json` (gênero `psych-hoaxes`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 15–21 min (~2.400–3.300 palavras); FINO (12–15 min, ~1.900–2.400) para casos de fonte única; RICO (24–27 min, ~3.400–3.800) para casos com arquivo denso (Piltdown, Enfield).
- **Dispositivos:** 3–5 open loops nos primeiros 20s (o detalhe, quem sabia, por que ninguém testou); rehook a cada 2–4 min; re-engage ~3 e ~6 min; pattern interrupt a cada 30–90s; a pergunta central ("por que isso durou tanto?") só fecha no fim; o veredito calibrado é o clímax, não o susto.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — artigo original ou paper de replicação, laudo/exame, reportagem de época digitalizada, transcrição de gravação/áudio, decisão judicial ou release de museu/instituição; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[ALLEGED] explícitas no roteiro.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada do próprio registro (o detalhe que denuncia a fraude, dito sem adjetivo) + o tempo que ela durou.
- **Exemplos:**
  1. "The file marks on the teeth were still visible under a microscope. Someone made that jaw by hand."
  2. "The camera caught her bending the bar by hand. The famous photographs went into the books anyway."
  3. "Eighty-seven million people watched a trainer die. The trainer never existed."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); "you won't believe"; afirmar culpa de pessoa viva sem registro público; prometer veredito que o episódio não fecha.

## 8. Thumbnail

- **Composição:** 1 objeto-símbolo (mandíbula, fita cassete, foto antiga, bilhete, selo) + 1 elemento de exame (lupa, pinça, carimbo REJECTED, seta fina apontando um detalhe) + 3–5 palavras que não repetem o título.
- **Paleta:** sépia/arquivo com 1 cor de sinal (vermelho de carimbo ou azul de tinta) · **Fonte:** serifada de jornal ou sans condensada bold, testada a 120px.
- **Nunca:** rosto de pessoa acusada/viva reconhecível, foto de vítima, gore, dinheiro voando, seta e círculo vermelho de clickbait, primeiro frame escuro/ilegível.

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — classe "crime/documentary" da tabela do `10`; auditoria de mercado do recorte doc/edu cita CPM $10–25 (~$2,75–6,88 RPM) [ALEGADO — longformstudio, ago/2026]; só a Analytics do canal confirma.
- **Produto digital:** pack "hoax file" ($7–27) com linha do tempo, método do falsificador e checklist "how to test a claim"; guia de mídia literacy aplicado aos casos do canal.
- **Patreon/membros:** sim — early access, versão sem trilha, Q&A de casos, dossiê em PDF com as fontes primárias.
- **Afiliado/brand:** livros de ciência e jornalismo investigativo; streamings e festivais de documentário; cursos de fact-checking/mídia literacy [ALEGADO — categoria com anunciantes; pitch com brand-safety one-pager].
- **Rota no funil (`references/21`):** short (o detalhe que não fecha) → inscrito → long (o caso completo) → pack/dossiê.

## 10. Produção

- **Custo/tempo por vídeo:** 8–12h (pesquisa 4–6h; roteiro 2–3h; montagem 2–3h) + TTS; sem locução humana, locação ou equipe.
- **Assets:** Internet Archive, Wikimedia Commons, arquivos de jornal digitalizados (Chronicling America, Trove, British Newspaper Archive quando acessível), papers open-access, releases de museus/universidades, arte procedural para diagramas; nunca footage de terceiros sem licença (o acusado pode usar isso contra o canal).
- **Voz:** TTS edge-tts (en-US, voz contida) ou ElevenLabs; ritmo 150–160 palavras/min; voz única e consistente = marca; legendas revisadas.

## 11. Riscos

- **Compliance/advertiser:** acusação de fraude contra pessoa viva é o risco central — sempre "alleged/reported", citar o registro (processo, reportagem, confissão pública) e nunca ir além dele; casos com mortes (curas milagrosas, fraudes médicas) exigem enquadramento educacional e zero imagem gráfica; thumbnails com objeto e não com pessoa.
- **Inautenticidade:** em jan/2026 o YouTube terminou 16 canais (35M de inscritos somados) sob a política de conteúdo inautêntico, com fiscalização no nível do canal [TNW, 2026]; o recorte corre risco duplo porque "debunk" é fácil de mass-produzir. Mitigação: pesquisa primária por vídeo, estrutura que varia por caso, veredito calibrado — nunca "10 farsas famosas" em série templated no mesmo formato de 60s.
- **Outros:** **strike de retaliação** — documentado em 2026: o episódio "The Hoax Files Episode 1 – Thirdphaseofmoon Exposed" foi derrubado por copyright strike do próprio acusado (mai/2026), e há casos de censura via DMCA fabricado contra exposés de golpes (custo estimado de $2k–5k para o fraudador) [gadgetreview, set/2026]. Mitigação: narrar com documentos em vez de adjetivos, arquivar fontes, não usar footage do acusado, manter counter-notification preparada; difamação é resolvida pela lei do país citado, e opinião/crítica é protegida — mas o processo custa. Sem acusar pessoas vivas de crime sem condenação pública.

## 12. 10 ideias-semente (títulos)

1. Piltdown Man: 41 Years of Fake Bones
2. The Enfield Poltergeist: The Case Nobody Can Close
3. 87 Million Views. One Fake Trainer.
4. The Sea That Vanished (and Never Did)
5. Lonelygirl15: The Girl Who Wasn't
6. The Cottingley Fairies: Two Girls, Five Photos
7. He Sold the Eiffel Tower. Twice.
8. The Night Nobody Actually Panicked
9. Archaeoraptor: The Fossil That Was Two Animals
10. The Medicine That Glowed in the Dark

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 20–80 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 6–8 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; ≥300 inscritos; nenhum vídeo limitado por advertiser ou derrubado por claim.
