---
name: dark-master
description: >
  Cérebro completo para canais dark/faceless no YouTube — planejar, empacotar, roteirizar, produzir, monetizar
  e escalar vídeos long-form e Shorts em qualquer idioma. Use quando o usuário falar de
  "canal dark", "faceless", "monetizar canal", "bater 4000 horas", "10 milhões de views de Shorts",
  "short viral", "hook", "retenção", "thumbs", "impulso" ou mencionar os canais Cold File Diaries,
  Financial Crime Files, Laudo Final, The Midnight Archive, ou os comandos /dark, /dark-lancar,
  /dark-build, /dark-audit, /dark-repurpose, /dark-monetizar. Cobre o algoritmo (CTR/AVD/AVP,
  bolhas de Shorts, engaged views), hooks e títulos (Y1–Y11), thumbnails e A/B, arquitetura de retenção
  do MrBeast, storytelling de documentário (5 atos), repurposing cross-platform, auto-dublagem
  multi-idioma, compliance YPP (politica de conteúdo inautentico), RPM por nicho, product-led monetization
  (tripwire $7–27) e a trilha 0→YPP. NÃO usar para edição de vídeo comum, upload de terceiros, métricas
  de TikTok/Instagram, nem parecer jurídico de copyright.
metadata:
  author: Liiiraa
  version: "1.0.0"
---

# dark-master

Skill-mãe para construir e monetizar canais **dark/faceless** no YouTube. Ela funde três camadas:
o **conhecimento oficial/dados 2026**, as **metodologias destiladas** (MrBeast, yt-master, youtube-skills MIT, humanizer)
e os **pipelines de produção que já existem na máquina do usuário**.

## Regra zero — nível de confiança

- **[OFICIAL]** — documentação/declarações do YouTube (Help, Creator Insider, blog).
- **[PRATICANTE]** — medido por criadores/ferramentas; não publicado pelo YouTube. Regra de bolso.
- **[ALEGADO]** — dito num vídeo/curso sem verificação independente. Trate como hipótese.

Nunca apresente [PRATICANTE]/[ALEGADO] como fato. Números exatos de "80% de retenção", "70% de hook" etc.
**não são oficiais** — o YouTube não publica limiares.

## Foco vigente (ler SEMPRE primeiro)

**Antes de qualquer tarefa, leia `config/FOCUS.md`.** Ele define o objetivo atual, o canal alvo e a métrica norte; todo comando e agente se orienta por ele. Trocar o foco (via `/dark-focus`) reorienta a skill inteira.

Estado que evolui (memória de aprendizado): `data/metrics.csv`, `data/outliers.json`, `data/learnings.md`, `data/nichos.md`.

## Como a skill se atualiza

O loop é **propose-only**: `/dark-revisar` (semanal) puxa métricas → atualiza `data/` → **propõe** mudanças com evidência. Nada em regra travada (`REGRA_METADATA_2026`, Padrões Short 2/3/4, arquivos do projeto, `FOCUS.md`) muda sem **aprovação explícita** do usuário. Promoção só com evidência e sem quebrar baseline.

## Router de referências (ler sob demanda)

| Tarefa | LER OBRIGATORIAMENTE |
|---|---|
| Metodologia geral, confiança das fontes, cobertura do PDF | `references/00-metodo-e-fontes.md` |
| Long-form: CTR/AVD/AVP, 1º minuto, 8-min, retenção, capítulos | `references/01-algoritmo-longform.md` |
| Shorts: bolhas, engaged views, swipe-away, loops, 2026 | `references/02-algoritmo-shorts.md` |
| Títulos e hooks (Y1–Y11, pairing, micro-regras) | `references/03-hooks-e-titulos.md` |
| Thumbnails: psicologia, composição, A/B, teste 120px | `references/04-thumbnails.md` |
| Arquitetura de retenção do MrBeast | `references/05-mrbeast-retention.md` |
| Estrutura por minuto (o coração do PDF) | `references/05b-estrutura-por-minuto.md` |
| Regras criativas (formatos, audiência, brand deals) | `references/05c-regras-criativas.md` |
| Disciplina de produção (solo: bottlenecks, críticos) | `references/05d-disciplina-de-producao.md` |
| Métricas e leitura de gráficos (CTR/AVD/AVP, wow) | `references/05e-metricas-e-graficos.md` |
| Storytelling de documentário (5 atos, blocos, cold open) | `references/06-storytelling-documentario.md` |
| Roteiro long-form (template, linter, regras) | `references/07-roteiro-longform.md` |
| Repurposing long-form → Shorts/TikTok/Reels | `references/08-repurposing.md` |
| Monetização + compliance (YPP, conteúdo inautêntico, IA) | `references/09-monetizacao-e-compliance.md` |
| RPM por nicho e matemática de receita | `references/10-rpm-e-nichos.md` |
| Auto-dublagem / multi-idioma | `references/11-autodub-multilingua.md` |
| Pipeline de produção + mapa para os scripts locais | `references/12-producao-pipeline.md` |
| Imagens e voz (Nano Banana/Pollinations · edge-tts/ElevenLabs) | `references/13-imagens-e-voz.md` |
| Casos reais de canais que monetizam | `references/14-casos-canais-reais.md` |
| Outliers e aprendizados (Cooper/Springfield/Yuba) | `references/15-outliers-e-aprendizados.md` |
| Trilha 0→YPP (4.000h e rota Shorts 10M) | `references/16-trilha-zero-a-ypp.md` |
| Anti-IA: tirar cara de texto gerado (humanizer) | `references/17-anti-ia.md` |
| Configurações do canal (checklist pré-publicação) | `references/18-configuracoes-canal.md` |
| Produtos digitais (tripwire $7–27, bumps, upsells) | `references/19-produtos-digitais.md` |
| Perfil de cada canal (branding, voz, calendário, status) | `references/canais/<canal>.md` |
| **Cold File Diaries — regras travadas** (PORTE, metadata, Padrões Short 2/3/4, anti-inauthentic, checklist) | `references/canais/cold-file-diaries-operacao.md` |
| Motor de monetização (funil, lives, produto, matemática até o YPP) | `references/21-motor-de-monetizacao.md` |
| Métricas via API (OAuth, queries, fallback manual) | `references/22-metricas-api.md` |
| Nichos, subnichos e **outliers** (método + monitor) | `references/23-nichos-e-outliers.md` |

Regras práticas dos vídeos-fonte: `references/20-videos-fonte.md`.

## Princípios de trabalho

1. **Embalagem antes do roteiro.** Título + thumbnail + ideia são decididos **antes** de produzir. Se o pacote não vende, a ideia morre. [PRATICANTE MrBeast/yt-master]
2. **Título e thumbnail são um par.** Nunca repetem as mesmas palavras; juntos leem em <1s. [PRATICANTE]
3. **Os primeiros 30s (ou 3s no Short) são o algoritmo real.** Sem "oi", sem logo, sem intro. Abra no meio da ação / no payoff. [OFICIAL]
4. **Retenção é o sinal mais pesado; satisfação > watch time bruto.** [OFICIAL]
5. **Shorts = aquisição; long-form = receita e profundidade.** Funil: Short → inscrito → long-form. [PRATICANTE]
6. **Formato pode repetir; substância não.** Cada vídeo precisa de pesquisa/perspectiva própria, ou cai na política de **conteúdo inautêntico**. Isso é existencial para canal dark. [OFICIAL]
7. **Escreva como uma pessoa, para uma pessoa.** Aplique as regras anti-IA (`17-anti-ia.md`) em todo texto publicável. [PRATICANTE]
8. **GATE 100%.** Sem todas as imagens prontas, não gera voz nem motion. (Regra travada dos projetos do usuário.)
9. **Deixe rastro.** Registre métricas D+2/D+7 e replique o que funcionou (outliers). [PRATICANTE]
10. **Urgência real:** o YPP **dobra** em 01/02/2027 (8.000h/20M). Priorize entrar antes. [OFICIAL]
11. **Respeite o calendário travado do canal.** No Cold File Diaries: 1 LONG (21:00 BRT) + 1 SHORT (12:00 BRT) por dia, **mesmo caso**, e a **regra rolante** de produzir o vídeo do **dia+1** — nunca abaixo de 7 agendados. Leia `canais/cold-file-diaries-operacao.md` antes de gerar título/thumb/roteiro/pacote.

## Fluxo recomendado

```
/dark-lancar  → cria/valida canal (nome, branding, calendário, settings)
/dark-focus   → define/troca o FOCO atual (canal, objetivo, métrica norte)
/dark         → ideia → título → thumb-brief → roteiro (long ou short) → checklist
/dark-build   → roda o pipeline de produção do canal alvo (imagens → voz → motion → thumbs → pacote)
/dark-audit   → gate anti-inauthentic + YPP + divulgação de IA
/dark-repurpose → fatia long-form em Shorts multi-plataforma
/dark-monetizar → trilha 0→YPP com metas e checkpoints
/dark-revisar → loop semanal: métricas → aprendizados → propõe evoluções (propose-only)
/dark-scan    → varre canais e alerta outliers (vídeos acima da baseline do canal)
```

## Subagentes

- `dark-strategist` — ideação, packaging, diagnóstico por métrica.
- `dark-roteirista` — roteiro long-form/short (5 atos + hooks + open loops).
- `dark-packager` — títulos, thumbnails, capítulos, plano de A/B.
- `dark-auditor` — gate anti-inauthentic + YPP + IA.
- `dark-produtor` — executa o pipeline (imagens/voz/motion) por canal.
- `dark-analyst` — lê métricas, cruza com o FOCUS e propõe evoluções com evidência.
- `dark-scout` — descobre nichos/subnichos/outliers de concorrentes.

## Limites

- Não edita vídeo de terceiros nem faz upload sem autorização explícita.
- Não copia o PDF do MrBeast nem transcrições integrais de terceiros para arquivos publicados — apenas parafraseia com citação.
- Reconhece as licenças das skills externas em `vendors/ATTRIBUTION.md`.
