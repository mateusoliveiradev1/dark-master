# Modelo — Cybercrime (hackers, vazamentos, dark web e crimes digitais)

> Categoria: Tech · Subnicho: hackers, vazamentos, dark web e crimes digitais · Slug: `tech-cybercrime`
> Lane: long-first · Idioma: en (docs PT-BR) · RPM (classe): $18–25 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`) — busca ampla "cybercrime documentary": 0/8 gates; estreitamento "hacker documentary": 0/8 gates, mas **5 canais com fome** (outlier ≥3×) e **3 emergentes** (≤90d + 2/3 gates). Revalidar em 2–4 semanas.

## 1. Posicionamento (1 frase)

Casos reais de hacking, vazamentos e crime digital reconstruídos do primeiro registro ao desfecho — documentário longo para adultos que já acompanham Blackfiles, Cybernews e Darknet Diaries e querem saber como a investigação terminou, não como se invade um sistema.

## 2. Público e promessa

- **Público:** 25–44, EUA/Reino Unido/Canadá/Austrália (geos de CPM alto); consome documentário de hacking (Blackfiles, Cybernews, Cryton, Lume, Hacker Group Machina), o podcast Darknet Diaries e true crime; chega por buscas do tipo "cyber crime documentary dark web" e "cyber attacks documentary" (autocomplete da coleta: 67 termos, com cauda non-EN forte) e pelos títulos que rompem no nicho ("most wanted hacker", "wannacry"). Ver `evidencia.md`.
- **Promessa do canal:** em todo vídeo, o espectador sai com a linha do tempo verificada de um caso real, o ponto exato em que o sistema falhou, quem investigou e o que os documentos oficiais mostram.
- **Inimigo da promessa:** tutorial de ataque, glamourização do atacante, vítima como espetáculo, cifra sem fonte, pessoa viva sem "alleged".

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Perfis de hackers e grupos (Mitnick, Gonzalez, LulzSec, Evil Corp, grupos APT) | média ("cybercriminals", "cybercrime investigator") | média-alta no EN long (incumbentes ativos) | biografia investigativa com linha do tempo + documento de tribunal |
| Ataques que pararam o mundo (WannaCry, NotPetya, Colonial Pipeline, MOVEit) | alta ("cyber attacks documentary", "cyber war") | média | anatomia do incidente: o que quebrou, a resposta, o custo |
| Vazamentos e extorsão (Hacking Team, Ashley Madison, ransomware, Change Healthcare) | média ("cybercrime documentary and investigation", "report") | média-baixa | o que o vazamento revelou e o que mudou depois |
| Dark web e mercados (Silk Road, mercados de malware, infostealers) | alta ("cyber crime documentary dark web") | alta em Shorts de choque; média no doc | como o mercado funcionava e como a investigação derrubou |
| Investigação e forense digital (unidade NIT do FBI, atribuição, apreensão de cripto) | média ("cybercrime documentary questions and answers") | baixa | a caçada: como a prova ligou o crime ao acusado |

## 4. Lane e formato

- **Lane:** long-first — no cluster, os 5 canais com outlier ≥3× operam em vídeo longo: REDACT (~11:07, 61,4 mil views), Quin (13,1–14,2× em 517–560 mil), Kesit ("Belgesel", 25,5 mil), Beta Decodes (116,9 mil), SiliconUnbound (9,1 mil); os incumbentes confirmam o formato (Blackfiles 22–31 min, Cybernews 38–41 min, John Hammond 15–40 min). Nenhum Short aparece no topo da amostra.
- **Duração alvo:** long 15–25 min na entrada (12–15 min para caso único); Short 20–28s. **Cadência:** 1 long/semana + 1–2 Shorts de teaser.
- **Mix:** ≤20% Shorts; Short é teaser do long (Related Video + comentário fixado), nunca receita.

## 5. Fingerprint de formato (o que o recomendador lê)

Um caso por vídeo; narração contida sobre evidência de tela (linha de log, extrato de transação, documento com tarja, linha do tempo animada, reconstrução de terminal sem comandos reais); capítulos por fase (o alvo, a intrusão, a descoberta, a caçada, a atribuição); 15–30 min; sem apresentador; thumb escura com 1 símbolo (tarja CLASSIFIED, máscara, terminal, cifra) + 3–5 palavras; fontes on-screen no rodapé ("DOJ, 2021"; "CISA advisory"; "court filing"). Anti-modelo: tela de tutorial, payload, passo a passo.

## 6. Estrutura de roteiro

- **Beats:** `models/tech-cybercrime/beats.json` (gênero `tech-cybercrime`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO (~2.900–3.300 palavras, 18–21 min) · FINO (~1.900–2.400, 12–15 min) para caso de uma única peça.
- **Dispositivos:** 3–5 open loops nos primeiros 20s (a cifra, o alvo, o desfecho que não fecha); rehook a cada 2–4 min (nova prova, novo nome, mudança de fase); re-engage em ~3 e ~6 min; pattern interrupt a cada 30–90s (documento, zoom, reconstrução); pergunta central ("how did they get caught?") fechada só no beat ARQUIVO.
- **Pesquisa obrigatória (1 peça primária por vídeo):** DOJ press release ou indictment; docket de tribunal (CourtListener/RECAP); advisory CISA/FBI (série AA); relatório público (Verizon DBIR, Chainalysis, Europol); FBI Vault; ou linha do tempo própria montada a partir de 2+ fontes.

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada + detalhe concreto de documento (a cifra, o domínio, a linha de log). Nunca um passo de ataque.
- **Exemplos:**
  1. "He stole 170 million card numbers while teaching the FBI how hackers worked." (Albert Gonzalez, condenado)
  2. "The ransom was $4.4 million in bitcoin. Four weeks later, the FBI had most of it back." (Colonial Pipeline, 2021)
  3. "One domain, registered for $10.69, and the attack stopped mid-morning." (kill switch do WannaCry, 2017)
- **Proibido:** instrução técnica acionável, ferramenta ofensiva em contexto de uso, data/local antes do gancho, meta-linguagem, número sem fonte.

## 8. Thumbnail

- **Composição:** 1 sujeito (silhueta, máscara, terminal, tarja) + 1 elemento de prova (hash, cifra, carimbo, linha de log) + 3–5 palavras.
- **Paleta:** terminal escuro (preto, verde fosforescente, vermelho de alerta) · **Fonte:** mono/condensada, caixa alta, keyword destacada (WANTED · KILL SWITCH · $81M · BREACH).
- **Nunca:** rosto de pessoa viva implicada sem "alleged"; print de instrução/passo de ataque; bandeira de país como culpada; gore; número que o vídeo não comprova.

## 9. Monetização

- **AdSense (classe):** $18–25 [ALEGADO] — classe tech/cyber. Referências de mercado: CPM de cybersecurity $20–30 [ALEGADO — Opus.pro, mai/2026]; Technology avg RPM $21,2 [ALEGADO — Autonolab, set/2026]; recorte mais conservador dá Tech & AI $7–15 [ALEGADO — ReelPilot, jun/2026]. O número real só se confirma no Analytics; a mediana global de 300 canais auditados é ~$2,30 [PRATICANTE — AIR, jul/2026] e a dispersão dentro do nicho é maior que a diferença entre nichos.
- **Produto digital:** tripwire $7–27 "Cyber Case File" (dossiê com fontes primárias, linha do tempo e cronologia do tribunal); upsell $47–97 "research kit" (templates de timeline + lista de bases públicas). Referência real do nicho: Blackfiles Academy, do maior canal faceless de hacker histories.
- **Patreon/membros:** "o arquivo do mês" + fontes comentadas e voto no próximo caso; referência de preço no mercado do nicho: Darknet Diaries Plus a $7,49/mês.
- **Afiliado/brand:** VPN/privacidade (o Cybernews roda patrocínio de privacidade nos próprios docs), livros (Ghost in the Wires), cursos de segurança defensiva. Corte: ferramentas de ataque, "cursos de hacking", forex/sinais.
- **Rota no funil:** short de um detalhe do caso → inscrito → long do caso completo → playlist "Cyber Files" → produto.

## 10. Produção

- **Custo/tempo por vídeo:** 10–20 h por long; a pesquisa primária é o gargalo (docket, advisory, release).
- **Assets:** FBI Vault, DOJ press releases, dockets (CourtListener/RECAP), advisories CISA/FBI, relatórios (Verizon DBIR, Chainalysis, Europol), capturas reconstruídas (terminal estilizado, sem comandos reais), mapas de rota do dinheiro.
- **Voz:** narrador único, 150–160 wpm, tom contido (nada de "voz de hacker"); TTS/clone com revisão humana de pronúncia técnica.

## 11. Riscos

- **Compliance/advertiser:** a política de conteúdo perigoso do YouTube proíbe "demonstrating how to use computers or information technology with the intent to steal credentials, compromise personal data, or cause serious harm"; o enquadramento documental (EDSA) exige contexto no próprio vídeo/áudio. Zero passo a passo, zero comando, zero captura de exploit — é o limite mais importante do nicho.
- **Inautenticidade:** 1 peça primária por vídeo e ângulo próprio; variar estrutura entre episódios (caso → mecanismo vs mecanismo → caso); o formato "explainer de arquivo" vira template com facilidade.
- **Outros:** pessoas vivas = charged/alleged/prosecutors say; não expor vítimas nem republicar dados vazados; não afirmar autoria de grupo ou Estado sem documento oficial; evidência fabricada com IA em acusação é o pior cenário (precedente de 2026 com canal processado) — difamação é o risco jurídico central.

## 12. 10 ideias-semente (títulos)

1. WannaCry: 200,000 Computers and the $10.69 That Stopped It
2. The Hacker Who Stole 170 Million Cards While Working for the FBI
3. Colonial Pipeline: The $4.4 Million Ransom and the Coins the FBI Followed
4. NotPetya: The $10 Billion Malware That Looked Like Ransomware
5. The Bangladesh Bank Heist: $81 Million Gone by Morning
6. Hacking Team: The Spyware Company That Got Leaked
7. Stuxnet: The Machine That Destroyed Itself
8. Mirai: The Day 100,000 Cameras Broke the Internet
9. Silk Road: $1.2 Billion, One Username, One Life Sentence
10. Change Healthcare: One Stolen Login, 190 Million Records

## 13. Métricas de sucesso

- **D+2:** CTR 4–7% [PRATICANTE]; retenção nos primeiros 30s ≥70%; AVP ≥35% num long de 15–25 min.
- **D+7:** ≥1.000 views/dia de vida do canal (espelha o gate do modelo); comentários pedindo o próximo caso.
- **Meta de validação:** em 30 dias, 4 longs publicados, ≥1 vídeo com outlier ≥3× contra a mediana do canal e ≥1.000 views/dia de vida. Se não bater, estreitar para a interseção "caso nomeado + documentos oficiais" (ex.: ransomware, dark web) e revalidar antes de escalar.
