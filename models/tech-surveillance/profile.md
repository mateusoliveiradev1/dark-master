# Modelo — Vigilância

> Categoria: Tech · Subnicho: vigilância, privacidade e rastreamento de dados · Slug: `tech-surveillance`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $15–25 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`) — 1/16 canais pequenos passaram os 3 gates (meta ≥3). O único passante e o único emergente vivem no subcruzamento **CCTV/câmeras-como-evidência** (adjacente true crime, long-form 22–35 min); o subcruzamento declarado **privacidade/data tracking** veio frio na segunda busca (0/8 gates, 0 outliers). Watchlist: revalidar em 2–4 semanas; **não escalar** antes de ≥3 gates no cruzamento declarado.

## 1. Posicionamento (1 frase)

O arquivo da vigilância moderna: cada episódio reconstrói, com documento na mão (contrato, auditoria, log ou reportagem), como um sistema de câmeras, dados ou spyware passou a observar pessoas comuns — para quem já leu a manchete e quer ver o mecanismo por dentro, sem panfleto e sem paranoia.

## 2. Público e promessa

- **Público:** 25–54 anos, Tier 1 (US/UK/CA/AU); profissionais de tech/segurança/IT e leitores de privacidade (404 Media, EFF, Citizen Lab, comunidades OSINT); assistem long-form à noite; valorizam documento e detalhe técnico; detestam susto sem prova.
- **Promessa do canal:** todo episódio entrega o mecanismo completo — quem construiu, quanto custou, quem acessa, o que capturou de fato — com fonte visual, linha do tempo e o que ainda não se sabe.
- **Inimigo da promessa:** ativismo panfletário, teoria da conspiração sem fonte, "eles estão te ouvindo" como clickbait, doxxing de pessoas comuns, número sem documento, "AI persona" opinando como especialista em segurança/política.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Câmeras urbanas, LPR e reconhecimento facial | alta — "police surveillance documentary uk", "security camera documentary", "china surveillance documentary" | média-alta (o adjacente CCTV/true crime está lotado; o ângulo "sistema por dentro" está aberto) | o mapa da rede: quem instala, quem paga, quem consulta; o contrato e o log |
| Data brokers e rastreamento comercial | média-alta — "surveillance capitalism documentary", "digital surveillance documentary" | média | a economia do dado: o que é coletado, quanto rende, o que erra (loyalty, apps, ad tech, fingerprinting) |
| Spyware e espionagem estatal | média — "surveillance technology documentary", "stingray surveillance technology documentary" | média | o arquivo do ataque: Citizen Lab/Anistia, alvos, resposta institucional; risco geopolítico alto |
| Vigilância estatal e "safe city" | alta — "government surveillance documentary", "mass surveillance documentary", "uk surveillance documentary" | média | o projeto, o financiamento, a fiscalização que não aconteceu (Serbia/China/UK) |
| CCTV como evidência (ponte de fome comprovada) | alta — "cctv crime documentary", "cctv documentary english" | alta (adjacente true crime) | série-âncora de descoberta: o que a câmera pegou + como a rede se formou; usar só com ângulo de sistema, não de gore |

## 4. Lane e formato

- **Lane:** long-first — os canais com gates/outliers do scan são todos long-form de 22–35 min (verificado nos últimos uploads: Crime Watch UK-TV 22–35 min; FINAL FRAME CRIME 23–29 min) e o autocomplete é dominado por "documentary". **Ressalva dura:** a evidência de lane vem do adjacente CCTV; no cruzamento tech/privacidade não há passante — o lane é prescrição a validar, não leitura de prova.
- **Duração alvo:** long 18–28 min (PADRÃO ~2.900–3.300 palavras; RICO até 3.800) · Short 20–28s.
- **Cadência:** 2 long/semana + 1 Short a cada 2–3 longs (ratio 0,28–0,40; `10`). Evitar cadência diária: os canais diários do scan têm mediana de 224–1.000 views e dependem de hit isolado.
- **Mix:** ≥80% long-form; Short = 1 número verificável do sistema → comentário fixado → long completo.

## 5. Fingerprint de formato (o que o recomendador lê)

Prescrição do modelo: 16:9, 18–28 min, 2 uploads/semana em horário fixo; narração voice-only sóbria e consistente; thumb com 1 sujeito (câmera/LPR em close, still de CCTV com rosto e placa desfocados, ou página de contrato com tarja) + 1 numeral + 3–5 palavras; paleta CCTV (verde-cinza/azul-aço) + tarja preta de redação + acento âmbar; capítulos nomeados como partes do sistema ("The Network", "The Contract", "The Access", "The Cost"); descrição com fontes e links de documentos; zero slogan.

O que **converge** nos canais com tração do scan: long-form de câmeras + caso, título de uma frase com o que a câmera pegou, upload frequente. A camada "canal tech/privacidade" não apareceu no feed das duas queries — fingerprint é prescrição, não leitura de evidência.

## 6. Estrutura de roteiro

- **Beats:** `models/tech-surveillance/beats.json` (gênero `tech-surveillance`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO · **Palavras:** ~2.900–3.300 (18–21 min a ~150–160 palavras/min; `30`). FINO para arquivo curto; RICO para investigação densa (24–28 min).
- **Dispositivos:** 3 open loops nos primeiros 20s; rehook a cada 2–4 min; re-engage ~3 e ~6 min; pattern interrupt a cada 30–90s; pergunta central ("como isso funciona e quem controla") que só fecha no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — contrato/licitação, relatório de auditoria, documento judicial, pedido FOIA, relatório técnico (EFF/ACLU/Citizen Lab/Consumer Reports) ou dado compilado próprio; 2+ fontes cruzadas; separar [FATO]/[REPORTADO]/[ALEGADO].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada (a promessa do sistema vs. o documento) + objeto-símbolo (o poste, o contrato, o painel de acesso).
- **Exemplos:**
  1. "They promised the cameras would cut crime. The evidence turned out to be more complicated." *(padrão AJC/Atlanta 2026)*
  2. "One pole. One solar panel. One database you're not allowed to query." *(padrão LPR/Flock)*
  3. "Your loyalty card earned you a discount. It earned the chain $527 million." *(KIRO 7/Consumer Reports, jan/2026)*
- **Proibido:** abstração/filosofia, data/local antes do gancho, slogan ("Big Brother"), meta-linguagem ("nesse vídeo"), número sem documento.

## 8. Thumbnail

- **Composição:** 1 sujeito (câmera/LPR em close; still de CCTV com rosto e placa desfocados; contrato com tarja) + 1 numeral ("60,000", "1 IN 8", "$527M") + 3–5 palavras que **não repetem** o título.
- **Paleta:** verde-cinza CCTV/azul-aço + preto + 1 acento âmbar · **Fonte:** sans-serif bold condensada, alto contraste, legível a 120px.
- **Nunca:** rosto identificável ou placa legível de pessoa comum, close de ferida/sangue, olho vermelho genérico, "Big Brother" literal, foto íntima de terceiro.

## 9. Monetização

- **AdSense (classe):** $15–25 [ALEGADO] — tech/segurança no topo de intenção (ref `10`: Tech/AI $7–21; Documentário $12,6); guias 2026 põem o nicho faceless "Cybersecurity & Privacy" em $14–24 [ALEGADO]; audiência Tier-1 compra ferramentas de segurança. Confirmar só no Analytics; temas políticos/estatais podem cair para limited ads conforme self-certification.
- **Produto digital:** "The Surveillance Files" ($9–19) — dossiê por episódio (linha do tempo, documentos citados, pedidos FOIA/DSAR prontos para copiar); upsell: guia "How to Opt Out" (processo de 30–90 dias por broker).
- **Patreon/membros:** "Access Log" — drop mensal de documentos, early access 48h, Q&A com pesquisadores convidados.
- **Afiliado/brand:** ferramentas de privacidade/segurança (password managers, e-mail aliasing) com divulgação explícita; nunca VPN genérica como única receita.
- **Rota no funil (`21`):** Short (um número) → inscrito → long do sistema → playlist "The Watchers" → pack + membros.

## 10. Produção

- **Custo/tempo por vídeo:** 8–12h (pesquisa documental 3–5h + roteiro 1,5–2h + imagens/voz 1–2h + edição 2–3h); ferramentas: `script_builder.py`, `lint-roteiro.py`, edge-tts/ElevenLabs, arte procedural (`29`), FFmpeg (`12`/`13`).
- **Assets:** portais de compras públicas, documentos judiciais, relatórios EFF/ACLU/Citizen Lab/Consumer Reports, mapas procedurais, stills de CCTV licenciados/creditados ou recriações gráficas próprias; nada de reupload de footage de terceiros sem commentary transformativo.
- **Voz:** voice-only brand, TTS sóbria ~150–160 palavras/min; divulgar síntese quando aplicável; nunca simular fala de pessoa real.

## 11. Riscos

- **Compliance/advertiser:** temas políticos/estatais e spyware podem limitar ads; jan/2026 mudou a monetização de temas sensíveis [OFICIAL]; sem rosto/placa de pessoa comum (privacidade e advertiser); evitar "AI persona" dando conselho de segurança/política/lei (balde 3 do conteúdo inautêntico [OFICIAL]); self-certification honesta.
- **Inautenticidade:** 1 peça primária por vídeo (contrato/auditoria/linha do tempo própria); variar estrutura entre episódios; não reciclar roteiro; o formato repete, a substância não (`09`).
- **Outros:** difamação — nomear empresas/fornecedores sempre com documento + "alleged/reported"; geopolítica — citar documentos oficiais dos dois lados, não virar propaganda de Estado nem campanha de ONG; não publicar dados pessoais encontrados na pesquisa (doxxing); YPP dobra em 01/02/2027 (8.000h/20M) [OFICIAL].

## 12. 10 ideias-semente (títulos)

1. One Camera for Every Eight Residents: Inside Atlanta's $21M Surveillance Center *(AJC, ago/2026)*
2. The Cameras Don't Belong to the City: Private License Plate Networks *(debate Flock Safety, mai/2026)*
3. $527 Million: What Your Loyalty Card Is Really For *(KIRO 7/Consumer Reports, jan/2026)*
4. Gotham: The Software That Connects the Databases *(DW Documentary, fev/2026)*
5. Spyware Against Freedom: The Targets Nobody Warned *(NZZ, ago/2026; Citizen Lab/Anistia)*
6. The Safe City That Skipped Its Privacy Review *(Serbia/Huawei; meta.mk, 2026)*
7. 60,000 Cameras, One Question: Does More Surveillance Mean Less Crime? *(AJC, parte 2, ago/2026)*
8. Tracked Without Cookies: Fingerprinting in 2026 *(privacyscore.dev, jun/2026; explainer evergreen)*
9. 30 to 90 Days per Broker: The Opt-Out Economy *(lunyb, ago/2026)*
10. Who Decides What the Bodycam Shows? *(ponte CCTV; investigação com pedido de registros)*

> Regra antes de produzir qualquer ideia: 2+ fontes cruzadas; documento visual para cada número; empresas/pessoas com "alleged/reported" quando não houver decisão; separar [FATO]/[REPORTADO]/[ALEGADO].

## 13. Métricas de sucesso

- **D+2:** CTR ≥4% (long-form documentário); retenção no 1º minuto ≥65–70% [PRATICANTE, `01`]; AVP ≥30% em vídeo de 18–28 min.
- **D+7:** ≥2.000 views no primeiro long; inscritos e conversão Short→long medidas; comentários por 1k views (pergunta fixada respondida).
- **Meta de validação:** re-scan em 2–4 semanas com as queries do `evidencia.md`; o modelo só escala com **≥3 canais pequenos passando os 3 gates** no cruzamento declarado. Até lá, operar como piloto controlado (máx. 4–6 vídeos).
