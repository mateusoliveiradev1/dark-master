# Modelo — Catástrofes naturais (terremotos, tsunamis, vulcões e clima extremo)

> Categoria: Natureza · Subnicho: desastres naturais, clima extremo e forças da natureza · Slug: `nature-extreme`
> Lane: mixed · Idioma: en (docs PT-BR) · RPM (classe): $6–12 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`). Corte amplo `natural disaster documentary`: 0/8 canais passando os 3 gates, 4 emergentes e fome em 4 canais; corte estreito `volcano documentary`: 1/8 passando (Disaster Pulse, 28 dias), 2 emergentes e fome em 3 canais (flare de 1.626,5×). Revalidar em 2–4 semanas antes de escalar.
> Diferenciação: este modelo é **natureza/clima** (terremotos, tsunamis, furacões, vulcões, enchentes, glaciares). Desastre industrial (mina, planta química, fábrica, obra) pertence a `dark-history-disasters` — não sobreponha os dois.

## 1. Posicionamento (1 frase)

Anatomia documental das forças da natureza — terremotos, tsunamis, vulcões, enchentes e clima extremo — para espectadores de 25 a 54 anos que querem a cadeia de causas, a ciência e o registro oficial, em tom contido no lugar do sensacionalismo.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália). Audiência adulta que já consome documentário de desastre não gráfico (Fascinating Horror, PBS/NatGeo, canais oficiais USGS/NOAA) e acompanha eventos extremos pelo noticiário. Observação honesta da coleta: os rompimentos maiores de 2026 estão em PT-BR e hindi (Um Documentário, Nature Khauf) — o lane EN está mais jovem e menos cheio (ver `evidencia.md`).
- **Promessa do canal:** em cada episódio, a anatomia completa de um desastre natural: o dia normal, o gatilho geológico ou climático, a cronologia, a resposta e o que a ciência registrou.
- **Inimigo da promessa:** tragedy porn, número sem fonte, imagem de vítima, desastre recente sem distância, catastrofismo climático, culpa afirmada sem "according to the report", thumbnail apelativa sem entrega.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Tsunamis e ondas extremas (2004, Tōhoku 2011, Messina 1908, Lituya 1958, Peraliya) | alta — 87 termos no corte amplo; fome cross-canal em EN e PT | média | ciência da onda + cronologia + resposta (âncoras: The Last Day, Um Documentário) |
| Vulcões e supererupções (Krakatoa 1883, Anak Krakatau, St. Helens, Tambora) | alta — 203 termos no autocomplete ("mt st helens", "iceland", "active volcano") | média | vulcanologia + impacto no clima e nos alertas (âncoras: Disaster Pulse, Impossible Places Global) |
| Terremotos, avalanches e colapsos de terreno (Yungay 1970, Nepal, Messina) | média-alta | média | tectônica + a cadeia de decisões; história reconhecível em qualquer país |
| Enchentes, furacões e tempestades extremas (Mumbai 2005, Surat 2006, Banqiao 1975) | média-alta — shorts de flood com 700 mil+ views | média-alta no estilo "footage" | clima + infraestrutura + decisões; alimenta o lane Short |
| Clima extremo e glaciares (GLOF Nepal 2026, secas, "ano sem verão") | média | baixa | presente/futuro com ciência e sem alarmismo; exige distância de eventos recentes |

## 4. Lane e formato

- **Lane:** mixed — justificativa com número: o long-form converge em EN (The Last Day, 12–24 min, outlier 183,7×) e em PT/hindi (Um Documentário ~1h diária; Nature Khauf 17–28 min, 1–6,8M views por vídeo); o Short também mostra rompimento (Extreme Disasters 01, shorts de 21–25s com 704.875 views; Infinite Partways, 1m40 em hindi com 1.045.481). Ver `evidencia.md`.
- **Duração alvo:** long 12–20 min (flagship 30–45 min); short 20–28s. **Cadência:** 2 longs + 3 shorts por semana.
- **Mix:** até ~40% Shorts. Short é teaser do episódio (nunca solto): aponta para o long do dia e o funil Short→long é medido (`21`). Se o funil não medir, cortar Shorts e operar long-first.

## 5. Fingerprint de formato (o que o recomendador lê)

Long 12–20 min em 16:9; short 20–28s em 9:16. Cadência semanal estável. Thumbnail de arquivo dessaturada com 1 número/ano e 1 elemento natural (onda, coluna de cinza, fissura, rio). Narração em voiceover, sem rosto, tom contido; trilha mínima ou ausente. Série numerada/nomeada ("Disaster Files 03: ..." ou equivalente). Descrição com capítulos e fontes; camadas [FATO]/[REPORTADO] e disclaimer educativo.

## 6. Estrutura de roteiro

- **Beats:** `models/nature-extreme/beats.json` (gênero `nature-extreme`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). FINO (1.900–2.400 palavras, 12–15 min) para eventos menores; RICO (3.400–3.800) para flagships de 24–27 min.
- **Dispositivos:** re-hook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s (arquivo → mapa/animação → dado de satélite); pergunta central resolvida só no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: USGS (terremoto/deslizamento), NOAA (clima/ciclones), Smithsonian Global Volcanism Program, NASA Earth Observatory, relatório oficial de inquérito, dados de mortalidade compilados, imagem de satélite. Nada entra sem 2 fontes cruzadas e camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada (o mar que recuou, o muro que era baixo, o som ouvido a milhares de quilômetros) + relógio (os minutos exatos).
- **Exemplos:**
  1. "The sea pulled back more than a kilometer. Then it came back as a wall."
  2. "The town survived the earthquake. Then the mountain came down."
  3. "The seawall was built for the biggest wave in a century. The water went over it."
- **Proibido:** gore, imagem de vítima, data ou local antes do gancho, abstração, catastrofismo, meta-linguagem ("in this video"), culpar pessoa viva sem "alleged/according to the report".

## 8. Thumbnail

- **Composição:** 1 sujeito natural (onda, coluna de cinza, fissura, rio transbordando) + escala humana mínima (silhueta, telhado, carro) + 3–5 palavras com 1 número ou ano.
- **Paleta:** dessaturada (cinza-chuva, azul-petróleo) com um único acento (azul profundo ou vermelho lava). **Fonte:** condensed sans bold, alto contraste, legível a 120px.
- **Nunca:** corpos, vítimas identificáveis, desastre recente sem distância, fogo com pessoas, repetir as palavras do título.

## 9. Monetização

- **AdSense (classe):** $6–12 [ALEGADO]. Em `references/10`, documentário aparece em ~$12,6 e dark history em ~$11–13 [ALEGADO]; um estúdio de documentário publica faixa de $5–12 para "disaster stories" [ALEGADO — sentrismg; fonte em `evidencia.md`]; a AIR Media-Tech mede mediana real de $2,30 em 300 canais e alerta que a dispersão dentro do nicho é maior que entre nichos [PRATICANTE] — a classe depende de execução não gráfica, público Tier-1 e ad-load. Anunciantes plausíveis: seguro, turismo, streaming documentário, preparação de emergência [ALEGADO].
- **Produto digital:** tripwire de $9–19. Dossiê em PDF (linha do tempo, mapa, dados USGS/NOAA, documentos e bibliografia).
- **Patreon/membros:** episódio estendido, documentos-fontes e votação do próximo alvo.
- **Afiliado:** livros de geologia, clima e história natural.
- **Rota no funil (`21`):** short → inscrito → episódio long → dossiê/produto → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 8–14 h de pesquisa/roteiro + 4–8 h de montagem. **Assets:** domínio público e institucional (USGS, NOAA, NASA Earth Observatory, Smithsonian GVP, Wikimedia, Europeana, Internet Archive) + mapas/diagramas procedurais próprios. Direitos checados caso a caso (footage de tempestade/caçadores costuma ter licença restrita).
- **Voz:** TTS de qualidade (edge-tts no protótipo, ElevenLabs na publicação), ritmo pausado (~140–150 palavras por minuto). Divulgação de IA no pacote quando voz/visual forem sintéticos.
- **GATE 100%:** sem todas as imagens aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** morte é o núcleo do tema. Mitigação: foco em ciência, cronologia e resposta; zero gore; zero vítima em foco; autoclassificação honesta; eventos recentes só com distância e verificação — "como aconteceu" monetiza melhor que "veja acontecer" [ALEGADO — sentrismg; evitar eventos com menos de ~1 ano].
- **Conteúdo inautêntico:** o subnicho atrai o perfil que a política mira (docs de desastre em massa, template fixo, narração sintética sem direção humana). O modelo se protege com 1 peça primária por episódio, estrutura variável e pesquisa própria; a política de "conteúdo inautêntico" (15/07/2025, aperto em 2026) mira mass-produced/repetitive, não IA em si [OFICIAL/REPORTADO].
- **Vítimas e famílias:** sem imagens de vítimas, sem áudio de gritos, sem desastre muito recente sem distância; números só com fonte primária; nomes de mortos apenas quando já são registro público e a fonte confirma.
- **Clima:** nem alarmismo nem negacionismo — fato com fonte (USGS/NOAA/IPCC), separando [FATO]/[REPORTADO]; evitar previsão catastrófica sem base.

## 12. 10 ideias-semente (títulos)

1. The Sea Pulled Back a Mile: Anatomy of the 2004 Tsunami
2. Lituya Bay 1958: The Wave That Reached 524 Meters
3. Krakatoa: The Loudest Sound in Recorded History
4. Yungay 1970: The Mountain That Buried a Town
5. Tōhoku 2011: The Seawall Built for the Wrong Century
6. Tambora 1815: The Eruption That Canceled Summer
7. Messina 1908: Under a Minute, Then the Sea
8. Valdivia 1960: One Earthquake, Three Continents
9. Galveston 1900: The City That Built a Wall Too Late
10. Nepal 2026: The Glacier That Let Go (só com distância, verificação e respeito às vítimas)

> Todo número, data e afirmação desses títulos precisa de fonte primária na pesquisa do episódio (USGS/NOAA/GVP/relatório). Nenhum entra no roteiro sem 2 fontes.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVP/AVD lidos contra a referência de mercado [PRATICANTE, ref `01`]; CTR comparado à mediana da própria conta (o YouTube não publica meta de CTR).
- **D+7:** episódio novo acumulando ≥1.000 views/dia; inscritos crescendo acima de 1% dos views; short do dia entregando cliques no long (funil medido).
- **Meta de validação em 30 dias:** 3 longs + shorts publicados; soma dos 5 primeiros ≥10.000; se 2+ episódios derem outlier ≥5× contra a mediana do canal, o formato confirma e o modelo pode subir para PASSA em novo scan.
