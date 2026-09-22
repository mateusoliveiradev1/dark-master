# Modelo — Civilizações perdidas

> Categoria: Arqueologia · Subnicho: civilizações perdidas, cidades desaparecidas e colapsos antigos · Slug: `archaeology-lost-civilizations`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–14 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — 0/13 canais passam os 3 gates; 4 emergentes ≤90d; fome do algoritmo em 7 canais; flares de 280,6× (4,49M views), 148,5× e 115,5×)

## 1. Posicionamento (1 frase)

Documentário de evidência sobre cidades e civilizações perdidas para espectadores 25–55 no mercado EN que querem saber o que foi escavado, como foi datado e por que a cidade caiu — separando o que a arqueologia sustenta do que a pseudociência inventou — sem sensacionalismo e sem "civilização secreta".

## 2. Público e promessa

- **Público:** EUA/Reino Unido/Canadá/Austrália/Índia, 25–55; consome BBC, Discovery, Netflix e canais de história; sessões de 15–30 min; o gênero documentary/history é evergreen e absorve bem vídeo longo (faceless.my, 2026). A coleta mostra demanda global também fora do EN — El Dorado em hindi rendeu outliers de 148,5× e 67,2× em dois canais diferentes (jul–ago/2026) —, o que sustenta uma versão EN pelo ângulo de evidência, não pelo mistério sobrenatural.
- **Promessa do canal:** todo episódio reconstrói uma cidade perdida ou um colapso antigo com fontes publicadas — cronologia, datação, o que a escavação e o sensoriamento remoto mostram — e enfrenta o mito com evidência.
- **Inimigo da promessa:** "civilização avançada secreta" (Atlântida literal, estilo Hancock) apresentada como fato; "alguém mais construiu"; hipótese sem fonte vendida como descoberta; desrespeito à autoria e ao patrimônio de povos indígenas e africanos.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Cidades reveladas por tecnologia (LiDAR/radar): Casarabe, Maya, Angkor | alta — autocomplete `lost city` com 343 termos (ruidoso: jogos/filmes) e 107 no eixo de doc; outlier de 115,5× em "Lost Cities Beneath the Jungle" (jul/2026) | média — o padrão "cidade perdida na selva" está quente e ainda aberto no EN faceless | "O varrimento achou o que a expedição não achou": LiDAR, mapa antes/depois e estratigrafia |
| Colapsos antigos (Maya, Cahokia, Indus, Ancestral Pueblo) | alta — `lost history documentary` e `lost civilization documentary explained`; 18,0× em "The Rise and Fall of Mesopotamia" (ago/2026) | média | O que derrubou: clima, água, comércio e instituições, com registros paleoclimáticos |
| Cidades submersas (Thonis-Heracleion, Pavlopetri, Atlit-Yam) | média-alta — `ancient lost civilizations documentary`; tema litorâneo conecta com o cluster de mistérios do mar | baixa-média — poucos canais faceless dedicados | Arqueologia subaquática: sedimento, conservação e datação do que a água preservou |
| Mito do ouro (El Dorado, Guatavita, Muisca) | alta fora do EN — dois canais em hindi com outliers de 148,5× (149.390 views) e 67,2× (69.649 views), jul–ago/2026; no EN ainda raso | média | O ritual real x a cidade inventada; o que as tentativas de drenagem do lago acharam |
| Atlântida e "civilização avançada" como estudo de caso da pseudociência | alta — `lost civilization documentary graham hancock` no autocomplete; S Rao fez 4,0× com o ângulo "What Really Happened? \| Evidence" (ago/2026) | alta — o espaço é dominado pelo ângulo pseudocientífico | "A evidência não sustenta": Platão como fonte literária, Göbekli Tepe como contraexemplo e o custo real da desinformação |

## 4. Lane e formato

- **Lane:** long-first — justificativa: os outliers da coleta são documentários/títulos de cidade (Dholavira 4,49M; "Lost Cities Beneath the Jungle" 615k; "Beneath Florida" 443k), o gênero documentary/history paga ordens de magnitude acima de Shorts ($0.03–0.10, `references/10`), e o formato exige mapa + datação + cronologia. A duração não foi medida no scan (o coletor Data API não expõe duração); a faixa-alvo vem dos players do gênero — explicadores de 8–20 min e docs de 20–45 min (faceless.my, 2026) [PRATICANTE]. Shorts ≤20% apenas como teaser medido.
- **Duração alvo:** long 16–24 min (core) + compilação de biblioteca de 40–70 min ocasional · short 20–28s · **Cadência:** 2 long/semana + 1 short.
- **Mix:** ~85% long / ~15% short; o Short é teaser do sítio da semana com Related Video apontando para o long (nunca CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

16–24 min, 16:9, 2 longs/semana; título de sítio específico ou pergunta de evidência; thumbnail com 1 estrutura (pirâmide de terra, portão de pedra, muralha, cidade sobre a água) + 1 elemento de descoberta (linha de LiDAR, corte de sedimento, mapa) + 3–5 palavras; cold open de escavação/arquivo sem intro; voz única contida (voice-only brand); mapas, plantas, LiDAR e arte procedural no lugar de reenactment. Convergência observada na coleta: os outliers repetem "cidade específica + revelação por tecnologia/evidência" — Aiwala (Dholavira), Documentary Empire ("Lost Cities Beneath the Jungle" e "Rise and Fall of Mesopotamia") e Mr. True States ("Beneath Florida Lies a Lost World"). Ressalva honesta: o maior flare (Aiwala) publica no mercado hindi — o último upload, conferido em 2026-09-22, é uma aula de história em hindi —, então o padrão não é 1:1 do mercado EN.

## 6. Estrutura de roteiro

- **Beats:** `models/archaeology-lost-civilizations/beats.json` (gênero `archaeology-lost-civilizations`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); RICO (24–27 min, ~3.400–3.800) para casos densos (Casarabe/Maya); FINO (12–15 min, ~1.900–2.400) para sítios com pouca fonte publicada.
- **Dispositivos:** rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central que só se fecha no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — relatório de escavação, artigo revisado por pares (ex.: Prümers et al., *Nature* 2022), dossiê de inscrição da UNESCO, conjunto de datações por radiocarbono ou compilação paleoclimática; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada entre a lenda/o senso comum e o registro material, com um objeto ou camada como fio condutor.
- **Exemplos:**
  1. "The city had street grids and water reservoirs. Then the desert covered it for nearly four thousand years." (Dholavira)
  2. "Laser pulses through the jungle found pyramids taller than the treetops, in a basin every map called empty." (Casarabe)
  3. "The lake was drained, dredged and searched. The city of gold was never there — but the ritual behind the legend was real." (El Dorado/Guatavita)
- **Proibido:** "civilização avançada" sem evidência, alienígenas, "tecnologia impossível", data/local antes do gancho, "in this video", prometer descoberta que o episódio não mostra.

## 8. Thumbnail

- **Composição:** 1 estrutura do sítio + 1 elemento de evidência (linha de varredura LiDAR, corte de solo, mapa com marca) + 3–5 palavras que não repetem o título.
- **Paleta:** terra/areia + verde selva ou azul sedimento + 1 cor de sinal (ciano ou âmbar) · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** alienígenas, olho brilhante, caveira de cristal, "pirâmide impossível" de clickbait, imagem de saque, símbolo de sociedade secreta, primeiro frame escuro.

## 9. Monetização

- **AdSense (classe):** $8–14 [ALEGADO] — History, Documentary e Dark History caem na mesma vizinhança: auditoria de 98 nichos faceless de 07/09/2026 estima Documentary $12,6, Dark History $12,2 e History $9,9 [ALEGADO]; outras tabelas do gênero ficam em $4–9 [ALEGADO, reelpilot]. Como sempre, a classe só se confirma na Analytics do canal (geografia e watch time mudam a banda).
- **Produto digital:** pack "site files" ($7–27) com linha do tempo, mapas, glossário de datação (radiocarbono, estratigrafia, LiDAR) e o guia "how a lost city gets found".
- **Patreon/membros:** sim — early access, mapas em alta resolução, Q&A de casos e newsletter "what the evidence says".
- **Afiliado/brand:** livros e audiobooks de arqueologia/história (Amazon Associates, Audible/Storytel), cursos e streaming de documentários, turismo cultural [ALEGADO — categoria com anunciantes; exigir brand-safety one-pager por causa da vizinhança pseudocientífica].
- **Rota no funil (`references/21`):** short (teaser de 1 artefato) → inscrito → long (documentário completo) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 8–14h (pesquisa 5–7h, roteiro 2–3h, montagem 2–3h) + TTS; sem locução humana, locação ou equipe. A pesquisa é o gargalo — e é o que protege a monetização (ver riscos).
- **Assets:** domínio público e licenças claras (Wikimedia Commons, The Met Open Access, UNESCO, NASA/ISS, mapas Natural Earth); imagens de LiDAR/figuras de artigos com permissão dos autores (contato direto); plantas, cortes e mapas próprios feitos no canal.
- **Voz:** TTS edge-tts (en-US, contida) ou ElevenLabs; 150–160 palavras/min; voz única e consistente = marca; legendas revisadas; divulgar uso de IA no pacote quando aplicável.

## 11. Riscos

- **Compliance/advertiser:** o nicho faz fronteira com pseudociência e conspiração — conteúdo conspiratório/desinformação derruba monetização e reputação mesmo quando dá views. Manter enquadramento educacional, rótulos explícitos de hipótese e zero alegação sobrenatural. Sem gore; sítios funerários tratados com respeito.
- **Inautenticidade:** em jan/2026 o YouTube removeu 16 canais (35M de inscritos, 4,7B de views acumuladas, ~US$10M/ano) sob a política de conteúdo inautêntico, com detecção no nível do canal e foco em narração sintética + thumbnail em template + loop de estoque sem comentário original [air.io, 28/08/2026; TNW, 15/06/2026]. Mitigação obrigatória: 1 peça primária por vídeo, estrutura que varia entre episódios, ângulo próprio e metadados que não se repetem.
- **Outros:** pressão da audiência por "mistério proibido" (educar sem deboche); disputas nacionalistas sobre autoria (Great Zimbabwe é o caso-símbolo — a arqueologia colonial negou a autoria local por décadas); não publicar coordenadas de sítios não protegidos nem incentivar saque; direitos de figuras de LiDAR/artigos; separar consenso de hipótese em disputa (a hipótese do impacto no Younger Dryas é debate geológico legítimo, mas não sustenta "civilização avançada").

## 12. 10 ideias-semente (títulos)

1. Dholavira: The City That Ran Out of Water
2. The Lidar Scan That Found 26 Settlements Under the Amazon
3. Angkor: Did the Water Network Kill the City?
4. Great Zimbabwe: The Stone City Colonial Archaeology Refused to Credit
5. Cahokia: A City on the Mississippi, Left Behind by 1400
6. El Dorado Was a Ritual, Not a City
7. The Maya Cities Emptied. The Maya Did Not.
8. Thonis-Heracleion: The Port That Sank Into the Seafloor
9. Göbekli Tepe: Built by Foragers, Before the Cities
10. Atlantis: What Plato Actually Wrote

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–3k views por long no início (nicho de cauda longa, com picos por sítio); 30–100 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; datação e fontes citadas em 10/10 episódios; ≥500 inscritos; nenhum vídeo limitado por advertiser/compliance.
