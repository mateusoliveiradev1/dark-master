# Learnings — o que a skill aprendeu (com evidência)

> Formato: `[data] observação — evidência — decisão`.
> Só entra aqui o que tem evidência (dados de `data/metrics.csv` ou teste documentado). Propostas de mudança de REGRA vão para `/dark-revisar` e exigem aprovação.

## Regras aprendidas

- [2026-09-21] **Hipótese forte, ainda não regra:** Springfield Three (Short, AVP **136%**) rendeu 7,30h e 4 inscritos, enquanto Yuba teve AVP 43,58%. AVP >100% indica rewatch; com um caso, não prova que o loop causou alcance. Manter como hipótese e testar 4–6 Shorts comparáveis.
- [2026-09-23] **Longs têm cohort pequena e concentrate valor nos que chegam.** Zodiac e Cooper estão acima da mediana de AVD/watch hours, mas a mediana de alcance segue baixa e a maioria dos longs tem poucas views. O gargalo é **distribuição/embalagem**, não retenção isolada.
- [2026-09-17] Hook em 2ª pessoa + número impossível + pergunta aberta performou (Cooper Short ~1.190). → **PADRÃO SHORT 2, travado.**
- [2026-09-17] Karaokê que conta a história no mudo + detalhes concretos + loop aberto performou (Springfield ~1.180). → **PADRÃO SHORT 3.**
- [2026-09-17] Hook abstrato/filosófico ("The question is not...") derrubou o alcance (video01). → **PROIBIDO abstração no hook.**

## Hipóteses em teste

- Funil Short→long: os longs têm poucas views; medir se Related Video + comentário fixado + CTA elevam.
- Auto-dub: medir watch time por idioma após ligar.
- Testar **loop fim→começo** como uma variável, sem usar AVP >100% como prova causal de distribuição.
- [2026-09-23] **Voz Remy (Edge) — constância e pronúncia.** Teste de escuta do dono no video01 (Eliza Samudio, PT-BR): "ainda tinha partes que a voz mudava e algumas pronúncias erradas". O arquivo ouvido foi gerado com o mapa de entrega ANTIGO (rate/pitch trocando quase a cada bloco = variação audível) → fixes aplicados no `gerar_voz_pt.py` (mapa em 3 zonas hook/corpo/outro, fades de 20ms nas emendas, concat re-encode) **ainda NÃO validados em escuta**. Pronúncia: "Samudio"→respell "Samúdio" aprovado; demais nomes pendentes de calibração (`scripts/calibrar_pronuncia.py`). *(evidência: teste documentado 23/09)*
- [2026-09-23] **Pronúncia: pack aprovado de ouvido.** `rottweiler`→"rótiváiler" (**perfeito**) e `Vespasiano`→"Vespaziano" (**normal**) aprovados pelo dono nos áudios de `02_audio/_pronuncia/`; `Samudio`→"Samúdio" já aprovado na calibração. `Dayanne`→"Daiane" verificado por ida-e-volta na frase real ("Daiane foi absolvida...") — pendente oitiva. Rede automática: `voice_engine --pronounce` usa **a frase da própria narração** como contexto (carrier genérico lia pior) e o pack vale na produção via patch do `gerar_voz_pt.py`. Cronologia: `lint-roteiro --cronologia` + `timeline_kit` (plate + datestamps).

## Descartado (não repetir)

- Shorts com rewatch abaixo da coorte ainda precisam de teste controlado; não registrar “gastam alcance” como regra geral.

## Revisão semanal — 2026-09-23

- **Coleta real concluída:** 16 vídeos entre 22/08 e 20/09; 31,05 horas de exibição públicas acumuladas. A métrica norte subiu, mas o crescimento continua concentrado em poucos vídeos com alta retenção, não em uma base saudável de longs. *(evidência: `data/metrics.csv`, API)*
- **Baseline corrigida:** 8 Shorts confirmados com mediana de **81 views** e 8 longs confirmados com mediana de **19 views**; todos os 16 mapeamentos estão confirmados. Os três Shorts históricos de 1.218–1.253 views são outliers, não a mediana. *(evidência: banco + `data/metrics.csv`; captura de 2026-09-23)*
- **Shorts têm distribuição muito desigual:** três outliers têm 1.218–1.253 views; os cinco demais estão entre 1 e 86 views. `SHORTS` somou 3.574 views e representa navegação vertical entre Shorts, não conversão Short→Long. Sem impressões/CTR, ainda não dá para separar empacotamento de distribuição. *(evidência: Analytics API, 81 linhas de tráfego)*
- **Funil ainda não está fechado:** há 20 views de `RELATED_VIDEO`, mas nenhum par Short→Long pôde ser atribuído porque os IDs de origem não pertencem ao conjunto mapeado; portanto não se atribui causalidade ao funil. *(evidência: `traffic_sources`)*
- **Prioridade proposta:** testar somente o título nos próximos longs e instalar o Long como vídeo relacionado nos próximos 4 Shorts. Loop permanece hipótese; Short 2/3/4 e FOCUS continuam travados.

## Mudanças de regra propostas (aguardando aprovação)

- **Nenhuma alteração de regra travada nesta revisão.** Os testes abaixo são experimentos e não mudam `REGRA_METADATA*`, `FOCUS.md` ou os padrões Short 2/3/4.

## Experimentos propostos (uma variável por vez)

1. **Loop no próximo Short:** manter hook concreto + loop fim→começo sem alterar tema nem CTA; medir AVP, engaged views e inscritos em D+2/D+7. `shown-in-feed` só entra se vier do Studio. Risco: uma amostra não prova causalidade.
2. **Embalagem de Short:** testar somente o título, mantendo thumbnail, teaser e CTA; medir alcance, AVD, engaged views e inscritos. Risco: o tema continua sendo uma variável de confundimento.
3. **Funil Short→Long:** adicionar somente o Long como vídeo relacionado; medir `RELATED_VIDEO`, detalhe, views e horas. Comentário fixado e CTA verbal ficam para testes separados.

## Próximo checkpoint

- **D+2/D+7:** repetir a captura diária; a consulta de 2026-09-23 retornou 16 títulos, datas e durações com 16 mapeamentos confirmados.
- **Studio:** importar shown-in-feed, chose-to-view, CTR e impressões somente se a coleta automática não conseguir; não estimar.
- **Mapeamento:** 16 IDs confirmados, 0 pendentes e 0 conflitos; atribuições de `RELATED_VIDEO` continuam abertas porque os IDs de origem não têm correspondência no conjunto.
- **Decisão pendente:** nenhuma mudança de regra; se os testes confirmarem padrão, pedir aprovação explícita antes de alterar qualquer referência travada.
