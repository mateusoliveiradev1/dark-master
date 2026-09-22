# Modelo — Small town secrets

> Categoria: True crime · Subnicho: crimes e segredos de cidades pequenas · Slug: `true-crime-small-town`
> Lane: mixed · Idioma: en (docs PT-BR) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md`) — 0/8 canais nos gates na busca principal e 0/8 na estreita (meta ≥3). Sinal adjacente real: 2 outliers cross-canal ≥3x e autocomplete com 114 termos. Revalidar com as queries estreitas do `evidencia.md` antes de escalar.

## 1. Posicionamento (1 frase)

Documentário sóbrio sobre crimes e segredos de cidades pequenas dos EUA, contado por arquivos, mapas e cronologia, para quem quer o caso da cidadezinha sem espetáculo e sem gore.

## 2. Público e promessa

- **Público:** 25–54 anos, EUA/Canadá/Reino Unido/Austrália; consome Explore With Us, dreading, Matt Orchard, cold case podcasts e arquivos de jornal local; busca "small town mystery", "small town killer", "small town lost".
- **Promessa do canal:** todo episódio entrega um caso local com cronologia, mapa e documento, e o que a cidade preferia não lembrar.
- **Inimigo da promessa:** gore, psychic como prova, teoria sem fonte, reencenação da voz da vítima, caso ativo sem report novo.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Cartas e segredos anônimos | média (não aparece no autocomplete; prova = short do Circleville a 5,8x) | baixa no formato sóbrio | a carta como objeto-símbolo; documento-foco |
| Desaparecimentos em cidade pequena | alta ("small town mystery ... lost / kidnap / killer") | média | cronologia minuto a minuto; mapa da rotina |
| Casos resolvidos com virada local | alta ("... solved") | média | a virada fica na segunda metade, sem adiantar culpado |
| Silêncios da cidade (casos que a comunidade abafa) | média ("small town stories") | baixa | tese "todos sabiam" com provas de silêncio (atas, jornais, obituários) |

## 4. Lane e formato

- **Lane:** mixed — justificativa: o sinal cross-canal aparece nos dois polos: longs de 23:02–48:00 (12.910 e 9.540 views) no ângulo psychic small town (ver `evidencia.md`) e shorts de 0:46 com 4,9–6,0x, porém teto de 1,3–1,6k views. Long carrega RPM e biblioteca; short testa hook barato.
- **Duração alvo:** long 16–24 min (evidência: 23:02 repetido em 2 canais) · short 20–60s (evidência: 0:46 do Traceory Files).
- **Cadência:** piloto 2 long + 2–3 shorts/semana (testa hook e funil); ao estabilizar, convergir para ~1 short por 2–3 longs (ratio 0.28–0.40, `references/10`) para não derrubar o RPM.
- **Mix:** short = porta de entrada de 1 ideia do caso da semana; long = receita, profundidade e autoridade. Se o funil short→long não medir em 30 dias, cortar shorts.

## 5. Fingerprint de formato (o que o recomendador lê)

- Long 16–24 min, 16:9, narração over sóbria e única (voz consistente = marca), mapa desenhado + foto de arquivo + documento na tela; sem host.
- Short vertical 9:16 de 0:20–1:00, texto de título no centro-alto, hashtags poucas e fixas (`#documentary` — padrão observado no Traceory Files).
- Thumbnail tipográfica com 1 objeto do caso (carta, mapa, telefone) e 3–4 palavras.
- Título por objeto/contradição, sem adjetivo genérico; thumb e título não repetem palavras.
- Cadência constante, série nomeada ("Small Town Files") para o recomendador ler como coleção.

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-small-town/beats.json` (gênero `true-crime-small-town`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO (18–21 min, ~2.900–3.300 palavras); FINO para caso com pouca fonte.
- **Dispositivos:** 3–5 open loops nos primeiros 20s; rehook a cada 2–4 min; re-engage ~3 min e ~6 min; pattern interrupt a cada 30–90s; pergunta central que só fecha no bloco CHAVES (`references/30`).
- **Pesquisa obrigatória:** 1 peça primária por vídeo — recorte de jornal local digitalizado, documento judicial (CourtListener/PACER), ata municipal, mapa. Sem peça primária, não publica (`references/09`, `references/30`).

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada + objeto-símbolo (a carta, o telefone, a conta de luz, o arquivo).
- **Exemplos:**
  1. "The first letter knew what the family had done that weekend. It arrived on Monday."
  2. "The vault was open, the alarm was armed, and the teller was still sitting at her window."
  3. "He left at 9. She called at 9:04. The call log ends there."
- **Proibido:** abstração, data/local antes do gancho, meta-linguagem ("in this video"), gore, psychic como prova.

## 8. Thumbnail

- **Composição:** 1 objeto do caso (carta/mapa/telefone/estrada) + 1 pista visual (aro, seta, carimbo) + 3–4 palavras que o título não repete.
- **Paleta:** sépia/verde-floresta com 1 acento de carimbo (vermelho). **Fonte:** sans condensada, caixa alta.
- **Nunca:** corpo, sangue, criança, rosto de vítima ou de pessoa viva, psychic como manchete, foto de cena crua.

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — faixa de Crime/True Crime não-gráfico (`references/10`); tom contido + arquivo reduzem yellow icon; confirmar no Analytics do canal.
- **Produto digital:** "Small Town File" — dossiê por caso (linha do tempo, documentos, mapa) a $9–19 (tripwire $7–27, `references/19`).
- **Patreon/membros:** "The Unclosed File" — acesso antecipado + documentos comentados (audiência de true crime paga por profundidade, `references/14`).
- **Afiliado/brand:** serviços jurídicos, streaming e finanças compram inventário documental não-gráfico [ALEGADO]; oferecer brand-safety (fontes, capítulos, aviso de conteúdo) para deals diretos.
- **Rota no funil (`references/21`):** short → inscrito → long → produto.

## 10. Produção

- **Custo/tempo por vídeo:** long 8–14 h (pesquisa primária + roteiro + narração + mapa/motion); short 1–2 h.
- **Assets:** public records, CourtListener/PACER, Chronicling America (Library of Congress), Wikimedia Commons e mapas próprios desenhados; manter log de origem/licença de cada clipe (evita risco de reuso, `evidencia.md`).
- **Voz:** TTS sóbrio (edge-tts/ElevenLabs), ritmo ~150–160 palavras/min (`references/30`); divulgar voz sintética quando aplicável (`references/09`).

## 11. Riscos

- **Compliance/advertiser:** violência gráfica derruba elegibilidade; thumbnail e primeiros 15s são gatilho próprio (OFICIAL, ver `evidencia.md`); conteúdo focado em abuso infantil fica inelegível mesmo não-gráfico; evitar sensitive events (mass shootings, desastre ativo).
- **Inautenticidade:** formato pode repetir, substância não — 1 pesquisa primária e ângulo próprio por vídeo (`references/09`, `references/30`).
- **Difamação/direitos:** pessoas vivas = "alleged"; 2+ fontes; correções respeitosas; sem reencenação em 1ª pessoa de vítima falecida (política do YouTube desde 2024).
- **Gate do modelo:** sem ≥3 canais-evidência passando, o nicho fica em **piloto**; não escalar cadência antes de achar o cruzamento que passa (`references/23`).

## 12. 10 ideias-semente (títulos)

1. The Circleville Letters: The Town That Got Its Secrets in the Mail
2. Skidmore, Missouri: The Killing Everyone Saw
3. The Springfield Three: Three Women, One Night, No Trace
4. Maura Murray: The Crash on a Quiet New Hampshire Road
5. Brandon Lawson: The 911 Call From a Dark Highway
6. The Yuba County Five: Five Men, One Car, No Answers
7. 657 Boulevard: Someone Was Watching Before They Moved In
8. Zebb Quinn's Last Night: One Handprint, One Puppy, One Missing Man
9. The Greenbrier Ghost: A Mother, a Ghost Story, and a Murder Trial
10. The Burger Chef Murders: The Last Shift

## 13. Métricas de sucesso

- **D+2:** CTR e retenção de 30s acima da mediana do canal [PRATICANTE] — o YouTube não publica limiar oficial.
- **D+7:** views e inscritos da série; conversão short→long (se mixed estiver rodando).
- **Meta de validação (30 dias):** 1 vídeo ≥3x a mediana do canal com retenção de 30s estável; revalidar o nicho com as queries estreitas do `evidencia.md` antes de aumentar cadência.
