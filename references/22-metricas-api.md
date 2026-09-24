# 22 — Métricas: coleta, persistência e diagnóstico

## Fluxo diário

1. `python scripts/channel_scan.py "<pasta-do-canal>" --today AAAA-MM-DD --json`
2. `python scripts/yt_metrics.py --channel <canal> --project "<pasta-do-canal>" --days 30`
3. `python scripts/yt_analysis.py --channel <canal> --project "<pasta-do-canal>" --today AAAA-MM-DD --save-experiments`

O primeiro comando responde **o que existe e o que precisa ser produzido**. O segundo coleta o que o canal realmente publicado. O terceiro calcula baseline, funil, retenção, gargalos e experiments.

`/dark-revisar` executa os três e começa o resumo executivo antes do relatório completo.

## Fonte de verdade

- `config/FOCUS.md`: objetivo e métrica norte.
- `00_CANAL/CALENDARIO*`: data, caso, série e ordem.
- Arquivos reais: estado de roteiro, pesquisa, imagens, voz, captions, Long, Short, thumbs e pacote.
- `videos` no banco: vínculo entre ID publicado, `videoNN`, caso, série e data.
- `snapshots`: histórico de métricas por captura e período.
- `traffic_sources`: origem, detalhe, views, engaged views e watch hours.
- `retention_points`: curva por vídeo.
- `experiments`: hipóteses persistidas; não são regras.

## OAuth

Execute uma vez:

```bash
python scripts/yt_auth.py
```

Escopos necessários:

- `youtube.readonly`
- `yt-analytics.readonly`
- `yt-analytics-monetary.readonly` apenas após monetizar

Sem `youtube.readonly`, a Analytics API pode funcionar, mas `videos.list` falha. O coletor preserva títulos históricos conhecidos, classifica pelo histórico/AVD/AVP e marca os IDs restantes como `unmatched`; não inventa título, data ou duração.

Tokens ficam em `~/.config/opencode/secrets/yt-token.json`. Nunca registrar ou versionar o conteúdo.

## O que o coletor obtém

Por vídeo:

- `views` públicas
- `engagedViews`
- `estimatedMinutesWatched`
- `averageViewDuration`
- `averageViewPercentage`
- likes, dislikes, comments e shares
- inscritos ganhos e perdidos
- título, data de publicação, duração e privacy status quando o Data API está autorizado

Persistência:

- `scripts/yt_db.py` migra Postgres/SQLite sem descartar tabelas.
- `yt_metrics.py` atualiza todos os campos no `upsert` e preserva valores manuais ausentes.
- Uma captura é idempotente por `channel + period_start + period_end`; repetir no mesmo dia mantém a mais recente.
- `data/metrics.csv` continua legível, mas o banco é a fonte de histórico.

## Tráfego

A Traffic Source API usa `video` como filtro, não dimensão. O coletor:

1. consulta `insightTrafficSourceType` por vídeo;
2. consulta `insightTrafficSourceDetail` para `RELATED_VIDEO`;
3. salva tudo em `traffic_sources`.

`SHORTS` significa navegação vertical entre Shorts. Não é conversão Short→Long. Para Short→Long, use `RELATED_VIDEO` ou `END_SCREEN`; `END_SCREEN` pode ficar agregado porque o detalhe não é suportado para essa fonte.

## Retenção

- A API retorna 100 pontos por vídeo elegível.
- `audienceWatchRatio` é a retenção absoluta.
- `relativeRetentionPerformance` compara com vídeos de duração semelhante.
- A queda é calculada entre pontos consecutivos; o primeiro bucket não vira queda artificial.
- Shorts podem não ter curva. AVP/AVD continuam disponíveis, mas não substituem uma curva quando ela falta.

## CTR e exposição

O relatório Targeted Queries usado pelo coletor não retorna reach/CTR. Para automatizar:

- usar o YouTube Reporting API e o relatório de reach; ou
- importar valores do YouTube Studio.

CTR e impressões ficam n/d até chegarem de uma dessas fontes. `shown-in-feed` e `chose-to-view` também exigem Studio/fonte declarada. Nunca preencher zero.

## Contagem de views em 2026

- `views` públicas passam a contar desde o primeiro frame para todos os formatos.
- `engagedViews` é o valor usado para a maior parte da analytics, YPP e receita.
- `estimatedMinutesWatched` é watch time público; não chamar de qualificado sem o Studio.
- O Analytics pode ter defasagem de 48–72h. O coletor usa três dias de segurança por padrão (`--lag-days`).

## Baseline e diagnóstico

Baseline por:

- canal
- Short/long
- duração
- idade do vídeo
- série/tema quando houver amostra suficiente

O relatório mostra:

- total e evolução
- baseline, coorte e tamanho da amostra
- engaged rate e inscritos por 1.000 views
- diagnóstico por vídeo
- outliers por formato
- fontes de tráfego
- pares Short→Long
- quedas de retenção
- estoque e próximos vídeos do calendário
- conflitos de mapeamento
- experiments de uma variável

Confiança:

- baixa: uma amostra ou sem métrica de exposição;
- média: comparação repetida dentro da coorte;
- alta: somente quando a API e a coorte sustentam a conclusão sem contraste relevante.

## Learned vs hypothesis

- Um vídeo outlier é caso de estudo.
- Uma hipótese precisa de 4–6 vídeos comparáveis ou mais tempo se o tráfego for baixo.
- AVP >100% indica rewatch; não prova loop projetado nem causa de distribuição.
- Uma regra só é promovida com evidência repetida e aprovação explícita quando é travada.
- `data/learnings.md` registra decisões; `data/outliers.json` registra sinais; o banco registra a telemetria.

## Fallback

Se OAuth/API falhar:

1. mantenha o último snapshot;
2. rode o scanner de calendário;
3. mostre qualidade degradada e números antigos com a data deles;
4. não gere causalidade nem zere campos;
5. descreva a ação necessária, como reautorizar OAuth ou importar Studio.

## Verificação

```bash
python -m py_compile scripts/yt_db.py scripts/channel_scan.py scripts/yt_metrics.py scripts/yt_analysis.py
python scripts/yt_db.py doctor
python scripts/channel_scan.py "<pasta-do-canal>" --json
python scripts/yt_analysis.py --channel <canal> --project "<pasta-do-canal>"
```
