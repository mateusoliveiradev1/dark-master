# Modelos de canal — blueprints por nicho/subnicho

Cada pasta em `models/` é um **modelo reutilizável** de canal dark: posicionamento, subnichos, lane, fingerprint de formato, beats, bancos de hook (long + short), thumbnail, monetização, produção, riscos e ideias-semente.

**Modelo ≠ playbook.** Playbook (`playbooks/`) = canal real com regras travadas. Modelo = **blueprint de partida**, sempre revalidado com pesquisa real antes de virar canal (`references/23`). Canal novo ≠ clone — adapte voz, branding e calendário.

## Como usar

1. Escolha um modelo pelo índice (abaixo) — ou deixe o `dark-strategist` escolher pelo seu FOCUS.
2. Revalide com dados **atuais**: `python scripts/niche_scan.py --brief "<query de validação>"` (o `evidencia.md` do modelo traz a coleta original e a query).
3. Só avance se **≥3 canais pequenos** passarem os 3 gates (`23`). Se reprovar, estreite o cruzamento formato×tópico (as queries mais estreitas estão no `evidencia.md`).
4. Gere o plano de roteiro com os beats do modelo:
   `python scripts/script_builder.py --genre <slug> --beats-file models/<slug>/beats.json --porte padrao --out "<videoNN>/01_roteiro"`
5. Hooks: use o banco do modelo (`hooks.md`) + `references/31` (Shorts). Teste **1 variável por vez**.

## Estrutura de cada modelo

```
models/<slug>/
├─ profile.md     # posicionamento, subnichos, lane, fingerprint, thumb, monetização, riscos, 10 ideias
├─ hooks.md       # banco de hooks long (10) + short (15, EN/PT) + loops
├─ beats.json     # pronto para script_builder --beats-file (gênero = slug)
└─ evidencia.md   # validação real: canais, gates, outliers, fome, autocomplete, trends, fontes
```

Templates em `models/_template/`. Status da validação vai na tabela abaixo (PASSA / PARCIAL / REPROVA + data).

## Índice (38 modelos)

| # | Slug | Modelo | Query de validação | Lane | RPM (classe) | Status |
|---|---|---|---|---|---|---|
| 1 | `true-crime-cold-cases` | Cold cases (EUA) | cold case documentary | long-first | $8–15 | PARCIAL 22/09 (1/11 gates; fome 3; 10 falham só idade) |
| 2 | `true-crime-disappearances` | Desaparecimentos | missing person documentary | mixed | $8–15 | PARCIAL 22/09 (fome 2–4; Trends ALTA) |
| 3 | `true-crime-unknown-offenders` | Assassinos não identificados | unidentified killer documentary | long-first | $8–15 | PARCIAL 22/09 (4 emergentes 2/3 gates) |
| 4 | `true-crime-cults` | Cultos e seitas criminosas | cult documentary | long-first | $8–15 | REPROVA 22/09 (0/9; sem fome) |
| 5 | `true-crime-heists` | Heists e roubos históricos | heist documentary | mixed | $8–15 | PARCIAL 22/09 (1 passer + 1 quase; fome 7) |
| 6 | `true-crime-organized-crime` | Crime organizado | organized crime documentary | long-first | $8–15 | PARCIAL 22/09 (fome 3–5; só falha idade) |
| 7 | `true-crime-serial-killers` | Serial killers (bio) | serial killer documentary | long-first | $6–12 | PARCIAL 22/09 (1/12; fome ALTA; flare 10,5×) |
| 8 | `true-crime-small-town` | Small town secrets | small town mystery documentary | mixed | $8–15 | PARCIAL 22/09 (fome 2; 114 autocompletes) |
| 9 | `dark-history-disasters` | Desastres industriais | industrial disaster documentary | long-first | $6–12 | PARCIAL 22/09 (1/8; fome 3; 3 emergentes) |
| 10 | `dark-history-pandemics` | Pandemias e pragas | history of pandemics documentary | long-first | $8–14 | REPROVA 22/09 (0/16; flare 22×; revalidar) |
| 11 | `dark-history-regimes` | Regimes e repressão | dictatorship documentary | long-first | $8–14 | PARCIAL 22/09 (fome 8; flare 342×; 2 emergentes) |
| 12 | `dark-history-forgotten-wars` | Guerras esquecidas | forgotten war documentary | long-first | $8–14 | PARCIAL 22/09 (fome 3; flare 146×; Trends ALTA) |
| 13 | `finance-fraud` | Fraudes e golpes | fraud documentary | long-first | $21–23 | PARCIAL 22/09 (fome 5; 2 flares; Trends ALTA) |
| 14 | `finance-ponzi-crypto` | Ponzi e cripto | crypto scam documentary | mixed | $18–25 | PARCIAL 22/09 (fome 4; Madoff em 2 canais) |
| 15 | `finance-offshore` | Lavagem e offshore | money laundering documentary | long-first | $21–23 | PARCIAL 22/09 (1/16 ES; fome 10; Trends ALTA) |
| 16 | `finance-corporate-collapse` | Colapsos corporativos | corporate collapse documentary | long-first | $18–25 | PARCIAL 22/09 (fome 9; 2 emergentes) |
| 17 | `forensic-toxicology` | Toxicologia forense | forensic toxicology documentary | long-first | $8–15 | REPROVA 22/09 (0/16; absorvido por true crime genérico) |
| 18 | `forensic-medical-mysteries` | Mistérios médicos | medical mystery documentary | long-first | $8–15 | REPROVA 22/09 (0/14; outliers triviais) |
| 19 | `forensic-epidemics` | Surtos e bio-riscos | disease outbreak documentary | long-first | $10–18 | REPROVA 22/09 (0/15; sem fome) |
| 20 | `forensic-pharma` | Escândalos farmacêuticos | pharmaceutical scandal documentary | long-first | $18–25 | REPROVA 22/09 (0/16; só canais seniores) |
| 21 | `mystery-unexplained` | Mistérios inexplicados | unexplained mystery documentary | mixed | $8–15 | PARCIAL 22/09 (fome 2–4; flare 969×) |
| 22 | `mystery-sky` | Fenômenos aéreos | UFO documentary | mixed | $5–10 | REPROVA 22/09 (0; demanda alta, oferta ficção) |
| 23 | `mystery-ocean` | Oceano profundo | deep sea mystery documentary | long-first | $8–14 | PARCIAL 22/09 (fome 4+4; 5 emergentes; flare 1.432×) |
| 24 | `mystery-space` | Espaço e astronomia | space mystery documentary | long-first | $8–14 | PARCIAL 22/09 (fome 7; flares 421×/162×) |
| 25 | `intel-espionage` | Espionagem | spy documentary | long-first | $10–18 | PARCIAL 22/09 (fome 6+1; fome EN fraca) |
| 26 | `intel-assassinations` | Atentados políticos | political assassination documentary | long-first | $10–18 | PARCIAL 22/09 (fome 6; flare 1.237×) |
| 27 | `psych-dark-psychology` | Psicologia dark | psychology experiment documentary | long-first | $10–18 | PARCIAL 22/09 (fome 4; flare 2.222×) |
| 28 | `psych-hoaxes` | Hoaxes e enganos | hoax documentary | mixed | $8–15 | PARCIAL 22/09 (1 passer; fome 3; 2 emergentes) |
| 29 | `tech-ai` | IA e falhas de tech | AI failure documentary | mixed | $15–25 | REPROVA 22/09 (0/16; 0 fome; poluído por AI slop) |
| 30 | `tech-cybercrime` | Cybercrime | cybercrime documentary | long-first | $18–25 | PARCIAL 22/09 (fome 6; 4 emergentes; flare 58×) |
| 31 | `tech-surveillance` | Vigilância | surveillance documentary | long-first | $15–25 | PARCIAL 22/09 (1 passer; fome fora do cruzamento) |
| 32 | `nature-extreme` | Catástrofes naturais | natural disaster documentary | mixed | $6–12 | PARCIAL 22/09 (1/16; fome 7; 6 emergentes; flare 184×) |
| 33 | `nature-animal-attacks` | Ataques de animais | animal attack documentary | mixed | $6–12 | PARCIAL 22/09 (fome 7; 4 emergentes; risco de policy) |
| 34 | `survival-shipwrecks` | Naufrágios | shipwreck documentary | long-first | $8–14 | PARCIAL 22/09 (1/16; fome 4; 4 emergentes) |
| 35 | `survival-aviation` | Aviação e acidentes | aviation disaster documentary | long-first | $8–14 | PARCIAL 22/09 (1/16; fome 3; flare 34×) |
| 36 | `folklore-urban-legends` | Lendas urbanas | urban legend documentary | mixed | $6–12 | PARCIAL 22/09 (1/16; fome 10; 2 emergentes) |
| 37 | `archaeology-artifacts` | Arqueologia e artefatos | archaeology mystery documentary | long-first | $8–14 | PARCIAL 22/09 (11/14 falham só idade; fome 6) |
| 38 | `archaeology-lost-civilizations` | Civilizações perdidas | lost civilization documentary | long-first | $8–14 | PARCIAL 22/09 (fome 7; 5 flares; 4 emergentes) |

> RPM é **classe [ALEGADO]** (estimativa de mercado, `10`/`14`); a monetização real se confirma no Analytics do canal. O modelo é um ponto de partida — a decisão é do `/dark-nicho verify` + `config/FOCUS.md`.

## Legenda de status

- **PASSA** — ≥3 canais pequenos passando os 3 gates (`23`). Pronto para piloto.
- **PARCIAL** — <3 gates, mas com **fome do algoritmo** (≥2 canais com outlier ≥3×) e/ou **emergentes** (≤90d + 2/3 gates). Revalidar em 2–4 semanas.
- **REPROVA** — sem fome nem emergentes na coleta. Não escalar; estreitar o cruzamento.

## Achados da rodada completa (38 modelos, 22/09/2026)

- **O gargalo é o gate de idade ≤45d, não a demanda.** Em ~30 dos 38 modelos, os canais falham *só* a idade e passam os outros dois gates. O tier **emergente** (≤90d + 2/3) virou a watchlist padrão — revalidar em 2–4 semanas.
- **Fome cross-canal (outlier ≥3×) apareceu em 33/38 modelos.** Destaques: mystery-unexplained (flare 969×), psych-dark-psychology (2.222×), intel-assassinations (1.237×), archaeology-lost-civilizations (281×), nature-extreme (184×), mystery-ocean (1.432×), archaeology-artifacts (403×).
- **Padrões de outlier que se repetem:** (1) *contradição/erro sistêmico* no título ("They searched the wrong field"); (2) *reveal forense* (DNA, laudo, documento); (3) *série em 2 partes* segurando a parte 2; (4) *mito vs registro* ("why every movie gets this wrong"); (5) *arquivo selado/declassificado*.
- **Mercados quentes fora do EN:** hindi e espanhol dominam a fome em espionagem, arqueologia, desastres e offshore — sinal de tema com apetite global ainda sem líder EN pequeno. Lane EN segue aberto nesses cruzamentos.
- **Modelos REPROVA (não escalar agora):** `dark-history-pandemics`, `forensic-toxicology`, `forensic-medical-mysteries`, `forensic-epidemics`, `forensic-pharma`, `mystery-sky`, `tech-ai`. Motivos: absorvidos por true crime genérico, oferta só sênior, ou poluição de AI slop.
- **Limitações de coleta:** Trends retornou 429 em vários scans (quota pública) e `--comments` não foi coletado (falta escopo `force-ssl` no `yt_auth.py` — rodar uma vez para habilitar).
- **Regra de ouro mantida:** nenhum modelo virou canal; a decisão passa pelo `/dark-nicho verify` com dados frescos + `config/FOCUS.md`.
