# 30 — Sistema de roteiro (master)

O roteiro é a peça mais importante: ele decide retenção, satisfação e monetização. Este é o **sistema canônico** para escrever roteiro de canal dark (long-form e Short). Complementa `06` (storytelling), `07` (template), `05b` (estrutura por minuto) e `17` (anti-IA).

## Princípios inegociáveis

1. **Hook na 1ª frase.** Nada de introdução, saudação ou contexto antes do gancho.
2. **Promessa cumprida nos primeiros 30s.** O que o título promete, o roteiro entrega já.
3. **Sem dull moments.** Se não move a história ou a emoção, corta.
4. **Fim abrupto.** Não sinalize o fim (só para hype do payoff). Nunca "obrigado por assistir".
5. **Narrador habita o arquivo.** Não comenta o vídeo ("nesse canal", "nesse vídeo", "assista o short").
6. **Substância própria.** Pesquisa/perspectiva original por vídeo (ou cai no conteúdo inautêntico, `09`).
7. **Respeito e legalidade.** Sem gore; pessoas vivas = "suspeito/acusado"; 2+ fontes.
8. **Voz humana.** Anti-IA (`17`): sem "não é só X, é Y", triads forçadas, travessões em excesso.
9. **Comprimento é uma decisão editorial.** Um forense de 30–35, 45–60 ou 60–70 minutos só é aprovado se cada minuto trouxer mudança verificável; biografia sem função investigativa não preenche duração.
10. **O Short tem roteiro próprio.** Ele abre uma porta para o long, mas não repete a abertura nem entrega o caso inteiro; valide-o como peça independente.

## Nicho-agnóstico (qualquer nicho)

O sistema **não é só para true crime**. Vale para qualquer nicho (fitness, finanças, história, tech, música…).

- Use o gênero **`generic`** (COLD OPEN → CONTEXTO → DESENVOLVIMENTO → VIRADA → CONSEQUÊNCIA → FECHAMENTO+TEASER) para começar.
- Para um nicho específico, **defina os beats** num JSON e passe com `--beats-file`:
  ```json
  { "fitness": [
      ["HOOK",0.06,"promessa/transformacao"],
      ["PROBLEMA",0.18,"a dor do espectador"],
      ["METODO",0.34,"o passo a passo"],
      ["PROVA",0.22,"resultado/experimento"],
      ["OBJECAO",0.14,"quebrar a duvida"],
      ["CTA",0.06,"proximo passo"]
  ]}
  ```
- Guarde os beats do canal em `playbooks/<canal>/beats.json` (exemplo em `assets/beats-exemplo.json`). **Cada canal tem o seu** — não importe de outro.
- `python scripts/script_builder.py --list-genres` lista os disponíveis.

## Roteiro com pesquisa (usar os subagentes e juntar)

Roteiro perfeito **não se escreve de memória**. O fluxo obrigatório:

```
dark-scout (nicho/outliers)  ┐
dark-researcher (caso/tema)  ┼→  BRIEF DE PESQUISA (fatos, fontes, ângulos, contradições, demanda)
                             ┘         │
                                       ▼
                            dark-roteirista  →  plano + narração
                                       │
                                       ▼
                          validação (script_builder + lint) → GATE de fatos
```

Regras:
- **1 peça de pesquisa primária por vídeo** (linha do tempo, dado compilado, comparação) — senão cai no conteúdo inautêntico (`09`).
- Fontes com camadas **[FATO]/[REPORTADO]/[LENDA]**; nada entra sem fonte.
- Buscar **ângulo não coberto** (gap) e **contradições** — é o que diferencia de IA genérica.
- Combinar **2+ fontes** e cruzar números.
- O roteirista **não inventa**; se falta dado, corta ou marca como lenda.
- Para cada episódio, preencha `PESQUISA_BRIEF.md`, `PESQUISA_FONTE.md`, `CLAIMS.json` e, em casos cronológicos, `LINHA_DO_TEMPO.md` (`36`).
- Claims materiais recebem IDs; `FATO` exige `source_ids`; `REPORTADO`, `LENDA`, `HIPOTESE` e `INTERPRETACAO` permanecem separados.
- Um scaffold vazio, uma fonte sem localizador ou uma afirmação sem fonte resulta em `INCONCLUSIVO`, nunca em aprovação.
- Para forense, a cronologia deve cobrir a vida inteira quando isso alterar acesso, oportunidade, risco, conflito ou interpretação; não force biografia irrelevante.
- A reconstrução só usa sequência mínima sustentada pelas evidências e explicita o grau de certeza.

### Pesquisa de título e rotação antes do roteiro

O título não é gerado no vazio. Antes de escolher o título final:

1. preencha `01_roteiro/TITLE_RESEARCH.md` com tema, subtema, ângulo, idioma, mercado, formato, candidatos, URLs e datas;
2. rode `python scripts/title_research.py --candidates <candidatos> --history <pasta-do-canal> --current <video> --out <video>/01_roteiro/TITLE_RESEARCH.json --markdown <video>/01_roteiro/TITLE_RESEARCH_CHECK.md`;
3. compare o resultado com o histórico, mas não trate heurística como demanda ou CTR;
4. escolha o título humano e grave-o em `youtube_package.txt`;
5. depois de fechar o esqueleto, rode `python scripts/rotation_audit.py --current <video> --previous <pasta-do-canal> --out <video>/01_roteiro/ROTATION_AUDIT.json`.

O `rotation_audit.py` compara somente os três episódios anteriores por padrão e mede título, hook, sequência de beats e CTA. `FAIL` exige mudança; `REVIEW` exige aprovação humana; `INCONCLUSIVO` significa que faltou título, mapa ou histórico. A rotação não proíbe repetir tema ou série: proíbe repetir a mesma substância sem ângulo, prova ou mudança editorial real.

### Gate semântico do long

- `ROTEIRO_MAP.json` é o sidecar obrigatório do long: cada bloco tem `beat`, `text`, `claim_ids`, `target_words`, `target_seconds`, `question`, `state_change`, `rehook` e `payoff`.
- O texto do mapa deve corresponder a `narration_v3.txt`; marcadores ficam apenas no sidecar, nunca na narração TTS.
- Toda claim deve estar mapeada a pelo menos um bloco; claims não usadas só entram com justificativa explícita.
- O validador estrito bloqueia beats fora de ordem, blocos sem pergunta, mudança de estado, payoff final, rehooks insuficientes, claims desconhecidas e divergência mapa/narração.
- Depois da voz, rode `scripts/timing_audit.py` com `captions_times.json` e o TTS final; `TIMING_AUDIT.json` só pode ser `PASS` dentro da janela-alvo.
- Rode `scripts/originality_audit.py` contra os últimos episódios; near-duplicate ou template repetitivo bloqueia a entrega.
- `TITLE_RESEARCH.md` e `TITLE_RESEARCH.json` registram os candidatos e a decisão humana; a demanda não é inferida sem fonte.
- Rode `scripts/rotation_audit.py` contra os três episódios anteriores; `REVIEW` bloqueia a aprovação automática e `FAIL` exige mudança editorial.
- `asset_manifest.py` deve fechar o GATE 100% comparando cada prompt numerado com o asset correspondente; `PROMPT_STATUS.json` guarda os faltantes para retry.
- Rode `scripts/compliance_audit.py`; qualquer `REVIEW` exige revisão humana antes da publicação.
- Rode `scripts/research_audit.py --strict`; `RESEARCH_AUDIT.json` só passa com fontes, localizadores, confiança e independência rastreáveis.
- Rode `scripts/script_scorecard.py`; `SCRIPT_SCORECARD.json` só passa no threshold do lane.
- Após D+2/D+7, rode `scripts/script_feedback.py` e `scripts/calibration_audit.py`; ambos são propose-only e nunca reescrevem regras automaticamente.

### Short→Long obrigatório no lane misto
- Gere `SHORT_FUNNEL.md`, `ROTEIRO_SHORT_PLANO.md` e `narration_short.txt` separados do long.
- O Short usa uma claim verificada, frame 1, texto ≤6, fala ≤8, uma ideia, payoff e loop visual/sonoro.
- O Short deve criar uma pergunta ou lacuna que o long expande; não é um teaser genérico nem um resumo do episódio.
- O CTA vai para comentário fixado/related video quando quebrar o loop.
- Aponte a claim, o beat do long, o pinned comment, o related video e métricas D+2/D+7.

### Anti-IA genérico (obrigatório)
- Frases próprias (`17-anti-ia.md`): sem "não é só X, é Y", triads forçadas, "no mundo de hoje", travessões em excesso.
- **Tom e ponto de vista** do canal (playbook), não um tom genérico.
- Estrutura que **varia** entre episódios (o formato pode repetir; a substância não).
- Detalhe concreto e específico > afirmação genérica.

## Formato: short, long ou ambos? (decisão, não regra)

**Não é obrigatório fazer short+long sempre.** O formato é uma **decisão do canal**, definida no `config/FOCUS.md` e no lane escolhido em `references/23`:

| Lane | Quando | O que produzir |
|---|---|---|
| **Shorts-first** | alcance/inscritos rápido; produção leve | ≥80% Shorts |
| **Long-first** | watch time/receita/autoridade | ≤20% Shorts |
| **Mixed** | funil (Short→long) validado | ambos, com medição do funil |

- Canal novo: comece por **um** lane e valide (não force os dois).
- Se for mixed, **só mantenha** se o funil Short→long estiver **medido** (`21-motor-de-monetizacao.md`).
- Registre a escolha no `FOCUS.md`; o `/dark-roteiro` respeita.

## Beats por gênero

### truecrime (12–25 min)
| Beat | Proporção | Função |
|---|---|---|
| HOOK | 4% | detalhe mais estranho VERIFICADO (não o crime) |
| CONTEXTO | 16% | quem/quando/onde; humaniza |
| PRESSAO | 13% | os pesos antes do fato |
| O DIA | 22% | cronologia minuto a minuto (beats curtos) |
| INVESTIGACAO/PERICIA | 19% | o que a polícia fez/falhou; ciência |
| FAMILIA/POS | 9% | quem luta pelo caso |
| TEORIAS | 13% | até 3, pró/contra, sem afirmar |
| CHAVES+OUTRO+TEASER | 4% | o que resolveria + CTA + próximo caso |

### darkhistory (15–30 min)
COLD OPEN (cena no presente) · CONTEXTO · O MUNDO DA ÉPOCA · A VIRADA · AS CONSEQUÊNCIAS · O ARQUIVO (o que sabemos e o que não) · OUTRO+TEASER.

### financial (15–25 min)
COLD OPEN · O ESQUEMA · OS PERSONAGENS · A ASCENSÃO · A QUEDA · O DINHEIRO (onde foi) · O LEGADO · OUTRO+TEASER.

### forense (30–70 min)
HOOK (fato do laudo) · VIDA_E_CONTEXTO (somente o que muda a investigação) · DESCOBERTA · LINHA_DO_TEMPO · EVIDÊNCIAS (cada uma responde a uma pergunta) · PERÍCIA (limites e significado) · CONTRADIÇÃO · RECONSTRUÇÃO (grau de certeza) · CONFIRMADO_DESCONHECIDO.

> Forense/truecrime: `O DIA` ou `RECONSTRUÇÃO` segue a cronologia; a linha do tempo é obrigatória, com datas e saltos marcados (`35`). Para long, cada bloco precisa ter mudança de estado, não repetição.

### short (20–45s)
HOOK (0–3s: impossibilidade completa ou pergunta em 2ª pessoa) · DESENVOLVIMENTO (1 ideia) · PAYOFF · LOOP (fim emenda no começo / loop aberto).

## Orçamento de palavras (PORTE)

| Porte | Duração | Palavras | Ritmo |
|---|---|---|---|
| FINO | 12–15 min | ~1.900–2.400 | casos com pouca fonte |
| PADRÃO | 18–21 min | ~2.900–3.300 | default |
| RICO | 24–27 min | ~3.400–3.800 | caso denso |
| FORENSE 30–35 | 30–35 min | ~4.200–5.600 | caso denso com progressão |
| FORENSE 45–60 | 45–60 min | ~6.300–9.600 | investigação extensive |
| FORENSE 60–70 | 60–70 min | ~8.400–11.200 | arquivo completo |

≈ **150–160 palavras por minuto** (narração dark, pausada). Short: ~2,5 palavras/segundo. A faixa longa só é válida se a pesquisa sustentar a progressão; não encha com biografia ou repetição.

## Dispositivos de retenção (onde inserir)

- **Re-engage ~3 min** e **~6 min** (progression + algo "só este canal faz").
- **Rehook a cada 2–4 min** em vídeos de 20–30 min; a cada 60–120s em vídeos de 30–70 min quando cada bloco tiver nova evidência, contradição, data ou hipótese.
- **Open loops** empilhados nos primeiros 20s (3–5 promessas) e fechados ao longo.
- **Pattern interrupt a cada 30–90s** (mudança visual/sonora).
- **Pergunta central** que só se resolve no fim.
- **Mudança de estado** a cada 30–60s: nova evidência, contradição, testemunha, data, hipótese, limite pericial ou pergunta ainda sem resposta.

## Fórmula do hook (escolha 1)

- **Cena concreta + detalhe impossível:** "Às 3h da manhã, a luz da cozinha acendeu sozinha — e ninguém estava em casa."
- **Pergunta em 2ª pessoa:** "Would you jump out of a plane for $200,000?"
- **Contradição verificada:** "O laudo dizia afogamento. O corpo não tinha água nos pulmões."
- **Número + stake:** "Três mulheres. Uma casa. Zero respostas."

**Proibido no hook:** data/local antes do gancho; filosofia/abstração; "nesse vídeo"; explicação.

## Ponte entre shorts e long (sem quebrar a lore)

Quem veio do Short precisa acolhimento, sem citar o Short: *"You heard the call. You haven't heard the room."* O hook do long **não** repete as mesmas 10 palavras do Short.

## Compliance no roteiro (checklist)

- [ ] Sem gore/descrição gráfica; foco em perícia/fatos.
- [ ] Suspeito vivo → "suspeito/acusado/alleged".
- [ ] 2+ fontes; dados verificáveis.
- [ ] `CLAIMS.json` completo; nenhuma claim material sem `source_ids`.
- [ ] `LINHA_DO_TEMPO.md` preenchida para casos cronológicos; datas novas foram adicionadas antes da escrita.
- [ ] Separação [FATO] / [REPORTADO] / [LENDA] / [HIPÓTESE] / [INTERPRETAÇÃO].
- [ ] Sem meta-linguagem; sem menção a duração.
- [ ] Divulgação de IA quando voz/visual sintético (no pacote).

## Fluxo de escrita (workflow)

1. **Brief do caso** (pesquisa: quem/quando/onde/vítimas/fontes/pergunta central). Preencha `PESQUISA_BRIEF.md`, `PESQUISA_FONTE.md`, `CLAIMS.json` e `ROTEIRO_MAP.json`; casos cronológicos também preenchem `LINHA_DO_TEMPO.md` (`35`, `36`).
2. **Pesquisar e escolher o título** com `TITLE_RESEARCH.md`, `title_research.py` e evidência datada de busca/Data API; a decisão final é humana e vai para `youtube_package.txt`.
3. **Definir a duração e o formato** (`--target-minutes 30-35` ou playbook do canal). Para forense, incluir vida, contexto e investigação que mudem a interpretação, sem biografia automática.
4. **Gerar o esqueleto** com `scripts/script_builder.py` (beats, orçamento, `ROTEIRO_MAP.json`, claims e checklist). Preencha o mapa com o texto real de cada bloco antes de validar. Se o lane for misto, usar `--funnel` para gerar o plano do Short separado.
5. **Escrever** `narration_v3.txt` bloco a bloco, preenchendo o `ROTEIRO_MAP.json` com `claim_ids`, pergunta, mudança de estado, rehook e payoff. Escrever `narration_short.txt` como peça independente, não como corte automático.
6. **Comparar com os últimos três episódios** com `scripts/rotation_audit.py`; mudar hook, ordem dos beats, ângulo, CTA ou fórmula se `ROTATION_AUDIT.json` retornar FAIL ou REVIEW.
7. **Passar o linter** (`lint-roteiro.py`) e o **validador estrito** (`script_builder.py --validate --strict`). O Short usa hook ≤8 palavras e seu próprio plano de loop/bridge.
8. **Aprovar fatos** antes de gerar voz (GATE de fatos). Se houver lacuna, registrar `INCONCLUSIVO` e cortar ou atribuir a hipótese.
9. **Auditar duração real depois da voz** com `scripts/timing_audit.py`; salvar `TIMING_AUDIT.json` com status `PASS` antes de considerar o roteiro pronto.
10. **Scaffold do vídeo** — o roteiro **não está entregue** sem esta etapa (**roteiro sem scaffold = entrega incompleta**):
    a. **Pastas + stubs**: `python scripts/novo_video.py NN "Caso" SERIE` (no canal real) ou `python scripts/new_video.py NN "Caso" SERIE --root "<canal>"` (skill) → cria `videoNN/{01_roteiro,02_audio,03_imagens,04_video_final}` + `TEMPLATE.txt`, `narration_v3.txt`, `narration_short.txt`, `tease.txt`, `PESQUISA_BRIEF.md`, `PESQUISA_FONTE.md`, `TITLE_RESEARCH.md`, `TITLE_CANDIDATES.txt`, `CLAIMS.json`, `ROTEIRO_MAP.json`, `LINHA_DO_TEMPO.md`, `SHORT_FUNNEL.md` e `youtube_package.txt` (stubs). O scaffold **nunca sobrescreve** arquivos existentes: narração, pesquisa, claims, mapa, timeline, título e funil são preservados.
    b. **PROMPTS.md completo por PORTE** — **FINO 26–30 · PADRÃO 32–36 · RICO 36–40 · FORENSE 30–35 38–48 · FORENSE 45–60 52–68 · FORENSE 60–70 68–88** — com o **sufixo travado do canal** (contrato: `playbooks/<canal>/style.json` → `image_suffix`, via `--channel`) e o header da regra de geração (`29`); mapeie os blocos **TEASE-A/B** nos números de imagem correspondentes (blocos do meio, min 7–12). Gere com `scripts/prompt_builder.py --style <preset-do-canal> --suffix "<sufixo>" --count <porte>` ou complete o esqueleto do scaffold.
    c. **youtube_package.txt base**: `TITLE` + alternativas + `ANGULO` + `DESCRIPTION` (Lego) + `TAGS` + `THUMB` spec + bloco `SHORT` + pinneds. O template do scaffold já sai no **formato que o validador cobra** (`TITLE:`, `DESCRIPTION (copiar e colar):`, `TAGS:`, linha começando com `CHAPTERS ...`) — não edite os rótulos, só preencha. **CHAPTERS ficam marcados `PENDENTE`** — só remapeie pós-build com a duração real (`ffprobe`/`remapar_chapters`), nunca antes. Preencher o pacote (título/descrição/tags/chapters) é **etapa autoral manual** — não é gerada por script.
    d. **Voz liberada no scaffold** (`python scripts/gerar_voz_v3.py videoNN`; identidade no contrato `playbooks/<canal>/voice.json`): a voz depende **só da narração + GATE de fatos**. **MOTION continua bloqueado pelo GATE 100%** (só com todas as imagens). Distinção que vale de agora em diante (resolve a contradição com o `PROTOCOLO_ANTI_INAUTHENTIC` item 5): **`imagens < 100% → não gera MOTION`**; a **voz pode (e deve) ser gerada no scaffold**.
    e. **Fechar o manifest dos assets** depois de gerar ou coletar as imagens: `python scripts/asset_manifest.py --images <video>/03_imagens --out <video>/01_roteiro/PROMPT_STATUS.json`. `FAIL` bloqueia motion; os IDs em `missing` entram no retry de prompts.

    **Verificação pós-scaffold** (antes de seguir):
    ```bash
    ls "<canal>/videoNN"                 # 01_roteiro 02_audio 03_imagens 04_video_final
    ls "<canal>/videoNN/01_roteiro"      # narration_v3.txt narration_short.txt TEMPLATE.txt PESQUISA_BRIEF.md PESQUISA_FONTE.md TITLE_RESEARCH.md TITLE_CANDIDATES.txt CLAIMS.json ROTEIRO_MAP.json LINHA_DO_TEMPO.md SHORT_FUNNEL.md

    ls "<canal>/videoNN/youtube_package.txt" "<canal>/videoNN/03_imagens/PROMPTS.md"
    ```
    - [ ] 4 pastas existem · narração/tease/PESQUISA/título/mapa **preservados** · `TITLE_RESEARCH.json` gerado · `ROTATION_AUDIT.json` PASS ou aprovado · PROMPTS.md com o sufixo do canal e TEASE-A/B mapeados · chapters `PENDENTE` · voz gerada (fatos aprovados) · `TIMING_AUDIT.json` = PASS.


## Ferramentas

```bash
# esqueleto (long-form forense de 30-35 + Short separado)
python scripts/script_builder.py --genre forense --target-minutes 30-35 --funnel \
  --target-long videoNN --case "Caso" --question "O que a evidência permite concluir?" \
  --out "<videoNN>/01_roteiro"

# esqueleto (long-form)
python scripts/script_builder.py --genre truecrime --porte padrao \
  --case "Hoffa" --date "1975" --place "Detroit" --sources "FBI vault; DOJ" \
  --out "<videoNN>/01_roteiro"

# validar estrutura/orcamento de um roteiro ja escrito
python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_v3.txt" --genre truecrime --strict \
  --map "<videoNN>/01_roteiro/ROTEIRO_MAP.json"

# canal com formato proprio (usa o porte de playbooks/<canal>/roteiro.json)
python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_pt.txt" \
  --channel laudo-final --genre forense

# comparar com episodios anteriores
python scripts/originality_audit.py --narration "<videoNN>/01_roteiro/narration_v3.txt" \
  --previous "<canal>" --out "<videoNN>/01_roteiro/ORIGINALITY_AUDIT.json"

# comparar candidatos de título com o histórico
python scripts/title_research.py --candidates "<videoNN>/01_roteiro/TITLE_CANDIDATES.txt" \
  --history "<canal>" --current "<videoNN>" --out "<videoNN>/01_roteiro/TITLE_RESEARCH.json" \
  --markdown "<videoNN>/01_roteiro/TITLE_RESEARCH_CHECK.md"

# comparar título, hook, beats e CTA com os três últimos episódios
python scripts/rotation_audit.py --current "<videoNN>" --previous "<canal>" \
  --out "<videoNN>/01_roteiro/ROTATION_AUDIT.json"

# fechar o GATE 100% de assets
python scripts/asset_manifest.py --images "<videoNN>/03_imagens" \
  --out "<videoNN>/01_roteiro/PROMPT_STATUS.json"

# compliance assistido
python scripts/compliance_audit.py --narration "<videoNN>/01_roteiro/narration_v3.txt" \
  --claims "<videoNN>/01_roteiro/CLAIMS.json" --out "<videoNN>/01_roteiro/COMPLIANCE_AUDIT.json"

# scorecard editorial
python scripts/script_scorecard.py --root "<videoNN>" --lane mixed --out "<videoNN>/01_roteiro/SCRIPT_SCORECARD.json"

# auditoria de pesquisa e calibração
python scripts/research_audit.py --root "<videoNN>" --strict --out "<videoNN>/01_roteiro/RESEARCH_AUDIT.json"
python scripts/calibration_audit.py --scorecard "<videoNN>/01_roteiro/SCRIPT_SCORECARD.json" \
  --channel "@Canal" --video-tag videoNN --out "<videoNN>/01_roteiro/CALIBRATION_AUDIT.json"

# feedback D+2/D+7 (propose-only)
python scripts/script_feedback.py --channel "@Canal" --video-tag videoNN --out "<videoNN>/01_roteiro/SCRIPT_FEEDBACK.json"

# auditar duracao real depois da voz
python scripts/timing_audit.py --narration "<videoNN>/01_roteiro/narration_v3.txt" \
  --captions-times "<videoNN>/02_audio/captions_times.json" --target-minutes 30-35 \
  --map "<videoNN>/01_roteiro/ROTEIRO_MAP.json" --voice "<videoNN>/02_audio/voice_FINAL.wav" \
  --out "<videoNN>/01_roteiro/TIMING_AUDIT.json"

# Short (references/31)
python scripts/script_builder.py --genre short --short --case "Hoffa" --out "<videoNN>/01_roteiro"
python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_short.txt" --genre short --short --strict \
  --claims "<videoNN>/01_roteiro/CLAIMS.json" --funnel-plan "<videoNN>/01_roteiro/SHORT_FUNNEL.md"

# banco de variacoes de hook (arquetipos de 31)
python scripts/script_builder.py --hooks 10 --case "Hoffa" --archetypes 1,3,4,5 --lang en
```

O agente `dark-roteirista` escreve o conteúdo; o `script_builder` garante **forma, tamanho e compliance**.
