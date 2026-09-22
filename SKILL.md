---
name: dark-master
description: >
  Skill completa para criar, produzir e monetizar canais dark/faceless no YouTube — do zero ou já existentes.
  Use quando o usuário falar de "canal dark", "faceless", "criar canal", "pesquisar nicho", "nicho", "outliers",
  "monetizar canal", "bater 4000 horas", "10 milhões de views de Shorts", "short viral", "hook", "retenção",
  "thumbs", "organizar a pasta/canal", "nome/handle disponível", ou os comandos /dark, /dark-nicho, /dark-lancar,
  /dark-canal, /dark-organizar, /dark-build, /dark-audit, /dark-scan, /dark-revisar, /dark-focus, /dark-repurpose,
  /dark-monetizar. Cobre pesquisa de nicho real, algoritmo (CTR/AVD/AVP, bolhas de Shorts, engaged views),
  hooks e títulos (Y1–Y11), hooks de Short (frame 1, arquétipos, loop), modelos de canal por nicho/subnicho,
  thumbnails e A/B, retenção do MrBeast, storytelling de documentário, repurposing,
  auto-dublagem, compliance YPP (conteúdo inautentico), RPM, monetização com produto digital e a trilha 0→YPP.
  NÃO usar para edição de vídeo comum, upload de terceiros, métricas de TikTok/Instagram, nem parecer jurídico.
metadata:
  author: Liiiraa
  version: "3.1.0"
---

# dark-master

Skill-mãe para **criar, produzir e monetizar** canais **dark/faceless** no YouTube. Funde o conhecimento oficial/dados 2026,
metodologias destiladas (MrBeast, yt-master, youtube-skills MIT, humanizer), **pesquisa de nicho real** e os
**pipelines de produção** que já existem na máquina do usuário.

## Entrada — sempre pergunte

**Antes de tudo, descubra:** é um **canal NOVO** ou **EXISTENTE**?
- **Novo** → `/dark-lancar` + `/dark-nicho` (pesquisa real de nicho) + `/dark-focus`.
- **Existente** → `/dark-canal` (entende o projeto) + carregue o **playbook** do canal.

Se não estiver claro, **pergunte**. Não assuma um canal.

## Regra zero — nível de confiança

- **[OFICIAL]** — documentação/declarações do YouTube.
- **[PRATICANTE]** — medido por criadores/ferramentas; não publicado pelo YouTube.
- **[ALEGADO]** — dito em vídeo/curso sem verificação. Hipótese.

Nunca apresente [PRATICANTE]/[ALEGADO] como fato. O YouTube **não publica** limiares como "80% de retenção".

## Foco vigente (ler SEMPRE primeiro)

Leia `config/FOCUS.md` — objetivo atual, canal alvo e métrica norte. Trocar via `/dark-focus`.
Memória de aprendizado: `data/metrics.csv`, `outliers.json`, `learnings.md`, `nichos.md`.

## Como a skill se atualiza

Loop **propose-only**: `/dark-revisar` puxa métricas → atualiza `data/` → **propõe** mudanças com evidência.
Regra travada **só muda com aprovação explícita**. Promoção só com evidência e sem quebrar baseline.

## Playbooks (casos de estudo — NÃO são regras gerais)

`playbooks/<canal>/` guarda perfil, operação e outliers de canais reais. Servem como **caso de estudo e engine de produção**.
**Canal novo ≠ clone de um playbook** — não importe voz, séries, metadata, padrões de Short ou branding.
Ver `playbooks/README.md`.

## Router de referências (ler sob demanda)

| Tarefa | LER OBRIGATORIAMENTE |
|---|---|
| Metodologia geral, confiança das fontes, cobertura do PDF | `references/00-metodo-e-fontes.md` |
| Long-form: CTR/AVD/AVP, 1º minuto, 8-min, retenção, capítulos | `references/01-algoritmo-longform.md` |
| Shorts: bolhas, engaged views, swipe-away, loops, 2026 | `references/02-algoritmo-shorts.md` |
| Títulos e hooks (Y1–Y11, pairing, micro-regras) | `references/03-hooks-e-titulos.md` |
| Thumbnails: psicologia, composição, A/B, teste 120px | `references/04-thumbnails.md` |
| MrBeast: retenção, por minuto, criativo, produção, métricas | `references/05*.md` |
| Storytelling de documentário (5 atos, blocos, cold open) | `references/06-storytelling-documentario.md` |
| Roteiro long-form (template, linter, regras) | `references/07-roteiro-longform.md` |
| Repurposing long-form → Shorts/TikTok/Reels | `references/08-repurposing.md` |
| Monetização + compliance (YPP, conteúdo inautêntico, IA) | `references/09-monetizacao-e-compliance.md` |
| RPM por nicho e matemática de receita | `references/10-rpm-e-nichos.md` |
| Auto-dublagem / multi-idioma | `references/11-autodub-multilingua.md` |
| Pipeline de produção + mapas para os scripts locais | `references/12-producao-pipeline.md` |
| Imagens e voz (Nano Banana/Pollinations · edge-tts/ElevenLabs) | `references/13-imagens-e-voz.md` |
| Casos reais de canais que monetizam | `references/14-casos-canais-reais.md` |
| Loop de aprendizado (genérico) | `references/15-loop-de-aprendizado.md` |
| Trilha 0→YPP (4.000h e rota Shorts 10M) | `references/16-trilha-zero-a-ypp.md` |
| Anti-IA: tirar cara de texto gerado (humanizer) | `references/17-anti-ia.md` |
| Configurações do canal (checklist pré-publicação) | `references/18-configuracoes-canal.md` |
| Produtos digitais (tripwire $7–27, bumps, upsells) | `references/19-produtos-digitais.md` |
| Motor de monetização (funil, lives, produto, matemática) | `references/21-motor-de-monetizacao.md` |
| Métricas via API (OAuth, queries, fallback) | `references/22-metricas-api.md` |
| **Pesquisa de nicho e outliers (método real)** | `references/23-nichos-e-outliers.md` |
| **Setup OAuth do YouTube (passo a passo)** | `references/24-setup-oauth-passo-a-passo.md` |
| **Entender o canal** (convenções + corrente de teaser) | `references/25-contexto-do-canal.md` |
| **Organização de arquivos e do PC** | `references/26-organizacao-e-arquivos.md` |
| **Nomes e handles (disponibilidade)** | `references/27-nomes-e-handles.md` |
| **Auditorias automáticas (todos os gates)** | `references/28-auditorias.md` |
| **Prompts de imagem + scaffolding de vídeo** | `references/29-prompts-de-imagem.md` |
| **Sistema de roteiro (master)** | `references/30-roteiro-master.md` |
| **Hooks de Short (frame 1, arquétipos, loop)** | `references/31-hooks-short.md` |
| **Modelos de canal por nicho/subnicho (38, com evidência real)** | `models/README.md` + `models/<slug>/` |
| Perfil/operação/outliers de um canal específico | `playbooks/<canal>/` |

## Princípios de trabalho

1. **Embalagem antes do roteiro.** Título + thumb + ideia decididos antes de produzir. [PRATICANTE]
2. **Título e thumbnail são um par.** Nunca repetem palavras. [PRATICANTE]
3. **Primeiros 30s (ou 3s no Short) são o algoritmo real.** Sem intro. [OFICIAL]
4. **Retenção é o sinal mais pesado; satisfação > watch time bruto.** [OFICIAL]
5. **Shorts = aquisição; long-form = receita.** Funil Short → inscrito → long-form. [PRATICANTE]
6. **Formato pode repetir; substância não.** Ou cai na política de **conteúdo inautêntico**. Existencial para canal dark. [OFICIAL]
7. **Escreva como uma pessoa.** Aplique o anti-IA (`17`). [PRATICANTE]
8. **GATE 100%.** Sem todas as imagens, não gera voz/motion.
9. **Deixe rastro.** Registre D+2/D+7 e replique outliers. [PRATICANTE]
10. **Urgência:** o YPP **dobra** em 01/02/2027 (8.000h/20M). [OFICIAL]
11. **Pesquisa antes de produzir.** Nicho se decide por **evidência de canal** (gates rígidos), não por lista pronta (`23`).
12. **Canal novo ≠ clone.** Não importe decisões de um playbook; defina as suas (`playbooks/README.md`).
13. **Entenda o canal antes de gerar.** Rode `channel_scan.py`, respeite calendário e **corrente de teaser** (`25`).
14. **Mantenha a casa organizada.** Rode `channel_organize.py` (dry-run → aplicar) e siga a estrutura padrão (`26`).
15. **Formato é decisão, não regra.** Short, long ou ambos dependem do **lane** do canal (`FOCUS.md` + `23`) — **não** assuma short+long sempre.
16. **Roteiro sempre com pesquisa.** Use os subagentes (`dark-researcher`, `dark-scout`) e combine num brief antes de escrever; anti-IA e 1 peça de pesquisa primária por vídeo (`30`).
17. **Short se ganha no frame 1.** Texto na tela (≤6 palavras) + fala ≤8 palavras nos 3s; loop projetado (AVP >100%). (`31`)
18. **Modelo antes do canal.** Escolha um blueprint validado em `models/` e revalide com dados frescos (`23`) — modelo não é clone de playbook.

## Fluxo recomendado

```
/dark-nicho   → pesquisa/valida NICHOS reais (discover/verify) com gates
/dark-lancar  → cria canal do zero (nome, branding, calendário, settings)
/dark-organizar → organiza a pasta do canal (dry-run → aplicar) + nomes/handles
/dark-canal   → entende um canal existente (projeto, regras, corrente de teaser)
/dark-focus   → define/troca o foco (canal, objetivo, métrica norte)
/dark         → ideia → título → thumb → roteiro → checklist
/dark-roteiro → gera/valida o roteiro (plano com beats, orçamento e compliance)
/dark-build   → roda o pipeline de produção do canal alvo
/dark-auditar → auditoria completa (imagens + áudio + legendas + pacote) + compliance
/dark-audit   → gate anti-inauthentic + YPP + IA
/dark-repurpose → fatia long-form em Shorts multi-plataforma
/dark-monetizar → trilha 0→YPP com metas e checkpoints
/dark-revisar → loop semanal de métricas e evolução (propose-only)
/dark-scan    → varre canais e alerta outliers
```

## Subagentes

- `dark-scout` — **pesquisa real** de nichos/subnichos/outliers (web + API + Trends/Reddit).
- `dark-researcher` — brief de pesquisa de um caso/tema (fatos, fontes, ângulos, contradições).
- `dark-roteirista` — roteiro long-form/short (beats, orçamento, anti-IA).
- `dark-packager` — títulos, thumbnails, capítulos, A/B.
- `dark-auditor` — gate anti-inauthentic + YPP + IA.
- `dark-produtor` — executa o pipeline por canal.
- `dark-analyst` — métricas → evolução com evidência.

## Limites

- Não edita vídeo de terceiros nem faz upload sem autorização explícita.
- Não apaga arquivos do usuário (organização é move-only, com dry-run).
- Não copia o PDF do MrBeast nem transcrições integrais — parafraseia com citação.
- Licenças externas em `vendors/ATTRIBUTION.md`.
