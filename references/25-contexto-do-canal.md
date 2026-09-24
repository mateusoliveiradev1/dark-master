# 25 — Contexto real do canal

A skill precisa operar dentro do fluxo real do canal. Arquivo, calendário e regras do projeto têm precedência sobre notas antigas.

## Scan obrigatório

```bash
python scripts/channel_scan.py "<pasta-do-canal>" --today AAAA-MM-DD --json
```

O scanner:

- encontra o `CALENDARIO*` real;
- lê data, `videoNN`, caso, série e status;
- exclui pastas auxiliares, `video--help` e recaps;
- detecta apenas `videoNN`, `EPNN` ou `episodeNN` regulares;
- separa estado de Long, Short, roteiro, pesquisa, áudio, captions, imagens, thumbs e pacote;
- calcula estoque futuro, dia atual, próximos 7 dias, próximo a produzir e corrente de teasers;
- mostra a verdade do disco, não apenas o texto “PRONTOS” no calendário.

## Prontidão real

Um vídeo só aparece como `pronto` quando possui:

1. pesquisa aprovada;
2. `narration_v3.txt` ou narration canônico;
3. imagens completas conforme o porte declarado;
4. voz final canônica;
5. `captions.srt`;
6. `videoNN_YOUTUBE.mp4` ou `videoNN_FINAL.mp4`;
7. `videoNN_SHORT.mp4`;
8. pelo menos 3 thumbnails;
9. `youtube_package.txt` sem `PENDENTE`, com título e chapters válidos.

Backup, arquivo parcial, peça temporária ou qualquer MP4 dentro de `_parts` não conta como final.

Estados:

- `pronto`
- `validar_acessorios`
- `montagem`
- `imagens`
- `roteiro`
- `backlog`
- `ausente`

## Fontes de contexto

Ler no projeto:

- `CALENDARIO*`
- `REGRA_METADATA*`
- `TEMPLATE_ROTEIRO*`
- `PIPELINE*`
- `PROTOCOLO_ANTI_INAUTHENTIC*`
- `BRANDING*`
- `CHECKLIST*`

Ler na skill:

- `config/FOCUS.md`
- `playbooks/<canal>/profile.md`
- `playbooks/<canal>/operacao.md`
- `playbooks/<canal>/outliers.md`

Playbook descreve o canal; não é copiado para canais novos.

## Mapeamento publicado

O relatório cruza:

```text
data/caso/série + título publicado + formato → videoNN
```

Regras:

- título exato e formato compatível podem ser confirmados automaticamente;
- ambiguidade exige confirmação do usuário;
- sem título, data ou duração, o item fica `unmatched`/`unknown`;
- dois IDs na mesma tag/par formato entram em `conflitos_mapeamento`;
- não inferir caso de uma métrica isolada.

Depois da confirmação, o vínculo é persistido no banco para D+2, D+7, tráfego e retenção.

## Corrente de teasers

```text
videoNN --(outro cita)--> caso do videoNN+1
videoNN --(tease.txt)---> Short Padrão 4 / CTA específico
```

O scanner compara o caso esperado com o final do narration e marca:

- `ok`: próximo caso comprovado;
- `revisar`: sem menção inequívoca.

Se o calendário mudar:

1. atualizar `CALENDARIO*`;
2. revisar o vídeo anterior;
3. regenerar voz/motion/outro apenas se aprovado;
4. regenerar `tease.txt` e Short afetado;
5. validar novamente o scan;
6. registrar a mudança no experimento/checkpoint.

## Uso pelo `/dark-revisar`

A análise só produz recomendação de calendário depois de:

1. rodar o scanner;
2. validar estoque e corrente;
3. cruzar métricas com `videoNN`;
4. medir impacto e retrabalho;
5. respeitar regras travadas;
6. pedir aprovação.

O scanner nunca altera arquivos. Ele é a fonte de diagnóstico; `/dark-build` continua sendo responsável por produção.
