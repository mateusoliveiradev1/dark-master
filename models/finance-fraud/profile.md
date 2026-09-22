# Modelo — Fraudes e golpes

> Categoria: Finanças · Subnicho: fraudes, golpes e esquemas financeiros · Slug: `finance-fraud`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $21–23 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`) — 0/9 linhas de canal passam os 3 gates (todas falham a idade); fome do algoritmo em 5 canais (2 flares); 1 emergente; Trends ALTA

## 1. Posicionamento (1 frase)

Documentário investigativo sobre fraudes e golpes financeiros para espectadores 25–54 que querem o mecanismo completo do esquema: como o pitch funcionava, quem assinou o quê, para onde o dinheiro foi e em que pé ficou a justiça.

## 2. Público e promessa

- **Público:** EUA/UK/CA/AU (EN), 25–54, assiste Coffeezilla e Fern, além de documentários de fraude (Fyre, Madoff, FTX). Parte da audiência assiste antes de decidir sobre dinheiro, o que dá ao nicho "atenção com intenção comercial" [overseeros, 2026]. Sessão típica de 15–40 min por caso.
- **Promessa do canal:** todo episódio reconstrói um esquema do pitch à queda, com documentos primários e o número que fecha a conta, e termina com o status real: o que foi provado em juízo, o que segue alegado e o que nunca apareceu.
- **Inimigo da promessa:** acusação apresentada como veredito, assédio a pessoas vivas, cifra sem fonte, exploração de vítimas, conselho de investimento.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Ponzi e pirâmides (Madoff, Stanford, OneCoin) | alta (`fraud documentary`, `major fraud documentary`, `money fraud documentary`) | média: catálogo amplo, poucos canais novos com documentos primários | O fluxo do dinheiro: o que entrou, o que saiu, o que foi recuperado; série "Ponzi, by the Numbers" |
| Fraude corporativa e contábil (Enron, Wirecard, Theranos) | média-alta (`corporate fraud documentary`, `accounting fraud documentary`, `business fraud documentary`) | média-baixa | Auditoria forense na tela: o balanço, a assinatura, o relatório que ninguém leu |
| Cripto e fintech (FTX, rug pulls, memecoins) | alta (`crypto fraud documentary`) | alta: tema mais coberto (Coffeezilla domina em EN) | Só entrar com ângulo próprio (forense de blockchain, vítimas, docket); risco de envelhecer rápido |
| Golpes do consumidor (check fraud, romance/pig butchering, deepfakes) | alta (`online fraud documentary`, `check fraud documentary`, `insurance fraud documentary`) | média: o outlier de 86× veio desse recorte em formato bodycam/legal analysis | O golpe do dia a dia explicado passo a passo, com defesa prática; alto potencial de compartilhamento |
| Queda de tycoons e fugitivos (ex.: Vijay Mallya) | sem termo EN dedicado no autocomplete (lacuna) | baixa em EN: o outlier de 1.104,5× veio de canal de língua hindi | A ascensão, a dívida e os bancos que ficaram no prejuízo, com corte EN e fontes primárias |
| Fraude de arte, vinho e luxo | média (`art fraud documentary`, `wine fraud documentary`, `food fraud documentary`) | baixa | Colarinho branco em nicho de luxo: menos risco de difamação, mesmo mecanismo de confiança |

## 4. Lane e formato

- **Lane:** long-first. Os outliers da coleta são documentário long (2.233.271 views no doc de tycoon; 4.201.123 views no exposé), Coffeezilla sustenta 16–55 min com 2,4–8,3M views por upload recente e Fern roda ~18M views/mês, e é no long que a classe de RPM de finanças se realiza [ALEGADO]. Short fica como aquisição: $0.03–0.10 por view contra o RPM de long (`10`).
- **Duração alvo:** long 15–25 min · short 20–28s · **Cadência:** 2 long/semana + 1 short (ratio ~0,33, dentro da faixa 0,28–0,40 do `10`).
- **Mix:** ~75–80% long / 20–25% short; cada Short mostra 1 documento do episódio e aponta no Related Video para o long do dia.

## 5. Fingerprint de formato (o que o recomendador lê)

15–25 min, 16:9, 2 longs/semana; título com a cifra e/ou o mecanismo ("$400K", "215 Crore", "Vijay Mallya Story"); cold open com o detalhe verificável (extrato, sede vazia, frase do pitch); thumbnail com número grande + retrato de arquivo ou objeto-símbolo; voz única contida (voice-only brand); documentos na tela (autos judiciais, releases de SEC/DOJ, relatórios) + fluxograma do dinheiro + footage de arquivo licenciado; encerramento com status judicial real. Convergência observada nos canais-evidência: história financeira identificada pela cifra no título em formatos doc, 2D animado e bodycam/legal analysis. Referências de estilo sênior: Coffeezilla (investigação com documentos + disclaimers legais) e Fern (doc faceless de alta produção) [PRATICANTE].

## 6. Estrutura de roteiro

- **Beats:** `models/finance-fraud/beats.json` (gênero `finance-fraud`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras). RICO (24–27 min) para casos densos (Madoff, FTX); FINO (12–15 min) para golpes com pouca fonte.
- **Dispositivos:** rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central (onde foi o dinheiro?) fechada no bloco O DINHEIRO.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — autos judiciais (PACER/CourtListener), complaints e releases de SEC/DOJ/CFTC/FTC, relatório de auditor ou administrador judicial, ou reportagem investigativa com linha do tempo; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[ALLEGED] no roteiro; direito de resposta documentado quando houver pessoa viva.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** número + stake (a cifra) combinado com contradição verificada (a promessa contra o mecanismo).
- **Exemplos:**
  1. "Sixty-five billion dollars, one spreadsheet. The statements showed trades that never happened."
  2. "The customers sent money to buy crypto. It went to a firm next door."
  3. "€1.9 billion sat in an escrow account in Asia. Auditors flew out to check. The account was never there."
- **Proibido:** abstração; data ou local antes do gancho; meta-linguagem ("in this video"); acusação sem "alleged/charged"; cifra sem fonte; prometer recuperação do dinheiro.

## 8. Thumbnail

- **Composição:** 1 sujeito (retrato de arquivo/ilustração do investigado ou objeto-símbolo: extrato, cifra, cofre) + 1 número grande + 3–5 palavras que não repetem o título.
- **Paleta:** preto/cinza-escuro + verde-dinheiro e 1 vermelho de alerta · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** rosto de vítima, "cara de choque", cifra sem fonte, dinheiro empilhado falso, palavra acusatória sobre pessoa viva ("FRAUDSTER") sem base judicial.

## 9. Monetização

- **AdSense (classe):** $21–23 [ALEGADO] — classe alta de finanças (tabela do `10`: Finance/Investing $12–23; documentary $12,6) somada ao CPM de documentário/educação $10–25 [ALEGADO — longformstudio, 2026]. A classe só se confirma na Analytics do canal; tema controverso pode cair para limited ads.
- **Produto digital:** pack "The Fraud File" ($7–27): linha do tempo + fluxograma do dinheiro + glossário jurídico (SEC/DOJ) + checklist anti-golpe; guia "How to check before you invest".
- **Patreon/membros:** sim — early access, notas do caso e Q&A; o modelo existe em escala no nicho (Coffeezilla mantém Patreon público) [PRATICANTE].
- **Afiliado/brand:** identity protection, VPN, password manager, livros de negócios [ALEGADO — overseeros, 2026]. Nunca aceitar sponsor de produto financeiro que prometa retorno; disclosure FTC visível.
- **Rota no funil (`21`):** short (1 documento teaser) → inscrito → long (doc completo) → pack anti-golpe.

## 10. Produção

- **Custo/tempo por vídeo:** 10–16h (pesquisa 5–8h; roteiro 2–3h; montagem 3–4h) + TTS; sem locação nem equipe.
- **Assets:** registros oficiais (PACER/CourtListener, SEC/DOJ/CFTC/FTC, governos), domínio público, reportagens licenciadas, screen recording de documentos públicos, fluxogramas e mapas próprios, ilustração/2D ou 3D simples para reconstrução. Nunca footage de terceiros sem licença.
- **Voz:** edge-tts (en-US, voz contida) ou ElevenLabs; ritmo 150–160 palavras/min; voz única e consistente = marca; divulgar uso de IA no pacote quando aplicável.

## 11. Riscos

- **Difamação/legal:** o risco central do nicho. Pessoa viva só como "alleged/charged/suspect", com documento judicial, direito de resposta e disclaimers (o próprio Coffeezilla mantém aviso de hipérbole retórica e já respondeu a processo real). Não afirmar crime antes do processo; não usar "scam" como veredito fora do contexto jornalístico.
- **Compliance/advertiser:** finanças + controvérsia podem gerar limited ads; sem aconselhamento de investimento, sem cifra inventada, sem "get rich"; disclosure de afiliado (FTC) quando houver.
- **Inautenticidade:** o formato pode repetir, a substância não — 1 pesquisa primária por vídeo e estrutura variando entre episódios; template genérico + IA em massa é o alvo da política (`09`).
- **Outros:** direitos de footage jornalístico e de retratos; assédio e doxxing contra o criador (campanhas reais no nicho); tratamento de vítimas sem exploração.

## 12. 10 ideias-semente (títulos)

1. The $65 Billion Man: Inside the Madoff Statements
2. FTX: Where Customer Money Actually Went
3. OneCoin: The Coin That Was Never a Coin
4. Theranos: One Drop, Zero Proof
5. Wirecard: The €1.9 Billion That Wasn't There
6. Vijay Mallya: The Tycoon, the Banks, and the Bill
7. The Romance Scam Compounds: Where the Money Goes
8. The $400,000 Check That Should Never Have Cleared
9. Fake Gurus: The Business Model Behind "Get Rich" Courses
10. Ponzi, by the Numbers: How New Money Paid Old Investors

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% (docs de 15–30 min saudáveis rodam 30–45% [ALEGADO — longformstudio, 2026]).
- **D+7:** 1–5k views por long no início; 30–100 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; ≥500 inscritos; zero strike ou notificação legal; nenhum vídeo limitado por advertiser.
