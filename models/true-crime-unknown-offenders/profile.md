# Modelo — Assassinos não identificados

> Categoria: True crime · Subnicho: casos sem autor identificado (unknown offenders, John/Jane Doe) · Slug: `true-crime-unknown-offenders`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md`) — **0** canais pequenos passaram os 3 gates em duas buscas (8 + 8 analisados); 4 canais passaram 2/3 (falham só a idade ≤45d). Blueprint utilizável como piloto controlado, mas **não escalar** antes de um re-scan que faça ≥3 canais pequenos passarem os 3 gates.

## 1. Posicionamento (1 frase)

Arquivo aberto de casos sem nome: todo episódio reconstrói, com documento na mão, como um caso de vítima ou autor não identificados avançou (ou parou) — para o espectador de true crime que já conhece os casos famosos e quer o arquivo que ainda não virou manchete.

## 2. Público e promessa

- **Público:** 25–54 anos, EN (US/UK/CA/AU — Tier 1), já consome true crime em podcast (Crime Junkie, Dateline) e documentário longo; assiste à noite, muitas vezes sem som alto; circula em r/UnresolvedMysteries, WebSleuths e nos canais das organizações de identificação (DNA Doe Project, Othram). Valoriza detalhe documental e detesta sensacionalismo gratuito.
- **Promessa do canal:** todo episódio entrega o que o arquivo tem e o que ele não tem — linha do tempo verificada, o estado real da investigação e o que ainda falta para dar um nome.
- **Inimigo da promessa:** gore, teoria apresentada como fato, exploração da dor da família, "monster" como espetáculo, reencenação em 1ª pessoa de vítima morta (proibida pelo YouTube desde jan/2024).

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| John/Jane Doe identificados por genealogia genética | alta — "unidentified doe", "unidentified serial killer documentary" | média | a ciência como protagonista: como um perfil de DNA virou uma árvore familiar e um nome |
| Suspeito não identificado em caso aberto (unknown offender) | média-alta — "unidentified killer documentary uk/usa/canada/latest" | média | o que a polícia ainda tem (sketch, reconstrução, perícia) e o que já foi descartado |
| Cold case resolvido por DNA décadas depois | alta — "unsolved murders documentary", "unidentified killer documentary real stories" | média-alta (concorre com canais grandes de true crime) | a corrida do laboratório + o custo humano dos anos sem resposta |
| Doe ainda sem nome (apelo público / reconstrução facial) | média — "unidentified doe", "unidentified killer documentary full episode" | baixa | série "The Unnamed": caso aberto, fontes oficiais, pedido de informação com dignidade |
| Vítimas não identificadas em séries criminais | média — "unidentified serial killer" | média | foco na identificação das vítimas (não no algoz); menor risco de limited ads |

## 4. Lane e formato

- **Lane:** long-first — justificativa com números do scan: (a) os dois outliers cross-canal são long-form de arquivo — ZDF True Crime 3,5× (570.768 views, "Die unbekannte Tote") e Cold Case Reopened 4,8× (118.791 views, "NEW HAMPSHIRE 1985 Cold Case Solved After 32 Years"); (b) o canal de maior tração do espaço é long-form (Othram Studios: 42.397 views/dia, 208d — lançado como estúdio de "long-form, science-driven storytelling", 2 episódios → 750 mil espectadores e 100 mil horas em 1 mês [PR]); (c) `10`: long-form paga 50–200× mais por view que Short e documentário tem RPM de classe $12,6 [ALEGADO]; (d) `30`: faixa de documentário dark é 12–25 min. **Ressalva honesta:** o scan REPROVA (0/3 gates); o lane é hipótese até re-scan.
- **Duração alvo:** long 12–20 min (PADRÃO ~2.900–3.300 palavras) · Short 20–28s.
- **Cadência:** 2 long/semana + 1 Short a cada 2–3 longs (ratio 0,28–0,40 — `10`); evitar volume diário de Short (derruba o RPM do canal).
- **Mix:** ≥80% long-form; Short = 1 detalhe verificável do caso → comentário fixado → long completo.

## 5. Fingerprint de formato (o que o recomendador lê)

Prescrição do modelo: 16:9, 12–20 min, 2 uploads/semana em horário fixo; narração voice-only, sóbria e consistente (voice-only brand); thumb com 1 sujeito (reconstrução oficial, silhueta ou objeto de evidência) + 1 numeral de tempo + 3–5 palavras; paleta de arquivo (azul-aço, off-white, acento âmbar); estrutura em série com capítulos nomeados como fases do caso ("The File", "The Lab", "The Family", "What's Left"); descrição com fontes e links oficiais; zero cena de crime.

O que **converge** nos canais com maior tração (ZDF True Crime, Cold Case Reopened, Othram Studios): long-form documental, foco em arquivo/perícia, publicação em série, tom contido. A camada "canal dark novo" não apareceu no feed das queries testadas — fingerprint é prescrição a validar, não leitura de evidência.

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-unknown-offenders/beats.json` (gênero `true-crime-unknown-offenders`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO · **Palavras:** ~2.900–3.300 (18–21 min a ~150–160 palavras/min; `30`). FINO para caso com pouco documento; RICO para perícia densa (24–27 min, ~3.400–3.800).
- **Dispositivos:** re-engage ~3 e ~6 min; rehook a cada 2–4 min; pattern interrupt a cada 30–90s; 3–5 open loops nos primeiros 20s; pergunta central ("quem é / o que falta") que só fecha no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — cronologia compilada com fontes (Namus, Doe Network, DOJ/FBI vault), release oficial de identificação, reportagem local de referência ou documento judicial; cruzar 2+ fontes e separar [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada do arquivo (o número vs. o que a família sabia) + objeto-símbolo (tooth, bracelet, case number).
- **Exemplos:**
  1. "For forty-five years, the file said 'unidentified female.' Her family said her name every single day."
  2. "All she left behind was one tooth. That tooth had a family tree."
  3. "The case stayed sealed for thirty-two years. The DNA didn't."
- **Proibido:** abstração/filosofia, data/local antes do gancho, meta-linguagem ("nesse vídeo"), número sem fonte, gore.

## 8. Thumbnail

- **Composição:** 1 sujeito (reconstrução facial oficial com crédito, silhueta ou objeto de evidência) + 1 numeral de tempo ("32 YEARS", "45 YEARS") + 3–5 palavras que **não repetem** o título.
- **Paleta:** azul-aço/arquivo envelhecido + off-white + 1 acento âmbar · **Fonte:** sans-serif bold condensada, alto contraste, legível a 120px.
- **Nunca:** corpo, ferida, sangue, close de cena de crime, foto de pessoa viva não pública, jovem em sofrimento, "monster" gráfico (gatilhos de limited ads).

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — crime non-graphic em `10` ($8–15) e documentário ($12,6); web 2026 estima $6,50–12 para público US/Tier 1 e $4–7,50 para misto em "unsolved cases" (fluxnote.io) e $6–9 para true crime educacional non-graphic (longformstudio.app) [ALEGADO]. Confirmar só no Analytics; depende de self-certification honesta e zero gore.
- **Produto digital:** tripwire $9–19 — "Case File Pack" (PDF com cronologia, mapa, lista de fontes e status atual do caso); upsell: biblioteca completa de arquivos + guia "How a Doe Gets Their Name Back" (explainer do processo DNA→árvore→família).
- **Patreon/membros:** sim — "Open File": episódio extra mensal, early access 48h, voto no próximo caso, Q&A com pesquisadores convidados.
- **Afiliado/brand:** serviços de genealogia opt-in (com aviso de privacidade), audiobooks, streamings de documentário; evitar produtos que explorem vítimas.
- **Rota no funil (`21`):** Short (frame 1: "ONE TOOTH") → inscrito → long do caso → playlist da série → pack de arquivo + membros.

## 10. Produção

- **Custo/tempo por vídeo:** 6–10h (pesquisa 2–4h + roteiro 1,5–2h + imagens/voz 1–2h + edição 1,5–2h); ferramentas: `script_builder.py`, `lint-roteiro.py`, edge-tts/ElevenLabs, arte procedural (`29`), FFmpeg (`12`/`13`).
- **Assets:** Namus, Doe Network, FBI/DOJ vaults, Internet Archive, Wikimedia/National Archives, reconstruções oficiais (com crédito ao artista), mapas procedurais, documentos públicos redigidos.
- **Voz:** voice-only brand, TTS sóbria, ~150–160 palavras/min; divulgar síntese quando aplicável; **nunca** clonar voz de terceiros nem simular fala de vítimas/pessoas mortas.

## 11. Riscos

- **Compliance/advertiser:** thumbnail ou primeiros 15s gráficos = limited/no ads mesmo com roteiro educativo [OFICIAL]; corpos com ferimento visível em contexto educativo = limited ads [OFICIAL]; "child abuse" e "eating disorders" como foco = sem full monetização (jan/2026) [OFICIAL]; mar/2026: conteúdo com jovens em sofrimento ou shock/gore = inelegível [OFICIAL]. O formato forensic-focus (perícia/DNA) tem o menor risco de yellow icon (longformstudio.app).
- **Inautenticidade:** variar estrutura e ângulo entre episódios; 1 peça primária própria por vídeo; não reciclar roteiros; o formato repete, a substância não (`09`).
- **Outros:** reencenação em 1ª pessoa de pessoa morta é proibida desde 16/01/2024 [OFICIAL]; pessoa viva = "alleged/reported", sem acusação; tratar pedidos de familiares com respeito; direitos de imagem em fotos de arquivo; YPP dobra em 01/02/2027 (8.000h/20M) [OFICIAL].

## 12. 10 ideias-semente (títulos)

1. The Girl in the Parking Lot: 45 Years Without a Name *(caso Ventura County Jane Doe → identificada em fev/2026)*
2. One Tooth, 125,000 Relatives: The Tree That Gave Her a Name *(mesmo caso; árvore de 125 mil pessoas)*
3. She Was Jane Doe for 51 Years. One Weekend Ended It. *(Jane Clinton Doe / Cheryl Lynn Edwards, identificada em jun/2026)*
4. 38 Years Unnamed: The DNA Nobody Could Read *(Tyler Jane Doe, Texas)*
5. Four Barrels, No Names: The Bear Brook Puzzle *(Bear Brook, NH)*
6. The Sketch Was Wrong. The Teeth Were Right. *(conceito: reconstrução vs. perícia odontológica)*
7. The Doe Nobody Reported Missing *(padrão de Does nunca reportados)*
8. What It Takes to Give a Stranger a Name *(explainer do pipeline DNA→árvore→família; baixo risco de ad-limit)*
9. Unidentified: The Cases the News Forgot *(série/compilação com status atual de 3 Does)*
10. When the Killer Has No Face: Unknown Offenders, Explained *(conceito: suspeito não identificado, sketches e o que a polícia ainda tem)*

> Regra antes de produzir qualquer ideia: 2+ fontes cruzadas; pessoas vivas sem acusação; sem detalhe gráfico; separar [FATO]/[REPORTADO]/[LENDA].

## 13. Métricas de sucesso

- **D+2:** CTR ≥4% (long-form de documentário); retenção no 1º minuto ≥65–70% [PRATICANTE, `01`]; AVP ≥30% em vídeo de 12–20 min.
- **D+7:** ≥2.000 views no primeiro long; inscritos e conversão Short→long medidas; comentários por 1k views (pergunta fixada respondida).
- **Meta de validação:** re-scan em 30 dias com as queries estreitas do `evidencia.md`; o modelo só escala com **≥3 canais pequenos passando os 3 gates**. Até lá, operar como piloto controlado (máx. 4–6 vídeos).
