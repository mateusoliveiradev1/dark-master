# Deploy 24h — loop de aprendizado sempre no ar

## Resposta curta

- **Banco Neon: sim, já existe e responde.** `dark.env` tem `DATABASE_URL`, `yt_db.py` usa Postgres quando ela existe, e o ping retorna 1. É o banco do loop (`snapshots`, `traffic_sources`, `retention_points`, `outliers`, `learnings`, `experiments`).
- **Deploy 24h: sim, dá — via GitHub Actions agendado** (grátis, sem servidor). Este doc + `scripts/learn_loop.py` + `.github/workflows/learn-loop.yml` implementam.

## Arquitetura

```
GitHub Actions (cron) ── secrets ──> learn_loop.py ──> Neon (DATABASE_URL)
   diário 06:00 UTC:  collect (yt_metrics ~300un) + analyze (0un, local)
   domingo 07:00 UTC: + watch (outliers ~50un/canal) + revalidate (~150un/tema)
         │ открытия ficam em data/learn_loop/<data>.json (artifact)
         └──> propostas vão para learnings/outliers; REGRA SÓ MUDA COM APROVAÇÃO HUMANA
```

Princípio travado: o loop é **propose-only**. Ele coleta, analisa e propõe. Nunca reescreve thresholds, regras ou contratos sozinho.

## Setup (15 min)

1. **Segredos no GitHub** (repo Settings → Secrets → Actions):
   - `DATABASE_URL` — mesma do `dark.env` local (Neon).
   - `YT_TOKEN_JSON` — conteúdo de `~/.config/opencode/secrets/yt-token.json`.
   - `GOOGLE_CLIENT_SECRETS` — conteúdo de `client_secrets.json`.
2. **Habilitar Actions** no repo e rodar `learn-loop` manual (workflow_dispatch) uma vez.
3. **Conferir o artifact** `learn-loop-report` do dia.

## Quota (Data API: 10.000 un/dia)

| Etapa | Custo | Frequência |
|---|---|---|
| collect por canal próprio | ~300 un | diária |
| watch por canal monitorado | ~50 un | semanal |
| revalidate por tema | ~150 un | semanal, só vencidos (14d) |
| analyze | 0 un (banco local) | diária |

`learn_loop.py` estima antes e **corta revalidate primeiro** se passar de `--quota-budget` (default 8.000). Com 1 canal + 4 vigias + 3 temas: diária ~300, domingo ~800. Folga de sobra.

## Sem OAuth / sem rede

Cada etapa falha como **diagnóstico** (status DEGRADED, nunca zeros inventados): sem token, `collect`/`watch`/`revalidate` registram `FAIL` com o motivo; `analyze` roda no último snapshot. Ver `tests/test_graceful_offline.py`.

## Alternativa VPS (se um dia precisar de tempo real)

Actions com cron é suficiente para D+2/D+7 (granularidade diária). Se precisar de hora em hora: mesma `learn_loop.py` sob `systemd` timer numa VPS com as 3 envs (`DATABASE_URL`, token, client secrets). Não recomendado agora: custo sem benefício.

## Local

```bash
python scripts/learn_loop.py --all --dry-run   # estima quota sem gastar
python scripts/learn_loop.py --collect --analyze
python scripts/learn_loop.py --all --quota-budget 8000
```
