---
name: dark-master
description: >
  Skill completa para criar, produzir e monetizar canais dark/faceless no YouTube — do zero ou já existentes.
  Use quando o usuário falar de "canal dark", "faceless", "criar canal", "pesquisar nicho", "nicho", "outliers",
  "monetizar canal", "bater 4000 horas", "10 milhões de views de Shorts", "short viral", "hook", "retenção",
  "thumbs", "organizar a pasta/canal", "nome/handle disponível", ou os comandos /dark, /dark-nicho, /dark-lancar,
  /dark-canal, /dark-organizar, /dark-build, /dark-visual, /dark-auditar, /dark-audit, /dark-scan, /dark-revisar, /dark-focus, /dark-repurpose,
  /dark-monetizar. Cobre pesquisa de nicho real, algoritmo (CTR/AVD/AVP, bolhas de Shorts, engaged views),
  hooks e títulos (Y1–Y11), hooks de Short (frame 1, arquétipos, loop), modelos de canal por nicho/subnicho,
  thumbnails e A/B, retenção do MrBeast, storytelling de documentário, repurposing,
  auto-dublagem, voz/TTS (grátis e paga: edge, kokoro, piper, ElevenLabs, Fish, Gemini, OpenAI, Azure —
  escolha, custo, licença, clonagem e QA), compliance YPP (conteúdo inautentico), RPM, monetização com produto digital e a trilha 0→YPP.
  NÃO usar para edição de vídeo comum, upload de terceiros, métricas de TikTok/Instagram, nem parecer jurídico.
metadata:
  author: Liiiraa
  version: "3.2.0"
---
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
Memória de aprendizado: banco de métricas, `data/metrics.csv`, `outliers.json`, `learnings.md`, `nichos.md`.

## Como a skill se atualiza

Loop **propose-only** diário: `/dark-revisar` cruza calendário/estoque + API + histórico → persiste telemetria/experimentos → **propõe** mudanças com evidência.
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
| **Pipeline de produção + Remotion + mapas para os scripts locais** | `references/12-producao-pipeline.md` + `references/37-remotion-pipeline.md` + `references/38-remotion-contratos.md` |
| Imagens e voz (Nano Banana/Pollinations · motor TTS) | `references/13-imagens-e-voz.md` |
| **Voz free + paga** (providers, custos, licenças, clonagem, idioma/consistência, QA) | `references/34-voz-tts.md` |
| Casos reais de canais que monetizam | `references/14-casos-canais-reais.md` |
| Loop de aprendizado (genérico) | `references/15-loop-de-aprendizado.md` |
| Trilha 0→YPP (4.000h e rota Shorts 10M) | `references/16-trilha-zero-a-ypp.md` |
| Anti-IA: tirar cara de texto gerado (humanizer) | `references/17-anti-ia.md` |
| Configurações do canal (checklist pré-publicação) | `references/18-configuracoes-canal.md` |
| Produtos digitais (tripwire $7–27, bumps, upsells) | `references/19-produtos-digitais.md` |
| Motor de monetização (funil, lives, produto, matemática) | `references/21-motor-de-monetizacao.md` |
| **Métricas via API, persistência, calendário e diagnóstico** | `references/22-metricas-api.md` + `scripts/yt_analysis.py` |
| **Pesquisa de nicho e outliers (método real)** | `references/23-nichos-e-outliers.md` |
| **Setup OAuth do YouTube (passo a passo)** | `references/24-setup-oauth-passo-a-passo.md` |
| **Entender o canal** (convenções + corrente de teaser) | `references/25-contexto-do-canal.md` |
| **Organização de arquivos e do PC** | `references/26-organizacao-e-arquivos.md` |
| **Nomes e handles (disponibilidade)** | `references/27-nomes-e-handles.md` |
| **Auditorias automáticas (todos os gates)** | `references/28-auditorias.md` |
| **Prompts de imagem + scaffolding de vídeo** | `references/29-prompts-de-imagem.md` |
| **Sistema de roteiro (master)** | `references/30-roteiro-master.md` |
| **Hooks de Short (frame 1, arquétipos, loop)** | `references/31-hooks-short.md` |
| **Branding do canal (logo/banner/profile/watermark)** | `references/32-branding-canal.md` |
| **Versionamento do canal (git sem mídia) + Notion** | `references/33-versionamento-e-notion.md` |
| **Cronologia e linha do tempo (roteiro + edição)** | `references/35-cronologia-e-timeline.md` |
| **Contrato de pesquisa, claims, mapa semântico, duração real e funil Short→Long** | `references/36-pesquisa-claims-e-funil.md` + `scripts/timing_audit.py` |
| **Modelos de canal por nicho/subnicho (38, com evidência real)** | `models/README.md` + `models/<slug>/` |
| Perfil/operação/outliers de um canal específico | `playbooks/<canal>/` |

## Princípios de trabalho

1. **Embalagem antes do roteiro.** Título + thumb + ideia decididos antes de produzir. [PRATICANTE]
2. **Título e thumbnail são um par.** Nunca repetem palavras. [PRATICANTE]
3. **Primeiros 30s (ou 3s no Short) são o algoritmo real.** Sem intro. [OFICIAL]
4. **Retenção é o sinal mais pesado; satisfação > watch time bruto.** [OFICIAL]
5. **Shorts = aquisição; long-form = valor e retenção.** O Short é um roteiro separado, não um corte do long; o funil usa uma claim verificada, uma ponte e um loop. [PRATICANTE]
6. **Formato pode repetir; substância não.** Ou cai na política de **conteúdo inautêntico**. Existencial para canal dark. [OFICIAL]
7. **Escreva como uma pessoa.** Aplique o anti-IA (`17`). [PRATICANTE]
8. **GATE 100% (motion).** Sem todas as imagens, não gera **motion**; a **voz sai no scaffold** (depende só da narração + fatos aprovados).
9. **Remotion é o renderer visual canônico, não o dono do roteiro.** `dark-artdirector` cria a Visual Bible e o `RENDER_PLAN`; `dark-produtor` executa; `dark-visual-reviewer` aprova de forma independente. FFmpeg não cria visuals de novos episódios; fica só em encode/mux e derivados declarados.
10. **Deixe rastro.** Registre D+2/D+7 e replique outliers. [PRATICANTE]
11. **Urgência:** o YPP **dobra** em 01/02/2027 (8.000h/20M). [OFICIAL]
12. **Pesquisa antes de produzir.** Nicho se decide por **evidência de canal** (gates rígidos), não por lista pronta (`23`).
13. **Canal novo ≠ clone.** Não importe decisões de um playbook; defina as suas (`playbooks/README.md`).
14. **Entenda o canal antes de gerar.** Rode `channel_scan.py`, respeite calendário e **corrente de teaser** (`25`).
15. **Mantenha a casa organizada.** Rode `channel_organize.py` (dry-run → aplicar) e siga a estrutura padrão (`26`).
16. **Formato é decisão, não regra.** Short, long ou ambos dependem do **lane** do canal (`FOCUS.md` + `23`) — **não** assuma short+long sempre.
17. **Roteiro sempre com pesquisa rastreável.** Use `dark-researcher` e `dark-scout`, preencha `PESQUISA_BRIEF.md`, `PESQUISA_FONTE.md`, `CLAIMS.json` e `LINHA_DO_TEMPO.md` antes de escrever; o gate estrito não aceita placeholders (`30`, `36`).
18. **Short se ganha no frame 1.** Texto na tela (≤6 palavras) + fala ≤8 palavras nos 3s; uma ideia, payoff, loop visual/sonoro e bridge independente para o long (`31`, `36`).
19. **Modelo antes do canal.** Escolha um blueprint validado em `models/` e revalide com dados frescos (`23`) — modelo não é clone de playbook.
20. **Telemetria antes de palpite.** Toda conclusão mostra período, denominador, baseline, amostra, contraevidência e limitações; dado ausente é desconhecido.
21. **Produção é consequência do diagnóstico.** `/dark-revisar` cruza `videoNN` com calendário, estoque, teaser e regras; ele propõe, não reescreve.
22. **Motion design não é poster animado.** Cada cena não estática precisa evoluir em estados visuais; zoom/fade isolados, repetição de layout e transição genérica reprovam no QA. `references/37-remotion-pipeline.md` exige assets/camadas por estado, movimento por alvo e auditoria semântica anti-slideshow.

## Fluxo canônico de produção

```text
canal existente:Sem exigir nicho/outlier
canal novo:nicho → outlier
→ research → script → art direction → image prompts → assets
→ motion prompts → Remotion → QA
→ receipt visual independente → render final → auditoria
```

O planner falha closed em research/map/claims, shot specs, prompt plan READY, manifest, image audit, direitos, assets bloqueados, captions/timing, áudio quando o lane exigir, Visual Profile e review. `--allow-incomplete` é somente diagnóstico e nunca libera render. O escopo visual vive no episódio, separado do canal, e não copia identidade.

## Fluxo recomendado

```
canal existente: /dark-canal → /dark-focus → /dark
canal novo: /dark-nicho → /dark-lancar → /dark-focus → /dark
/dark → research → script → art direction → image prompts → assets
     → motion prompts → /dark-visual → /dark-build → /dark-auditar
```

`/dark-auditar` inclui o gate closed de Remotion, receipt independente, run ledger e auditoria final; métricas e outliers só entram quando explicitamente solicitados.

## Subagentes

- `dark-scout` — **pesquisa real** de nichos/subnichos/outliers (web + API + Trends/Reddit).
- `dark-researcher` — brief de pesquisa de um caso/tema (fatos, fontes, ângulos, contradições).
- `dark-roteirista` — roteiro long-form/short (beats, orçamento, anti-IA).
- `dark-packager` — títulos, thumbnails, capítulos, A/B.
- `dark-artdirector` — Visual Bible, direção de cenas, assets e iteração visual.
- `dark-visual-reviewer` — revisão independente de stills, frames, motion e acabamento.
- `dark-auditor` — gate anti-inauthentic + YPP + IA.
- `dark-produtor` — executa o pipeline por canal.
- `dark-analyst` — métricas, funil, calendário e aprendizado com evidência.

## Limites

- Não edita vídeo de terceiros nem faz upload sem autorização explícita.
- Não apaga arquivos do usuário (organização é move-only, com dry-run).
- Não copia o PDF do MrBeast nem transcrições integrais — parafraseia com citação.
- Licenças externas em `vendors/ATTRIBUTION.md`.
