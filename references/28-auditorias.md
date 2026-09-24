# 28 — Auditorias automáticas (todos os gates)

Nada sobe sem passar pelos gates. Cada script sai com **código 1 se falhar** (dá pra usar em CI).

## Orquestrador

```bash
python scripts/orchestrate.py plan --root "<canal>" --episode videoNN --channel-state existing
python scripts/orchestrate.py plan --root "<canal>" --episode videoNN --channel-state new
python scripts/audit_all.py "<videoNN>"            # um vídeo
python scripts/audit_all.py "<pasta do canal>"     # varre todos os videoNN
python scripts/audit_all.py "<videoNN>" --json     # saída para máquina
```

Para canal existente, o orquestrador não exige nicho/outlier. Para canal novo, ambos permanecem etapas explícitas. O escopo visual é isolado do canal e nunca copia identidade. A auditoria final exige o mesmo `runId`/`planHash` em todos os outputs e não aceita review ausente, divergente ou sem receipt independente.

## Gates

| Gate | Script | Verifica |
|---|---|---|
| **Imagens** | `image_audit.py` | resolução, aspecto 16:9, tamanho, brilho/desvio (imagem quase sólida), saturação, **duplicatas** + contact sheet |
| **Manifest de assets** | `asset_manifest.py` | cada prompt tem asset por identidade; hash, direitos e `blocked` são closed gates |
| **Planner closed** | `remotion.py plan` | research/map/claims, shot specs, prompt READY, manifest, image audit, captions/timing, voice/audio quando exigido e visual profile |
| **Staging/run** | `remotion.py` + `run_ledger.py` | staging isolado por run/hash, somente assets do ledger, `run.json` append-only e hashes |
| **Review independiente** | `visual_review.py` | F0/F50/F100, contact sheet por cena/sequência, derivados 120px quando ffmpeg existe e receipt com score/findings/`planHash` |
| **Pesquisa de título** | `title_research.py` | candidatos, fórmula, overlap com histórico e decisão humana; não infere demanda |
| **Rotação editorial** | `rotation_audit.py` | título, hook, sequência de beats e CTA contra os três episódios anteriores |
| **Áudio/voz** | `audio_audit.py` | duração, sample rate/canais, **loudness (LUFS)**, **true peak**, LRA, **clipping**, **silêncios longos** |
| **Legendas** | `captions_audit.py` | nº de cues, 1ª perto de 0:00, duração por cue, **sobreposições**, gaps, linhas/chars, **velocidade de leitura (CPS)**, cobertura vs áudio |
| **Pacote** | (presença) | `youtube_package.txt` / `PACOTE_PUBLICACAO.txt` |
| **Final** | `remotion.py audit` + `audit_all.py` | output, report, staging, run e receipt do mesmo `RenderPlan` |
| **Remotion** | `remotion.py audit` | RENDER_PLAN, RENDER_REPORT, duração, output e paths rastreáveis |
| **Visual** | `dark-visual-reviewer` | hierarquia, crop, safe area, captions, repetição, motion, pacing e score mínimo 92 |
| **Compliance/YPP** | `audit-ypp.py` | conteúdo inautêntico, gore, IA, etc. (`references/09`) |

`audit_all.py` consome `TITLE_RESEARCH.json`, `ROTATION_AUDIT.json` e `PROMPT_STATUS.json` quando eles existem. `INCONCLUSIVO` fica visível sem liberar motion; `FAIL` bloqueia. Rode os três pelo fluxo de `30-roteiro-master.md` antes da auditoria final.

## Alvos por canal

- **Áudio:** loudness alvo do projeto (ex.: `-16` ou `-14` LUFS), true peak ≤ **-1 dBTP**, LRA < 14.
- **Legendas:** 42 chars / 2 linhas; CPS ≤ 21; sem sobreposição; cobertura ≥ 90%.
- **Imagens:** ≥1280px de largura; aspecto 16:9; ≥50KB; sem duplicatas.

## Falhas x avisos

- **Falha** bloqueia (código 1): resolução/aspecto/arquivo, quase sólida, clipping, silêncio longo, loudness fora do alvo, cues vazias/sobrepostas/gaps, >chars, cobertura baixa.
- **Aviso** não bloqueia: cues curtas, leitura rápida (ajustar se possível, mas não impede publicar).

## Fluxo recomendado

```
canal existente (sem nicho/outlier) ou canal novo (nicho + outlier)
→ research → script → art direction → image prompts → assets
→ motion prompts → Remotion → QA
→ receipt visual independente → render final → audit_all → publicar
```

`--allow-incomplete` produz apenas diagnóstico com `releaseEligible=false`; ele nunca libera render, report ou output final.

## Comando

`/dark-auditar "<videoNN ou canal>"` roda tudo e devolve o veredito.
