# Modelo — IA e falhas de tech (falhas de IA, algoritmos e acidentes tecnológicos)

> Categoria: Tech · Subnicho: falhas de IA, algoritmos e acidentes tecnológicos · Slug: `tech-ai`
> Lane: mixed · Idioma: en (docs em PT-BR) · RPM (classe): $15–25 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md`) — busca ampla "AI failure documentary": 0/8 gates; cluster estreito "AI incident documentary": 0/8 gates e 0 fome. Não escalar sem novo scan.

## 1. Posicionamento (1 frase)

Anatomia documental de falhas reais de tecnologia — IA, algoritmos e sistemas — para espectadores de 25 a 54 anos que querem o post-mortem (o log, o documento, a linha do tempo), não o hype de "a IA vai acabar com o mundo".

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália). Gente que já consome ColdFusion, Asianometry, BobbyBroccoli e Modern MBA; lê Hacker News; desconfia de hype de IA e detesta "AI slop".
- **Promessa do canal:** em cada episódio, a reconstrução de uma falha tecnológica do primeiro erro ao relatório final: o que o sistema fazia, o que prometia, o minuto exato em que falhou, quem pagou a conta e o que mudou na engenharia ou na norma depois.
- **Inimigo da promessa:** catastrofismo ("a IA vai nos matar"), antropomorfismo apresentado como fato ("a IA enlouqueceu"), clipe viral não verificado, número sem fonte, previsão catastrófica como entretenimento.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Falhas de IA em produção (agentes que apagam dados, chatbots que derrapam, alucinação com dano real) | média-alta — 112 termos no teste "AI failure documentary"; incidentes catalogados no OECD.AIM | alta de hype, baixa de post-mortem com fonte | post-mortem técnico com peça primária e separação fato/reportado |
| Algoritmos de mercado e automação financeira (Flash Crash 2010, Knight Capital 2012) | média — 83 termos em "algorithm documentary" (trading/tiktok/social media) | baixa-média | cronologia minuto a minuto + documento de regulador (SEC/CFTC) |
| Casos clássicos de software e sistemas (Therac-25, CrowdStrike 2024, outages em cascata) | média — evergreen de busca | média | engenharia do erro + o que mudou na indústria |
| Viés e decisões automatizadas (COMPAS, Amazon recruiting, Apple Card) | média | média | método do estudo + o contraditório da empresa |
| Acidentes de automação física (robôs em demo, MCAS, veículos autônomos) | alta | média-alta | relatório de investigação; sem gore, sem "robô assassino" |

## 4. Lane e formato

- **Lane:** mixed — com execução **long-first na prática**. Justificativa com número: os canais-referência do espaço são 99% long-form (Asianometry, 713 vídeos, 99% long [ALEGADO — outlierkit]) e o topo do nicho é long analítico (ColdFusion, BobbyBroccoli); na coleta de 22/09, dos 16 canais pequenos analisados nas duas buscas, os 5 com ≤45d falharam todos o gate de 5 primeiros ≥10k — nenhum formato de entrada se sustentou em Short. Regra do ref `30`: mixed só se o funil Short→long estiver medido — começar com 2–3 longs e no máximo 1 short-teaser por semana, medindo a conversão.
- **Duração alvo:** long 12–20 min (flagship 25–40 min); short 20–28s. **Cadência:** 1 long/semana + 1 short-teaser na semana do long.
- **Mix:** até 25% Shorts, sempre apontando para o long do dia (`references/31`). Sem long no ar, não há short solto.

## 5. Fingerprint de formato (o que o recomendador lê)

Long-form 12–20 min, 16:9, cadência semanal; thumbnail escura com 1 objeto (tela de erro, chip, terminal, braço robótico) + 1 número; voz-off sem rosto, tom analítico e contido; estrutura por capítulos com linha do tempo na tela; descrição com fontes primárias; episódios em série numerada ("Tech Autopsy 07: ..."). Mistura observada nos canais-referência: evergreen ~85% e análise de crise ativa ~15% [ALEGADO — outlierkit/Asianometry]. Short: 9:16, frame 1 = erro na tela + 3–5 palavras.

## 6. Estrutura de roteiro

- **Beats:** `models/tech-ai/beats.json` (gênero `tech-ai`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). FINO (1.900–2.400) para incidentes menores; RICO (3.400–3.800) para flagships de 24–27 min.
- **Dispositivos:** re-hook a cada 2–4 min, re-engage por volta de 3 e de 6 min, 3–5 open loops nos primeiros 20s, pattern interrupt a cada 30–90s (terminal → documento → diagrama), pergunta central que só se resolve no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: post-mortem público da empresa, relatório de regulador (SEC, CFTC, NTSB, FTC, FDA), paper ou anais de conferência, auditoria interna publicada, reportagem investigativa com documentos. Nada entra sem 2 fontes cruzadas e camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada no documento (o monitor dizia OK, o laudo mostrou 100 vezes a dose) + relógio (o minuto exato da falha).
- **Exemplos:**
  1. "The machine printed 'treatment complete.' The therapist was already running toward the room."
  2. "In forty-five minutes, a trading algorithm took a company that was fine and left it almost dead: $440 million."
  3. "The internal documents said the recommendations were 'unsafe and incorrect.' The product shipped anyway."
- **Proibido:** catastrofismo e previsão ("o próximo incidente será"), antropomorfismo não atribuído, clipe viral sem verificação, data ou local antes do gancho, abstração, meta-linguagem ("in this video"), culpar pessoa viva sem "according to the report".

## 8. Thumbnail

- **Composição:** 1 objeto de tecnologia (tela de erro, chip, braço robótico, rack, terminal) + 1 número ou código ("54", "$440M", "9s") + 3–5 palavras.
- **Paleta:** fundo escuro (azul-noite, grafite) com um único acento (vermelho de alarme ou verde de terminal). **Fonte:** condensed sans bold, alto contraste, legível a 120px.
- **Nunca:** logo de empresa sem licença, rosto de pessoa real ou sintético ambíguo, número sem fonte, repetir as palavras do título, catastrofismo visual ("fim do mundo"), gore.

## 9. Monetização

- **AdSense (classe):** $15–25 [ALEGADO] — tech/AI tem anunciantes fortes (SaaS, cloud, dev tools, hardware) e em `references/10` aparece como Tech/AI $7–21 [ALEGADO]; a metade alta da classe só se confirma se a execução for analítica e não gráfica. Estimativas públicas dos canais-referência divergem entre si para o mesmo canal (ColdFusion: $613–$9,7K/mês em uma casa, $2,5K–$15,3K em outra e ~$48K/mês em uma terceira [ALEGADO]) — trate tudo como hipótese, nunca como plano.
- **Produto digital:** tripwire $9–19 — "post-mortem pack" (linha do tempo, diagrama do sistema, documentos e checklist de engenharia).
- **Patreon/membros:** episódio estendido com fontes comentadas e votação do próximo caso; referência de mercado: BobbyBroccoli opera em estratégia Nebula-first [fonte em `evidencia.md`].
- **Afiliado/brand:** livros de engenharia de software e segurança, cursos de SRE/observabilidade, ferramentas de dev (quando houver fit editorial).
- **Rota no funil (`21`):** short-teaser → inscrito → long → post-mortem pack → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 12–18 h de pesquisa + roteiro e 4–8 h de montagem (nicho intensivo em documento, não em filmagem). **Assets:** screen recordings e terminais recriados por arte procedural, diagramas de arquitetura, papers públicos, documentos de reguladores, imagens de imprensa licenciadas; UI de produtos: recriar quando possível, evitar captura de tela protegida.
- **Voz:** TTS (edge-tts no protótipo, ElevenLabs na publicação), ritmo pausado (~140–150 palavras/min). Divulgação de conteúdo sintético no pacote quando voz/visual forem gerados.
- **GATE 100%:** sem todas as imagens aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** falhas com morte (Therac-25, MCAS, autônomos) exigem modo técnico: sem gore, sem imagem de vítima, sem áudio de pânico; autoclassificação honesta; revisão humana quando cair limited ads.
- **Inautenticidade:** risco duplo — (a) o próprio subnicho atrai AI slop (a busca 1 ficou dominada por canais de "AI short films" e o autocomplete pede "generator/background music"); (b) a política de monetização mira conteúdo genérico, repetitivo ou de template, e a fiscalização de janeiro/2026 removeu 16 canais com 4,7B views [REPORTADO — fontes em `evidencia.md`]. Mitigação: 1 peça primária por episódio, estrutura variável, roteiro/voz próprios, disclosure, cadência sem flood.
- **Desinformação/hype:** clipes virais ("robô ataca engenheiro") e previsões catastróficas circulam sem verificação; o canal nunca usa um clipe sem fonte primária e sempre separa [FATO]/[REPORTADO]/[ESPECULAÇÃO]. Não afirmar intenção de um sistema ("the AI wanted").
- **Pessoas e empresas vivas:** "according to the report/company statement"; nunca afirmar culpa não julgada; empresas ativas = linguagem do documento.

## 12. 10 ideias-semente (títulos)

1. Therac-25: The Machine That Gave 100 Times the Dose
2. Knight Capital: $440 Million in 45 Minutes
3. The Flash Crash: One Trillion Dollars, Gone in Minutes
4. Zillow Offers: The Algorithm That Bought Houses Nobody Could Price
5. Tay: The Chatbot That Learned Hate in a Day
6. Amazon's Hiring Algorithm and the Résumés It Threw Out
7. Watson for Oncology: The Internal Documents Said "Unsafe and Incorrect"
8. COMPAS: The Score That Followed People Into Court
9. The AI Agent That Deleted a Company's Database in Nine Seconds
10. Computex 2026: The Humanoid That Fell Onstage

> Todo número, data e afirmação desses títulos precisa de fonte primária na pesquisa do episódio (relatório, paper, documentos, imprensa séria). Os casos de 2026 (9–10) entram como [REPORTADO] até segunda fonte.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; CTR lido contra a mediana da própria conta (o YouTube não publica meta de CTR [OFICIAL]); comentário técnico qualificado nas primeiras 24h.
- **D+7:** episódio novo acumulando ≥1.000 views/dia; inscritos crescendo acima de 1% dos views do episódio.
- **Meta de validação (30 dias):** 3 longs publicados com peça primária, ≥8.000 views cada; se 2+ episódios derem outlier ≥5× contra a mediana do canal, o formato se confirma e o modelo pode ser reavaliado com novo `--brief`/`--cluster` — hoje ele está REPROVA e não deve ser escalado.
