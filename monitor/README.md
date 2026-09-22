# monitor/ — canais vigiados

- `channels.json` — lista de canais que o `dark-scout` monitora (concorrentes/referências do nicho dark).
- O scan (`scripts/yt_scan_outliers.py --watch`) pega os últimos vídeos de cada canal, calcula a **mediana** e marca **outliers** (≥ `ratio_padrao`, default 3x).
- Os resultados vão para `data/dark.db` (tabela `outliers`) e são impressos como alerta.

## Uso
```bash
python scripts/yt_scan_outliers.py --watch            # roda a lista
python scripts/yt_scan_outliers.py --mine             # seu canal
python scripts/yt_scan_outliers.py --handle @Canal --ratio 5
```

## Rotina
Semanal. A janela de oportunidade de um outlier é de **2–6 semanas** — perder uma semana é entrar atrasado.

## Editar canais
Adicione entradas em `channels.json` (`handle` ou `id`). Use `"mine": true` para o canal próprio.
