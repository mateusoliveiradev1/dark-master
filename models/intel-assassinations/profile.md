# Modelo — Atentados políticos (assassinatos políticos, atentados e investigações oficiais)

> Categoria: Inteligência · Subnicho: assassinatos políticos, atentados e investigações oficiais · Slug: `intel-assassinations`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $10–18 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (0 de 14 canais pequenos passam os 3 gates; 1 emergente ≤90d; outlier ≥3× em 6 canais — ver `evidencia.md`)

## 1. Posicionamento (1 frase)

Anatomia documental de atentados políticos e do inquérito que veio depois (o dia, a falha de segurança, o laudo, o arquivo) para espectadores de 25 a 54 anos que querem o documento no lugar da teoria.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália), já consome true crime, história e geopolítica. As threads coletadas mostram o mesmo pedido: documentário "historically accurate", "focused on the autopsy evidence", sem "conspiracy talk" (r/letterboxd, r/history, r/JFKassasination, 2015–2026). A demanda se espalha por casos fora do eixo EUA (Indira Gandhi e Ahmad Shah Massoud foram os dois maiores outliers on-topic da coleta).
- **Promessa do canal:** cada episódio reconstrói um atentado com uma peça primária (relatório oficial, laudo, mapa de rota, ficha de arquivo) e fecha com o que a investigação provou e o que continua em aberto.
- **Inimigo da promessa:** teoria afirmada como fato, gore, glorificação do atirador, viés partidário, número sem fonte, ataque tratado como espetáculo.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Casos clássicos dos EUA (JFK, RFK, MLK, Malcolm X) | alta — threads de 2015 a 2026 pedindo o "melhor documentário sobre JFK"; o especial da ABC7 sobre JFK tem 1,6M de views | alta — streaming, TV e a camada de conspiração já ocupam o espaço | só o arquivo e o inquérito: o que o laudo provou e o que ficou em aberto, sem afirmar teoria |
| Líderes fora do eixo EUA (Indira e Rajiv Gandhi, Bhutto, Sadat, Rabin, Massoud, Lumumba) | alta nos números — Indira fez 14,4× e Massoud fez 1.236,9× contra a mediana do próprio canal | baixa-média em EN long-form: nenhum canal dedicado apareceu na amostra | um caso por episódio, com peça primária local e consequência documentada |
| Assassinatos que mudaram o curso de uma guerra (Franz Ferdinand em 1914, Massoud na véspera do 9/11) | alta — "What Actually Happened to EVERY Senator Who STABBED Julius Caesar?" fez 915.087 views (7,7×) | média | a cadeia de consequências: o que veio depois do tiro |
| Investigações oficiais e arquivos (Warren, HSCA, ARRB, autópsias, FOIA) | média-alta — em 2026 o r/JFKassasination segue pedindo material de evidência médica e comparação de laudos | baixa em EN long-form dedicado | o documento como protagonista: conclusão oficial × lacuna documentada |
| Atentados fracassados e falha de protocolo (Reagan 1981, Brighton 1984, João Paulo II 1981, 20 de julho de 1944) | média — sem outlier próprio na amostra | baixa | a falha de segurança como mecanismo central, em tom de análise |

## 4. Lane e formato

- **Lane:** long-first. Justificativa em número: toda a evidência de formato é long-form (America's Wars 10:52–52:30; Graven History 20:24–28:31; Inqalaab 16:12–53:35; Anuj Bhardwaj 24:52–33:59; StoryHouse Africa 4:03–2:31:59; Capital of DOC 7:58–23:00). O único canal de Shorts do cluster (No Thoughts, Head Empty, vídeos de 7s) é meme/entretenimento e está fora do cruzamento.
- **Duração alvo:** 18–30 min (faixa observada: 10–53 min). **Cadência:** 1–2 long/semana; o teto observado em canal de política/história foi de 2–3 por semana (Inqalaab).
- **Mix:** até 20% Shorts, sempre teaser do episódio da semana apontando para o long do dia (`31`).

## 5. Fingerprint de formato (o que o recomendador lê)

16:9, 1080p ou mais, 18–30 min, voiceover sem rosto, stills de arquivo, mapas de rota e documentos escaneados com zoom lento. Títulos de caso com fórmula verificada no nicho: "What Actually Happened to…", "The Untold Story", "The Tragic Last Days", "Two Days Before 9/11" (contagem regressiva). Episódios em série quando o caso pede (Part 1/2). Thumbnail de retrato de arquivo ou objeto com 1 número. Descrição com fontes e capítulos. Convergência confirmada em quatro canais com últimos uploads lidos em 22/09 (America's Wars, Graven History, Inqalaab, Anuj Bhardwaj).

## 6. Estrutura de roteiro

- **Beats:** `models/intel-assassinations/beats.json` (gênero `intel-assassinations`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). RICO para caso com arquivo denso (24–27 min, 3.400–3.800 palavras).
- **Dispositivos:** re-hook a cada 2–4 min; re-engage perto de 3 e de 6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central ("quem sabia, e o que foi feito com o aviso?") que só se resolve no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: relatório de comissão, laudo de autópsia, mapa de rota do dia, ata de interrogatório, ficha desclassificada, transcrição de julgamento. Toda afirmação em camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** documento ou objeto concreto + falha humana verificável (o guarda que saiu do posto, o motorista que virou à esquerda, a câmera que era uma bomba).
- **Exemplos:**
  1. "Two days before the planes hit New York, he was giving an interview to two men with a camera. The camera was a bomb."
  2. "The driver didn't know the route had changed, and the car stopped in front of the only man in Sarajevo who had walked away from the plan hours earlier."
  3. "For twelve years after the shots, the most important home movie in America sat in a vault, and almost nobody had seen a frame of it play."
- **Proibido:** abstração, data/local antes do gancho, meta-linguagem, gore, afirmar teoria, número sem fonte.

## 8. Thumbnail

- **Composição:** 1 retrato de arquivo ou 1 objeto (o carro, a rota no mapa, o relatório carimbado, a porta do quarto) + 1 número quando houver + 3–5 palavras.
- **Paleta:** sépia dessaturado e azul-aço, com um único vermelho. **Fonte:** serif condensada ou stencil, alto contraste, legível a 120px.
- **Nunca:** corpo, sangue, momento do disparo, footage do ataque, qualquer imagem gráfica (política de ads), rosto de pessoa viva tratado como culpado, repetir as palavras do título.

## 9. Monetização

- **AdSense (classe):** $10–18 [ALEGADO]. Fontes de mercado: Documentary a $12,6 e Dark History a $12,2 (autonolab, 07/09/2026) [ALEGADO]; History/Documentary com faixa de $6–14 e mediana de $9 nos EUA (fluxnote) [ALEGADO]. Contraponto honesto: a mediana de 300 canais auditados pela AIR Media-Tech em 2026 foi $2,30, e News & Politics ficou em $2,60; limited ads por violência/tema sensível pode cortar de 50% a 80% do RPM. O topo da faixa só se sustenta com audiência tier-1, mid-rolls e classificação limpa.
- **Produto digital:** dossiê de caso $9–19 (linha do tempo, mapa de rota, documentos e leitura comentada). Vende no fim das séries.
- **Patreon/membros:** páginas de arquivo anotadas, comparação de laudos, voto do próximo caso.
- **Afiliado/brand:** livros de história e true crime; serviços de streaming e documentário (categoria que costuma patrocinar o nicho) [ALEGADO].
- **Rota no funil (`21`):** Short-teaser → inscrito → long → dossiê → membro.

## 10. Produção

- **Custo/tempo por vídeo:** a pesquisa de arquivo e o roteiro são o gargalo; o visual é stills com motion sutil. Produção automatizada no formato documental é citada na faixa de $45–$180 por episódio (VoxBooster, 17/09/2026) [ALEGADO], e um case de história faceless citou ~$700/mês para 8 vídeos [ALEGADO, referência `14`]. Assets: National Archives, JFK Library, Mary Ferrell Foundation, Library of Congress, Wikimedia/Europeana, CIA CREST, salas de leitura FOIA, autos judiciais.
- **Voz:** TTS de qualidade (edge-tts no protótipo, ElevenLabs na publicação), ritmo pausado de narração dark, cerca de 150 palavras por minuto. Divulgar IA quando voz ou visual forem sintéticos.
- **GATE 100%:** sem todas as imagens licenciadas e aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** violência em contexto documental é elegível, mas "momento visível da morte", "sofrimento extremo", "execuções" e "glorificação da violência" ficam fora mesmo com contexto (Advertiser-friendly guidelines, atualização de agosto/2026; leitura da taxonomia em quasa.io, 22/08/2026). Regra do estúdio: nenhuma imagem de execução, sangue ou corpo; autoclassificação sempre.
- **Político/legal:** pessoas vivas = "alleged/accused"; nenhuma teoria apresentada como conclusão; nenhum detalhe operacional de ataque que sirva de instrução.
- **Política de conteúdo:** alegações falsas que minam confiança em processos democráticos não monetizam; documentário que cita a alegação deixando claro que é falsa segue elegível (atualização de agosto/2026). Consequência prática: o canal apresenta teoria como teoria, com a fonte e o contra-argumento.
- **Inautenticidade:** o tema atrai compilação de conspiração e slop de IA. Antídoto: 1 peça primária por episódio, estrutura variável, posição assumida, sem metadados duplicados.
- **Direitos:** newsreel e filmes de TV têm dono; checar licença antes de usar.
- **Ética:** o canal centra a vítima e o sistema, nunca o atirador como protagonista; nada que possa incentivar imitação.

## 12. 10 ideias-semente (títulos)

1. Two Days Before 9/11: The Assassination of Ahmad Shah Massoud
2. The Wrong Turn That Started a World War
3. Indira Gandhi: The Guards Standing Beside Her
4. The Last Song in Rabin's Pocket
5. The Truck That Joined Sadat's Parade
6. Shinzo Abe: The Gun Built from Tape and Two Tubes
7. Martin Luther King: The Window Across the Street
8. What Happened to the Men Who Killed Caesar
9. The JFK Files: What Was Released and What Is Still Sealed
10. Benazir Bhutto: The Last Rally on the Rawalpindi Road

> Todo número e nome próprio nesses títulos tem base documental a confirmar na pesquisa do episódio, com 2 fontes cruzadas e camada [FATO]/[REPORTADO]. Nada entra no roteiro sem verificação.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVD/AVP lidos contra a referência da `01`; CTR contra a mediana da própria conta, porque o YouTube não publica meta de CTR.
- **D+7:** pelo menos 1.000 views/dia no acumulado do canal; inscritos crescendo acima de 1% dos views do episódio.
- **Meta de validação em 30 dias:** 3 episódios publicados, com ≥8.000 views cada e soma dos 5 primeiros ≥10.000. Se 2 ou mais episódios derem outlier de 5× ou mais contra a mediana do canal, o formato está confirmado e o modelo pode ser promovido em novo scan.
