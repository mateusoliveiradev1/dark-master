# Modelo — Cold cases (EUA)

> Categoria: True crime · Subnicho: cold cases e casos arquivados dos EUA · Slug: `true-crime-cold-cases`
> Lane: long-first · Idioma: en (docs em PT-BR, exemplos em EN) · RPM (classe): $8–15 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md` — gates: 1 canal de 11 passa os 3; fome de algoritmo confirmada)

## 1. Posicionamento (1 frase)

Documentário de arquivo sobre cold cases dos EUA para espectadores 30–55 que querem a história completa — o que a polícia sabia, por que o caso esfriou e o que a perícia moderna reabriu — sem gore e sem sensacionalismo.

## 2. Público e promessa

- **Público:** EUA/Canadá/UK (EN), 30–55, consome Cold Case Files, Dateline, Forensic Files, Criminally Listed, That Chapter e conteúdo de genetic genealogy; assiste 20–40 min por caso e volta ao catálogo. Demografia de true crime costuma ser majoritariamente feminina e universitária [ALEGADO — faceless.my, 2026].
- **Promessa do canal:** todo episódio reconstrói um caso arquivado do começo ao fim com fontes públicas — cronologia, o que a perícia provou ou descartou, e quem nunca parou de lutar pelo caso.
- **Inimigo da promessa:** gore, close de ferimento, teorias apresentadas como fato, exploração da família, "assustador" de clickbait. O tom é de arquivo e justiça, não de espetáculo.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Cold cases resolvidos por DNA/genetic genealogy | alta (convergência de outliers em 3 canais) | média — 3 canais convergindo em jul–set/2026 | A ciência que reabre: cada exame, o que provou; enquadramento forensic-focus (menor risco de ad-limit) |
| Casos arquivados ainda abertos (1970s–1990s) | alta (`cold case murders documentary`, `cold case investigation documentary`) | média | Linha do tempo + o que falta; documento oficial; até 3 teorias com prós e contras |
| Identificação de vítimas não identificadas (Jane/John Doe) | média (`cold case solved`, `cold case resolved`) | baixa | Devolver o nome: DNA Doe Project, NamUs, kinship testing; foco humano e fechamento |
| Reaberturas por lei, universidades e unidades cold case | média | baixa | O sistema que destrava o caso (Carla Walker Act, classes de universidade, unidades dedicadas) |

## 4. Lane e formato

- **Lane:** long-first — justificativa: os outliers e a fome do algoritmo estão em documentário long (Red File 12,6M views num canal de 208 dias; Cold Cases Solved 192k views em 35 dias); long carrega watch time e RPM de classe $8–15 [ALEGADO] contra $0.03–0.10 do Short; o funil Short→long só se mantém se for medido.
- **Duração alvo:** long 15–25 min · short 20–28s · **Cadência:** 2 long/semana + 1 short (≤20% do volume).
- **Mix:** ~85% long / ~15% short; o Short é teaser do arquivo da semana com Related Video apontando para o long (nunca CTA genérico).

## 5. Fingerprint de formato (o que o recomendador lê)

15–25 min, 16:9, 2 longs/semana; título no padrão `[STATE] [YEAR] Cold Case Solved — [detalhe]` ou pergunta de arquivo; thumbnail dessaturada com o ano em destaque; cold open sem intro com um detalhe verificado do arquivo; voz única contida (voice-only brand); narrativa sobre documentos, mapas e releases oficiais, sem reenactment gráfico. Convergência observada nos canais-evidência: "solved/identified decades later" + footage de interrogatório como prova (Red File) e reconstrução cronológica (Cold Cases Solved, Cold Case Redemption, Crimewatch Central).

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-cold-cases/beats.json` (gênero `true-crime-cold-cases`) — usar com `--beats-file`.
- **Porte padrão:** PADRÃO — 18–21 min (~2.900–3.300 palavras); FINO (12–15 min, ~1.900–2.400) para casos com pouca fonte.
- **Dispositivos:** rehook a cada 2–4 min; re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s; pergunta central que só se fecha no fim.
- **Pesquisa obrigatória:** 1 peça primária por vídeo — release oficial (DOJ/sheriff/medical examiner), relatório de laboratório, reportagem local com linha do tempo, ou registro NamUs/CODIS; 2+ fontes cruzadas; camadas [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** detalhe impossível verificado + objeto-símbolo (a prova física: swab, stocking cap, fita de evidência).
- **Exemplos:**
  1. "Twenty-three years passed between the bite mark and the arrest. The swab never left the building."
  2. "She was found on a rainy street. Parts of her coat were bone dry."
  3. "One stocking cap waited fifty years to name a killer."
- **Proibido:** abstração/filosofia; data ou local antes do gancho; meta-linguagem ("in this video"); descrição gráfica; prometer o que o episódio não entrega.

## 8. Thumbnail

- **Composição:** 1 sujeito (retrato de arquivo ou objeto de prova) + 1 elemento de mistério (ano grande, fita de evidência, seta) + 3–5 palavras que não repetem o título.
- **Paleta:** dessaturada (cinza-azulado/âmbar) com 1 cor de destaque · **Fonte:** sans condensada bold, testada a 120px.
- **Nunca:** corpo, sangue, close de ferimento, "cara de choque" sensacionalista, primeiro frame escuro ou ilegível.

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] — crime não gráfico e documentary na tabela do `10`; fontes web divergem de $3–8 a $12–25 [ALEGADO] e a classe só se confirma na Analytics do canal.
- **Produto digital:** pack "case file" (linha do tempo + mapa + glossário forense) a $7–27; guia "how a cold case gets solved" (DNA, genetic genealogy, kinship testing).
- **Patreon/membros:** sim — early access, Q&A de casos e arquivo comentado; audiência de true crime tem conversão de membership acima da média [ALEGADO].
- **Afiliado/brand:** VPN, serviços legais e streaming [ALEGADO — faceless.my, 2026]; pitch com brand-safety one-pager (fontes, edição não gráfica, política de conteúdo).
- **Rota no funil (`21`):** short (teaser do arquivo) → inscrito → long (documentário completo) → pack/produto.

## 10. Produção

- **Custo/tempo por vídeo:** 8–12h (pesquisa 4–6h; roteiro 2–3h; montagem 2–3h) + TTS; sem locação, sem equipe.
- **Assets:** domínio público (Library of Congress, National Archives, Wikimedia Commons), releases oficiais (DOJ, sheriffs, NamUs), mapas e timelines próprios; nunca footage de terceiros sem licença.
- **Voz:** TTS edge-tts (en-US, voz contida) ou ElevenLabs; ritmo 150–160 palavras/min; voz única e consistente = marca.

## 11. Riscos

- **Compliance/advertiser:** true crime pode receber yellow icon (limited ads); a atualização de jan/2026 liberou monetização cheia para conteúdo não gráfico de temas sensíveis (dramatizado/discutido) e a de ago/2026 detalha a taxonomia de mortes (green/yellow/no-ads) — imagem gráfica no thumbnail ou nos primeiros 15s derruba o vídeo mesmo com enquadramento documental. Sem gore no roteiro e no visual; fontes e contexto visíveis.
- **Inautenticidade:** variar a estrutura entre episódios, pesquisa primária por vídeo e ponto de vista próprio; "stock footage + voz robótica" em massa é o alvo da política de conteúdo inautêntico; há relatos de flags automáticos em documentário roteirizado [ALEGADO — longformstudio, 2026] — manter originalidade e registro de fontes.
- **Outros:** pessoas vivas → "suspect/alleged"; risco de difamação; famílias (respeito acima do mínimo legal); casos ativos exigem cuidado extra; direitos de imagem de footage jornalístico.

## 12. 10 ideias-semente (títulos)

1. The Bite Mark That Convicted One of Their Own
2. The Stocking Cap That Waited Fifty Years
3. The Slides That Solved a 1971 Case
4. Four Nanograms and Forty-Seven Years
5. The Carla Walker Act: When a Case Changes the Law
6. The College Class That Reopened a 1980s Murder
7. What the First 48 Hours Missed
8. The Evidence That Sat in a Freezer for Nineteen Years
9. When DNA Arrives Fifty Years Late
10. The Families Who Never Stopped Calling

## 13. Métricas de sucesso

- **D+2:** CTR 4–6% [PRATICANTE]; retenção no 1º minuto ≥70%; AVP 35–45% [PRATICANTE].
- **D+7:** 1–5k views por long no início; 30–100 inscritos; cliques do Short para o long (Related Video) medidos.
- **Meta de validação (30 dias):** 8–10 longs publicados; ≥1 vídeo com outlier ≥3× a mediana do canal; retenção de 30s ≥70% em 8 de 10; ≥500 inscritos; nenhum vídeo limitado por conteúdo gráfico.
