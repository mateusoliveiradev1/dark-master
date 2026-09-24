# 15 — Loop de aprendizado diário

## Ciclo

```
calendário/produção → publicar → capturar → comparar → diagnosticar → propor 1 experimento → medir → aprender
```

1. **Medir diariamente:** `yt_metrics.py` preserva o histórico e consolida repetições do mesmo período.
2. **Ler produção:** `channel_scan.py` cruza data, caso, série, Long, Short, teaser, estoque e prazo.
3. **Comparar:** baseline do próprio canal por formato, duração, idade e série quando a amostra permitir.
4. **Diagnosticar:** separar packaging, hook, retenção, tráfego, conversão e monetização.
5. **Propor:** no máximo 1–3 experiments, uma variável por vez.
6. **Medir:** D+2, D+7, D+30 e captura final, sempre com a data de processamento da Analytics API.
7. **Aprender:** resultado positivo, neutro e negativo entram no estado do experimento.
8. **Promover:** regra somente após evidência repetida; regra travada exige aprovação explícita.

## Checkpoints

| Janela | Pergunta | Ação permitida |
|---|---|---|
| D+0 | o vídeo e o Short saíram corretamente vinculados? | corrigir link, fixado, playlist e relacionado sem trocar o conceito |
| D+2 | houve distribuição inicial? | registrar; não concluir causalidade |
| D+7 | packaging e retenção separaram? | propor uma variável para o próximo vídeo |
| D+30 | houve cauda, inscritos e watch time? | manter, ajustar ou descartar a hipótese |
| Semanal | baseline e estoque continuam saudáveis? | revisar próximos 7 dias e o vídeo do dia+1 |

A Analytics API pode atrasar 48–72h. “D+2” no relatório significa captura de D+2 com o período realmente disponível, não promessa de dado completo.

## Estados de um experimento

- `proposto`: definido, ainda sem aplicação.
- `em_teste`: aplicado a um grupo controlado.
- `positivo`: resultado repetido a favor.
- `neutro`: sem diferença relevante.
- `negativo`: resultado repetido contra.
- `inconclusivo`: amostra, scope ou dados insuficientes.

Cada experiment registra:

- canal e `videoNN`;
- escopo;
- uma única variável;
- hipótese;
- baseline;
- objetivo;
- data inicial/final;
- métrica de decisão;
- risco e fatores de confundimento;
- evidência;
- decisão.

## Evidência

- Um outlier é caso de estudo, não regra.
- AVP/AVD acima da mediana medem retenção ou rewatch; não explicam sozinhos a distribuição.
- CTR só separa packaging de distribuição quando há impressões/CTR válidos.
- Search, browse, related, end screen e Shorts são fontes diferentes.
- `SHORTS` é navegação vertical entre Shorts; não é Short→Long.
- Baseline deve usar mesma janela, formato e idade; comparar maturados com vídeos novos é inválido.
- Resultado negativo é aprendizado e não deve ser apagado.

## Gate de promoção

Não promover automaticamente. Um resultado só vira recomendação persistente quando:

1. há títulos/datas/IDs confirmados;
2. a métrica estava disponível na captura;
3. a comparação usa coorte equivalente;
4. o efeito aparece em mais de um caso ou o caso é explicitamente único;
5. contraevidência foi registrada;
6. qualquer regra travada foi aprovada pelo usuário.

## Ações no calendário

Para cada experimento, o relatório escolhe o melhor candidato futuro:

- **alto impacto, baixo retrabalho:** título ou CTA existente;
- **impacto médio:** thumbnail ou hook de Short;
- **alto retrabalho:** re-render do Long, teaser, motion ou cadeia de publicação;
- **dependência de teaser:** se o caso mudar, listar o vídeo anterior, teaser e Short afetados.

Nenhuma dessas ações acontece sem aprovação.

## Arquivos

- `data/metrics.csv`: leitura legível do snapshot atual.
- banco: histórico, tráfego, retenção, mapeamentos e experiments.
- `data/outliers.json`: sinais e conflitos de mapeamento.
- `data/learnings.md`: decisão humana-readable com evidência.
- playbook do canal: contexto e exceções específicas.
