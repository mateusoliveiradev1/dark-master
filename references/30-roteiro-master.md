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

1. **Brief do caso** (pesquisa: quem/quando/onde/vítimas/fontes/pergunta central).
2. **Gerar o esqueleto** com `scripts/script_builder.py` (beats + orçamento + checklist).
3. **Escrever** bloco a bloco (com o `dark-roteirista`), batendo o orçamento.
4. **Passar o linter** (`lint-roteiro.py`) e o **validador de estrutura** (`script_builder.py --validate`).
5. **Aprovar fatos** antes de gerar voz (GATE de fatos).

## Ferramentas

```bash
# esqueleto
python scripts/script_builder.py --genre truecrime --porte padrao \
  --case "Hoffa" --date "1975" --place "Detroit" --sources "FBI vault; DOJ" \
  --out "<videoNN>/01_roteiro/narration_v3.txt"

# validar estrutura/orcamento de um roteiro ja escrito
python scripts/script_builder.py --validate "<videoNN>/01_roteiro/narration_v3.txt" --genre truecrime
```

O agente `dark-roteirista` escreve o conteúdo; o `script_builder` garante **forma, tamanho e compliance**.
