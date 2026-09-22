# Modelo — Lavagem e offshore

> Categoria: Finanças · Subnicho: lavagem de dinheiro, paraísos fiscais e vazamentos (Panama/Paradise Papers) · Slug: `finance-offshore`
> Lane: long-first · Idioma: en · RPM (classe): $21–23 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`)

## 1. Posicionamento (1 frase)

Como o dinheiro atravessa fronteiras e sai do alcance do fisco — documentário longo para adultos que já assistem business/finance documentary e querem o mecanismo antes da manchete.

## 2. Público e promessa

- **Público:** 25–44 anos, EUA/Reino Unido/Canadá/Austrália e Índia; já consome MagnatesMedia, Modern MBA, ColdFusion, FINAiUS, FRONTLINE e o cluster de documentário financeiro; pergunta "how does money laundering actually work" no Reddit/ELI5 (mecânica, não escândalo).
- **Promessa do canal:** em todo vídeo, o espectador sai entendendo um veículo real de movimentação de dinheiro (empresa de fachada, trust, hawala, banco correspondente, trade-based) e o que um caso concreto prova sobre ele.
- **Inimigo da promessa:** escândalo sem mecanismo, cifra sem fonte, pessoa viva sem "alleged", e qualquer coisa que soe como manual operacional de lavagem.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Mecânica da lavagem (shell, trust, hawala, trade-based) | alta ("money laundering explained", "schemes", "history") | média-baixa no EN long-form | explicar o veículo ancorado num caso e num documento |
| Paraísos fiscais e jurisdições (Delaware, BVI, Cayman, Suíça, Dubai, Irlanda) | alta ("uk", "dubai", "london", "history") | média | "por que essa jurisdição existe e o que ela vende" |
| Vazamentos e inquéritos (Panama/Paradise/Pandora, Mossack Fonseca, Appleby) | média-alta ("gold mafia", "bbc", "al jazeera") | baixa | linha do tempo do vazamento + o que mudou depois (10 anos em 2026) |
| Bancos e compliance (HSBC, UBS, Danske, correspondentes) | média | média | a multa, o mecanismo e quem pagou de fato |
| Cripto e lavagem moderna (mixers, stablecoins, off-ramps) | alta | média | o elo entre banco tradicional e cripto sem promessa de "como fazer" |

## 4. Lane e formato

- **Lane:** long-first — no cruzamento coletado, os canais com outlier no tema operam em long-form (hawala de 22:08 com 671k views; Paradise Papers em canal de 40 dias; mafia deep dives de 68–111 min). O Short do cluster (64,8×) tem escala de 1.231 views: não sustenta lane short.
- **Duração alvo:** long 12–18 min na entrada; 25–45 min depois. Short: 20–28s (1 por long).
- **Mix:** ≤20% Shorts. Short é teaser do long (Related Video + comentário fixado), nunca receita.

## 5. Fingerprint de formato (o que o recomendador lê)

Um sujeito por vídeo (um mecanismo ou um caso), narração contida sobre documentos na tela (registro societário, contrato, tabela de valores, trecho de vazamento público), capítulos por fase do dinheiro, 12–18 min (série), sem apresentador, thumb escura com documento + cifra. Fontes on-screen no rodapé ("ICIJ, 2016"; "DOJ, 2012").

## 6. Estrutura de roteiro

- **Beats:** `models/finance-offshore/beats.json` (gênero `finance-offshore`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO (~2.900–3.300 palavras, 18–21 min) · FINO (~1.900–2.400, 12–15 min) para mecanismo único.
- **Dispositivos:** open loops nos primeiros 20s (o que o dinheiro fez, quem assinou, onde parou); rehook a cada 2–4 min; re-engage em ~3 e ~6 min; pattern interrupt a cada 30–90s com documento/mapa/zoom de registro; pergunta central ("where did the money actually go?") que só fecha no beat do dinheiro.
- **Pesquisa obrigatória (1 peça primária por vídeo):** banco de dados de vazamentos do ICIJ (offshoreleaks.icij.org), autos/notas do DOJ-SEC-FinCEN, relatório de regulador (FATF, OECD, EU Tax Observatory, GAO), registro público (Companies House, OpenCorporates) ou dado compilado (Oxfam 2026: até US$ 3,55 tri em offshore).

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** mecanismo concreto + stake (uma cifra verificada ou um detalhe impossível de documento).
- **Exemplos:**
  1. "A shell company can own an apartment, a yacht and a newspaper, and the only name on file belongs to a law firm."
  2. "Eleven and a half million documents left one law firm in Panama. What they showed was not a crime ring. It was an industry."
  3. "One bank paid 1.9 billion dollars in fines for moving drug money. The bank still exists."
- **Proibido:** abstração ("a verdade é uma questão de…"), data/local antes do gancho, meta-linguagem, número sem fonte, insinuação sobre pessoa viva sem "alleged".

## 8. Thumbnail

- **Composição:** 1 documento em close (carimbo, selo societário, tabela de valores) + 1 cifra grande + 3–5 palavras; paleta escura (verde-dólar dessaturado, cinza-petróleo, branco de papel).
- **Paleta:** escura, contraste alto · **Fonte:** sans condensada, caixa alta, keyword destacada (OFFSHORE · SHELL · LEAK · WHERE IT WENT).
- **Nunca:** rosto de pessoa viva implicada sem "alleged"; logo de banco como acusação; bandeira de país inteiro como culpada; notas empilhadas clichê; número que o vídeo não comprova.

## 9. Monetização

- **AdSense (classe):** $21–23 [ALEGADO] — classe finance/business documentary. Referências de mercado dão $10–25 para finance faceless e $7–12 para economic documentaries [ALEGADO]; o topo depende de audiência US/UK/CA/AU. O número real só se confirma na Analytics do canal.
- **Produto digital:** tripwire $7–27 "Offshore File Pack" (linha do tempo dos vazamentos + glossário de veículos + roteiro de pesquisa com fontes públicas); upsell $47–97 "research kit" (templates de checagem + lista de bases de dados).
- **Patreon/membros:** "o caso do mês + fonte primária comentada"; fan funding abre na faixa de entrada (500 inscritos).
- **Afiliado/brand:** livros de investigação, cursos de compliance/AML e bases de dados; cortar afiliado financeiro predatório (forex/sinais) — fora da promessa.
- **Rota no funil (`21`):** short de mecanismo → inscrito → long do caso completo → playlist "Follow the Money" → produto.

## 10. Produção

- **Custo/tempo por vídeo:** 10–20 h por long (8–20 h é a faixa de escrita de documentário do lane, segundo a referência de mercado; com fonte primária, conte 12–18 h). Voz TTS/clone + stock licenciado + documentos públicos.
- **Assets:** ICIJ Offshore Leaks Database; reportagens do Panama/Paradise Papers; releases de DOJ/SEC/FinCEN; relatórios FATF/OECD/EU Tax Observatory; Companies House e OpenCorporates; mapas de rota; trechos de autos.
- **Voz:** narrador único, ritmo pausado (150–160 wpm), TTS com revisão humana de pronúncia; voz própria clonada segura melhor a retenção neste lane que TTS genérico [ALEGADO].

## 11. Riscos

- **Compliance/advertiser:** crime financeiro é tema sensível — enquadramento educacional/documental, zero instrução operacional, zero glorificação. Política de conteúdo inautêntico em enforcement alto em 2026; documentário de arquivo com narração genérica é alvo.
- **Inautenticidade:** cada episódio precisa de 1 peça primária própria e de um ângulo não coberto; variar estrutura entre casos (mecanismo → caso; caso → mecanismo) para não virar template.
- **Outros:** difamação é o risco central — pessoa/empresa viva: "alleged", dupla fonte, nada de afirmar crime sem condenação; não republicar documento vazado não público (citar via reportagem pública e creditar ICIJ); cuidado com afirmações sobre jurisdições inteiras.

## 12. 10 ideias-semente (títulos)

1. How a Shell Company in Delaware Hides an Owner Nobody Can Find
2. Hawala: How Billions Move Across Borders Without a Single Bank Transfer
3. One Bank Laundered Drug Money and Paid 1.9 Billion to Stay Open
4. The Panama Papers: 11.5 Million Files and What They Actually Showed
5. Where Mossack Fonseca's Clients Went After the Firm Shut Down
6. The Double Irish: How Apple Cut Its Tax Bill With Paper Companies
7. The $200 Billion Company Nobody Is Allowed to Audit
8. Why Dubai Became the World's Laundromat
9. Trade-Based Laundering: The Invoice Is the Weapon
10. Cash-Only Businesses and the Oldest Trick in the Book
11. The Real Estate Loophole: Buying Skyscrapers With No Name
12. The Whistleblower, the Leak and the Price of Reading It

## 13. Métricas de sucesso

- **D+2:** CTR 4–7% [PRATICANTE]; retenção nos primeiros 30s ≥70%; AVP ≥35% num long de 12–18 min.
- **D+7:** long novo somando ≥1.000 views/dia de vida do canal (espelha o gate do modelo); comentários com pedidos de próximos casos/jurisdições.
- **Meta de validação:** em 30 dias, 4 longs publicados, ≥1 vídeo com outlier ≥3× contra a mediana do canal e ≥1.000 views/dia de vida. Se não bater, estreitar para a interseção "vazamento específico" e revalidar o modelo antes de escalar.
