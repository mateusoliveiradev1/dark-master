# Modelo — Espaço e astronomia

> Categoria: Mistérios · Subnicho: astronomia, cosmos e mistérios científicos do espaço · Slug: `mystery-space`
> Lane: long-first · Idioma: en (docs PT-BR, exemplos em EN) · RPM (classe): $8–14 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — 0/10 canais passam os 3 gates; fome do algoritmo em 7 canais únicos; flare de 421,3×; 1 emergente ≤90d; revalidar em 2–4 semanas)

## 1. Posicionamento (1 frase)

Documentário de ciência sobre o espaço para espectadores 25–55 no mercado EN que querem a resposta completa de um mistério astronômico — o que os dados provam, o que descartam e o que segue aberto — com rigor, fonte primária e zero pseudociência.

## 2. Público e promessa

- **Público:** EUA/Reino Unido/Canadá/Austrália (EN), 25–55, público STEM-curioso que consome Astrum, PBS Space Time, Dr. Becky, Cool Worlds, John Michael Godier e a onda "sleepy space" (The Sleepy Space Channel, 101 Sleepy Facts); assiste 12–25 min por episódio e mantém biblioteca de fundo (1–3h). A demanda é global: a coleta de ago–set/2026 mostra fome em canais de espaço em Hindi (Cosmic Door 7,2×), Tâmil (Tamil Unmaigal 421,3×) e Hindi generalista (Gupt vigyan 13,9×).
- **Promessa do canal:** todo episódio responde uma pergunta científica do espaço com uma peça de pesquisa primária — como a medição foi feita, o que ela provou ou descartou, e o que falta medir.
- **Inimigo da promessa:** pseudociência apresentada como fato (aliens, encobrimento da NASA, "energias"); doom/apocalipse sem base; mistério mantido aberto à força (ou vendido como resolvido o que segue aberto); render bonito passado como fotografia real.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Missões e sondas interestelares (Voyager, Pioneers, New Horizons) | alta — outlier de 29,8× (535.488 views) em `Calm Space` com a pergunta "Why Voyager 1…"; ecos em NSN Space News e Boring Science | média | Registro de missão + escala (light-time, heliopausa, potência) com telemetria e release oficial |
| Cosmologia de escala (superaglomerados, voids, tamanho do universo) | alta — `Cosmic Door` 7,2× (145.582, Laniakea, Hindi); `space biggest mysteries` e `deep space mystery` na demanda; busca "how big is the universe" 500 mil+/mês [ALEGADO — fluxnote] | média | Números e mapas: comparar escalas com honestidade e mostrar o método de medição |
| Física extrema (buracos negros, spacetime, matéria escura) | alta — `Magnetic Space` 4,2× (51.149, Spacetime 100 anos); Physics com RPM médio $19,1 [ALEGADO — autonolab] | média | 100 anos de teoria + o que as medições provaram ou ainda não |
| Exoplanetas e mundos extremos | média-alta — `Sleepy Space Science` 5,8× (207.963, "Why Does Everything In The Universe Spin?"); onda sleep-space usa exoplanetas (The Sleepy Space Channel) | média-alta (sleep-space já é commodity) | Catálogo de recordes (denser than lead, o mais frio, TRAPPIST-1) sempre com paper-fonte |
| Sinais e anomalias não resolvidas (Wow!, FRBs, 'Oumuamua, Betelgeuse) | média-alta — `space anomalies`, `space theories`, `space mysteries explained` e `mysterious space facts` no autocomplete | média | "O que os dados dizem e o que falta" — hipóteses rotuladas, nunca afirmadas |

## 4. Lane e formato

- **Lane:** long-first — justificativa: a fome da coleta está em long-form (Calm Space com 535.488 views no vídeo do Voyager em ~13 dias; outliers de 4,2–29,8× em 3 canais de espaço; docs de 1–3h na onda sleep-space). Education & Science tem o maior RPM mediano do mercado ($10,22; 77% das views monetizadas; 1,84 anúncios/sessão — AIR, 300 canais reais, 2025–2026), e Shorts pagam $0,03–0,10 [ALEGADO, `references/10`] — o long paga ordens de magnitude acima por view.
- **Duração alvo:** long 12–22 min (core; PADRÃO–RICO) + compilações ocasionais de 45–90 min para biblioteca · short 20–28s · **Cadência:** 2 long/semana + 1 short (≤20% do volume).
- **Mix:** ~85% long / ~15% short; o Short é teaser do arquivo da semana com Related Video apontando para o long (nunca CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

12–22 min, 16:9, 2 longs/semana; título-pergunta científica ou número impossível; thumbnail com 1 objeto/hardware e escala (sonda, antena, planeta, buraco negro) + 3–5 palavras; cold open sem intro com um dado verificado (light-time, distância, potência); voz única contida (voice-only brand); imagens NASA/ESA/JPL + gráficos e diagramas próprios; render sempre rotulado. Convergência observada na coleta (ago–set/2026): pergunta "why/what" com mistério científico (Calm Space — Voyager 1; Sleepy Space Science — "Why Does Everything In The Universe Spin?"), escala/cosmologia (Cosmic Door — Laniakea) e física fundamental (Magnetic Space — Spacetime, 100 anos). Alerta de adjacência: a onda sleep-space (docs de 1–3h a ~100 palavras/min; "101 Sleepy Facts" publicando quase diariamente) já é a versão commodity do tema.

## 6. Estrutura de roteiro

- **Beats:** `models/mystery-space/beats.json` (gênero `mystery-space`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); RICO (24–27 min, ~3.400–3.800) para biblioteca; FINO (12–15 min, ~1.900–2.400) para perguntas com pouca fonte primária.
- **Dispositivos:** rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central que só fecha no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — paper revisado por pares, release/telemetria NASA-ESA-JPL, dado de missão (Gaia, Kepler/K2, JWST, Voyager), circular da IAU; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[ESPECULAÇÃO].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** número verificado com escala humana (light-time, km, anos, watts) ou pergunta científica direta ancorada em fato.
- **Exemplos:**
  1. "Voyager 1 is farther from Earth than any object humans have ever built, and it is still answering calls that take almost a full day to arrive."
  2. "The Sun holds 99.86 percent of all the mass in the solar system. Everything else is a rounding error."
  3. "A radio burst hit an Ohio telescope in 1977 so hard the astronomer circled it and wrote one word: 'Wow.' It lasted 72 seconds and never returned."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); pseudociência; prometer resposta que o episódio não dá.

## 8. Thumbnail

- **Composição:** 1 sujeito (planeta, sonda, antena de rádio, buraco negro renderizado) + 1 elemento de escala (número grande, Terra como ponto minúsculo, régua de distâncias) + 3–5 palavras que não repetem o título.
- **Paleta:** preto/cobalto profundo com 1 cor de sinal (âmbar) · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** alien, disco voador, explosão apocalíptica, seta/círculo de clickbait, primeiro frame escuro/ilegível, rosto de cientista sem licença.

## 9. Monetização

- **AdSense (classe):** $8–14 [ALEGADO] — Education & Science é o maior RPM mediano de 2026 ($10,22; P25–P75 $2,31–$19,50 — AIR, 300 canais reais) e as estimativas de mercado do recorte espaço variam: Astronomy ~$14,0 / Space ~$10,1 / Space Exploration ~$9,8 [ALEGADO — autonolab, 98 nichos faceless, 07/09/2026] e $5–11 [ALEGADO — fluxnote, 26/06/2026]. A clase só se confirma na Analytics do canal.
- **Produto digital:** pack "Cosmic Scale Files" ($7–27) com cartões de escala (light-time, distâncias, temperatura), cheat-sheet de unidades astronômicas e guia "how we measure the universe".
- **Patreon/membros:** sim — early access, versão sem trilha, Q&A de perguntas da comunidade e diagramas em alta resolução.
- **Afiliado/brand:** telescópios e óptica (Celestron, Unistellar), cursos (Brilliant, CuriosityStream), livros de divulgação; sponsors de ciência pagam $300–2.500 por menção em canais pequenos [ALEGADO — fluxnote].
- **Rota no funil (`references/21`):** short (teaser do arquivo) → inscrito → long (documentário completo) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 8–12h (pesquisa 4–6h; roteiro 2–3h; montagem 2–3h) + TTS; sem locução humana, locação ou equipe.
- **Assets:** domínio público e oficial (NASA Image Library, ESA/Hubble/Webb, JPL, STScI, Wikimedia Commons), dados de missão (JPL Horizons), mapas e diagramas próprios; render/ilustração sempre rotulado como representação.
- **Voz:** TTS edge-tts (en-US, voz contida) ou ElevenLabs com voz própria clonada; ritmo 150–160 palavras/min; legendas revisadas; voz única e consistente = marca.

## 11. Riscos

- **Compliance/advertiser:** manter enquadramento educacional; doom, aliens-como-fato e thumbnails de catástrofe puxam limited ads. Tragédias espaciais humanas (Challenger, Columbia) só com tratamento histórico/engenharia, sem espetáculo.
- **Inautenticidade:** em 2026 o YouTube apertou a política de conteúdo inautêntico (3 categorias inelegíveis — genérico/repetitivo/template, off-putting e AI personas em temas sensíveis; enforcement no nível do canal) e em jan/2026 terminou 16 canais com 35M de inscritos e 4,7B de views [TechCrunch 07/2026; TNW 06/2026; OutlierKit 03/2026]. Mitigação: 1 peça primária por vídeo, estrutura que varia, voz própria, comentário editorial visível, cadência humana (≤3 longs/semana) e disclosure de IA quando sintético.
- **Outros:** precisão é a moeda do nicho (erro numérico custa credibilidade — citar unidade e fonte); direitos de imagens (NASA/ESA em geral liberam com créditos; nunca reutilizar footage de terceiros); não atribuir erro/fraude a cientistas nomeados sem fonte; separar fato/reportado/especulação e publicar correções.

## 12. 10 ideias-semente (títulos)

1. Voyager 1 Is Nearing One Light-Day From Earth. Here's What That Means
2. The Wow Signal: 72 Seconds That Were Never Explained
3. Boötes Void: 330 Million Light-Years of Almost Nothing
4. K2-38b: The Planet Denser Than Lead
5. 'Oumuamua Accelerated on Its Way Out. Here's What That Tells Us
6. TRAPPIST-1: Seven Worlds Inside Mercury's Orbit
7. The First Exoplanets Were Found Around a Dead Star
8. What Dimmed Betelgeuse — and What It Didn't Mean
9. A Signal That Repeats Every 16 Days
10. One Light-Year, Drawn to Scale

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 30–100 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; ≥500 inscritos; nenhum vídeo limitado por advertiser/compliance.
