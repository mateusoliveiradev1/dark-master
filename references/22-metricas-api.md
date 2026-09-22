# Métricas — motor de dados (YouTube Analytics CLI + OAuth)

Como puxar métricas reais do Cold File Diaries para o loop `/dark-revisar`.

## Ferramenta
- Vendor: `vendors/youtube-analytics-cli` ([Bin-Huang/youtube-analytics-cli](https://github.com/Bin-Huang/youtube-analytics-cli)).
- Usa YouTube Data API v3 + YouTube Analytics API v2. Saída **JSON** no stdout (fácil de parsear por agente).
- Requer **OAuth 2.0** (service account **não** funciona em APIs do YouTube).

## Setup OAuth (uma vez)
1. Google Cloud Console → criar projeto → habilitar **YouTube Data API v3** e **YouTube Analytics API**.
2. Credentials → **OAuth 2.0 Client ID** (tipo **Desktop app**).
3. Obter **refresh token** com os escopos:
   - `https://www.googleapis.com/auth/youtube.readonly`
   - `https://www.googleapis.com/auth/yt-analytics.readonly`
   - `https://www.googleapis.com/auth/yt-analytics-monetary.readonly` (só retorna receita **após** monetizar)
4. Guardar as credenciais **fora do repo** (ex.: `~/.config/opencode/secrets/yt-oauth.json`) — **nunca** commitar.

## Queries padrão (copy/paste)

```bash
# Por vídeo (últimos 30 dias) — ordenado por views
youtube-analytics-cli report \
  --metrics views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained \
  --start-date 2026-08-21 --end-date 2026-09-21 \
  --dimensions video --sort -views --max-results 50

# Diário (canal)
youtube-analytics-cli report \
  --metrics views,likes,subscribersGained \
  --start-date 2026-09-01 --end-date 2026-09-21 --dimensions day

# Fonte de tráfego (Short e long)
youtube-analytics-cli report \
  --metrics views --start-date 2026-08-21 --end-date 2026-09-21 \
  --dimensions insightTrafficSourceType --sort -views

# Retenção de um vídeo (por trecho)
youtube-analytics-cli report \
  --metrics audienceWatchRatio,relativeRetentionPerformance \
  --start-date 2026-08-21 --end-date 2026-09-21 \
  --dimensions elapsedVideoTimeRatio \
  --filters video==VIDEO_ID;audienceType==ORGANIC
```

## Como alimentar a skill
1. Rodar a query por vídeo → converter para linhas de `data/metrics.csv`.
2. `/dark-revisar` lê o CSV, atualiza `data/outliers.json` e `data/learnings.md`, propõe evoluções.
3. Retenção por trecho → identificar o **segundo exato** da queda (ver `05e`).

## Fallback (se API falhar)
- Colar manualmente os números do Studio no `data/metrics.csv`.
- Registrar no `learnings.md` que a fonte foi manual.

## Notas de quota/limite
- Rodar o report **semanalmente**, não diariamente, no começo.
- Antes de monetizar, métricas de receita retornam vazio/0 (normal).
- Nunca expor o refresh token em logs/saídas.

## Checklist
- [ ] OAuth configurado com os 3 escopos.
- [ ] Credenciais fora do repo.
- [ ] Query por vídeo rodando e virando CSV.
- [ ] `/dark-revisar` consumindo o CSV.
