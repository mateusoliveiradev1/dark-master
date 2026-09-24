# 36 — Pesquisa, claims e funil Short→Long

Este documento é o contrato entre `dark-researcher`, `dark-roteirista` e o gerador de vídeo. O roteiro não começa com uma história; começa com uma base verificável que sustenta cada afirmação, cada data e cada imagem.

## 1. O que deve ser entregue antes da narração

Todo episódio precisa ter, no mínimo:

- `PESQUISA_BRIEF.md`: caso, pergunta central, ângulo editorial, lacunas, contradições, pessoas, riscos e plano de reconstrução.
- `PESQUISA_FONTE.md`: fontes com título, autor, data, tipo, URL, trecho/localizador e limitações.
- `TITLE_RESEARCH.md` e `TITLE_RESEARCH.json`: tema, subtema, ângulo, candidatos, evidências de busca, fórmula, decisão humana e limitações;
- `ROTATION_AUDIT.json`: comparação do título, hook, sequência de beats e CTA com os três episódios anteriores;
- `CLAIMS.json`: afirmações estruturadas que o roteiro pode usar.
- `LINHA_DO_TEMPO.md`: linha do tempo canônica, incluindo biografia e contexto quando eles ajudam a explicar o caso.
- `SHORT_FUNNEL.md`: Short de aquisição, ponte para o long e contrato de loop.
- `ROTEIRO_MAP.json`: mapa semântico do long, com um registro por bloco e referência às claims.
- `narration_v3.txt`: só depois da aprovação da pesquisa e do preenchimento do mapa.
- `narration_short.txt`: roteiro independente, nunca um corte automático do long.

Um arquivo vazio ou com placeholders não conta como pesquisa. O readiness check deve devolver `INCONCLUSIVO` ou `FALHA`, nunca `PASSA`.

## 2. Contrato de claims

Cada afirmação material recebe um ID estável. O formato canônico é:

```json
{
  "case_id": "morgan-nick",
  "claims": [
    {
      "id": "C001",
      "text": "A ligação foi registrada às 18h04.",
      "layer": "FATO",
      "source_ids": ["S001", "S002"],
      "primary_source": true,
      "locator": "p. 12, paragrafo 3",
      "confidence": "ALTA",
      "contradiction_id": null,
      "use_in": ["HOOK", "CRONOLOGIA"]
    }
  ]
}
```

Camadas válidas:

- `FATO`: documento oficial, laudo, sentença, registro público ou fonte primária verificável.
- `REPORTADO`: imprensa, entrevista, relato ouFONTE secundária.
- `LENDA`: circula, mas não tem sustentação suficiente; usar apenas para explicar a crença, nunca como fato.
- `HIPOTESE`: hipótese investigativaexplicitamente identificada.
- `INTERPRETACAO`: leitura permitida pelos dados, mas não equivalente a fato.

Regras:

- Toda claim `FATO` tem `source_ids`.
- Toda claim numérica tem fonte e localizador.
- Duas páginas que repetem o mesmo despacho não são duas fontes independentes.
- Fato sem fonte fica fora da narração.
- Divergência numérica vira uma claim separada ou um `contradiction_id`; nunca é arredondada silenciosamente.
- O roteiro pode ser mais fluente, mas não pode criar fato novo durante a escrita.

## 3. Pesquisa de título e rotação

A pesquisa editorial é separada da pesquisa factual:

- `TITLE_RESEARCH.md` registra tema, subtema, ângulo, nicho, formato, idioma, mercado e candidatos;
- cada evidência de demanda, concorrência, autocomplete, Data API ou comentário tem URL, data e limitação;
- `title_research.py` só compara overlap, fórmula e histórico; não produz score de demanda;
- `rotation_audit.py` compara o candidato e o roteiro final com os três episódios anteriores, separando tema, hook, estrutura, ângulo e CTA;
- repetição de tema ou série é permitida quando a prova, a pergunta, o ângulo ou o estado final mudam; `REVIEW` exige aprovação humana e `FAIL` bloqueia.

A pesquisa factual continua sendo pré-requisito: título escolhido não autoriza inventar claim.

## 4. Pesquisa completa para long forense

Um long de 30–70 minutos não é uma biografia automática. A completeness é definida por cobertura útil:

1. **Origem:** nascimento, família, infância e contexto social somente quando muda a interpretação do caso.
2. **Linha de vida:** escola, trabalho, relacionamentos, deslocamentos, tratamentos, conflitos e redes de contato relevantes.
3. **Antecedentes:** separações, processos, dependência, dívidas, conflitos e eventos anteriores, somente quando comprovados e relevantes.
4. **Descoberta:** primeira.notificação, corpo, objeto, ligação, testemunha ou改动 that starts the case.
5. **Investigação:** chamadas, deslocamentos, algoritmos, entrevistas, perícia, documentos e decisões.
6. **Contradigções:** incompatibilidades entre versões, laudos, horários, locais e registros.
7. **Reconstrução:** sequência mínima que explica os fatos confirmados, com graus de certeza.
8. **Desfecho:** o que foi confirmado, descartado, continua aberto e por quê.

Não copie uma biografia inteira. Cada frase biográfica precisa passar neste teste: muda quem tinha acesso, motivo, oportunidade, risco, percepção ou interpretação? Se não muda, mova para o apêndice da pesquisa ou corte.

## 5. Evidência forense

Cada evidência follows a chain:

`EVIDÊNCIA → O QUE MEDE → O QUE PROVA → O QUE NÃO PROVA → HIPÓTESE → DÚVIDA`

O roteiro não pode dizer “foi encontrado DNA” sem explicar o valor probatório. Não pode transformar depoimento de suspeito, memória de testemunha, teoria policial ou limitação de laboratório em fato provado.

Registro obrigatório de evidência:

- physical or documentary item;
- source and date collected or published;
- what the source actually states;
- what can be inferred;
- what cannot be inferred;
- contradictions;
- visual evidence plan and rights status.

## 6. Long de 30–35, 45–60 e 60–70 minutos

O comprimento não é preenchimento. O roteiro precisa conter mais progressão verificada, não fatos repetidos.

Default word windows:

- 30–35 min: 4.200–5.600 words.
- 45–60 min: 6.300–9.600 words.
- 60–70 min: 8.400–11.200 words.

For a forensic channel, use a block structure with a new state change every 30–90 seconds:

1. Cold Open: the verified contradiction.
2. Case question: what the viewer needs to understand.
3. Contexto de vida: somente fatos que alteram a investigação.
4. Discovery: exact time, place, action and reaction.
5. Evidence blocks: each one answers a question and creates the next.
6. Investigation and forensic laboratory.
7. Contradiction and revised hypothesis.
8. Reconstruction with confidence labels.
9. Confirmed, unknown and unresolved.
10. Final question or bridge to the next file.

Para um caso de 30–35 minutos, use pelo menos três camadas: vida e contexto, sequência do caso e investigação posterior. Cada rehook deve mudar evidência, interpretação, cronologia ou risco.

## 7. Short de aquisição

O Short não é uma introdução encurtada do long. É uma promessa separada.

Um Short válido tem:

- visual no primeiro frame que comunique tensão, contradição ou resultado;
- texto na tela com no máximo seis palavras;
- hook falado com no máximo oito palavras nos primeiros três segundos;
- uma ideia só;
- uma claim verificada ou uma lacuna documentada com precisão;
- progressão visível em vez de linguagem dramática repetida;
- payoff antes dos últimos dois segundos;
- loop visual, sonoro e semântico projetado;
- bridge que cria uma razão para abrir o long sem revelar todo o payoff do long.

O Short e o long compartilham o caso ou a pergunta, mas não as mesmas dez primeiras palavras. O Short pode revelar uma parte do caso; o long ainda precisa conter valor não resolvido.

Estrutura recomendada do Short:

`HOOK → SETUP → EVIDENCE → TURN → PAYOFF → BRIDGE → LOOP`

CTA deve ficar no comentário fixado ou no related video quando quebrar o loop. Não use linguagem genérica de inscrição, like ou “assista até o fim”.

## 8. Ponte do funil

Antes de publicar, registre em `SHORT_FUNNEL.md`:

- long alvo e ID do caso;
- claim usada pelo Short;
- pergunta que o Short abre;
- questão sem resposta que ele envia para o long;
- beat do long que expande essa questão;
- loop visual e sonoro;
- comentário fixado;
- link do related video;
- métrica a observar em D+2 e D+7.

O funil só é válido quando o Short é satisfatório sozinho e o long é valioso sozinho. O Short não pode ser clickbait; o long não pode começar como se o Short já tivesse contado a história inteira.

## 9. Compliance e confiança

- Pessoa viva é descrita como `suspeito`, `acusado`, `alegado`, `condenado` ou `inculpado`, conforme o status jurídico verificado.
- Não invente diálogo, memória, motivo, resultado de DNA, confissão, conclusão pericial ou pensamento privado.
- Omitir detalhe gráfico, salvo quando estritamente necessário e lícito; foque em prova e consequência.
- Livros, processos, laudos oficiais, entrevistas e jornalismo confiável devem ser identificados.
- O narrador deve declarar a incerteza quando o registro for incerto.
- A resposta final distingue `estabelecido`, `provável`, `possível` e `desconhecido`.

## 10. Gate final

Um long não é aprovado para voz até que tudo isto seja verdadeiro:

- `PESQUISA_BRIEF.md` está preenchido;
- `TITLE_RESEARCH.md` e `TITLE_RESEARCH.json` registram candidatos, evidências e decisão humana;
- `ROTATION_AUDIT.json` é PASS ou tem REVIEW aprovado contra os três episódios anteriores;
- `PROMPT_STATUS.json` é PASS antes de motion;
- `CLAIMS.json` não tem claim material sem fonte;
- `LINHA_DO_TEMPO.md` tem eventos reais, não placeholders;
- o roteiro usa IDs de claim ou permite mapear cada frase material a uma claim;
- o roteiro não tem cena, diálogo ou resultado forense inventado;
- o comprimento corresponde à duração escolhida;
- cold open, rehooks, cascade de evidências, contradição, reconstrução e payoff final existem;
- o Short tem plano, narração, bridge e loop próprios;
- `SHORT_QA.json` valida o vídeo final, frame 1, duração e loop visual;
- `ROTEIRO_MAP.json` corresponde à narração e não deixa claims órfãs;
- `script_builder.py --strict` e `lint-roteiro.py` passam;
- `timing_audit.py` confirma a duração real depois da voz;
- `research_audit.py --strict` confirma fontes, localizadores, confiança e independência;
- `script_scorecard.py` atinge o threshold do lane;
- `script_feedback.py` e `calibration_audit.py` só geram propostas após métricas reais, nunca alteram regras sozinhos.

Se a pesquisa estiver incompleta, o resultado correto é `INCONCLUSIVO`, não um roteiro mais convincente.
