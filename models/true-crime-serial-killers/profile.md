# Modelo — Serial killers (bio)

> Categoria: True crime · Subnicho: biografias criminais e casos conhecidos · Slug: `true-crime-serial-killers`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $6–12 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (gates rígidos: 1/3 na query ampla, 0/3 na estreita — ver `evidencia.md`)

## 1. Posicionamento (1 frase)

Documentários de arquivo sobre serial killers e os casos que os cercam, para espectadores de true crime que querem o processo investigativo — o que os registros provam e onde a polícia falhou — em vez de gore e sensacionalismo.

## 2. Público e promessa

- **Público:** hipótese (a API não expõe idade/gênero) — adultos 25–54 nos mercados EN (EUA, Reino Unido, Canadá, Austrália); já consomem Dr. Insanity, 48 Hours, Casefile, Real Crime e canais faceless de case-file; binge em playlist; consumo noturno/em segundo plano (funciona bem como áudio + visual). Confirmar no Analytics do canal.
- **Promessa do canal:** todo episódio reconstrói um caso (biografia criminal ou caso conhecido) a partir de registros — linha do tempo, perícia, interrogatório, julgamento e consequência — com vítimas nomeadas e respeito.
- **Inimigo da promessa:** sensacionalismo; gore/descrição de ferimentos; teoria vendida como fato; foto real de vítima; imagem sintética realista de pessoa real do caso; clickbait que o episódio não entrega.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Biografias de nomes conhecidos (Kemper, Ramirez, Green River, Hillside Strangler) | alta — termos: `serial killer documentary edmund`, `ramirez`, `green river`, `hillside strangler`, `biography` | alta (Netflix + catálogos de estúdio dominam) | "o que o processo provou vs o que a TV repete": arquivo + contradição verificada |
| Case files / FBI files / interrogatório | alta — termos: `fbi files`, `interrogation`, `interview`, `police`, `caught` | média | reconstrução do processo (linha do tempo + transcrições citadas) — o formato de menor risco de yellow icon (`09`) |
| Cold case/unsolved ligados a serial killers | alta — termos: `cold case`, `unsolved`, `unidentified`, `unknown` | média | DNA/genética forense como protagonista (aparece no cluster: Othram Studios, laboratório de DNA, 42,4k views/dia) |
| Fora dos EUA / lesser known | média — termos: `uk`, `asia`, `africa`, `india`, `japan`, `russia` | baixa–média | casos internacionais sem cobertura EN saturada (gap apontado pelas fontes web: "casos regionais/sem cobertura internacional") |

## 4. Lane e formato

- **Lane:** long-first — justificativa: os 3 canais com outlier ≥3× no cluster são long-form, com medianas de 1,2M (Red File), 84k (FBI Investigates) e 32k (Crimewatch Central) views por vídeo; o formato dominante do nicho é o documentário longo (40–55 min nos catálogos de estúdio; 16–25 min nos canais faceless novos). Ver `evidencia.md`.
- **Duração alvo:** 16–24 min (PADRÃO ~18–21) · **Cadência sugerida:** 2 long/semana + ≤1 Short a cada 2 semanas (≤20% Shorts).
- **Mix:** o long-form carrega watch hours, receita e autoridade; o Short é só a porta do caso da semana. Se o funil Short→long não for medido, cortar Shorts.

## 5. Fingerprint de formato (o que o recomendador lê)

- Documentário narrado 16–24 min, uma voz, b-roll de arquivo/documentos/mapas + arte procedural; sem talking head, sem intro de canal.
- Capítulos nomeados (linha do tempo); cortes a cada 4–8s; trilha contida.
- Títulos com citação, contradição ou reveal verificável (padrão dos outliers do cluster: Red File 10,5× com citação + reveal de DNA; FBI Investigates 4,3× com "FBI Manhunt").
- Thumb: 1 sujeito (silhueta/arquivo estilizado) + 1 elemento documental (selo "CASE FILE", data, mapa) + 2–4 palavras; paleta dessaturada (cinza/âmbar/azul), nada de sangue.
- Fingerprint é hipótese de partida — a API externa não expõe estilo nem watch time; validar nos primeiros 5 uploads por convergência de formato.

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-serial-killers/beats.json` (gênero `true-crime-serial-killers`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO (18–21 min; ~2.900–3.300 palavras; ~150–160 palavras/min). FINO para caso com pouca fonte; RICO para biografia densa (24–27 min).
- **Dispositivos:** open loops nos primeiros 20s (3–5 promessas); rehooks a cada 2–4 min; re-engage ~3 e ~6 min; pergunta central que só fecha no fim; pattern interrupt a cada 30–90s; fim abrupto sem "obrigado por assistir".
- **Pesquisa obrigatória:** 1 peça primária por vídeo — linha do tempo montada a partir de 3+ fontes (court records, FBI Vault, jornais de época digitalizados, transcrições) com separação [FATO]/[REPORTADO]/[LENDA]. Sem peça primária, o vídeo cai no balde "genérico/repetitivo" da política de conteúdo inautêntico (`09`).

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada / detalhe de arquivo (nunca o crime em si).
- **Exemplos (banco completo em `hooks.md`):**
  1. "The report says he acted alone. The file shows two sets of tire tracks."
  2. "They questioned him for six hours and let him go. They already had the match."
  3. "The interview lasted four hours. The recording stops after forty minutes."
- **Proibido:** gore/ferimento no gancho; data/local antes do gancho; abstração; meta-linguagem ("nesse vídeo"); prometer o que o episódio não mostra.

## 8. Thumbnail

- **Composição:** 1 sujeito (silhueta, objeto ou cena de arquivo estilizada) + 1 elemento documental (selo de arquivo, data, mapa) + 3–5 palavras que **não repetem** o título.
- **Paleta:** dessaturada (preto/cinza/âmbar); fonte sans condensada, alto contraste; testar legibilidade a 120 px.
- **Nunca:** cena de crime, sangue/ferimento, foto real de vítima, rosto sintético realista de pessoa real do caso, rosto de pessoa viva sem contexto/alleged, número sensacionalista.

## 9. Monetização

- **AdSense (classe):** $6–12 RPM [ALEGADO] — true crime/documentário não-gráfico; fontes web estimam $5–12 (FalconVid, 27/08/2026) e $4–10 (faceless.my, 09/05/2026); o índice da skill usa $6–12. Não é verificável de fora — só o Analytics confirma.
- **Produto digital:** dossiês "case file" (PDF com linha do tempo + fontes, $9–19) e packs de série; tripwire na descrição do episódio.
- **Patreon/membros:** sim — acesso antecipado, arquivo comentado, versão áudio (podcast crossover; Dr. Insanity publica áudio no Spotify).
- **Afiliado/brand:** audiolivros (Audible) e ferramentas de pesquisa/arquivo; evitar afiliações agressivas (VPN/apostas) que conflitam com a promessa documental. Brand deals são difíceis com advertiser limits — priorizar receita direta (produto + membros).
- **Rota no funil (`21`):** long explora e retém → Short do caso da semana → inscrito → membro/produto. Medir a conversão antes de manter Shorts.

## 10. Produção

- **Custo/tempo por vídeo:** ~8–14 h (pesquisa 4–6 h + roteiro/revisão 2–4 h + voz/imagem/edição 2–4 h), free tier — estimativa a validar no piloto.
- **Assets:** domínio público e arquivos oficiais (FBI Vault, NARA, Library of Congress, Wikimedia, Europeana), jornais de época digitalizados, processos judiciais públicos, mapas procedurais, documentos escaneados. Nada de foto de agência sem licença.
- **Voz:** TTS consistente (edge-tts/ElevenLabs) — voz única = marca; ~150–160 palavras/min; legenda queimada opcional; disclosure de IA quando voz/visual sintético (obrigatório, `09`).

## 11. Riscos

- **Advertiser limit (yellow icon) — o risco nº 1 do nicho.** [OFICIAL] A política de conteúdo amigável ao anunciante restringe conteúdo em que sangue, violência ou ferimento é **foco** sem contexto; contexto documentário/educacional conta a favor (YouTube Help, answer/6162278). [ALEGADO] Fontes de mercado dizem que true crime é "o nicho que mais coleta yellow icons" (FalconVid, 27/08/2026) e que CPMs ficam em $5–12. Mitigação: foco perícia (o menor risco, `09`), passado + linguagem factual, sem ferimento nos primeiros 15s nem na thumb, self-certification honesta a cada vídeo, pedir human review quando o automático errar, auditar os últimos 10 episódios (se 8/10 vêm limited, o formato está errado, não o caso).
- **Conteúdo inautêntico.** True crime faceless é o formato que mais cai em "template/slideshow" (`09`). Antídotos: 1 peça de pesquisa primária por vídeo, tomar posição, variar hook e estrutura entre episódios, nunca reutilizar metadados, limpar back catalog.
- **Pessoas vivas, vítimas e famílias.** Suspeito vivo = "suspect/alleged"; nunca foto real de vítima como centro do episódio; nunca imagem sintética realista de pessoa real do caso; linguagem de presunção de inocência em caso aberto; 3 fontes independentes; risco real de reclamação de família (harassment).
- **Direitos autorais.** Fotos e footage de TV/agências têm dono; claim vem da agência, não da pessoa retratada. Usar acervo público/open license e música licenciada; evitar news footage sem fair use claro.
- **Temas sensíveis.** Casos centrados em crianças ou abuso sexual permanecem restritos para anúncios; não usar como foco do canal.
- **Divulgação de IA.** Conteúdo sintético/altered deve ser divulgado; marcar não penaliza por si só (`09`).
- **Timing YPP.** Requisitos dobram em 01/02/2027 (8.000h ou 20M views de Shorts) — o modelo long-first já é o caminho de watch hours; validar o piloto antes da data.
- **Saturação e gate.** O cruzamento formato×tópico **reprovou os gates rígidos** nas duas buscas (1 canal gate-pass na ampla; 0 na estreita) — o topo está saturado e poucos canais <45d aparecem. Entrar só com diferenciação clara (perícia/arquivo, casos de uma camada abaixo, mercados não-EUA) e revalidar em ~2–4 semanas antes de escalar produção.

## 12. 10 ideias-semente (títulos)

1. Ted Bundy's Final Interview — and the Timeline That Breaks It
2. The Green River Killer: 49 Confessions and One File Still Open
3. The Traffic Stop That Ended the Hillside Strangler
4. Ed Kemper: The Confession Transcript Investigators Didn't Expect
5. BTK: The Floppy Disk That Closed a 30-Year File
6. Golden State Killer: What the DNA Files Still Don't Explain
7. The Serial Killer Who Wrote His Own Case File
8. Two Decades in a Freezer: The DNA That Finally Matched
9. The Serial Killer Who Confessed to 90 Murders — and the Ones He Didn't
10. Forgotten Files: The Killer Hiding in Plain Sight for 20 Years

## 13. Métricas de sucesso

- **D+2 (metas do modelo — benchmarks de praticante, não oficiais):** CTR ≥4% na thumb; retenção 30s ≥70% [PRATICANTE]; AVP estável entre capítulos (sem queda abrupta no minuto 1).
- **D+7:** ≥5.000 views por long (piso de sanidade para canal novo); inscritos por 1.000 views ≥2; 1 Short puxando o long da semana (conversão medida).
- **Meta de validação (30 dias):** 6–8 longs publicados, mediana do canal ≥20k views/vídeo, retenção média ≥40%, zero yellow icon nos últimos 10 (ou <3 limited), 1 outlier ≥3× da mediana do próprio canal. Se não bater, trocar o ângulo (caso/camada) antes de trocar o nicho.
