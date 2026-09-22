# 25 — Contexto do canal (a skill entende onde está operando)

Cada canal tem **fluxo, convenções e amarras próprias**. Antes de gerar qualquer coisa, a skill precisa **ler o canal** e respeitar o encadeamento — senão produz em cima de um fluxo já amarrado e quebra tudo.

## Passo 1 — Escanear o canal

```bash
python scripts/channel_scan.py "C:/Users/Liiiraa/Downloads/canal dark1"
```
Reporta: arquivos de contexto (branding, metadados, pipeline, template), estado de cada vídeo (roteiro/tease/imagens/áudio/final/thumbs/pacote), o **próximo a produzir** e a **corrente de teaser**.

## Passo 2 — Ler as convenções travadas do canal

Antes de gerar, leia (na pasta do projeto):
- `CALENDARIO*` — ordem/datas dos casos e séries.
- `REGRA_METADATA*` — títulos/descrições/chapters/tags.
- `TEMPLATE_ROTEIRO*` — blocos, tamanhos ("PORTE"), regras de voz.
- `PIPELINE*` — cadência, regras de estoque, tempos.
- `PROTOCOLO_ANTI_INAUTHENTIC*` — variação obrigatória.
- `BRANDING*` — identidade visual/voz.
- O playbook do canal na skill (`playbooks/<canal>/profile.md` + `operacao.md`).

## A CORRENTE DE TEASER (armadilha crítica)

No Cold File Diaries, **o fim de cada vídeo anuncia o caso do dia seguinte pelo nome**:
> *"And tomorrow — New York, nineteen ten ... Dorothy Arnold of New York ... The full file — tomorrow night."*

Isso amarra os vídeos em corrente:
```
videoNN  --(outro cita)-->  caso do videoNN+1
videoNN  --(tease.txt)---->  Short Padrão 4 (blocos do meio + CTA específico)
```

### Consequência: mudar o fluxo exige regerar
Se você **reordenar, inserir ou remover** um caso no calendário:

1. **Atualize** o `CALENDARIO_30.txt`.
2. **Regere o outro/teaser do vídeo ANTERIOR** (ele cita o caso que mudou).
   - No projeto: refazer voz + motion + tail + short do vídeo anterior.
3. **Regere o `tease.txt`** do vídeo afetado e o **Short (Padrão 4)** correspondente.
4. **Rebuild** dos vídeos tocados (`build_video.py videoNN --from voz`).
5. Se um vídeo sair/entrar, **conserte a ponta** antes e depois dele.

> Regra: **a corrente não pode ter buraco nem apontar para o caso errado.** O `channel_scan.py` mostra a corrente; revise-a após qualquer mudança de grade.

## Passo 3 — Operar dentro do fluxo

- **Nunca** escolha o caso por conta própria num canal com calendário travado — use o caso do dia/dia+1.
- Respeite a **regra rolante** (produzir o dia+1) e a **série do dia da semana**.
- Ao gerar roteiro, o bloco `CHAVES+OUTRO+TEASER` **já deve citar o próximo caso do calendário**.
- Ao gerar Short, use o `tease.txt` (Padrão 4) e o CTA específico.

## Passo 4 — Se o canal NÃO tiver calendário (canal novo)

Use `/dark-lancar` para criar: nicho → séries → calendário → branding → settings. A partir daí a corrente passa a valer.

## Checklist de contexto (antes de gerar)

- [ ] Rodei `channel_scan.py` e li a corrente.
- [ ] Sei o **caso do dia** e o **caso do dia+1**.
- [ ] Li as regras travadas do canal (metadata, template, pipeline, anti-inauthentic).
- [ ] O outro/teaser do vídeo **anterior** aponta para o caso certo.
- [ ] Se mudei a ordem, **regenerei** o vídeo anterior + tease + Short afetados.
- [ ] Respeitei a série do dia da semana e o PORTE.

## Multi-canal

A skill serve vários canais. Sempre identifique **qual** (pelo `FOCUS.md` ou perguntando) e carregue o perfil + contexto daquele canal — as convenções NÃO são intercambiáveis (voz, idioma, séries, metadados, fluxo).
