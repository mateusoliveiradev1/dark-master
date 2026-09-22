# Modelo — Mistérios médicos

> Categoria: Forense/médico · Subnicho: casos médicos inexplicados e diagnósticos impossíveis · Slug: `forensic-medical-mysteries`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md` — 0/14 canais passam os 3 gates; termo de busca com intenção mista; autocomplete profundo)
> **Não lançar sem revalidação.** O modelo é um blueprint de partida; a evidência de canal ainda não existe neste cruzamento.

## 1. Posicionamento (1 frase)

Documentário de arquivo sobre casos médicos inexplicados e diagnósticos impossíveis para espectadores de 25–55 anos que querem a ciência por trás do mistério — sintomas, exames que erraram e o diagnóstico que ninguém viu — sem gore, sem conselho médico e sem sensacionalismo.

## 2. Público e promessa

- **Público:** EN (EUA/UK/Canadá/Austrália), 25–55, adulto e curioso; consome Mystery Diagnosis, Chubbyemu, Real Responders (compilações de casos médicos), podcasts de mistério médico (MrBallen `Medical Mysteries`, Sawbones) e o documentário `Diagnosis` da Netflix; assiste 15–40 min por caso e volta ao catálogo. No Reddit, a demanda é explícita: threads pedindo "YouTube channels about medical mysteries" e recomendações recorrentes de Chubbyemu, Sawbones e Dark History (Bailey Sarian) — ver `evidencia.md` §Fontes web.
- **Promessa do canal:** todo episódio reconstrói um caso clínico documentado do primeiro sintoma ao diagnóstico com fontes públicas — o que a medicina testou, o que descartou e o que o caso ensinou.
- **Inimigo da promessa:** conselho médico e autodiagnóstico, desinformação (antivacina, "cura milagrosa"), gore e close de procedimento, sensacionalismo "os médicos escondem isso", exposição de paciente vivo sem registro público.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Casos clássicos inexplicados (auto-brewery, trimetilaminúria, porfiria) | alta (`medical mysteries`, `medical mysteries solved`) | média no cruzamento — nenhum canal dedicado pequeno comprovado na coleta | O caso completo: sintoma → hipótese → mecanismo; base do acervo evergreen |
| Diagnósticos impossíveis (anos até nomear a doença) | alta (`medical mystery documentary full episodes`, `real stories`, `series`) | média — formato canônico é de TV (Mystery Diagnosis, 2005–2011) | "A odisseia": a peregrinação médica e o exame que virou o jogo |
| Toxicologia e exposições ocupacionais como mistério clínico | média | baixa | O detalhe físico (duas gotas, uma luva) + a ciência da absorção |
| História médica sombria (experimentos, surtos iatrogênicos) | média | média-baixa — Instant Medical (51,7k subs, 322d, 26k views/dia) mostra tração | Ética + caso: o que foi feito em nome da ciência, com fontes históricas |

## 4. Lane e formato

- **Lane:** long-first — decisão do modelo. **A evidência NÃO confirmou o cruzamento**: 0/14 canais pequenos passaram os 3 gates em dois scans (`evidencia.md`). Sinais adjacentes, não aprovação: o formato canônico é long (Mystery Diagnosis, 43 min por episódio; Chubbyemu, ~1,5M views/vídeo em média com upload de baixa frequência [PRATICANTE — OutlierKit 08/2026]); tópicos de mistério médico em Shorts performam dentro de canal generalista (NOFiCTiON: 41.186 e 20.385 views nos dois Shorts de auto-brewery e trimetilaminúria, jul/2026).
- **Duração alvo:** long 15–25 min · short 20–28s · **Cadência:** 2 longs/semana + 1 short (≤20% do volume).
- **Mix:** ~85% long / ~15% short; o Short é teaser de um caso com Related Video apontando para o long da semana (sem CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

15–25 min, 16:9, 2 longs/semana; título de caso ou pergunta (nunca "documentary" como muleta); cold open com o detalhe clínico mais estranho e verificado; voz única contida (voice-only brand); visual de arquivo público (Wellcome Collection, NIH/CDC, Wikimedia), diagramas de anatomia, laudos e timelines; card de disclaimer nos primeiros 15s e fontes na descrição; sem reenactment gráfico.

**Ressalva honesta:** este fingerprint é **design-alvo**, não convergência observada — nenhum canal-evidência do cruzamento foi encontrado convergindo nele (o termo de busca retorna ficção, filmes e canais generalistas; ver `evidencia.md` §Verificação de canais).

## 6. Estrutura de roteiro

- **Beats:** `models/forensic-medical-mysteries/beats.json` (gênero `forensic-medical-mysteries`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); FINO (12–15 min, ~1.900–2.400) para casos com pouca fonte.
- **Dispositivos:** pergunta central ("what did the tests miss?") que só fecha no fim; rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — case report (BMJ, NEJM, BMJ Case Reports), relatório do CDC/WHO ou estudo peer-reviewed; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[LENDA]. Nunca diagnosticar nem prescrever; o vídeo conta o que a fonte documentou.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada (o laudo diz X, o corpo diz Y) + detalhe concreto do caso.
- **Exemplos:**
  1. "The breathalyzer said she was drunk. She hadn't had a drink in years."
  2. "The gloves were the best money could buy. Two drops went through them anyway."
  3. "Insomnia runs in this family. So does dying before fifty."
- **Proibido:** conselho médico ou "ask your doctor" no gancho; prometer diagnóstico que o episódio não mostra; data/local antes do gancho; gore; afirmação sobre médico ou hospital vivo sem atribuição ("according to the case report").

## 8. Thumbnail

- **Composição:** 1 sujeito (laudo, exame, objeto clínico ou silhueta de paciente) + 1 elemento de mistério (traçado de ECG, interrogação sobre o exame, ano) + 3–5 palavras que não repetem o título.
- **Paleta:** clínica dessaturada (branco, azul-petróleo, cinza) com 1 acento vermelho de alerta · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** agulha, ferimento, corpo, sangue, rosto de paciente real identificável, "cara de choque" sensacionalista, promessa de cura ou de diagnóstico.

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — classe health/documentary; guia de nicho faceless de saúde (2026) reporta $8–15 para saúde/wellness [ALEGADO]; tabelas de CPM de faceless colocam History/True Crime em $5–12 e documentário em faixa média [ALEGADO]. A classe só se confirma na Analytics do canal.
- **Produto digital:** "case file" pack ($7–27) com timeline, glossário clínico e lista de fontes; guia "how impossible diagnoses get solved" (viés diagnóstico, doenças raras, o papel do exame certo).
- **Patreon/membros:** early access, Q&A de casos e versão comentada do arquivo de fontes.
- **Afiliado/brand:** evitar suplemento, app de saúde e qualquer claim terapêutico (risco YMYL/medical policy); buscar editores, cursos de ciência, streaming e marcas de pesquisa; disclose sempre.
- **Rota no funil (`21`):** short (teaser do caso) → inscrito → long (documentário completo) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 10–14h (pesquisa clínica 5–7h; roteiro 2–3h; montagem 2–3h; checagem de fontes 1h) + TTS; sem locação, sem equipe.
- **Assets:** domínio público (Wellcome Collection, NIH, CDC, Wikimedia Commons, Internet Archive), case reports com citação, diagramas de anatomia e timelines próprios; nunca footage hospitalar de terceiros sem licença.
- **Voz:** edge-tts (en-US, voz contida) ou ElevenLabs; ritmo 150–160 palavras/min; voz única e consistente = marca.
- **Disclaimer médico obrigatório (pacote):** card nos primeiros 15s + texto fixo na descrição: *"This content is for educational and documentary purposes only. It is not medical advice, diagnosis, or treatment. If you have a health concern, consult a qualified healthcare professional."* — fontes listadas na descrição. **Nunca** criar persona de médico (humana ou IA) dando diagnóstico ou conselho (ver §11).

## 11. Riscos

- **Compliance/advertiser:** a política de desinformação médica do YouTube abre exceção para contexto **educacional/documentário/científico** — por isso contexto e fontes são obrigatórios em todo episódio. A política de monetização é explícita: **"AI personas related to sensitive topics"** não podem monetizar — um "médico de IA" dando diagnóstico/conselho derruba o canal. O narrador é um contador de histórias com fontes, nunca um especialista. Sem gore (yellow icon) e sem conteúdo que contrarie o consenso médico (ex.: vacinas, tratamentos).
- **Inautenticidade:** variar a estrutura entre episódios e manter 1 peça de pesquisa primária por vídeo; "stock + voz robótica" em massa é o padrão que a política de conteúdo inautêntico penaliza.
- **Outros:** privacidade de pacientes vivos (usar casos públicos/documentados; preservar anonimato quando a fonte preserva); alegações sobre médicos/hospitais → atribuir à fonte ("according to the case report"); direitos de imagens de arquivo; sensibilidade de familiares em casos recentes.

## 12. 10 ideias-semente (títulos)

1. The Woman Whose Body Brewed Alcohol
2. Two Drops on a Glove Killed a Chemist
3. The Family That Couldn't Sleep
4. They Called It Psychosis. It Was an Antibody.
5. The Blue People of Troublesome Creek
6. The Toxic Lady of Riverside
7. The Boy Whose Muscles Turned to Bone
8. The First Person to Survive Rabies
9. The Disease That Made Everything Smell Like Rot
10. Born Without the Ability to Feel Pain

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 30–100 inscritos; nenhum vídeo em limited ads por conteúdo médico.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; nenhum strike/limitação por medical policy; **revalidar a evidência do nicho** com query mais estreita (ver `evidencia.md` §Revalidação) antes de escalar cadência.
