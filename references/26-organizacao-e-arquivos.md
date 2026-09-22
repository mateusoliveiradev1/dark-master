# 26 — Organização de arquivos e do PC

Como a skill mantém a pasta do canal **100% organizada** — vídeos separados, arquivos no lugar certo — sem quebrar nada. Toda ação de faxina é **dry-run por padrão**.

## Estrutura padrão de um canal

```
<canal>/
├─ 00_CANAL/                 # o "cérebro" do canal
│  ├─ BRANDING.txt
│  ├─ CALENDARIO_30.txt
│  ├─ REGRA_METADATA*.txt
│  ├─ PIPELINE*.txt
│  ├─ TEMPLATE_ROTEIRO*.txt
│  ├─ PROTOCOLO_ANTI_INAUTHENTIC*.txt
│  ├─ CHECKLIST*.txt
│  └─ assets/                # fonte, logo, banner, músicas, thumbs de playlist
├─ scripts/                  # engines de produção (não confundir com a skill)
├─ videoNN/  (ou 01_EPISODES/EPxx_*/)
│  ├─ 01_roteiro/            # narration*.txt, PESQUISA_FONTE.md, tease.txt, TRADUCAO_PT.txt
│  ├─ 02_audio/              # voice_FINAL.wav, captions.srt, captions_full.srt, *_KARA.ass
│  ├─ 03_imagens/            # 01.jpg…, PROMPTS.md, _contact_sheet.jpg
│  ├─ 04_video_final/        # *_FINAL.mp4, *_YOUTUBE.mp4, *_SHORT.mp4, thumb_*.png
│  └─ youtube_package.txt    # título/descrição/tags/chapters
└─ 99_ARCHIVE/               # o que não é mais usado, mas não pode sumir
```

Nomes das subpastas de vídeo: `01_roteiro`, `02_audio`, `03_imagens`, `04_video_final` (numeração fixa). Capa/thumb sempre em `04_video_final`.

## O que vai para onde

| Arquivo | Destino |
|---|---|
| roteiro, pesquisa, tease, tradução | `01_roteiro/` |
| voz, SRT, ASS, bed | `02_audio/` |
| imagens, prompts, contact sheet | `03_imagens/` |
| MP4 final/YouTube/Short, thumbs | `04_video_final/` |
| pacote de publicação | raiz do `videoNN/` |
| branding, calendário, regras, assets | `00_CANAL/` |
| engines .py | `scripts/` |
| obsoleto | `99_ARCHIVE/` |

## Regras de faxina (seguras)

1. **Dry-run primeiro** — o script lista o que **faria**, sem mover nada.
2. **Só move, nunca apaga** por padrão. Apagar exige `--delete` explícito.
3. **Backups** (`.bak_*`) vão para `99_ARCHIVE/backups/`, não somem.
4. **Caches** (`_parts/`, `__pycache__/`, `.tailfix_done`, etc.) podem ir para `99_ARCHIVE/cache/` ou ser ignorados.
5. **Arquivos soltos na raiz** → mover para a subpasta correspondente pelo tipo (mp4→04, srt/wav→02, jpg/png→03, txt de roteiro→01) ou para `99_ARCHIVE/` se não identificar.
6. **Nunca renomear** arquivos do pipeline (quebra scripts). Renomear só a pedido explícito.
7. Toda ação gera um **relatório** (`ORGANIZACAO.md`) com o que foi feito.

## Scripts

```bash
# relatório (só lê, não mexe):
python scripts/channel_organize.py "<pasta do canal>"

# aplicar a organização (move arquivos):
python scripts/channel_organize.py "<pasta do canal>" --apply

# mover backups/caches para 99_ARCHIVE:
python scripts/channel_organize.py "<pasta do canal>" --apply --archive
```

## Checklist de organização

- [ ] Raiz do canal sem arquivos soltos.
- [ ] Cada `videoNN/` com as 4 subpastas + pacote.
- [ ] `00_CANAL/` com branding/calendário/regras + assets.
- [ ] Backups e caches arquivados.
- [ ] Relatório `ORGANIZACAO.md` gerado.
