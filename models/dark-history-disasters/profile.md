# Modelo — Desastres industriais (colapsos, explosões e acidentes de trabalho)

> Categoria: Dark history · Subnicho: desastres industriais, colapsos e acidentes de trabalho · Slug: `dark-history-disasters`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $6–12 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`). Busca ampla: 0/8 canais passando os 3 gates; cluster estreito `mining disaster documentary`: 1/8 + 3 emergentes + fome em 3 canais (outliers 5,8×–32,4×). Revalidar em 2–4 semanas antes de escalar.

## 1. Posicionamento (1 frase)

Anatomia documental de desastres industriais reais — minas, plantas químicas, fábricas e obras — para espectadores de 25 a 54 anos que querem a cadeia de decisões e o relatório oficial, em tom contido no lugar do sensacionalismo.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália). Audiência adulta e educada que já consome Fascinating Horror, Plainly Difficult, os vídeos oficiais do USCSB e true crime não gráfico; muitos também ouvem o mesmo conteúdo em podcast.
- **Promessa do canal:** em cada episódio, a anatomia completa de um desastre de trabalho: o que funcionava normalmente, os avisos que foram arquivados, a falha de engenharia, o inquérito e o que mudou na norma depois.
- **Inimigo da promessa:** gore, tragedy porn, imagem de vítima identificável, número sem fonte, culpa afirmada sem "according to the report", thumbnail apelativa sem entrega.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Mineração e colapso de minas (Knox, Sunshine, Sago, Westray, Chile 2010) | alta — cluster estreito com 110 termos e casos nomeados ("knox mine disaster documentary", "sago mine disaster documentary") | média | cronologia do turno + ciência do colapso + resposta e resgate |
| Química, refinaria e explosões de planta (Bhopal, Flixborough, TPC Group, LyondellBasell) | alta — termos amplos (bbc, discovery, netflix) + dois outliers de Bhopal no cluster amplo | média | relatório de investigação (CSB e equivalentes) + diagrama/animação do evento |
| Incêndios de fábrica e colapso de edifícios (Triangle 1911, Rana Plaza 2013) | média — "factory explosion documentary" com 105 termos | média | a norma que nasceu depois; herança legal e trabalhista |
| Barragens, obras e rejeitos (dam e tailings failures) | média | baixa | geotecnia + responsabilidade corporativa |
| Acidentes "pequenos" e esquecidos (grain elevator, hot work, confined space, turno noturno) | baixa-média | baixa | o detalhe banal que mata — formato "one shift" de 12–15 min |

## 4. Lane e formato

- **Lane:** long-first. Justificativa com número: o único canal que passou os 3 gates no cluster estreito (One Documentary, 19 dias) rompeu com documentário longo de ~40 min ("Full Documentary"); os canais de referência do nicho publicam long (Fascinating Horror ~10–12 min semanais; USCSB 5–20 min). Ver `evidencia.md`.
- **Duração alvo:** 12–20 min no padrão, 30–40 min para o episódio-flagship do mês. **Cadência:** 1 long por semana, mais 1 Short-teaser na semana em que houver flagship.
- **Mix:** até 20% Shorts. Short é teaser do episódio da semana, sempre apontando para o long do dia (`references/31`).

## 5. Fingerprint de formato (o que o recomendador lê)

Duração 12–20 min (flagship 30–40), 16:9, 1080p ou mais. Cadência semanal. Thumbnail de arquivo dessaturada com um número ou ano. Narração em voiceover, sem rosto, tom contido; sem música ou com drone mínimo (Fascinating Horror não usa trilha [ALEGADO — ver `evidencia.md`]). Estrutura fixa de capítulos e descrição com fontes, camadas [FATO]/[REPORTADO] e disclaimer educativo. Episódios organizados em série numerada ("Disaster Files 03: ...").

## 6. Estrutura de roteiro

- **Beats:** `models/dark-history-disasters/beats.json` (gênero `dark-history-disasters`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). FINO (1.900–2.400 palavras, 12–15 min) para incidentes menores; RICO (3.400–3.800) para flagships de 24–27 min.
- **Dispositivos:** re-hook a cada 2–4 min, re-engage por volta de 3 min e de 6 min, 3 a 5 open loops nos primeiros 20s, pattern interrupt a cada 30–90s (arquivo → mapa/planta → documento), pergunta central que só se resolve no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: relatório oficial (CSB, NIOSH, MSHA, BSEE ou equivalente), inquérito coronário, sentença, histórico de inspeções, dados compilados de acidentes. Nada entra sem 2 fontes cruzadas e camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** detalhe impossível verificado no relatório (o alarme silenciado, a válvula que não existia, o mapa errado) + relógio (os minutos exatos).
- **Exemplos:**
  1. "The alarm had been silenced so many times that the system stopped counting it as a warning."
  2. "One valve was missing. The other was never installed. The schedule didn't change."
  3. "The mine map showed solid rock ahead. Twelve men walked toward a river."
- **Proibido:** gore, imagem de vítima, data ou local antes do gancho, abstração, meta-linguagem ("in this video"), culpar pessoa viva sem "alleged/according to the report".

## 8. Thumbnail

- **Composição:** 1 sujeito (estrutura: torre, silo, guindaste, boca de mina) + 1 elemento humano mínimo (silhueta de capacete) + 3–5 palavras com 1 número ou ano.
- **Paleta:** dessaturada (cinza-aço, sépia) com um único acento vermelho ou amarelo de alerta. **Fonte:** condensed sans bold, alto contraste, legível a 120px.
- **Nunca:** corpos, sangue, fogo com vítimas, rostos de vítimas identificáveis, desastre recente sem distância, repetir as palavras do título.

## 9. Monetização

- **AdSense (classe):** $6–12 [ALEGADO] para dark history/desastre não gráfico (becomeviral; estimativas Social Blade e HypeAuditor para o canal-referência [ALEGADO], fontes em `evidencia.md`). Audiência adulta e educada atrai anunciantes de streaming documentário, seguros, certificação de segurança e serviços legais [ALEGADO]. Em `references/10`, dark history aparece na classe ~$11–13 [ALEGADO] e documentário em $12,6 [ALEGADO] — a faixa depende mais da execução (não gráfico, com contexto) do que do tópico.
- **Produto digital:** tripwire de $9–19. Dossiê em PDF do caso (linha do tempo, cadeia de falhas, mapa da planta, documentos oficiais e bibliografia).
- **Patreon/membros:** episódio estendido, documentos-fontes e votação do próximo alvo. O canal-referência do nicho sustenta Patreon + membros (fonte de podcast em `evidencia.md`).
- **Afiliado:** livros de engenharia de segurança e história industrial.
- **Rota no funil (`21`):** Short-teaser → inscrito → episódio long → dossiê/produto → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 10–16 h de pesquisa e roteiro por episódio, mais 4–8 h de montagem. **Assets:** acervo público (National Archives, Library of Congress, Wikimedia, Europeana) + diagramas/mapas procedurais próprios + documentos oficiais (CSB, MSHA, NIOSH, BSEE). Direitos de cada clipe e documento devem ser checados caso a caso antes de entrar no vídeo.
- **Voz:** TTS de qualidade (edge-tts para protótipo, ElevenLabs para publicação), ritmo pausado (~140–150 palavras por minuto). Divulgação de IA no pacote quando voz ou visual forem sintéticos.
- **GATE 100%:** sem todas as imagens aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** morte e ferimento são o núcleo do tema. Mitigação: foco em engenharia, inquérito e norma; zero gore; zero corpo ou vítima em foco; autoclassificação honesta; pedir revisão humana quando cair limited ads. A política de monetização exige conteúdo "original e autêntico" e veda mass-produced/repetitious [OFICIAL — atualização de 15/07/2025; aperto em julho de 2026, fontes em `evidencia.md`].
- **Conteúdo inautêntico:** o subnicho atrai exatamente o perfil que a política mira (docs de desastre gerados em massa com narração sintética e template fixo). O modelo se protege com 1 peça primária por episódio, estrutura variável de um episódio a outro e roteiro/voz próprios.
- **Pessoas e empresas vivas:** pessoas citadas vivas = "alleged/according to the report"; nunca afirmar culpa não julgada; empresas ativas = linguagem do relatório oficial.
- **Vítimas e famílias:** sem imagens de vítimas, sem áudio de gritos, sem desastres muito recentes sem distância e sem verificação; nomes de mortos apenas quando já são registro público e a fonte primária confirma.

## 12. 10 ideias-semente (títulos)

1. The Alarm They Learned to Ignore: Port Neches and the Popcorn Polymer
2. The Knox Mine Disaster: The Day They Dug Into the Susquehanna
3. Westray: 26 Miners and the Law That Came After
4. Sago: 13 Miners and the Map That Was Wrong
5. Flixborough: The Pipe That Was Never Designed
6. Sunshine Mine 1972: The Fire That Rewrote Mine Rescue
7. Triangle: The Locked Doors That Built the Fire Codes
8. Rana Plaza: The Cracks They Painted Over
9. Chile 2010: 69 Days in the Refuge
10. Bhopal: The Gas, the Plant, and the Warnings on File

> Todo número, data e afirmação desses títulos precisa de fonte primária na pesquisa do episódio (relatório, inquérito ou imprensa da época). Nenhum entra no roteiro sem 2 fontes.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVD e AVP lidos contra a referência de mercado de ~23,7% de retenção média e queda de ~55% dos espectadores no primeiro minuto [PRATICANTE, ref `01`]; CTR comparado à mediana da própria conta (o YouTube não publica meta de CTR).
- **D+7:** episódio novo acumulando pelo menos 1.000 views/dia no canal; inscritos crescendo acima de 1% dos views do episódio.
- **Meta de validação em 30 dias:** 3 episódios publicados, com pelo menos 8.000 views cada e soma dos 5 primeiros acima de 10.000. Se 2 ou mais episódios derem outlier de 5× ou mais contra a mediana do canal, o formato está confirmado e o modelo pode ser promovido a PASSA em novo scan.
