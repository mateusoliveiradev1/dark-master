# Modelo — Psicologia dark (experimentos, comportamento e manipulação)

> Categoria: Psicologia · Subnicho: experimentos psicológicos, comportamento humano e manipulação · Slug: `psych-dark-psychology`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $10–18 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (0/14 canais únicos passam os 3 gates; fome real e 2 canais long-form EN a 2/3 gates — ver `evidencia.md`).
> Blueprint válido para piloto de formato, com lançamento condicionado a re-scan que passe os gates (≥3 canais ≤45d). Revalidar em 2–4 semanas.

## 1. Posicionamento (1 frase)

Estudo de caso documental de experimentos psicológicos reais e da mecânica do comportamento humano (obediência, conformidade, histeria coletiva, confinamento, persuasão) para espectadores de 25 a 54 anos que querem ciência contada como história, sem autoajuda e sem diagnóstico.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália, Irlanda). Consome true crime, dark history, documentário de ciência e "psychology explainers". O que a demanda mostra: no r/psychologyresearch há pedido explícito por conteúdo "science-based rather than something that mentions psychology but is really self help"; no r/psychologystudents, fãs de experimento em vídeo citam Mind Field (Vsauce) como referência de formato.
- **Promessa do canal:** em cada episódio, um experimento ou caso clínico por inteiro. A pergunta da época, o desenho, o que deu errado, a crítica/replicação e o que a ciência mantém hoje, sempre com documento e fonte.
- **Inimigo da promessa:** autoajuda genérica ("5 signs you're being manipulated"), diagnóstico de espectador, manipulação ensinada como tutorial, número sem procedência, sensacionalismo de choque.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Experimentos clássicos (obediência, conformidade, privação, escolha) | alta — 106 termos em "psychology experiment documentary" | média — Why Did God?, En Dias Como Hoy e Echo Trace cobrem o tema no long e no minidoc | o experimento por dentro: setup, método, o que deu errado e a crítica/replicação |
| Casos clínicos e famílias estudadas (Genain, Galvin, quintuplos) | alta — flares de 1,16M e 802k no History Mark | baixa em EN long-form — 1 canal convergente domina a evidência | "o estudo que falhou": ciência, ética e as pessoas por trás do dado |
| Histeria coletiva e pânico moral | média — "mass hysteria" aparece em Why Did God? e no History Mark | baixa | cronologia do surto + o que a ciência conseguiu medir (e o que nunca explicou) |
| Confinamento e isolamento (Acali, Biosphere 2, privação linguística) | alta — Acali retold por 4+ canais entre 2023 e 2026 (ver `evidencia.md`) | baixa-média | diário de bordo: o que a convivência forçada revelou, com registro de época |
| Mecânica da manipulação (persuasão, propaganda, grupos, cultos) | alta — 272 termos em "dark psychology" | alta em Shorts; média em long EN | mídia-literacia: reconhecer a tática, nunca um manual de manipulação |

## 4. Lane e formato

- **Lane:** long-first. Justificativa em número: os dois canais EN com flare no cruzamento são 100% long — History Mark: Exposed (14 de 14 uploads entre 19:56 e 45:16) e Why Did God? (10 de 10 entre 8:07 e 13:15). Os canais de maior views/dia das duas buscas (Stories hub 912.766/dia, The First Humans 7M 652.795/dia, ScenicMotionsBeyondVerse 122.755/dia) são Shorts de 0:04 a 0:30 e não convergem com documentário. Ver `evidencia.md`.
- **Duração alvo:** 10–20 min (faixas observadas: 8–13 min no Why Did God?, 20–45 min no History Mark). **Cadência:** 1 long por semana, com 1 Short-teaser a cada 2–3 longs quando a série tiver fôlego.
- **Mix:** até 20% Shorts. O Short é teaser do episódio, sempre apontando para o long do dia (ref `31`). O tema está saturado de Shorts com narração sintética — o valor do modelo está no long com fonte.

## 5. Fingerprint de formato (o que o recomendador lê)

Duração 10–20 min, 16:9, voiceover sem rosto, tom contido de documentário. Cadência semanal. Thumbnail de arquivo dessaturada com 1 rosto histórico (ou silhueta) e 1 objeto-símbolo do experimento. Títulos com nome próprio (o estudo, a família, o experimento) e uma contradição. Descrição com fontes públicas e aviso educativo. Convergência confirmada nos dois canais-evidência: 100% long-form, sem Shorts no feed (leitura de 2026-09-22).

## 6. Estrutura de roteiro

- **Beats:** `models/psych-dark-psychology/beats.json` (gênero `psych-dark-psychology`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min) quando houver arquivo e 3 fontes; FINO, 1.900–2.400 palavras (12–15 min) quando só o estudo original estiver disponível. ≈150–160 palavras/min (narração dark, pausada).
- **Dispositivos:** re-hook a cada 2–4 min, re-engage por volta de 3 min e de 6 min, 3 a 5 open loops abertos nos primeiros 20s, pattern interrupt a cada 30–90s, pergunta central (ética ou científica) que só se resolve no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio (estudo original, registro/arquivo do experimento, transcrição pública ou dado compilado) + 1 crítica ou replicação. Serve: paper original, reanálise publicada, reportagem de época com documento, entrevista posterior de participante. Nada entra sem 2 fontes cruzadas e camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada + stake (o resultado famoso vs. o que o arquivo mostra; o experimento desenhado para provar violência que terminou em amizade).
- **Exemplos:**
  1. "Sixty-five percent of ordinary people flipped the final switch. Four decades later, researchers went back to the tapes and found a different story."
  2. "A teacher, a whistle and five days. That is how a normal high school became a movement no one could stop."
  3. "Ten strangers on a raft and a scientist who wrote in his journal that he hoped they would turn on each other. By week two, they were best friends."
  4. "Identical quadruplets, one diagnosis, one famous study — and a question the researchers never answered."
  5. "Twelve children. Six diagnoses. One genome that researchers still study today."
- **Proibido:** abstração, data ou local antes do gancho, meta-linguagem ("neste vídeo"), sensacionalismo de choque, prometer diagnóstico ou aconselhamento.

## 8. Thumbnail

- **Composição:** 1 sujeito de arquivo (retrato histórico, silhueta, mãos) + 1 objeto-símbolo do experimento (botão, cerca, máscara, cronômetro, porta) + 3–5 palavras, sempre com 1 nome próprio ou 1 número.
- **Paleta:** dessaturada (cinza, sépia, azul-noite) com um único acento âmbar ou vermelho. **Fonte:** condensed sans bold, alto contraste, legível a 120px.
- **Nunca:** gore, corpo ferido, texto de diagnóstico ("you are being manipulated"), rosto de pessoa viva fora de contexto público documentado, repetir as palavras do título.

## 9. Monetização

- **AdSense (classe):** $10–18 [ALEGADO]. A classe se ancora em Education $10–15 e Documentary $12,6 da tabela de `10` [ALEGADO]; fontes web de 2026 reportam $4–12 para "psychology" genérico e até $20 em psicologia de finanças — a faixa alta depende de público US, retenção e enquadramento documentário/científico (fontes em `evidencia.md`). Nunca apresentar como fato; confirmação só no Analytics.
- **Janela regulatória [OFICIAL]:** em janeiro de 2026 o YouTube flexibilizou a monetização de temas sensíveis não gráficos com enquadramento educativo; as diretrizes advertiser-friendly citam "apresentar dados sobre psicologia humana" como exemplo de contexto científico elegível. Isso favorece análise e documentário, não choque e não aconselhamento.
- **Produto digital:** "source file" de $9–19 por episódio ou série (estudo original anotado, crítica, replicações, linha do tempo e bibliografia) vendido no fim dos episódios.
- **Patreon/membros:** acesso antecipado, arquivo de fontes e votação do próximo estudo.
- **Afiliado:** livros de referência do subnicho (Obedience to Authority, The Lucifer Effect, Hidden Valley Road e afins).
- **Rota no funil (`21`):** Short-teaser → inscrito → episódio long → source file → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 10–15 horas por episódio (pesquisa 6–9h com paper original e 2 críticas; roteiro 2–3h; montagem 3–4h). Assets: Wikimedia, Internet Archive, arquivos públicos e arte procedural; nunca usar trechos de filmes licenciados (The Raft, 2018, e similares não são domínio público).
- **Voz:** TTS de qualidade (edge-tts para protótipo, ElevenLabs para publicação), ritmo pausado de narração dark, ≈150 palavras/min. Divulgação de IA no pacote quando voz ou visual forem sintéticos.
- **GATE 100%:** sem todas as imagens aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/saúde [OFICIAL]:** a política de misinformation médica do YouTube se aplica a saúde mental e tratamento. Regra do modelo: sem diagnóstico, sem conselho clínico, sem promessa terapêutica; disclaimer educativo no pacote; toda afirmação científica com estudo citado e crítica/replicação ao lado.
- **YMYL e credencial:** fontes de 2026 alertam que "conselho não verificado" e recomendação de tratamento sem credencial violam políticas de saúde do Google Ads. O modelo fica do lado da história e da ciência, nunca do "how to".
- **Enquadramento "dark":** nunca ensinar manipulação; o ângulo é mídia-literacia ("como reconhecer"). Caso observado em 2026: canal faceless de psicologia dark com cerca de 200k inscritos foi demonetizado em março, segundo relato do próprio canal [REPORTADO]. Evitar estética "anti-establishment" e títulos de "truques".
- **Inautenticidade:** o tema é ímã de Shorts com narração sintética (117 vídeos em 259 dias em um único canal hindi de dark psychology; Shorts virais de histórias humanas com 912k views/dia no cruzamento). O modelo se protege com 1 peça primária por episódio, estrutura variável e voz própria.
- **Pessoas e ética:** participantes de experimentos são pessoas, algumas vivas. Nome e imagem apenas em contexto público documentado; sem detalhe clínico privado; sem culpar famílias; [FATO] separado de [REPORTADO]. Temas de autolesão e suicídio não podem ser focais.
- **Direitos:** arquivo com licença verificada; filmes e séries sobre os casos têm direitos próprios.

## 12. 10 ideias-semente (títulos)

1. The Tapes That Rewrote the Stanford Prison Experiment
2. The Third Wave: Four Days That Turned a School Into a Movement
3. The Acali Raft: 101 Days at Sea With a Scientist Waiting for a Mutiny
4. The Genain Quadruplets and the Schizophrenia Study That Failed Them
5. Six Schizophrenia Diagnoses in One Family: What the Genome Study Found
6. Little Albert: The Experiment Psychology Spent a Century Trying to Undo
7. The Laughter Epidemic That Closed a School With No Pathogen in Sight
8. Robbers Cave: The Summer Camp Experiment That Manufactured a Feud
9. Biosphere 2: Two Years Sealed Inside, and the Group That Split in Half
10. The Forbidden Experiment: The Research Question No Ethics Board Will Ever Approve Again

> Todo número citado nesses títulos (nomes, contagens, duração, dias) precisa de fonte primária na pesquisa do episódio. Nenhum entra no roteiro sem 2 fontes.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVD e AVP lidos contra a referência de mercado [PRATICANTE] e contra a mediana da própria conta (o YouTube não publica meta de CTR).
- **D+7:** episódio novo com pelo menos 1.000 views/dia no acumulado do canal; inscritos crescendo acima de 1% dos views do episódio.
- **Meta de validação em 30 dias:** 3 a 4 episódios publicados, com pelo menos 8.000 views cada e soma dos 5 primeiros acima de 10.000. Se 2 ou mais episódios derem outlier de 5× ou mais contra a mediana do canal, o formato está confirmado e o modelo pode ser promovido a PASSA em novo scan.
