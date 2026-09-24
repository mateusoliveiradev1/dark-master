# 37 — Pipeline Remotion

O Remotion é o renderer visual canônico para todo episódio novo. Ele roda depois da pesquisa, do roteiro, da direção de arte, dos prompts de imagem, dos assets e dos prompts de motion. Não é dono da narrativa e não reescreve o motor de roteiro. FFmpeg fica restrito a encode/mux e derivados explicitamente declarados; nunca cria a camada visual.

## Contrato de entrada

O `RENDER_PLAN_LONG.json` ou `RENDER_PLAN_SHORT.json` é uma projeção visual do episódio. Ele consome, sem alterar:

- `ROTEIRO_MAP.json`;
- `CLAIMS.json`;
- captions e `captions_times.json`;
- áudio final;
- imagens e documentos;
- `style.json`, `motion.json`, `voice.json` e `roteiro.json`.

Cada cena contém `id`, `type`, `purpose`, `startSeconds`, `durationSeconds`, `sourceBlockIds`, assets, headline, body, metadata, motion e transições. O renderer não aceita path absoluto, `..`, URL externa ou asset não rastreável.

## Fluxo obrigatório para novos episódios

```text
canal existente (sem nicho/outlier) ou canal novo (nicho + outlier)
→ research → script → art direction → image prompts → assets
→ motion prompts → Remotion → QA
→ F0/F50/F100 + contact sheets + receipt independente
→ render final + RENDER_REPORT → auditoria final
```

O Remotion não deve transformar uma pasta de imagens em cenas por ordem numérica. Para episódios novos, research/map/claims, `SHOT_SPECS.json`, `PROMPT_PLAN.json` em `PROMPTS_READY`, manifest, image audit, direitos, assets não bloqueados, captions/timing, voice/audio quando o lane exigir e Visual Profile são gates de entrada. Assets são resolvidos por `assetId`, `promptId` e `shotId`; material legado só pode ser inspecionado com `--allow-incomplete`, que grava um plano diagnóstico sem capacidade de release.

Cada cena declara os campos do contrato visual, `imagePrompt`, `motionPrompt`, estados, crops, assets, claims, fontes e intenção de movimento. `states` preserva `assetIds`, `visibleLayers`, `hiddenLayers`, `focalPoint` e `annotation`; o planner não substitui silenciosamente uma seleção de assets pelo asset primário. O runtime separa o alvo do movimento: câmera/mídia, texto, annotation e vetores não compartilham a mesma transformação global. O contrato de motion usa estados percentuais `0-100` e proíbe zoom/fade genéricos como única mudança.

## Comandos

```bash
python scripts/orchestrate.py plan --root "<canal>" --episode videoNN --channel-state existing
python scripts/remotion.py doctor --root "<canal>" --channel <canal>
python scripts/remotion.py plan <videoNN> --root "<canal>" --channel <canal> --format long
python scripts/remotion.py stills <videoNN> --root "<canal>" --channel <canal> --format long
python scripts/visual_review.py --plan "<canal>/videoNN/01_roteiro/RENDER_PLAN_LONG.json" --format long
python scripts/visual_review.py --plan "<canal>/videoNN/01_roteiro/RENDER_PLAN_LONG.json" --receipt "<receipt.json>"
python scripts/remotion.py render <videoNN> --root "<canal>" --channel <canal> --format long
python scripts/remotion.py audit <videoNN> --root "<canal>" --channel <canal> --format long
```

`plan` cria os sidecars em `01_roteiro` e um diretório de staging exclusivo por run/hash em `04_video_final/_remotion/runs/<runId>/public`. Só assets referenciados pelo ledger são copiados; `asset_ledger.json` e `run.json` registram hashes, versões, gates e perfil. `stills` produz F0/F50/F100 e contact sheets por cena/sequência. `render` exige receipt PASS e nunca sobrescreve output existente. `audit` exige plano, relatório, receipt, staging e MP4 do mesmo run.

## Motor visual

O pacote `remotion/` usa versõesRemotion alinhadas, React, Zod, `@remotion/media`, captions, motion blur, noise, paths, shapes e transitions conforme a necessidade da cena. A cena final combina imagem IA, documentos, mapas, timeline, evidence board, comparação, citação, dados, capítulo e end card em uma linguagem coerente com o canal.

A skill instala o pacote com `npm --prefix remotion ci`; não usa `latest` no lockfile. O `doctor` exige Node, ffmpeg, ffprobe e o entrypoint do Remotion.

## Gates

- `doctor` PASS antes de gerar plano;
- research/map/claims, shot specs, prompt READY, manifest, image audit, direitos, assets, captions/timing, audio do lane e Visual Profile PASS;
- auditoria semântica anti-slideshow: cada cena não estática precisa registrar pelo menos duas mudanças editoriais entre estados, além de amostra F0/F50/F100 e contact sheet;
- receipt independente com reviewer, score, findings e `planHash` igual ao plano;
- `RENDER_REPORT` e `run.json` com hashes de input/output e versões de Remotion/Node/ffmpeg;
- `audit` PASS antes de usar o MP4 na auditoria final.

Novos renders sempre usam `engine: remotion`. Não existe fallback visual por FFmpeg ou `engine: legacy` no caminho de release; `--allow-incomplete` é diagnóstico e não libera render.
