# 28 — Auditorias automáticas (todos os gates)

Nada sobe sem passar pelos gates. Cada script sai com **código 1 se falhar** (dá pra usar em CI).

## Orquestrador

```bash
python scripts/audit_all.py "<videoNN>"            # um vídeo
python scripts/audit_all.py "<pasta do canal>"     # varre todos os videoNN
python scripts/audit_all.py "<videoNN>" --json     # saída para máquina
```

Roda todos os gates e imprime uma tabela com veredito por vídeo. Falha se qualquer gate falhar.

## Gates

| Gate | Script | Verifica |
|---|---|---|
| **Imagens** | `image_audit.py` | resolução, aspecto 16:9, tamanho, brilho/desvio (imagem quase sólida), saturação, **duplicatas** + contact sheet |
| **Manifest de assets** | `asset_manifest.py` | cada prompt numerado tem asset; IDs faltantes ficam disponíveis para retry |
| **Pesquisa de título** | `title_research.py` | candidatos, fórmula, overlap com histórico e decisão humana; não infere demanda |
| **Rotação editorial** | `rotation_audit.py` | título, hook, sequência de beats e CTA contra os três episódios anteriores |
| **Áudio/voz** | `audio_audit.py` | duração, sample rate/canais, **loudness (LUFS)**, **true peak**, LRA, **clipping**, **silêncios longos** |
| **Legendas** | `captions_audit.py` | nº de cues, 1ª perto de 0:00, duração por cue, **sobreposições**, gaps, linhas/chars, **velocidade de leitura (CPS)**, cobertura vs áudio |
| **Pacote** | (presença) | `youtube_package.txt` / `PACOTE_PUBLICACAO.txt` |
| **Final** | (presença) | `04_video_final/*.mp4` |
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
título → title_research → rotação dos últimos 3 → roteiro → lint_roteiro → imagens → image_audit → asset_manifest
         → voz → audio_audit → captions.srt → captions_audit → RENDER_PLAN → stills
         → dark-artdirector → dark-visual-reviewer → Remotion/motion → final
         → audit_all → audit-ypp → publicar
```

## Comando

`/dark-auditar "<videoNN ou canal>"` roda tudo e devolve o veredito.
