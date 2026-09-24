# 15 — Outliers e aprendizados

Registro vivo do que funcionou no canal do usuário. **Atualize após cada rodada D+2/D+7.**

## Dados reais (API, consulta encerrada em 20/09/2026)

| Vídeo | Formato | Views | Engaged | AVD | AVP% | Watch h | Subs |
|---|---|---|---|---|---|---|---|
| Yuba County Five | short | 1.253 | 517 | 14s | 43,58% | 2,35 | 1 |
| Springfield Three | short | 1.222 | 536 | 47s | **136,48%** | **7,30** | **4** |
| D.B. Cooper | short | 1.218 | 451 | 22s | 67,21% | 3,07 | 1 |
| Zodiac long | long | 27 | 10 | 2.405s | 298,13% | **6,68** | 0 |
| Gardner long | long | 25 | 23 | 577s | 76,75% | 3,68 | 0 |
| Sodder long | long | 22 | 20 | 122s | 17,03% | 0,67 | **5** |
| D.B. Cooper long | long | 38 | 31 | 161s | 24,67% | 1,38 | 3 |
| Springfield long | long | 16 | 6 | 12s | 1,84% | 0,02 | 0 |
| Yuba long | long | 9 | 3 | 55s | 7,32% | 0,03 | 0 |
| Black Dahlia long | long | 0 | 0 | 0s | 0% | 0 | 0 |
| Circleville long | long | 0 | 0 | 0s | 0% | 0 | 0 |
| Sodder short | short | 25 | 18 | 20s | 52,67% | 0,10 | 0 |
| Zodiac short | short | 76 | 26 | 768s | 2.402,11% | 5,55 | 0 |
| Black Dahlia short | short | 10 | 3 | 38s | 120,25% | 0,03 | 0 |
| Gardner short | short | 86 | 24 | 23s | 68,49% | 0,18 | 1 |
| Circleville short | short | 1 | 1 | 8s | 23,86% | 0 | 0 |

**Total watch hours públicos (30d): 31,05 h.** Use o YouTube Studio para watch hours qualificados do YPP.

### Leitura da captura
- Baseline: 8 Shorts, mediana de 81 views; 8 longs, mediana de 19 views.
- Os três Shorts outliers têm 15,04×–15,47× a mediana do formato, mas a amostra não prova causalidade.
- Springfield combina o maior AVD, AVP acima de 100% e mais inscritos da coorte. AVP indica rewatch; não prova que o loop causou distribuição.
- Zodiac e Gardner mostram que alguns longs concentram watch time quando recebem alcance. O alcance mediano continua sendo o gargalo.
- CTR, impressões, shown-in-feed e chose-to-view não vieram da API. Não estimar.

## Regras travadas derivadas dos Shorts outliers
- **PADRÃO SHORT 2** — 2ª pessoa + número impossível + pergunta aberta. Não reabrir video02.
- **PADRÃO SHORT 3** — hook concreto, karaokê que conta a história no mudo e loop aberto.
- **PADRÃO SHORT 4 TEASE** — 32s, hook + dois blocos do meio + CTA específico para video23+.

## Status em 2026-09-23
- 16 vídeos API, 81 linhas de tráfego e 300 pontos de retenção.
- 4.028 views públicas, 1.669 engaged views e 15 inscritos ganhos no snapshot.
- 16 mapeamentos confirmados; 0 títulos, datas ou durações pendentes.
- `SHORTS` = 3.574 views de navegação vertical; não representa conversão Short→Long.
- `RELATED_VIDEO` = 20 views, mas 0 pares Short→Long confirmados porque os IDs de origem estão fora do conjunto mapeado.

## Protocolo de análise
1. Rodar `/dark-revisar`; ele chama `yt_metrics.py` e `yt_analysis.py`.
2. Preservar o mapeamento confirmado e exigir confirmação antes de ligar novos IDs a `videoNN`.
3. Comparar cada vídeo com a mediana do próprio formato, nunca com benchmark genérico.
4. Testar uma variável nos próximos 4–6 vídeos e registrar resultado, risco e contraevidência.
5. Registrar o que não funcionou e nunca promover um único vídeo a regra.

## Tabela de outliers

| # | Título | Tipo | Duração | Hook | Thumb | Views | Retenção | Subs | Lição |
|---|---|---|---|---|---|---|---|---|---|
| 05 | Yuba County Five | Short | 33s | número + VANISHED | não avaliado no ciclo | 1.253 | AVP 43,58% | 1 | alcance alto não implica retenção alta |
| 03 | Springfield Three | Short | 35s | staccato + concreto + loop | não avaliado no ciclo | 1.222 | AVP 136,48% | 4 | loop é hipótese, não causalidade |
| 02 | D.B. Cooper | Short | 33s | 2ª pessoa + impossível + pergunta | não avaliado no ciclo | 1.218 | AVP 67,21% | 1 | padrão ativo; efeito ainda não isolado |

## Loop D+2/D+7
- Rodar `python scripts/yt_metrics.py --channel @ColdFileDiaries --project "C:\Users\Liiiraa\Downloads\canal dark1" --days 30`.
- Rodar `python scripts/yt_analysis.py --channel @ColdFileDiaries --project "C:\Users\Liiiraa\Downloads\canal dark1" --save-experiments`.
- Repetir a captura diária; comparar o mesmo vídeo quando houver snapshots maduros.
- Propor 1–3 experimentos; uma variável por vez; aprovação antes de alterar produção.
- Prints do Studio só entram com fonte e data declaradas.
