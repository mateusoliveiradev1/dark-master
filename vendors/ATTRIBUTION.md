# Atribuições e licenças

A skill `dark-master` destila conteúdo de várias fontes. Créditos abaixo. **Não redistribua material de terceiros sem respeitar as licenças.**

## Skills MIT embutidas (vendors/)
| Pasta | Repositório | Licença | Uso |
|---|---|---|---|
| `vendors/youtube-skills` | https://github.com/sergebulaev/youtube-skills | MIT | Fórmulas de hook/título (Y1–Y11), heurísticas de algoritmo, princípios de thumbnail, voice rules |
| `vendors/pedronauck-skills` | https://github.com/pedronauck/skills | ver repo | `marketing/humanizer` (anti-IA), `marketing/hormozi-ad-factory` (hooks), `mine/yt-master` (algoritmo PT-BR) |
| `vendors/youtube-analytics-cli` | https://github.com/Bin-Huang/youtube-analytics-cli | ver repo | Métricas via YouTube Data + Analytics API (usado em `22-metricas-api.md`) |

## Fontes destiladas (sem embutir arquivos)
- **Guia de produção do MrBeast** ("How To Succeed In MrBeast Production") — parafraseado em `05-mrbeast-retention.md` e `01`/`06`. **Não** copiado.
- **Vídeos-fonte do usuário** (5) — destilados em `20-videos-fonte.md` e nas references temáticas.
- **Pesquisa 2026** — YouTube Help, Creator Insider, blog YouTube, e estudos de terceiros (AIR, AutoNoLab, ReelPilot, Metricool, Retensis, etc.). Citados inline com selo de confiança.

## Regras de uso
1. Nunca publicar transcrições integrais de terceiros.
2. Nunca copiar o PDF do MrBeast.
3. Manter este arquivo ao atualizar vendors.
4. Ao instalar novas skills externas, adicionar linha nesta tabela.

## Reinstalar/atualizar vendors
```bash
cd ~/.config/opencode/skills/dark-master/vendors
git -C youtube-skills pull
git -C pedronauck-skills pull
```
