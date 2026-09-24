# 00 — Método e fontes

Como esta skill pensa, de onde vem cada afirmação e como usar os selos de confiança.

## Selos de confiança

- **[OFICIAL]** — YouTube Help, Creator Insider, blog do YouTube, documentação de monetização.
- **[PRATICANTE]** — medido por criadores/ferramentas de terceiros; não é publicado pelo YouTube.
- **[ALEGADO]** — afirmado em vídeo/curso sem verificação. Hipótese, não fato.

Nunca trate [PRATICANTE] ou [ALEGADO] como verdade. Use como heurística e valide com os dados do próprio canal.

## Fontes primárias

1. **Guia de produção do MrBeast** ("How To Succeed In MrBeast Production") — parafraseado. Cobre CTR/AVD/AVP, estrutura por minuto, formatos, disciplina de produção.
2. **Vídeo "Por que seus Shorts travam em 1.000 views"** (canal O Milionário) — bolhas, VTR/HCR/RPR/CTR-perfil, cenários de explosão. [ALEGADO, com partes alinhadas ao oficial]
3. **Pesquisa oficial/2026** — Creator Insider (set/2026), políticas de monetização, auto-dublagem (fev/2026), RPM, inauthentic content (jul/2025 e jul/2026).
4. **Vídeos-fonte do usuário** — ver `20-videos-fonte.md`.
5. **Skills externas MIT** — ver `vendors/ATTRIBUTION.md`.

## Correções importantes vs. o vídeo de Shorts

O vídeo-fonte afirma coisas úteis mas imprecisas. A skill corrige:

| Alegação do vídeo | Realidade |
|---|---|
| "As 3 primeiras horas decidem" | YouTube continua testando por **semanas**; muitos vídeos pegam a maior parte das views 1 mês depois. [OFICIAL] |
| "Retenção >80%", "hook >70%", "RPR 15–25%" | Não existe limiar oficial. São regras de bolso. [PRATICANTE] |
| "Inscritos ajudam no Shorts" | A maioria das views de Shorts vem de **não-inscritos**; <10% dos inscritos clicam. [OFICIAL] |
| "Descobri com gerentes do YouTube" | Não verificável. [ALEGADO] |
| "Bolha 1 = 300–2.000 pessoas" | Mapeia ao modelo oficial **explore/exploit** (seed audience → expansão). O número exato é alegado. |

## Como usar a skill na prática

1. Identifique a tarefa e siga o router do `SKILL.md`.
2. Leia as referências exigidas **antes** de gerar saída.
3. Sempre que citar número, mantenha o selo.
4. Para material de caso, use o contrato de `36`: `PESQUISA_BRIEF.md`, source ledger, `CLAIMS.json` e `LINHA_DO_TEMPO.md`; não confie em um briefing textual sem IDs.
4. Antes de publicar, rode o gate: `dark-auditor` (anti-inauthentic) + `18-configuracoes-canal.md`.
5. Registre o resultado em `15-loop-de-aprendizado.md`.

## Cobertura do PDF do MrBeast

O guia de produção foi mapeado **seção por seção** para a skill. Índice fiel: `vendors/mrbeast-source-index.md`. Destinos:

| Parte do PDF | Onde está na skill |
|---|---|
| Front matter (regras, players, results>horas) | `05d` |
| Cap. 1 — CTR/AVD/AVP, 1º min, "1 out of 10", wow factor | `05e` + `01` |
| Cap. 1 — linha do tempo (1–3, 3–6, back half, minute mark) | `05b` |
| Cap. 2 — creating content (bottlenecks, críticos, consultores, comunicação) | `05d` |
| Cap. 3 — creative (formatos, audiência, dieta, brand deals, rapid-fire) | `05c` |
| Cap. 4 — carreira | `05d` |
| Formatos (last-to-leave, stair-stepping, chase) | `05c` + `06` |
| Re-engagements 3min/6min + escalada | `05` + `05b` |

Inaplicável a canal dark solo (não entra): gestão de 200+ funcionários, Beast Burger/Feastables, rede de dublagem própria — apenas a lição é adaptada.

## Referências de apoio (diretórios relevantes na máquina)
- Skills: `~/.config/opencode/skills/` (`yt-master`, `faceless-video`, `media-pipeline`).
- Projetos do usuário:
  - `C:\Users\Liiiraa\Downloads\canal dark1` (Cold File Diaries)
  - `C:\Users\Liiiraa\Downloads\The-money-files` (Financial Crime Files)
  - `D:\dark-forense` (Laudo Final)
  - `C:\Users\Liiiraa\Downloads\canal-dark` (The Midnight Archive — biblioteca de código)
