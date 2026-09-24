# 35 — Cronologia e linha do tempo

Casos forenses, true crime, colapsos financeiros e desastres **são uma linha do tempo**. Se o espectador se perde na ordem dos fatos, o vídeo perde autoridade — e o canal forense vive de autoridade. Esta referência é o método para o roteiro **e** para a edição saírem cronologicamente perfeitos.

> Vale para: `truecrime`, `forense`, `financial`, `darkhistory`, desastres. **Não** force em vídeos temáticos/analíticos (aí a ordem é por argumento, não por data).

## Passo 1 — LINHA_DO_TEMPO.md (a tabela canônica)

Criada **antes de escrever** (junto com o brief de pesquisa, `30`), em `<videoNN>/01_roteiro/LINHA_DO_TEMPO.md`:

| data | fato | camada | fonte |
|---|---|---|---|
| 2010-06-04 | Eliza sai do Rio para Minas; nunca mais é vista | FATO | sentença |
| 2010-06-08 | Carro apreendido em blitz; perícia entra | FATO | laudo IC-MG |
| 2010-07-07 | IC-MG apresenta laudo do sangue do carro | FATO | laudo IC-MG |
| ? | Corpo nunca encontrado | FATO | — |

- **data**: `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, `DD/MM/YYYY` ou `?` (fato sem data — o plate marca com nó vazado).
- **fato**: **rótulo curto** (≤ ~60 chars). É o que aparece no plate — frase longa vira texto cortado.
- **camada**: `FATO` / `REPORTADO` / `LENDA` (mesma regra de fontes do `30`).
- **fonte**: o documento de origem (não o link; links vão para a descrição).
- Ordem da tabela = ordem narrativa. Fato fora de ordem vira **salto explícito** no roteiro.
- **Para forense de 30–70 min**, mantenha três camadas no mesmo arquivo: vida e contexto relevantes, sequência do caso/descoberta e investigação/reconstrução. Inclua nascimento, família, escola, trabalho, relações, deslocamentos e eventos anteriores somente quando alterarem acesso, oportunidade, risco, conflito ou interpretação.
- **Não force uma biografia.** O objetivo é cobertura útil, não biografias. Um dado entra quando muda a hipótese ou dá contexto a uma ação.
- **Toda data nova entra antes da narração.** O roteiro pode abrir no futuro, mas o recuo ao início deve ser marcado e a fonte deve estar disponível.
- Template: `assets/template-linha-do-tempo.md`.

## Passo 2 — Roteiro ancorado

Regras que fazem o roteiro parecer laudo, não resumo:

1. **Cada bloco declara a data na 1ª frase** (falada por extenso): "No dia quatro de junho de 2010, ...". Nada de "algum tempo depois".
2. **Salto para trás é marcado**: "Meses antes, ...", "Um ano antes, ...", "O carro tinha sido apreendido..." (mais-que-perfeito conta como marca).
3. **Uma data por bloco.** Duas datas no mesmo bloco = espectador perdido.
4. **"O DIA" é minuto a minuto** (beat de `30`): blocos curtos, cada um com hora/data quando houver.
5. **Só entra data que está na tabela.** Data nova = atualizar a tabela primeiro (e a fonte).
6. **Cold open pode abrir no futuro** (o momento mais forte) — o recuo ao início da história vem em seguida e é permitido.
7. Payoff de mistério não inventa data: sem data = `?` na tabela e "a data exata nunca foi confirmada" no roteiro.

## Passo 3 — Linter cronológico

```bash
python scripts/lint-roteiro.py "<videoNN>/01_roteiro/narration_pt.txt" \
  --cronologia "<videoNN>/01_roteiro/LINHA_DO_TEMPO.md" --lang pt --genero forense
```

Checa: **ordem** (data que recua sem marcador), **saltos marcados** (ok), **datas fora da linha do tempo**, **eventos sem eco no roteiro** (tabela não narrada) e ignora o cold open (`--cold-open 3`). É advisory: flag = revisar, não necessariamente erro.

## Passo 4 — Edição (linha do tempo na tela)

```bash
python scripts/timeline_kit.py videoNN --root "<canal>" --channel <canal>
# -> 04_video_final/timeline_plate.png + datestamps.ass + comando ffmpeg pronto
```

Duas peças:

1. **`timeline_plate.png`** — a linha do tempo completa (até 12 eventos; 2 faixas acima de 6). Use no **cold open** (teaser do caso), num **recap** no meio ou antes do "LAUDO". Paleta/fonte vêm do `style.json` do canal.
   - `--to-imagens` coloca em `03_imagens/38_timeline.png` (estilo Money Files: o plate vira imagem do motion). **Cuidado:** em canais que usam `montar_motion` com glob `01..40`, isso o inclui no vídeo — de propósito.
2. **`datestamps.ass`** — a **data corrente na tela** (canto superior direito, abaixo da letterbox), com *carry-forward*: a data fica até a próxima ser falada. Gerado a partir do `captions.srt` (timing real da narração).
   - Queimar depois do motion: `ffmpeg -y -i "<videoNN>_FINAL.mp4" -vf "ass='<...>/datestamps.ass'" -c:v libx264 -preset veryfast -crf 19 -c:a copy "<videoNN>_DATADO.mp4"`.
   - `--skip-first 20` segura o stamp nos primeiros segundos (se quiser cold open limpo); `--margin-v` ajusta a altura (letterbox de 90px → 130 fica logo abaixo da tarja).

Regras de edição:
- O stamp **não cobre rosto, prova ou texto de tela** — canto superior direito é o lugar seguro.
- Duração mínima ~1,5s (o kit descarta marcas mais curtas para não piscar).
- O plate aparece **parado** (é gráfico, não motion) com motion de zoom lento por cima; legível a 120px (regra de thumb, `04`).
- Datas na tela e datas faladas têm que bater com a tabela — se divergirem, o linter avisa.

## Checklist cronológico

- [ ] `LINHA_DO_TEMPO.md` completa (com camadas e fontes) antes de escrever.
- [ ] Cada bloco com data na 1ª frase; saltos marcados; 1 data por bloco.
- [ ] `--cronologia` sem flags de ordem (ou flags justificadas).
- [ ] Nenhuma data fora da tabela; nenhum evento da tabela sem eco.
- [ ] Plate gerado e aprovado (rótulos curtos, legível).
- [ ] `datestamps.ass` queimado no final; spot-check de 3 marcas no vídeo pronto.
- [ ] Descrição/chapters coerentes com a cronologia (chapters pós-build, `12`).
- [ ] `ROTEIRO_MAP.json` corresponde à narração e cada claim está ligada a um bloco.
- [ ] Depois da voz, `TIMING_AUDIT.json` confirma a janela real de duração.

## Ferramentas

```bash
# linter (estrutura + IA + cronologia)
python scripts/lint-roteiro.py <narration> --cronologia <LINHA_DO_TEMPO.md> --lang pt --genero forense

# duracao real da voz
python scripts/timing_audit.py --narration <narration> --captions-times <captions_times.json> \
  --target-minutes 30-35 --map <ROTEIRO_MAP.json> --voice <voice_FINAL.wav> --out <TIMING_AUDIT.json>

# linha do tempo na edição (plate + datestamps)
python scripts/timeline_kit.py videoNN --root "<canal>" --channel <canal>
python scripts/timeline_kit.py videoNN --root "<canal>" --channel <canal> --plate-only --to-imagens
```
