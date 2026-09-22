# Modelo — Espionagem

> Categoria: Inteligência · Subnicho: espiões, arquivos declassificados e operações secretas · Slug: `intel-espionage`
> Lane: long-first · Idioma: en (docs em PT-BR; exemplos em EN) · RPM (classe): $10–18 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — 0/16 canais passam os 3 gates; 12/16 passam os gates 2–3; 2 emergentes ≤90d; 6 outliers ≥3× no brief + 1 no cluster; fome concentrada no mercado hindi/sul-asiático — o lane EN exige estreitamento e revalidação em 2–4 semanas)

## 1. Posicionamento (1 frase)

Documentário de arquivo sobre espiões, agências e operações secretas para espectadores de língua inglesa, 25–55, que querem o caso como ele está nos papéis — o que o documento declassificado prova, o que segue censurado e quem pagou o preço — sem teoria da conspiração e sem glorificar violência.

## 2. Público e promessa

- **Público:** EUA / Reino Unido / Canadá / Austrália, 25–55, maioria masculina; consome história da Guerra Fria, documentário true-crime e livros de espionagem (Ben Macintyre é a porta de entrada citada no r/coldwar); assiste 20–60 min por sessão e mantém o canal como biblioteca de fundo. Players adjacentes observados: Spy Wars: Declassified (27,4k seguidores no Postbox), Eyes Wide Open (235,1k views no doc sobre Ted Shackley), Real Stories, The WAR Room, Blackfiles [ALEGADO — 236k inscritos e 20M+ views de vida, citados em post de dez/2025].
- **Promessa do canal:** todo episódio abre um arquivo real (CIA FOIA/CREST, FBI Vault, NARA, The National Archives UK série KV) e reconstrói a operação em cronologia — o que os documentos provam, onde se contradizem e o que continua fora do público.
- **Inimigo da promessa:** teoria da conspiração apresentada como fato (MJ-12, "encobrimento" sem documento); difamação de pessoa viva; gore; exaltação de violência, golpes ou assassinatos; footage de conflito atual como espetáculo; título "TOP SECRET" sem fonte primária.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Guerra Fria e arquivos clandestinos (KGB/CIA/MI6/Stasi) | alta — `spy documentary cold war`, `spy documentary kgb`, `spy documentary soviet`, `spy documentary russian` no eixo de 265 termos | média — no cluster EN, 4 dos 8 canais passam os gates 2–3, mas todos com mais de 130 dias; o ângulo "papel primeiro" segue pouco servido no faceless | O documento abre o episódio: papel tarjado + linha do tempo + mapa de Berlim/Viena |
| Operações de engenharia secreta (Azorian/K-129, túnel de Berlim, U-2) | alta — `declassified` e `cia` no topo; The WAR Room e Pure Declassified produzem nesse formato em 2026 | média-alta — footage de TV (Real Stories, Witness) domina os 52 min; produção própria com arquivo oficial é diferencial | A operação como problema de engenharia: números, tolerâncias e o erro humano |
| Espiões duplos e traições internas (Philby, Blake, Ames, Hanssen) | alta e durável — threads do r/coldwar e r/AskHistorians pedem exatamente "accurate Cold War espionage"; `spy catcher documentary` e `spycops documentary` aparecem no autocomplete | média — players grandes e antigos (1M+), brecha no faceless com arquivo | "Quem sabia o quê, quando": o erro de ofício que expôs a rede |
| Mossad e serviços regionais | alta — `spy documentary mossad`, `israeli spy documentary` | média — território sensível; a geopolítica atual contamina o enquadramento | Somente casos históricos documentados (Entebbe, Osirak, anos 60–80), nunca operações ativas |
| Micro-história com objeto-símbolo (moeda furada, rádio, perna de madeira) | média-alta — o autocomplete do eixo não aprofunda, mas o formato prende em Shorts e longs curtos | baixa no EN faceless | Um objeto carrega o episódio inteiro: anel Duquesne, moeda oca de Brooklyn, Virginia Hall |

## 4. Lane e formato

- **Lane:** long-first — justificativa: a classe documentário paga RPM ordens de magnitude acima de Shorts (`references/10`; Shorts $0.03–0.10 [ALEGADO]); a evidência de formato nos players reais é long (Spy Wars: Declassified com docs cinematográficos; Eyes Wide Open, 1:21:49; Pure Declassified, "FULL DOC"); no cluster, History Paradox (92,3k subs) puxa 2.039.017 views/dia e Nitesh Upadhyay 68.606 views/dia — tração de biblioteca, não de feed de Shorts.
- **Duração alvo:** long 20–30 min (PADRÃO–RICO) · short 20–28s (teaser) · **Cadência:** 2 long/semana + 1 short (≤20% do volume).
- **Mix:** ~85% long / ~15% short; o Short é teaser de um objeto/caso e aponta Related Video para o long do dia (nunca CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

20–30 min, 16:9, 2 longs/semana; título no padrão arquivo/caso ("The [Operation]", "The Spy Who...", "KGB vs CIA"); thumbnail com 1 objeto e 3–5 palavras; voice-only brand contida; documentos tarjados na tela, mapas históricos e arte procedural no lugar de reenactment; sem talking head. Convergência observada nos players: Spy Wars: Declassified publica docs de espionagem com gancho de pergunta ao espectador no corpo ("where are you watching from"); The WAR Room trata a operação como problema de engenharia ("WARNING: How the CIA Actually..."); Pure Declassified publica documentários inteiros sobre a CIA; os canais de TV (Real Stories, Witness) competem com 52 min de footage licenciado — a brecha do modelo é arquivo oficial + estrutura própria.

## 6. Estrutura de roteiro

- **Beats:** `models/intel-espionage/beats.json` (gênero `intel-espionage`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); RICO (24–27 min, ~3.400–3.800) para operação densa (Azorian, K-129); FINO (12–15 min, ~1.900–2.400) para caso de fonte única.
- **Dispositivos:** pergunta central "quem sabia?" que só fecha no fim; rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — documento do CIA FOIA Reading Room/CREST, FBI Vault, NARA, The National Archives UK (KV), relatório do Senado (Church/ Pike/Select Committee) ou autos judiciais; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada no documento + relógio da operação (o que o papel diz vs. o que aconteceu; quem sabia e desde quando).
- **Exemplos:**
  1. "The tunnel under Berlin was the West's best wiretap. Moscow knew about it before the first cable was tapped."
  2. "The ship was officially a deep-sea mining vessel. Its real cargo was a sunken Soviet submarine."
  3. "A newspaper delivery boy cracked a Soviet spy network open with a coin that wasn't a coin."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); vender revelação que o arquivo não sustenta.

## 8. Thumbnail

- **Composição:** 1 objeto (pasta de dossiê com selo, carimbo vermelho, moeda furada, fita de áudio, mapa com alfinetes) + no máximo 1 elemento humano mínimo (silhueta, mão, olho) + 3–5 palavras que não repetem o título.
- **Paleta:** papel bege/sépia + vermelho de carimbo + azul-noite · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** explosão, fogo, sangue, pessoa viva real nomeada em contexto acusatório, bandeiras atuais, rosto sintético com aparência de foto real, seta/círculo de clickbait.

## 9. Monetização

- **AdSense (classe):** $10–18 [ALEGADO] — classe documentário/espionagem histórica; a tabela do `references/10` traz Documentary $12,6 e Dark History ~$11–13 [ALEGADO]; estimativas públicas do vertical "mystery" ficam abaixo ($5–8 [ALEGADO — faceless.my, 2026]); a classe só se confirma na Analytics do canal.
- **Produto digital:** packs "declassified dossier" ($7–27) — linha do tempo, mapas, glossário de tradecraft (dead drop, legend, exfil) e bibliografia primária; guia "how a spy case gets declassified".
- **Patreon/membros:** early access, versão estendida com os documentos na tela, Q&A de arquivos.
- **Afiliado/brand:** livros de espionagem (Ben Macintyre, David Corn), plataformas de streaming documental; a categoria tem histórico de anunciantes de privacidade/VPN [ALEGADO — validar brand safety por vídeo].
- **Rota no funil (`references/21`):** short (1 objeto do caso) → inscrito → long (o arquivo completo) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 8–12h por long (pesquisa 4–6h — a peça primária é o gargalo; roteiro 2–3h; montagem 2–3h) + TTS; sem locução humana, locação ou equipe.
- **Assets:** CIA FOIA Reading Room/CREST, FBI Vault, NARA (domínio público), Library of Congress, Wikimedia Commons, relatórios do Senado; nunca footage de terceiros sem licença e nunca re-upload de documentário de TV.
- **Voz:** edge-tts (en-US, voz contida) ou ElevenLabs; 150–160 palavras/min; voz única e consistente = marca; legendas revisadas.

## 11. Riscos

- **Compliance/advertiser:** a política de sensitive events barra monetização de conteúdo que "lucra ou explora" o evento e limita footage cru de conflito sem contexto educacional [OFICIAL — YouTube Help]; referências a FTO em contexto documental podem receber limited ads; o update de ago/2026 liberou temas controversial não gráficos para monetização plena — o enquadramento de arquivo/educacional é o ativo. Evitar por completo conflitos atuais (Ucrânia/Gaza): conteúdo que explora ou deprecia a guerra da Ucrânia segue inelegível [OFICIAL].
- **Difamação:** pessoa viva nunca é "espião" ou "traidor" sem condenação ou documento; usar "convicted", "charged", "according to the file"; precedente real em 2026: YouTuber de true crime condenado a £40 mil por difamação no Reino Unido (Rzucek v Vinnicombe, abr/2026) — o foro EN/UK é ativo; docudramas também enfrentam ações por "implicação" (casos Netflix/Wasp Network).
- **Geopolítica:** a fome atual do tópico é regional (Índia/Paquistão, ISI/R&AW) e não migra automaticamente para o público EN; os flares do brief são Shorts/2D em hindi. O modelo escolhe casos históricos consolidados (Guerra Fria, WW2) e nunca episódios ativos.
- **Inautenticidade:** existe uma onda de canais faceless de "spy stories" com voz sintética e narrativa genérica (ex.: War of shadows: Declassified, 2026) — exatamente o padrão que a política de conteúdo inautêntico mira. Mitigação: peça primária por vídeo, estrutura que varia, posição própria, zero find-and-replace.
- **Direitos:** documentos oficiais em domínio público podem ser exibidos; música licenciada; recriações com atores só com rótulo explícito de dramatização.

## 12. 10 ideias-semente (títulos)

1. Project Azorian: The CIA Ship That Lifted a Soviet Submarine
2. The Berlin Tunnel: Eleven Months the KGB Let Run
3. The Hollow Nickel: A Spy Ring Found in Loose Change
4. The Mole MI6 Sent to Washington: Kim Philby
5. The U-2 Cover Story That Lasted Four Days
6. The KGB Officer Who Warned the West: Oleg Gordievsky
7. The Man the FBI Trusted With Its Files: Robert Hanssen
8. One Leg and a Radio: Virginia Hall in Occupied France
9. The Night the FBI Took 33 Spies: The Duquesne Ring
10. The Body That Carried the Invasion: Operation Mincemeat

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 30–100 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; ≥500 inscritos; nenhum vídeo limitado por advertiser/compliance.
