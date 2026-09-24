# 37 — Pipeline Remotion

O Remotion é o renderer visual do canal. Ele roda depois da pesquisa, do roteiro, da voz, dos captions, do timing e do GATE 100% de imagens. Não é dono da narrativa e não reescreve o motor de roteiro.

## Contrato de entrada

O `RENDER_PLAN_LONG.json` ou `RENDER_PLAN_SHORT.json` é uma projeção visual do episódio. Ele consome, sem alterar:

- `ROTEIRO_MAP.json`;
- `CLAIMS.json`;
- captions e `captions_times.json`;
- áudio final;
- imagens e documentos;
- `style.json`, `motion.json`, `voice.json` e `roteiro.json`.

Cada cena contém `id`, `type`, `purpose`, `startSeconds`, `durationSeconds`, `sourceBlockIds`, assets, headline, body, metadata, motion e transições. O renderer não aceita path absoluto, `..`, URL externa ou asset não rastreável.

## Comandos

```bash
python scripts/remotion.py doctor --root "<canal>" --channel <canal>
python scripts/remotion.py plan <videoNN> --root "<canal>" --channel <canal> --format long
python scripts/remotion.py plan <videoNN> --root "<canal>" --channel <canal> --format short
python scripts/remotion.py stills <videoNN> --root "<canal>" --channel <canal> --format long
python scripts/remotion.py render <videoNN> --root "<canal>" --channel <canal> --format long
python scripts/remotion.py audit <videoNN> --root "<canal>" --channel <canal> --format long
```

`plan` cria os sidecars em `01_roteiro`. Assets são copiados para `04_video_final/_remotion/public`; o bundle só enxerga esse staging. `stills` produz amostras de hook, contexto, evidência, virada, clímax e final. `render` não sobrescreve output existente. `audit` exige plano, relatório e MP4 final.

## Motor visual

O pacote `remotion/` usa versõesRemotion alinhadas, React, Zod, `@remotion/media`, captions, motion blur, noise, paths, shapes e transitions conforme a necessidade da cena. A cena final combina imagem IA, documentos, mapas, timeline, evidence board, comparação, citação, dados, capítulo e end card em uma linguagem coerente com o canal.

A skill instala o pacote com `npm --prefix remotion ci`; não usa `latest` no lockfile. O `doctor` exige Node, ffmpeg, ffprobe e o entrypoint do Remotion.

## Gates

- `doctor` PASS antes de gerar plano;
- contratos e assets completos;
- `RENDER_PLAN` válido e sem path inseguro;
- stills revisados pelo `dark-artdirector` e `dark-visual-reviewer`;
- `RENDER_REPORT` presente;
- `audit` PASS antes de usar o MP4 na auditoria final.

O renderer é opt-in por `motion.json`: `engine: legacy` mantém o pipeline existente; `engine: remotion` usa este fluxo. Falha de Remotion não cai silenciosamente para legacy.
