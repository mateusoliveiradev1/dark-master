# 15 — Loop de aprendizado (genérico)

Como a skill aprende com o resultado de **qualquer** canal. Os dados reais de um canal específico ficam no playbook dele (`playbooks/<canal>/outliers.md`).

## O ciclo

```
publicar → medir (D+2 / D+7 / D+30) → comparar com a baseline → extrair padrão → replicar/testar
```

1. **Medir** — `/dark-revisar` puxa métricas e grava em `data/` (banco + CSV).
2. **Comparar** — sempre contra a **baseline do próprio canal**, nunca benchmark universal.
3. **Extrair** — o que o outlier tem que os outros não têm? (hook, tema, formato, thumb, timing)
4. **Registrar** — `data/learnings.md` com **evidência**.
5. **Testar** — 1 variável por vez nos próximos 4–6 vídeos.

## Outliers

- **Outlier** = vídeo que bate a própria baseline (≥3×; ≥5× forte; ≥10× flare).
- Alerta automático: `scripts/yt_scan_outliers.py --watch`.
- Extraia a **estrutura transferível**, não o conteúdo.

## Loop D+2/D+7

| Janela | O que olhar | Ação |
|---|---|---|
| D+2 | views, "chose to view", AVD | consertar hook se swipe alto |
| D+7 | retenção, inscritos, watch time | ajustar corpo/payoff |
| D+30 | cauda longa, back catalog | replicar padrão vencedor |

## Registro (evidência > opinião)

Só entra em `data/learnings.md` o que tiver dado ou teste documentado. Propostas de mudança de **regra travada** vão por `/dark-revisar` e exigem aprovação.

## Anti-padrões

- Concluir com amostra pequena (1 vídeo).
- Mudar 5 variáveis de uma vez.
- Comparar com canal grande (baseline errada).
- Ignorar o que **não** funcionou.

## Casos de estudo

Dados reais e lições por canal ficam em `playbooks/<canal>/outliers.md` (ex.: `playbooks/cold-file-diaries/outliers.md`).
