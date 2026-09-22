# Modelo — Colapsos corporativos

> Categoria: Finanças · Subnicho: colapsos, escândalos contábeis e quedas de empresas · Slug: `finance-corporate-collapse`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $18–25 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — gates rígidos 0/16 na coleta; fome do algoritmo em 9 canais com outlier ≥3×; 2 emergentes ≤90d com 2/3 gates)

## 1. Posicionamento (1 frase)

Documentário de autópsia financeira sobre por que uma empresa grande morreu, para espectadores EN de 25–54 que já conhecem o nome e querem os números — a decisão que condenou a empresa, o que o balanço escondia e onde o dinheiro foi parar — com documento primário e sem sensacionalismo.

## 2. Público e promessa

- **Público:** EUA/UK/CA/AU (EN), 25–54, renda média-alta, acompanha negócios e mercados; consome MagnatesMedia (1,9M subs), ColdFusion (5,2M), Company Man (1,8M), How Money Works (1,7M), Business Casual (1,1M), Logically Answered (912k), Modern MBA (801k), Wall Street Millennial (366k) [snapshot OutlierKit, 27/07/2026]; assiste 10–25 min por caso e volta ao catálogo. É a audiência que atrai anunciante de B2B, corretoras e educação de negócios (CPM Tier-1).
- **Promessa do canal:** todo episódio reconstrói uma queda com fontes verificáveis (filings, relatórios anuais, processos, trade press) e explica em uma frase a decisão que a tornou inevitável.
- **Inimigo da promessa:** "fraude" afirmada como fato sem processo; número sem fonte; culpa pessoal sem sentença; exploração de funcionários/aposentados para reter; "segredo" que o vídeo não entrega.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Rise-and-fall clássico (Enron, Lehman, Sears, Toys "R" Us, Circuit City) | alta (`collapse documentary`, `corporations documentary`) | média–alta (exemplares grandes já estabelecidos no nicho) | Autópsia com documento primário: a decisão única + o número que a resume; nunca o resumo de Wikipedia |
| Escândalo contábil (Wirecard, WorldCom, Toshiba, Luckin) | alta | média | A mecânica contábil explicada: o que o balanço escondia, quem assinou, o que a auditoria viu — e o que ficou em [ALEGADO] |
| Colapso rápido (Credit Suisse, SVB, Signature) | alta (busca por evento) | média | Cronologia hora a hora com números oficiais; história ativa exige atualização e linguagem "alleged" para pessoas vivas |
| Colapsos fora do eixo EUA (Reliance Comm, ABG Shipyard, Greensill, Cipaganti) | média | **baixa em EN** | Caso global com fonte local traduzida; evidência de fome: outliers 4,9× (The Business Obituary, Reliance), 10,4× (True Doc, ABG), 35,4× (NET CREATIVE, Cipaganti — canal em ID) |

## 4. Lane e formato

- **Lane:** long-first — justificativa: **100% dos canais-evidência** das duas varreduras publicam em long-form; o formato convergente do teardown 2026 é narração de 9–12 min sobre filings/B-roll (OutlierKit, 27/07/2026); o RPM long-form (≈metade do CPM $10–25 do formato, [PRATICANTE/OutlierKit]) é 20–200× o do Short (`10`); nenhum outlier de Short apareceu na coleta.
- **Duração alvo:** long **12–18 min** (com 8+ min garantindo mid-roll) · short 20–28s · **Cadência:** 1 long/semana (solo) a 2 longs/semana; 1 short a cada 2–3 longs.
- **Mix:** ~85–90% long / 10–15% short; o Short leva o número do colapso + Related Video para a autópsia (nunca CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

12–18 min, 16:9, 1–2 uploads/semana; cold open **outcome-first** (resultado antes da história, número concreto, sem intro); título outcome-reveal ("How [company] lost [X]", "[N] days that ended [company]", "The [decision] that killed [company]"); thumbnail com logo/ícone + número grande; narração única a 150–160 palavras/min; visual de filings, gráficos, arquivo, tabelas e motion graphics próprios; sem host. Convergência observada nos canais-evidência: outcome-first desde o título — "How America's 7th Largest Company Vanished in 24 Days" (24,3×), "How to Destroy a Billion-Dollar Empire" (16,3×), "Circuit City Cut Its Experts. Then It Collapsed." (3,8×), "Lehman Brothers' Fatal Flaw | The $50 Billion Cover-Up" (19,5×).

## 6. Estrutura de roteiro

- **Beats:** `models/finance-corporate-collapse/beats.json` (gênero `finance-corporate-collapse`) — usar com `--beats-file`.
- **Porte padrão:** FINO — 12–15 min (~1.900–2.400 palavras), alinhado à faixa do formato (9–12 min no teardown); PADRÃO — 18–21 min (~2.900–3.300) só em casos densos com múltiplos documentos (Enron, Wirecard).
- **Dispositivos:** cold open sem intro; rehook a cada 2–4 min (revelação/virada de fase); 3–4 open loops nos primeiros 20s; pattern interrupt a cada 30–90s (gráfico, trecho de arquivo, tabela); a **decisão fatal** como pergunta central que só fecha no fim; re-engage ~3 e ~6 min.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — filing (SEC/EDGAR, Companies House), relatório anual, processo (DOJ/court records) ou trade press com números; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[ALEGADO] (`30`).

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** número + stake (resultado antes da história) e contradição verificada (o documento vs a narrativa).
- **Exemplos:**
  1. "At its peak, this company was the seventh-largest in America. Its accountants signed off on everything."
  2. "The auditors went looking for €1.9 billion. It wasn't hidden. It never existed."
  3. "One handshake in a hotel lobby led to a $10 billion verdict."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); acusação sem [ALEGADO]/sentença; número sem fonte; prometer colapso que o episódio não entrega.

## 8. Thumbnail

- **Composição:** 1 símbolo (logo real da empresa, gráfico caindo, recibo, fita de evidência) + 1 número grande (valor perdido, dias do colapso) + 3–4 palavras que não repetem o título.
- **Paleta:** cinza-escura com vermelho de "queda" ou âmbar; 1 cor de destaque · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** rosto de pessoa viva com enquadramento acusatório; insinuação de crime sem condenação; screenshot de manchete sem crédito; primeiro frame escuro/ilegível; sensacionalismo com vítimas (funcionários, aposentados).

## 9. Monetização

- **AdSense (classe):** $18–25 [ALEGADO] (faixa do operador; coerente com CPM de $10–25 do formato → RPM ≈metade, [PRATICANTE/OutlierKit]; fontes públicas divergem de $2 a $23 [ALEGADO] — a classe só se confirma na Analytics do canal, `10`/`23`).
- **Produto digital:** "collapse case-file pack" a $7–27 — cronologia, comparação de balanços, checklist dos sinais que aparecem antes da queda; guia "financial autopsy" (como ler um filing).
- **Patreon/membros:** sim — early access, planilha do caso do mês, Q&A de leitura de balanço; audiência de negócios tem alta propensão a pagar por análise [ALEGADO].
- **Afiliado/brand:** livros de negócios/história corporativa, plataformas de dados financeiros (uso editorial/nominativo), cursos; sponsors de fintech/B2B/SaaS têm fit alto com a audiência [ALEGADO — OutlierKit/faceless.my, 2026].
- **Rota no funil (`21`):** short (o número do colapso) → inscrito → long (autópsia completa) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 16–28h (pesquisa 4–8h; roteiro 3–5h; montagem visual 6–10h; voz 1h; packaging 1–2h) [PRATICANTE — OutlierKit, 27/07/2026]; cadência realista semanal/quinzenal para solo.
- **Assets:** filings e relatórios (SEC/EDGAR, Companies House, RI), court records, arquivo público (Prelinger, Wikimedia, footage governamental), stock licenciado (Storyblocks/Artgrid/Envato), motion graphics próprios. Clipes de jornal: só trecho curto e transformativo, se necessário — é a maior fonte de claim (OutlierKit).
- **Voz:** TTS edge-tts (en-US, voz contida) ou ElevenLabs; 150–160 palavras/min; voz única e consistente = marca.
- **Disclosure:** voz/visual sintético declarado no pacote (política de conteúdo alterado/sintético).

## 11. Riscos

- **Difamação:** o principal risco do nicho. Pessoas vivas (fundadores, CFOs, auditores) → "alleged", atribuir a acusação a quem a fez ("prosecutors said", "the SEC alleged") e nunca transformar insinuação em fato. Casos reais de 2026: condenação de £40.000 no Reino Unido contra canal de YouTube por vídeos difamatórios (Rzucek v Vinnicombe, abr/2026); ação por implicação contra documentário sobreviveu à primeira instância e só caiu em anti-SLAPP quase dois anos depois (Schneider v. Warner Bros. Discovery, set/2026); cessar-e-desistir de empresa contra trailer de documentário por edição que sugeria violação de ordem judicial (Kalshi vs. Netflix, jul/2026). Vitória judicial não devolve o custo.
- **Copyright:** clipe de broadcast sem licença é a causa mais comum de claim no formato; usar stock licenciado, arquivo de domínio público e motion graphics próprios; fair use é defesa, não permissão (OutlierKit).
- **Inautenticidade/qualidade:** onda de documentários faceless quase idênticos com fontes rasas e erros factuais (caso Craftsman/Sears documentado pelo Something This Week, set/2026) — diferenciar com peça primária por vídeo, fontes no description e estrutura que varia entre episódios. Evita conteúdo inautêntico (`09`) e o erro que se replica entre canais.
- **Advertiser:** conteúdo financeiro atrai escrutínio de precisão (sem conselho de investimento, sem promessa); evitar enquadramento acusatório em thumb/título; manter tom documental para não puxar limited ads.
- **Marcas:** logos de empresas em contexto editorial/nominativo são aceitáveis, mas sem sugerir endosso ou parceria; não usar assets da empresa como se fossem próprios.

## 12. 10 ideias-semente (títulos)

1. The Footnote That Took Down Enron
2. Wirecard: €1.9 Billion, Missing
3. The Handshake That Cost Texaco $10 Billion
4. 167 Years, One Weekend: The Credit Suisse Collapse
5. How Lehman's Balance Sheet Broke in 24 Days
6. Circuit City Fired Its Best People First
7. Reliance Communications: The Debt That Ate a Dynasty
8. Toys "R" Us: The Buyout That Killed the Stores
9. What the Auditor's Letter Actually Said
10. The Weekend Silicon Valley Bank Died

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 30–100 inscritos; comentários do tipo "do [company] next" (demanda explícita para a próxima autópsia).
- **Meta de validação (30 dias):** 6–8 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 6 de 8; nenhum claim de footage/nenhum strike; 1 peça primária documentada por vídeo (lista de fontes na descrição).
