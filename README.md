<div align="center">

# dark-master

**A skill que transforma canais dark/faceless em negócio no YouTube.**

Algoritmo, roteiro, thumbnails, Shorts, outliers, monetização e auto-evolução — com dados reais.

[![Site](https://img.shields.io/badge/site-dark--master.vercel.app-B91C1C?style=flat-square)](https://dark-master.vercel.app/)
[![Next.js](https://img.shields.io/badge/Next.js-15-000?style=flat-square&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-000?style=flat-square&logo=react)](https://react.dev/)
[![Python](https://img.shields.io/badge/Python-3.12-000?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-B91C1C?style=flat-square)](LICENSE)

</div>

---

## O que é

**dark-master** é uma skill para o [opencode](https://opencode.ai) que reúne, num único sistema:

- o **algoritmo do YouTube** (Shorts e long-form), validado por dados de 2026;
- o **guia de produção do MrBeast**, destilado e adaptado a operador solo;
- um **motor de dados** que puxa métricas reais via API e **propõe melhorias**;
- e a ligação aos **pipelines de produção** de canais dark que já existem na sua máquina.

Ela não "chuta": lê o seu canal, respeita o calendário e as regras travadas, produz e aprende com o resultado.

> **Site:** https://dark-master.vercel.app/ · **Privacidade:** https://dark-master.vercel.app/privacy

---

## Destaques

- **Embalagem antes do roteiro** — título + thumbnail + ideia decididos antes de produzir.
- **Shorts com loop** — engenharia de retenção (AVP > 100%) e funil para o long-form.
- **Cérebro de algoritmo** — bolhas de Shorts, CTR/AVD/AVP, 1º minuto, capítulos, compliance YPP.
- **Anti-inautenticidade** — variação obrigatória por vídeo, humanizer (25 tells de IA), disclosо de IA.
- **38 modelos de canal** — blueprints por nicho/subnicho com gates, outliers, hooks, beats e monetização, validados com dados reais.
- **Shorts de engenharia** — hook de 3s (frame 1 + texto na tela), 14 arquétipos, loop (AVP >100%) e validação automática.
- **Auto-evolução** — `/dark-revisar` puxa métricas, detecta outliers e propõe mudanças com evidência.
- **Entende o canal** — lê calendário, regras travadas e a **corrente de teaser** antes de gerar.
- **Multi-idioma** — auto-dublagem e títulos/descrições traduzidos.
- **Seguro** — segredos fora do repositório; o token só acessa **leitura** do seu canal.

---

## Estrutura do repositório

```
dark-master/
├─ SKILL.md                     # entrada da skill (router + princípios)
├─ references/                  # 36 referências (algoritmo, roteiro, monetização…)
│  ├─ 05…05e*                   # MrBeast: retenção, por minuto, criativo, produção, métricas
│  ├─ 09-monetizacao-e-compliance.md
│  ├─ 21-motor-de-monetizacao.md
│  ├─ 22-metricas-api.md
│  ├─ 23-nichos-e-outliers.md
│  ├─ 24-setup-oauth-passo-a-passo.md
│  ├─ 25-contexto-do-canal.md
│  ├─ 26-organizacao-e-arquivos.md
│  ├─ 27-nomes-e-handles.md
│  ├─ 30-roteiro-master.md      # sistema de roteiro (pesquisa + beats + orçamento)
│  └─ 31-hooks-short.md         # hooks de Short (frame 1, arquétipos, loop)
├─ models/                      # 38 modelos de canal por nicho/subnicho (com evidência real)
├─ playbooks/                   # casos de estudo por canal (não são regras gerais)
│  ├─ cold-file-diaries/        # profile, operacao, outliers
│  └─ financial-crime-files/ · laudo-final/ · midnight-archive/
├─ config/FOCUS.md              # objetivo atual (manda em tudo)
├─ data/                        # metrics.csv, outliers.json, learnings.md, nichos.md
├─ assets/                      # templates (roteiro, thumb, pacote, hook factory)
├─ scripts/                     # yt_auth, yt_metrics, yt_scan_outliers, yt_db, channel_scan…
├─ site/                        # landing (Next.js) — deploy Vercel
├─ docs/                        # redirect do GitHub Pages → Vercel
└─ vendors/                     # skills MIT + atribuições (não versionado)
```

---

## Comandos

| Comando | O que faz |
|---|---|
| `/dark-nicho` | Pesquisa e valida **nichos reais** (discover/verify) com gates rígidos. |
| `/dark-lancar` | Lança um canal do zero (nome, branding, calendário, settings). |
| `/dark-organizar` | Organiza a pasta do canal (dry-run → aplicar) e checa nomes/handles. |
| `/dark-canal` | Entende um canal existente: projeto, regras e corrente de teaser. |
| `/dark` | Ideia → título → thumb → roteiro → checklist. |
| `/dark-roteiro` | Gera/valida o roteiro: plano com beats, orçamento e compliance. |
| `/dark-build` | Roda o pipeline de produção do canal alvo. |
| `/dark-auditar` | Auditoria completa: imagens + áudio + legendas + pacote + compliance. |
| `/dark-audit` | Gate anti-inauthentic + YPP + divulgação de IA. |
| `/dark-scan` | Varre canais e alerta outliers acima da baseline. |
| `/dark-revisar` | Loop semanal: métricas → aprendizados → propostas. |
| `/dark-focus` | Define/troca o foco (canal, objetivo, métrica norte). |
| `/dark-repurpose` | Fatia long-form em Shorts multi-plataforma. |
| `/dark-monetizar` | Trilha 0→YPP com metas e checkpoints. |

## Subagentes

`dark-scout` · `dark-researcher` · `dark-roteirista` · `dark-strategist` · `dark-packager` · `dark-auditor` · `dark-produtor` · `dark-analyst`

## Scripts

| Script | Função |
|---|---|
| `yt_auth.py` | OAuth do YouTube (uma vez). |
| `new_video.py` | Cria a pasta padrão de um vídeo (scaffold). |
| `script_builder.py` | Gera o plano de roteiro (beats/orçamento), valida long **e Short** e gera variações de hook. |
| `prompt_builder.py` | Gera os prompts de imagem (consistentes) e pode renderizar. |
| `yt_metrics.py` | Puxa métricas por vídeo → banco + CSV. |
| `yt_scan_outliers.py` | Detecta outliers (vídeos ≥ N× a mediana do canal). |
| `niche_scan.py` | Pesquisa em tempo real: `--brief` (gates+outliers), `--cluster` (fome cross-canal), `--comments`, `--suggest`, `--trends`. |
| `image_audit.py` | Audita imagens geradas (resolução, aspecto, brilho, duplicatas) + contact sheet. |
| `audio_audit.py` | Audita voz: loudness (LUFS), true peak, clipping, silêncios longos. |
| `captions_audit.py` | Audita SRT/VTT: cues, sobreposição, CPS, cobertura vs áudio. |
| `audit_all.py` | Orquestra todas as auditorias e dá o veredito por vídeo. |
| `channel_organize.py` | Organiza a pasta do canal (dry-run → aplicar). |
| `name_check.py` | Checa disponibilidade de nome/handle. |
| `yt_db.py` | Camada de dados (Neon Postgres ou SQLite). |
| `channel_scan.py` | Lê o projeto do canal e a corrente de teaser. |
| `audit-ypp.py` | Checklist do gate YPP. |
| `lint-roteiro.py` | Lint anti-IA/compliance no roteiro. |
| `title-check.py` | Sinais heurísticos de título. |
| `ctr-baseline.py` | CTR vs baseline. |

---

## Começando

### 1. Instalar a skill (opencode)

Copie/symlink esta pasta para:

```bash
# global (disponível em todo projeto)
~/.config/opencode/skills/dark-master

# ou ver ~/.config/opencode/opencode.json -> skills.paths
```

Reinicie o opencode. Depois use `/dark-canal` ou `/dark`.

### 2. Conectar as métricas (opcional, recomendado)

```bash
python -m pip install google-api-python-client google-auth-oauthlib
python scripts/yt_db.py doctor       # testa o banco (Neon/SQLite)
python scripts/yt_auth.py            # OAuth (abre o navegador)
python scripts/yt_metrics.py         # puxa métricas
python scripts/yt_scan_outliers.py --watch
```

Passo a passo completo em [`references/24-setup-oauth-passo-a-passo.md`](references/24-setup-oauth-passo-a-passo.md).

### 3. Definir o foco

Edite `config/FOCUS.md` (ou rode `/dark-focus`) para apontar o objetivo, o canal e a métrica norte.

---

## Banco de dados

Usa **Neon Postgres** quando `DATABASE_URL` está definida; senão cai para **SQLite** local (`data/dark.db`). Tabelas: `snapshots`, `outliers`, `learnings`. A camada é agnóstica de backend.

```
DATABASE_URL=postgresql://…   # em ~/.config/opencode/secrets/dark.env
```

## Segurança

- `client_secrets.json`, `yt-token.json` e `dark.env` ficam em `~/.config/opencode/secrets/` — **fora do repositório**.
- Escopos **somente leitura**; o token não publica nem altera nada.
- `.gitignore` protege `vendors/*/` e `data/dark.db`.

---

## Site (Next.js)

```bash
cd site
npm install
npm run dev      # http://localhost:3000
npm run build    # produção
```

Animado com Framer Motion (canvas, cursor, scroll reveals, contadores), **tema claro/escuro** e **i18n PT/EN**.
Deploy automático no **Vercel** a cada push na `master` (Root Directory = `site`).

---

## Roadmap

- [x] Modelos de canal por nicho/subnicho (38, com validação real via Data API)
- [x] Roteiro com pesquisa assistida (subagentes + `script_builder` + lint anti-IA)
- [x] Sistema de Shorts (frame 1, arquétipos, loop) + validação automática
- [ ] Completar `--comments` (rodar `yt_auth.py` com escopo force-ssl)
- [ ] Painel de métricas (dashboard) além do CLI
- [ ] Suporte a mais idiomas na narração

## Contribuindo

Abra uma issue ou PR. Mantenha os selos de confiança nas referências (`[OFICIAL]` / `[PRATICANTE]` / `[ALEGADO]`) e não versione segredos.

## Licença

MIT. As skills externas estão creditadas em [`vendors/ATTRIBUTION.md`](vendors/ATTRIBUTION.md).

<div align="center"><sub>Construído para canais dark que querem virar negócio.</sub></div>
