# Modelo — Escândalos farmacêuticos

> Categoria: Forense/médico · Subnicho: escândalos da indústria farmacêutica e ensaios escondidos · Slug: `forensic-pharma`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $18–25 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md`) — 0/16 canais pequenos passam os 3 gates; "fome" só em micro-canais (maior outlier: 683 views); demanda sênior real (fern 2,93 M; Into the Shadows 206,8 mil). Blueprint pronto para revalidar com recorte estreito; não escalar como entrada EN direta.

## 1. Posicionamento (1 frase)

Reconstituição documental do escândalo farmacêutico, do papel timbrado à conta final, para espectadores 25–54 que já ouviram falar dos opioides e agora querem o rastro: o ensaio, o memo, a bula, o processo — e o que a empresa respondeu.

## 2. Público e promessa

- **Público:** EN (US/UK/CA/AU), 25–54, audiência já montada de documentário dark/true crime (Into the Shadows, Coffeehouse Crime, fern, DW Documentary) somada a pacientes e famílias tocadas por medicamentos (opioides, fen-phen, talco, fator VIII) e à comunidade on-line de crítica farmacêutica. Sessão típica de 20–45 min por caso; o tema tem camada pessoal (quem assiste pode estar tomando o remédio da vez).
- **Promessa do canal:** todo episódio termina com a mesma prova de trabalho: documento primário na tela, o que está provado em juízo, o que segue alegado e o status real hoje.
- **Inimigo da promessa:** "big pharma" como xingamento ou veredito, gore, conselho médico, culpado sem processo, cifra sem fonte, paciente como espetáculo, catastrofismo sobre remédio em uso.

## 3. Subnichos cobertos

| Subnicho | Demanda | Saturação | Ângulo do modelo |
|---|---|---|---|
| Opioides e a era Purdue/OxyContin | alta (cultural: Painkiller/Dopesick na Netflix/Hulu; fern 2,93 M em 2026) | alta em EN (sêniores dominam) | Só com recorte não coberto: a fileira internacional (Grünenthal/tramadol/tapentadol) e o rastro do dinheiro pós-bankruptcy |
| Ensaios escondidos e dados suprimidos (Study 329/Paxil, Vioxx, Tamiflu) | média (sem termo forte no autocomplete — lacuna) | baixa-média | "O dado que sumiu": report do ensaio vs. paper publicado, endpoint trocado; literacia de ensaio clínico na tela |
| Segurança pós-mercado e recalls (fen-phen, Depakine, ranitidina/NDMA, implantes) | média | média-baixa | "Aprovado — e depois": cronologia do sinal, do boletim ao recall; fecho com o que a regra mudou |
| Preços e patentes (Daraprim/Shkreli, insulina, Restasis/soberania tribal) | alta (`pharmaceutical industry documentary`; Shkreli é cultura pop) | média | O mecanismo do preço: quem paga, quem negocia, o que a lei permite — cruza com `finance-fraud` |
| Sangue e contaminação (fator VIII/HIV, plasma) | média (histórico) | baixa | Arquivo + comissões oficiais; caso com conclusão documental, menos volátil que caso vivo |
| Vigilância e fraude de ensaio (dados fabricados, aprovação acelerada) | média | baixa | Perna forense pura: laudo de auditoria, retratação de artigo, investigação de agência |

## 4. Lane e formato

- **Lane:** long-first. Os sinais de demanda são de long: fern fez 2,93 M views com um doc de **44:42** (05/08/2026, ~61 mil views/dia); Into the Shadows, 206,8 mil com **24:55**; DW, 3,2 M com 42:26 evergreen. É no long que a classe de RPM de saúde/documentário se realiza [ALEGADO]. Shorts entram como aquisição (1 documento por Short), sem carregar o canal.
- **Duração alvo:** long 18–30 min · short 20–28s · **Cadência:** 1 long/semana + 1 short a cada 2–3 longs (ratio ~0,3, dentro da faixa 0,28–0,40 do `10`). É o modelo mais pesado de pesquisa da biblioteca — a cadência menor é decisão, não fraqueza.
- **Mix:** ~75–80% long / 20–25% short; cada Short mostra 1 documento (a carta da FDA, o memo) e aponta no Related Video para o long do dia.

## 5. Fingerprint de formato (o que o recomendador lê)

18–30 min, 16:9, 1–2 uploads/semana; título com o nome do medicamento/empresa + o número do caso ("$1.9B", "7 million") ou o documento ("the files", "the audit"); cold open com o documento na tela; thumbnail com frasco/bula genérica + tarja de evidência + 3–5 palavras; narrador único contido (voice-only brand); PDFs e dockets em screen recording + arte procedural/mapas; fecho com status legal e right of reply; fontes listadas na descrição. Convergência observada nos sêniores-evidência: **um caso por vídeo**, 24–45 min, tom contido, document-based; micro-canais do tema apostam em Shorts e não escalam (ver `evidencia.md`).

## 6. Estrutura de roteiro

- **Beats:** `models/forensic-pharma/beats.json` (gênero `forensic-pharma`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras). RICO (24–27 min) para casos densos (Purdue, Vioxx); FINO (12–15 min) para recall/decisão regulatória com pouca fonte.
- **Dispositivos:** rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central fechada no bloco do documento.
- **Pesquisa obrigatória (1 peça primária por vídeo):** docket (CourtListener/PACER), documento de agência (FDA letters, MedWatch, Drugs@FDA, EMA), release DOJ/SEC/AG estadual, memo de litígio, ou investigação colaborativa com método aberto (The Examination/World of Pain, ProPublica). 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[ALLEGED] no roteiro; right of reply registrado quando houver empresa/pessoa viva.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada (o rótulo/o paper diz X; o documento mostra Y) somada a número + stake (dose, preço, população exposta).
- **Exemplos:**
  1. "The label said the painkiller was not addictive. The company's own audit later found the claim wasn't backed by sufficient evidence."
  2. "Seven million prescriptions. One heart valve. The FDA pulled the combination, and the lawsuits kept coming."
  3. "It was banned in Denmark. It stayed on sale in India for a decade — and the editor who wrote that down spent ten years in court."
- **Proibido:** abstração ou filosofia; data/local antes do gancho; meta-linguagem ("in this video"); "big pharma" como veredito; acusação sem "alleged/charged"; cifra sem fonte; conselho ou alarme sobre medicamento em uso.

## 8. Thumbnail

- **Composição:** 1 sujeito (frasco/caixa de remédio sem marca legível, bula ou docket) + 1 elemento de evidência (tarja vermelha de censura sobre o documento, lupa, selo "evidence") + 3–5 palavras que não repetem o título.
- **Paleta:** branco clínico + azul-escuro + 1 vermelho de alerta (nunca textura de sangue) · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** foto de paciente ou de luto, agulha/braço, "cara de choque", nome de empresa com acusação sem base judicial, símbolo que explore origem histórica da empresa, imagem de criança doente.

## 9. Monetização

- **AdSense (classe):** $18–25 [ALEGADO] — classe-alvo de topo. Fontes de mercado 2026 põem saúde em $3–15 (medical explainer $6–15), Health Services em $7–22 RPM e o CPM de anunciantes farmacêuticos em $10–25 [ALEGADO — fluxnote/vidIQ, 2026]. O $18–25 só se confirma na Analytics, e YMYL/limited ads podem derrubar (yellow icon reduz 50–70% [ALEGADO]).
- **Produto digital:** "The Evidence Pack" ($7–27): linha do tempo do caso + guia "how to read a trial result" + checklists de fonte regulatória (FDA/EMA, docket). Produto de literacia, não de saúde.
- **Patreon/membros:** sim — notas do caso com links das fontes primárias, PDFs dos documentos e Q&A; audiência de documentário paga por profundidade (padrão do nicho).
- **Afiliado/brand:** livros (Empire of Pain, Bad Pharma), cursos de literacia de dados; **nunca** produto farmacêutico, suplemento, teste caseiro ou "cura". Disclosure visível.
- **Rota no funil (`21`):** short (1 documento teaser) → inscrito → long (caso completo) → Evidence Pack.

## 10. Produção

- **Custo/tempo por vídeo:** 12–20h (pesquisa documental 6–10h; roteiro 3–4h; montagem 4–6h) + TTS. Sem locação nem equipe; o custo real é a pesquisa.
- **Assets:** CourtListener/PACER (dockets), FDA (letters, MedWatch, Drugs@FDA), EMA, DOJ/SEC/AGs, comissões oficiais (ex.: Krever), domínio público, screen recording de PDFs públicos, mapas e arte procedural próprios. Nunca footage de terceiros sem licença; nunca prontuário ou imagem de paciente.
- **Voz:** edge-tts (en-US, voz contida) ou ElevenLabs; 150–160 palavras/min; voz única e consistente = marca; divulgar uso de IA no pacote quando aplicável.

## 11. Riscos

- **Difamação corporativa (o risco central):** empresas farmacêuticas usam e já usaram litígio para silenciar críticos — editor processado por 10 anos na Índia (Lundbeck), cientistas processados por J&J, ação de difamação contra críticos com efeito inibidor documentado (Cassava), trade libel contra revista científica (Pacira). Regras: "alleged/charged" para pessoa viva, documento judicial na tela, right of reply, nunca afirmar crime antes do processo.
- **Compliance/advertiser:** saúde é YMYL — política de desinformação médica (tratamento/prevenção, com exceção EDSA), risco de limited ads em conteúdo sensível, proibição de conselho/dose/"pare de tomar". Enquadrar como documento e história, não como orientação médica.
- **Inautenticidade:** o espaço já tem oferta de baixa qualidade gerada em massa ("scam/cover-up" com narração sintética e templates). O antídoto é a peça primária por vídeo + estrutura variando entre episódios; o formato pode repetir, a substância não (`09`).
- **Outros:** direitos de retratos e footage jornalístico; privacidade de pacientes; crueldade involuntária com audiência que sofre do tema (escrever com contenção).

## 12. 10 ideias-semente (títulos)

1. The Grünenthal Files: The Opioid Playbook Europe Kept
2. Fen-Phen: 7 Million Prescriptions, One Recalled Combination
3. Study 329: The Paxil Trial Report vs. the Published Paper
4. Daraprim: The $13.50 Pill That Became $750
5. Restasis: The Patent, the Tribe, and the Invalidated Claims
6. Factor VIII: The Warning That Came Years Late
7. Depakine: Europe's Quietest Pregnancy-Drug Scandal
8. Ranitidine: From the Heartburn Aisle to a Recall Case Study
9. Insulin: One Molecule, a Decade of Price Hikes
10. Beyond Purdue: How the Opioid Playbook Crossed Borders

> Título final de caso vivo passa por checagem: verbo de crime só com base judicial; empresa/pessoa sem condenação entra como "alleged". Vários destes títulos usam enquadramento "arquivo/documento" de propósito.

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 30–45% (docs de 15–30 min saudáveis rodam 30–45% [ALEGADO — longformstudio, 2026]).
- **D+7:** 1–5k views por long no início (nicho de pesquisa pesada não estoura no dia 1); 30–100 inscritos; cliques do Short para o long medidos.
- **Meta de validação (30 dias):** 4–5 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 3 de 4; zero strike, zero notificação legal e nenhum vídeo limitado por advertiser (os 3 sinais de sobrevivência deste nicho).
