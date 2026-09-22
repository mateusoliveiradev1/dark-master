# Modelo — Toxicologia forense

> Categoria: Forense/médico · Subnicho: venenos, envenenamentos e exames toxicológicos · Slug: `forensic-toxicology`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 — 0 canais passam os 3 gates nas duas coletas; fome 1 canal por busca (abaixo do critério ≥2) e 0 emergentes. Não lançar como canal dedicado sem revalidar/estreitar (`evidencia.md`).

## 1. Posicionamento (1 frase)

Documentário de perícia sobre envenenamentos em que o **laboratório é o detetive** — para espectadores de true crime e medicina forense que querem o que as amostras, os laudos e os autos provaram, não o método e não o espetáculo.

## 2. Público e promessa

- **Público:** hipótese (a API não expõe idade/gênero) — adultos 25–54 nos mercados EN (EUA, Reino Unido, Canadá, Austrália), os mesmos que consomem Casefile, Dr. Insanity, 48 Hours, Forensic Files e That Chapter; consumo noturno/em segundo plano (funciona como áudio + visual). Público secundário de ciência/perícia (ouvintes de podcast como The Toxpod). Confirmar no Analytics do canal.
- **Promessa do canal:** todo episódio reconstrói um envenenamento a partir de registros públicos — cronologia, cadeia de custódia, laudo toxicológico, tribunais — mostrando como a ciência chegou ao resultado, o que ela não conseguia provar e o que o caso mudou depois.
- **Inimigo da promessa:** instrução de método (dose, síntese, aquisição — proibido pela política de conteúdo perigoso); gore/autópsia gráfica; ângulo suicídio; teoria vendida como fato; sensacionalismo; "veneno perfeito" como entretenimento.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Casos criminais de envenenamento (doméstico, herança, relação) | **alta** — `poison murder case`, `murder by poison cases`, `poison crime documentary`; ciclo 2026 (Kouri Richins, Kenneth Law) | alta no formato notícia/compilação/TV; **baixa no formato perícia-foco** | "o que o laudo provou": cronologia + exame + o que o júri leu |
| Contaminação em massa (água, alimento, PFAS) | média-alta — `poisoned water documentary`, `poison food documentary`, `poison squad documentary` | média (gigantes de science-doc, ex. Veritasium/PFAS 34M) | instituições e documentos: o laudo coletivo, a regulação, o encobrimento |
| Envenenamentos históricos (arsênico vitoriano, casos reais do século XIX, radiológico) | média — `sweet poison documentary`, `salisbury poisoning documentary bbc` | baixa–média em EN | arquivo + ciência da época: o que os químicos podiam e não podiam detectar |
| O laboratório por dentro (técnicas, limites, erros) | média — `forensic toxicology lab`, `cases`, `poisons` (intenção de estudo: `lecture`, `mcqs`) | baixa (só oferta minúscula de educação; ex. The Toxicology Corner, 108 subs) | "como se pega um veneno" **sem método**: história das técnicas e limites do teste |
| Venenos naturais (plantas, animais, toxinas) | média — `poisonous animals documentary`, `poison arrow documentary`, `toxic beauty documentary` | média | ecologia + caso: a toxina na cultura, na medicina e no tribunal |

> Classificação de demanda vem dos 4 pools de autocomplete (514 termos) e do cluster; nenhuma linha usa volume estimado externo. Estreitar por subtema antes de produzir (`evidencia.md`).

## 4. Lane e formato

- **Lane:** long-first — justificativa: no cluster `poisoning documentary`, 5 de 8 canais pequenos passam 2/3 gates com tração de documentário longo (Red File mediana ~1,2M views; AccordHistoryVoice 350.937 views/dia; Hidden Genius 22.782/dia); o formato que domina o tema é o doc longo (48 Hours 40–90 min, A&E, BBC 47 min) e guias de operador 2026 apontam 18–25 min como faixa ótima de true crime [ALEGADO — YouDark]. Shorts pagam $0,03–0,10 e não sustentam a matemática [ALEGADO — `10`].
- **Duração alvo:** long 16–22 min (PADRÃO ~18–20) · short 20–28s · **Cadência:** 2 long/semana + ≤1 Short a cada 2 semanas.
- **Mix:** ~90% long / ≤10% short; o Short é teaser do caso da semana com Related Video para o long. **Condição:** o lane é recomendação para **depois da revalidação** — hoje os gates não aprovam lançamento.

## 5. Fingerprint de formato (o que o recomendador lê)

- Documentário narrado 16–22 min, 16:9, um narrador (voice-only brand), sem talking head e sem intro de canal; cold open no objeto do arquivo (o frasco, o certificado, a etiqueta da amostra).
- Reconstrução com documentos (laudos, certificados de óbito, transcrições), vidraria/cromatograma estilizados, mapas e linhas do tempo próprias; cortes a cada 4–8s; trilha contida.
- Capítulos nomeados por linha do tempo; fontes nomeadas em tela e na descrição.
- Títulos de contradição documental ("The Death Certificate Said X. The Lab Said Y.") ou pergunta; thumb dessaturada com 1 objeto (frasco, copo, envelope de exame) + 1 elemento documental (selo LAB REPORT, data) + 2–4 palavras que não repetem o título.
- Fingerprint é hipótese de partida — a API externa não expõe estilo nem watch time; validar nos 5 primeiros uploads por convergência.

## 6. Estrutura de roteiro

- **Beats:** `models/forensic-toxicology/beats.json` (gênero `forensic-toxicology`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO (18–21 min; ~2.900–3.300 palavras; 150–160 palavras/min). FINO (12–15 min) quando a fonte pública é escassa; RICO (24–27 min) para caso com autos densos.
- **Dispositivos:** 3–5 open loops nos primeiros 20s; rehooks a cada 2–4 min; re-engage ~3 e ~6 min; pergunta central ("o que a amostra podia provar?") que só fecha no fim; pattern interrupt a cada 30–90s; fim abrupto sem "obrigado por assistir".
- **Pesquisa obrigatória:** 1 peça primária por vídeo — laudo/relatório de medical examiner público, autos de julgamento, reportagem de referência cruzada com 2+ fontes; camadas [FATO]/[REPORTADO]; **nunca** dose, método ou aquisição. Sem peça primária, o vídeo cai no balde "genérico/repetitivo" da política de conteúdo inautêntico (`09`).

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada entre documento oficial e amostra (certificado × laudo, laudo × cronologia) — nunca o método nem o sofrimento.
- **Exemplos (banco completo em `hooks.md`):**
  1. "The death certificate said heart failure. Eleven years later, the same tissue sample said arsenic."
  2. "'It wasn't poison,' the doctor wrote. The lab report, filed a month later, says otherwise."
  3. "All that survived was one blood draw, a coffee cup, and a label with the wrong date."
- **Proibido:** dose/método/aquisição no gancho; gore; data/local antes do gancho; abstração; meta-linguagem; prometer o que o episódio não mostra.

## 8. Thumbnail

- **Composição:** 1 objeto (frasco de amostra, copo, envelope de exame, gráfico de cromatograma) + 1 elemento documental (selo "LAB REPORT", data, carimbo) + 3–5 palavras que **não repetem** o título.
- **Paleta:** dessaturada (cinza/petróleo) com 1 cor de destaque laboratorial (âmbar ou verde); fonte sans condensada, alto contraste, testada a 120 px.
- **Nunca:** corpo, sangue, ferimento, autópsia; comprimido/pó/substância em uso ou com dose legível; agulha/seringa; foto real de vítima; rosto de pessoa viva sem contexto/alleged; cena de crime.

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — classe crime/true crime não-gráfico do índice (`10`), com documentary a $12,6 [ALEGADO]. **Ressalva honesta:** fontes de mercado 2026 dão faixas menores para true crime faceless ($3–12; $6–9 educacional não-gráfico), e o risco de limited ads é estrutural neste subnicho; confirmar só no Analytics. Nunca tratar como fato.
- **Produto digital:** dossiês "case file" (PDF com linha do tempo, glossário de perícia e fontes, $9–19) e pack "como se lê um laudo" (educacional, sem método); tripwire na descrição.
- **Patreon/membros:** sim — early access, fontes comentadas e versão áudio (cross-over podcast, modelo Dr. Insanity); audiência de perícia é nichada e paga por profundidade.
- **Afiliado/brand:** livros de true crime/ciência forense, audiolivros e streaming; **nunca** fornecedores de químicos/equipamento de laboratório (conflita com a política de bens regulados). Brand deals são difíceis com advertiser limits; priorizar receita direta.
- **Rota no funil (`21`):** long explora e retém → Short do caso da semana → inscrito → membro/produto. Medir a conversão antes de manter Shorts.

## 10. Produção

- **Custo/tempo por vídeo:** ~8–14 h (pesquisa 4–6 h; roteiro/revisão 2–4 h; voz/imagem/edição 2–4 h), free tier — validar no piloto.
- **Assets:** domínio público e acervos abertos (Wellcome Collection para história da toxicologia, Internet Archive, Wikimedia, Europeana, relatórios oficiais de medical examiner/coroner), documentos e timeline próprios; cromatogramas/ilustrações procedurais. Nada de footage de TV/agência sem licença.
- **Voz:** TTS consistente (edge-tts/ElevenLabs) — voz única = marca; ~150–160 palavras/min; disclosure de IA quando voz/visual sintético (`09`).

## 11. Riscos

- **Método/dano — risco nº 1.** [OFICIAL] A política de conteúdo perigoso proíbe "instructions to kill or harm" e conteúdo de ingestão de substâncias que possam causar envenenamento; contexto educacional/documental (EDSA) é avaliado caso a caso, às vezes com age-restriction (support.google.com/youtube/answer/2801964). Mitigação: narrar laudo e investigação, nunca método/dose; zero "como funciona o veneno" em nível operacional.
- **Adjacência de suicídio.** Parte do tema em 2026 vem de casos de auto-envenenamento (Kenneth Law — guilty plea em 29/05/2026) e venda online de substâncias. Esse material é restrito e contamina o canal — **fora do modelo**; nunca tratar suicídio como arco do episódio.
- **Advertiser limit (yellow icon).** [ALEGADO] A categoria true crime coleta limited ads de forma instável; linguagem gráfica e imagem forte na thumb/15s são os gatilhos (Longform Studio 11/08/2026: forensic-focus é o enquadramento de menor risco; YouDark: flags +38% YoY). Mitigação: foco perícia, linguagem factual, self-certification honesta, pedir human review quando o automático errar.
- **Conteúdo inautêntico.** "Caso + arquivo" vira template com facilidade — exatamente o alvo da política de 2026 (`09`). Antídotos: 1 peça primária por vídeo, tomar posição, variar hook/estrutura, nunca reutilizar metadados.
- **Pessoas vivas, vítimas e famílias.** Suspeito vivo = "suspect/alleged"; condenado com recurso pendente = "convicted, appeal pending" (ex. Richins); nunca foto real de vítima como centro; risco de reclamação de família.
- **Direitos autorais.** Footage de tribunal/TV e fotos de agência têm dono; usar acervo aberto e produção própria.
- **Divulgação de IA.** Conteúdo sintético/altered deve ser divulgado; marcar não penaliza por si só (`09`).
- **Timing YPP.** Requisitos dobram em 01/02/2027 (8.000h ou 20M views de Shorts) — o long-first é o caminho de watch hours; validar antes da data.
- **Gate.** O cruzamento **reprovou os gates** nas duas coletas (0/16) e a fome é fraca (1 outlier por busca) — não escalar produção sem revalidação.

## 12. 10 ideias-semente (títulos)

1. The Death Certificate Said Heart Failure — the Lab Said Arsenic
2. Five Times the Lethal Dose, and One Question the Trial Never Answered
3. The Exhumation That Reopened a Case After Eleven Years
4. She Wrote About Grief — Her Search History Became Evidence
5. Thallium, 1994: The Poisoning Nobody Was Charged For
6. The Polonium Trail Through London
7. Arsenic and the Victorian Insurance Boom
8. What a Tox Screen Can't Detect
9. The Water Was Legal — the Blood Wasn't
10. One Vial, Two Verdicts

> Fatos, nomes e números de cada ideia só entram no roteiro depois de checados em 2+ fontes (camadas [FATO]/[REPORTADO]); casos com pessoa viva usam "alleged"/status atual do processo.

## 13. Métricas de sucesso

- **D+2 (metas do modelo — benchmarks de praticante, não oficiais):** CTR ≥4% na thumb; retenção 30s ≥70% [PRATICANTE]; sem queda abrupta no minuto 1; zero aviso de política de conteúdo perigoso.
- **D+7:** ≥3–5k views por long (piso de sanidade para canal novo); inscritos por 1.000 views ≥2; 1 Short puxando o long da semana (quando houver Short).
- **Meta de validação:** **primeiro, revalidar o nicho** em 2–4 semanas exigindo ≥3 canais pequenos passando os 3 gates (ou critério PARCIAL: ≥2 canais com fome, ou emergentes). No piloto de 30 dias: 4–6 longs publicados, mediana ≥5k views/vídeo, ≥1 outlier ≥3× da mediana do canal, <3 limited ads em 10, retenção média ≥40%. Se os gates não virarem: pivotar para `forensic-medical-mysteries` (modelo 18) antes de trocar de categoria.
