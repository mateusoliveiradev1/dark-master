# Learnings — o que a skill aprendeu (com evidência)

> Formato: `[data] observação — evidência — decisão`.
> Só entra aqui o que tem evidência (dados de `data/metrics.csv` ou teste documentado). Propostas de mudança de REGRA vão para `/dark-revisar` e exigem aprovação.

## Regras aprendidas

- [2026-09-21] **Loop vence.** Springfield Three (Short, AVP **136%**) rendeu 7,25h e 4 inscritos vs Yuba (AVP 43%) com 1 inscrito → projetar **fim→começo** e mirar AVP >100%. *(evidência: API)*
- [2026-09-21] **Long retém quem chega, mas não recebe tráfego.** Zodiac long: AVD 907s com 66 views; Sodder long: 5 inscritos com 20 views. → o gargalo é **tráfego**, não conteúdo.
- [2026-09-17] Hook em 2ª pessoa + número impossível + pergunta aberta performou (Cooper Short ~1.190). → **PADRÃO SHORT 2, travado.**
- [2026-09-17] Karaokê que conta a história no mudo + detalhes concretos + loop aberto performou (Springfield ~1.180). → **PADRÃO SHORT 3.**
- [2026-09-17] Hook abstrato/filosófico ("The question is not...") derrubou o alcance (video01). → **PROIBIDO abstração no hook.**

## Hipóteses em teste

- Funil Short→long: os longs têm poucas views; medir se Related Video + comentário fixado + CTA elevam.
- Auto-dub: medir watch time por idioma após ligar.
- Escalar o padrão de **loop** (AVP >100%) para os próximos Shorts.
- [2026-09-23] **Voz Remy (Edge) — constância e pronúncia.** Teste de escuta do dono no video01 (Eliza Samudio, PT-BR): "ainda tinha partes que a voz mudava e algumas pronúncias erradas". O arquivo ouvido foi gerado com o mapa de entrega ANTIGO (rate/pitch trocando quase a cada bloco = variação audível) → fixes aplicados no `gerar_voz_pt.py` (mapa em 3 zonas hook/corpo/outro, fades de 20ms nas emendas, concat re-encode) **ainda NÃO validados em escuta**. Pronúncia: "Samudio"→respell "Samúdio" aprovado; demais nomes pendentes de calibração (`scripts/calibrar_pronuncia.py`). *(evidência: teste documentado 23/09)*
- [2026-09-23] **Pronúncia: pack aprovado de ouvido.** `rottweiler`→"rótiváiler" (**perfeito**) e `Vespasiano`→"Vespaziano" (**normal**) aprovados pelo dono nos áudios de `02_audio/_pronuncia/`; `Samudio`→"Samúdio" já aprovado na calibração. `Dayanne`→"Daiane" verificado por ida-e-volta na frase real ("Daiane foi absolvida...") — pendente oitiva. Rede automática: `voice_engine --pronounce` usa **a frase da própria narração** como contexto (carrier genérico lia pior) e o pack vale na produção via patch do `gerar_voz_pt.py`. Cronologia: `lint-roteiro --cronologia` + `timeline_kit` (plate + datestamps).

## Descartado (não repetir)

- Shorts sem loop (AVP <50%) gastam alcance: priorizar cortes que emendam.

## Mudanças de regra propostas (aguardando aprovação)

- (nenhuma ainda)
