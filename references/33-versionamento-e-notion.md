# 33 — Versionamento do canal (git sem mídia) e Notion

O projeto do canal tem **centenas de GB de mídia** — git não é lugar para isso. Mas roteiro, pesquisa, PROMPTS, pacotes, scripts, branding e regras são **texto** e valem ouro: versionar protege contra perda, permite diff e histórico.

## 1) Git do canal — `scripts/channel_git.py`

```bash
python scripts/channel_git.py "<pasta do canal>"                  # auditoria (dry-run)
python scripts/channel_git.py "<pasta>" --init                    # .gitignore + git init
python scripts/channel_git.py "<pasta>" --init --commit           # + commit inicial
python scripts/channel_git.py "<pasta>" --status                  # status/log resumidos
```

**O que fica versionado:** roteiro, PESQUISA_FONTE, tease, captions (SRT/ASS), PROMPTS.md, youtube_package.txt, scripts, `00_CANAL/` (branding, calendário, regras), assets leves (fontes, logos, banners) e o pacote Notion.
**O que fica fora:** MP4, WAV/MP3, imagens geradas (03_imagens), render final (04_video_final), músicas, caches, backups, `99_ARCHIVE/` e segredos (`.env`, `client_secrets.json`, `yt-token.json`).

**Guardas:**
- `.gitignore` existente **nunca** é sobrescrito.
- O commit mede o staged; acima de **50 MB** ele **aborta e desfaz o stage** (mostra os maiores arquivos) — é a proteção contra mídia vazando.
- O template do ignore vive em `assets/gitignore-canal` (edite lá para todos os canais).

> Referência real (Cold File Diaries): 382 arquivos de texto (~16 MB) versionados; ~7.159 arquivos de mídia (~200 GB) fora. Pack do git: ~12,5 MiB.
> Mídia que precise de histórico (raro) → **Git LFS**, nunca no repo normal.

## 2) Notion — `scripts/notion_pack.py`

Gera um pacote **importável** (sem API/token) a partir da pasta real do canal:

```bash
python scripts/notion_pack.py "<pasta do canal>"      # -> <canal>/notion/
```

| Arquivo | Database | Conteúdo |
|---|---|---|
| `VIDEOS.csv` | Vídeos | 1 linha por `videoNN`: caso, série, data, **status do pipeline** (Backlog→Voz→Imagens→Montagem→Pronto), título, nº de imagens, pacote, nota do calendário |
| `CALENDARIO.csv` | Calendário | grade dos 30 dias (data, dia, ID, caso, série, short 12:00, long 21:00, nota) |
| `IDEIAS.csv` | Ideias | banco de posts/ideias (`00_CANAL/POSTS_BANCO_30DIAS.txt`) |
| `OUTLIERS.csv` | Outliers | outliers reais (`data/outliers.json`): formato, views, AVP, hook, padrão, lição |
| `NOTION_SETUP.md` | — | passo a passo: importar CSV, propriedades, views (Kanban por status, Calendar por data), relations e rotina |

- Import é **manual** (arrastar CSV → Import → CSV). O setup explica as propriedades e views.
- Regenerar é idempotente (sobrescreve CSVs; re-importe como *Merge*).
- Automação via API do Notion é opcional e futura: exige integração interna + token **fora do repositório**.

## Rotina

- **Domingo:** Ideias → aprovadas vão para o Calendário.
- **Diário:** atualizar `Status` do vídeo do dia no Kanban.
- **D+2/D+7:** `/dark-revisar` → atualiza `data/` → regenerar `notion_pack` (outliers e views entram no board).

## Checklist

- [ ] `channel_git.py --init` rodado (repo + `.gitignore`).
- [ ] Commit inicial feito (texto; mídia fora) e tamanho conferido.
- [ ] `notion_pack.py` rodado; CSVs importados; Kanban/Calendar criados.
- [ ] Rotina de atualização semanal definida.
