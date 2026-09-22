# Nichos e subnichos mapeados

> Mantido pelo `dark-scout`. Método completo em `references/23-nichos-e-outliers.md`.
> Validar demanda pela *recência* (vídeos recentes com views = em alta).

## Os 3 checks (antes de comprometer)
1. Canais **<20k inscritos** fazendo **5–20x** o normal = tópico aberto.
2. **Paga o suficiente** (RPM necessário definido antes).
3. Você consegue **50 vídeos** (escreva 20 ideias agora).

## Nicho principal: True Crime (EN)
| Subnicho | Demanda | Concorrência | RPM est. | Oportunidade |
|---|---|---|---|---|
| Cold cases / desaparecimentos | alta | média | $8–15 | ★★★★ |
| Assassinos não identificados | alta | média | $8–15 | ★★★ |
| Roubos/fraudes históricos | média | média | $8–15 | ★★★ |
| Cidade pequena / local | média | baixa | $8–15 | ★★★★ |
| Forense/perícia (focus) | média | baixa | $8–15 | ★★★★ (menor risco de ad-limit) |
| Mistérios americanos obscuros | alta | média | $8–15 | ★★★★ |
| Serial killers (bio internacional) | alta | média | $8–15 | ★★★ |
| Crime organizado (máfia/cartéis/orgs) | alta (295 termos em "mafia documentary") | média em EN; alta em hindi | $8–15 | ★★★ (REPROVA nos gates em 2026-09-22; sinal parcial: 2 canais EN <90d com outliers 8,8× e 21,4× — modelo `true-crime-organized-crime`) |
| Dark history (adjacente) | alta | média | $11–13 | ★★★★ |
| História acadêmica/speculative (long 30–60min) | média | baixa | $8–16 | ★★★★ (Patreon forte) |
| Crime financeiro (adjacente) | média | média | $21–23 | ★★★★★ (alto RPM) |

## Regras de descoberta
- **Nicho estreito > amplo.** "Desastres industriais" > "história".
- Sempre validar: existe vídeo **recente** (dias/semanas) com views no tema?
- Preferir subnicho com **comprador** (RPM e fit de produto).
- Olhar **outliers de concorrentes**: vídeo ≥3–5x a média do canal deles = padrão a estudar (janela de 2–6 semanas).
- Nunca copiar; adaptar o **padrão** (hook/formato/ângulo) ao seu canal.

## Candidatos a próximo canal (quando o CFD estabilizar)
- Crime financeiro (Financial Crime Files) — RPM mais alto.
- Dark history (Midnight Archive) — arte procedural, menor risco de inautenticidade.
- Frases de caça: nichos com **busca durável** ("por quê/como") + material evergreen.

## Log do scout
- [2026-09-21] Método de outliers/validação incorporado (ver `23`). Monitor via `scripts/yt_scan_outliers.py --watch`.
- [2026-09-22] **Crime organizado (slug `true-crime-organized-crime`)**: REPROVA nas 2 queries permitidas (`--brief "organized crime documentary"`: 0/6 canais passam; `--cluster "mafia documentary"`: 0/8 canais passam; falha sempre no gate de idade ≤45d). Sinal parcial forte: Ashes of Empires (52d, 1.980 subs, 5 primeiros 156.074, 10.565/dia, outlier 8,8×) e Endless Night Files (77d, 2.760 subs, 5 primeiros 427.349, 6.361/dia, outliers 21,4× e 8,3×), ambos long-form 18–44 min convergentes. Fome do algoritmo: SIM (3 canais no brief, 5 no cluster; 28× em Mafia Talks). Riscos: saturação em hindi, enxurrada de Shorts com narração IA, advertiser em violência/drogas. Fontes: `data/briefs/organized-crime-documentary.{md,json}`, `models/true-crime-organized-crime/evidencia.md`. Ação: re-scan por "albanian mafia documentary" ou "ndrangheta documentary"; não lançar antes de ≥3 canais passarem os gates.
- [2026-09-22] **Rodada completa: 38 modelos de canal** validados com `niche_scan.py --brief/--cluster` (evidência em `models/<slug>/evidencia.md`; briefs em `data/briefs/`). Padrão dominante: o gargalo é o gate de idade ≤45d — canais de 50–90d já rompendo — então o tier **emergente** (≤90d + 2/3 gates) entrou no scan e no `23`. Fome cross-canal em 33/38 modelos; mercados hindi/ES quentes em espionagem, arqueologia, desastres e offshore; 7 modelos REPROVA (não escalar sem re-scan).
- (data) — (achado, fonte, ação sugerida)
