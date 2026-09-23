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

### forense (10–15 min)
HOOK (fato do laudo) · CONTEXTO · O DIA · PERÍCIA (coração) · FAMÍLIA · TEORIAS · LAUDO/OUTRO+TEASER.
> Forense/truecrime: **O DIA é cronologia minuto a minuto** — linha do tempo obrigatória (`35`), com datestamps na edição.

### short (20–45s)
HOOK (0–3s: impossibilidade completa ou pergunta em 2ª pessoa) · DESENVOLVIMENTO (1 ideia) · PAYOFF · LOOP (fim emenda no começo / loop aberto).

## Orçamento de palavras (PORTE)

| Porte | Duração | Palavras | Ritmo |
|---|---|---|---|
| FINO | 12–15 min | ~1.900–2.400 | casos com pouca fonte |
| PADRÃO | 18–21 min | ~2.900–3.300 | default |
| RICO | 24–27 min | ~3.400–3.800 | caso denso |

≈ **150–160 palavras por minuto** (narração dark, pausada). Short: ~2,5 palavras/segundo.

## Dispositivos de retenção (onde inserir)

- **Re-engage ~3 min** e **~6 min** (progression + algo "só este canal faz").
- **Rehook a cada 2–4 min** (nova pista, twist, mudança de fase).
- **Open loops** empilhados nos primeiros 20s (3–5 promessas) e fechados ao longo.
- **Pattern interrupt a cada 30–90s** (mudança visual/sonora).
- **Pergunta central** que só se resolve no fim.

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
- [ ] Separação [FATO] / [REPORTADO] / [LENDA].
- [ ] Sem meta-linguagem; sem menção a duração.
- [ ] Divulgação de IA quando voz/visual sintético (no pacote).

## Fluxo de escrita (workflow)

1. **Brief do caso** (pesquisa: quem/quando/onde/vítimas/fontes/pergunta central). **Caso cronológico** (truecrime/forense/financial/desastres) → montar também a `LINHA_DO_TEMPO.md` (tabela canônica) e seguir o modo cronológico de `35`.
2. **Gerar o esqueleto** com `scripts/script_builder.py` (beats + orçamento + checklist).
3. **Escrever** bloco a bloco (com o `dark-roteirista`), batendo o orçamento.
4. **Passar o linter** (`lint-roteiro.py`) e o **validador de estrutura** (`script_builder.py --validate`).
5. **Aprovar fatos** antes de gerar voz (GATE de fatos).
6. **Scaffold do vídeo** — o roteiro **não está entregue** sem esta etapa (**roteiro sem scaffold = entrega incompleta**):
   a. **Pastas + stubs**: `python scripts/novo_video.py NN "Caso" SERIE` (no canal real) ou `python scripts/new_video.py NN "Caso" SERIE --root "<canal>"` (skill) → cria `videoNN/{01_roteiro,02_audio,03_imagens,04_video_final}` + `TEMPLATE.txt`, `narration_v3.txt`, `tease.txt`, `PESQUISA_FONTE.md` e `youtube_package.txt` (stubs). O scaffold **nunca sobrescreve** arquivos existentes: `narration_v3.txt`, `tease.txt` e `PESQUISA_FONTE.md` são preservados (aborta o overwrite).
   b. **PROMPTS.md completo por PORTE** — **FINO 26–30 · PADRÃO 32–36 · RICO 36–40** — com o **sufixo travado do canal** (contrato: `playbooks/<canal>/style.json` → `image_suffix`, via `--channel`) e o header da regra de geração (`29`); mapeie os blocos **TEASE-A/B** nos números de imagem correspondentes (blocos do meio, min 7–12). Gere com `scripts/prompt_builder.py --style <preset-do-canal> --suffix "<sufixo>" --count <porte>` ou complete o esqueleto do scaffold.
   c. **youtube_package.txt base**: `TITLE` + alternativas + `ANGULO` + `DESCRIPTION` (Lego) + `TAGS` + `THUMB` spec + bloco `SHORT` + pinneds. **CHAPTERS ficam marcados `PENDENTE`** — só remapeie pós-build com a duração real (`ffprobe`/`remapar_chapters`), nunca antes.
   d. **Voz liberada no scaffold** (`python scripts/gerar_voz_v3.py videoNN`; identidade no contrato `playbooks/<canal>/voice.json`): a voz depende **só da narração + GATE de fatos**. **MOTION continua bloqueado pelo GATE 100%** (só com todas as imagens). Distinção que vale de agora em diante (resolve a contradição com o `PROTOCOLO_ANTI_INAUTHENTIC` item 5): **`imagens < 100% → não gera MOTION`**; a **voz pode (e deve) ser gerada no scaffold**.

   **Verificação pós-scaffold** (antes de seguir):
   ```bash
   ls "<canal>/videoNN"                 # 01_roteiro 02_audio 03_imagens 04_video_final
   ls "<canal>/videoNN/01_roteiro"      # narration_v3.txt TEMPLATE.txt tease.txt PESQUISA_FONTE.md
   ls "<canal>/videoNN/youtube_package.txt" "<canal>/videoNN/03_imagens/PROMPTS.md"
   ```
   - [ ] 4 pastas existem · narração/tease/PESQUISA **preservados** · PROMPTS.md com o sufixo do canal e TEASE-A/B mapeados · chapters `PENDENTE` · voz gerada (fatos aprovados).

## Ferramentas

```bash
# esqueleto (long-form)
python scripts/script_builder.py --genre truecrime --porte padrao \
  --case "Hoffa" --date "1975" --place "Detroit" --sources "FBI vault; DOJ" \
  --out "<videoNN>/01_roteiro"

# validar estrutura/orcamento de um roteiro ja escrito
python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_v3.txt" --genre truecrime

# Short (references/31)
python scripts/script_builder.py --genre short --short --case "Hoffa" --out "<videoNN>/01_roteiro"
python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_short.txt" --genre short --short

# banco de variacoes de hook (arquetipos de 31)
python scripts/script_builder.py --hooks 10 --case "Hoffa" --archetypes 1,3,4,5 --lang en
```

O agente `dark-roteirista` escreve o conteúdo; o `script_builder` garante **forma, tamanho e compliance**.
