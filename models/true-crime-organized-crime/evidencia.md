# Evidência — Crime organizado (máfia, cartéis e organizações criminosas)

> Coleta: 2026-09-22 · método: `python scripts/niche_scan.py --brief "organized crime documentary" --max 8` + 1 busca estreita (`--cluster "mafia documentary" --max 8`) + leituras pontuais de canal (`--channel @CiampiRendo`, leitura direta de uploads dos canais-evidência) + `--suggest`/`--trends` + websearch (6 consultas)
> Brief completo: `data/briefs/organized-crime-documentary.md` · JSON: `data/briefs/organized-crime-documentary.json`
> A saída do `--cluster` rodou sem `--out`; os números estão transcritos abaixo.

## Veredito: **REPROVA**

- Canais pequenos analisados: **14 no total** (6 no brief + 8 no cluster, com 1 repetido) | passam os 3 gates: **0** (meta ≥3)
- Fome do algoritmo (outlier ≥3×): **3 canais** no brief e **5 canais** no cluster, com 3 outliers de 8× a 28× em canais EN | sinal: **SIM**
- Autocomplete: **84 termos** no brief, **295** em "mafia documentary", **124** em "cartel documentary", **75** em "albanian mafia documentary" (meta ≥15)
- Trends YouTube 12m: "organized crime documentary" **ALTA** (10,25 recente vs 0 anterior, volume baixo e leitura frágil) · "mafia documentary" **ESTÁVEL** (77 vs 74), rising "dixie mafia documentary" (+60%) · "cartel documentary" **BAIXA** (17 vs 22), rising "cali cartel documentary" (+60%) e "sinaloa cartel documentary" (+40%)

> Reprovou nas **duas** queries permitidas, sempre no gate de idade. O sinal de demanda e de outlier é forte; o que não existe é canal de long-form EN com menos de 45 dias passando os três gates. Fato estrutural do lane: documentário long-form publica 1 vídeo por semana, então 5 vídeos levam cerca de 5 semanas e o canal raramente é julgado antes dos 45 dias. Nota metodológica, não pedido de mudança da regra travada.

## Canais-evidência (gates: idade≤45d · 5primeiros≥10k · ≥1k views/dia)

Brief "organized crime documentary" (6 pequenos, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Ashes of Empires | 1.980 | 52d | 156.074 | 10.565 | 011 | 8,8× — 251.636 — "The Real Casino Story Ended 12 Years After the Movie (And It Was Worse)" |
| Endless Night Files | 2.760 | 77d | 427.349 | 6.361 | 011 | 21,4× — 280.456 — "The Albanian Mafia: How They Took Over Europe's Cocaine Trade" · 8,3× — 109.174 — "He Ran Europe's Cocaine Empire From a Prison Cell" |
| World Entertainment Documentaries | 1.430 | 113d | 35.465 | 4.696 | 011 | 0 |
| The Past Port | 4.650 | 123d | 2.890.319 | 194.282 | 011 | 0 |
| Hidden Ops India | 71.300 | 184d | 2.407.706 | 102.709 | 011 | 12,8× — 4.200.979 |
| FBI Investigates | 68.300 | 315d | 859.329 | 80.765 | 011 | 0 |

Cluster "mafia documentary" (43 canais encontrados, 8 pequenos analisados, 0 passam):

| Canal | Subs | Idade | 5 primeiros | Views/dia | Gates | Outliers |
|---|---|---|---|---|---|---|
| Ciampi Rendo | 7.630 | 75d | 287.404 | 251.072 | 011 | 13,0× — 521.234 — "He Gave His Enemy One Last Chance" (2026-09-13) |
| Mafia Talks | 84.300 | 294d | 560.129 | 68.074 | 011 | 28,0× — 749.952 — "The Real Aryan Brotherhood Behind 'Shot Caller' Movie Ran Am..." (2026-09-16) |
| FILMI SAMAA | 9.300 | 362d | 1.082.898 | 13.010 | 011 | 7,5× — 775.235 |
| AniInvox | 9.720 | 286d | 725.115 | 13.167 | 011 | 3,2× — 480.913 |
| Sr Facts Zone | 44.700 | 200d | 1.041.603 | 103.796 | 011 | 0 |
| AniDoc | 168.000 | 280d | 753.528 | 137.104 | 011 | 3,4× — 424.456 |
| Street Files | 35.200 | 343d | 218.326 | 26.486 | 011 | 0 |

Leitura honesta dos quase:

- **Ashes of Empires** (52d) e **Endless Night Files** (77d) passam 2 dos 3 gates com folga (5 primeiros de 156k e 427k; 10,5k e 6,4k views/dia) e são os únicos com formato convergente no lane EN. Faltam 7 e 32 dias, respectivamente, para o gate de idade.
- **Ciampi Rendo** (251k views/dia) e **The Past Port** (194k views/dia) são Shorts, não documentário. O "5 primeiros" de 2,89M do The Past Port é de Shorts de curiosidades (0:19 a 0:22). Não servem como evidência do cruzamento long-form.
- **Hidden Ops India, Mafia Talks, FILMI SAMAA, AniInvox, AniDoc** operam em hindi (Índia). O cluster "mafia documentary" está muito mais quente lá do que em EN.
- **FBI Investigates, Sr Facts Zone, Street Files** passam 2 gates por volume de biblioteca, não por rompimento.

## Outliers (janela de 2–6 semanas)

- **Mafia Talks** — 28,0× — 749.952 views — "The Real Aryan Brotherhood Behind 'Shot Caller' Movie Ran Am..." — 2026-09-16 — padrão: história real comparada a filme conhecido.
- **Endless Night Files** — 21,4× — 280.456 — "The Albanian Mafia: How They Took Over Europe's Cocaine Trade" — 2026-08-03 — padrão: série europeia com hook de impossibilidade e 24 min.
- **Endless Night Files** — 8,3× — 109.174 — "He Ran Europe's Cocaine Empire From a Prison Cell | The Albanian Mafia Part 2" — 2026-08-10 — a continuação segurou 39% do flare, sinal de que a série converte.
- **Ashes of Empires** — 8,8× — 251.636 (leitura posterior no mesmo dia: 251.679) — "The Real Casino Story Ended 12 Years After the Movie (And It Was Worse)" — 2026-08-26 — padrão: história real por trás de filme, 30 min.
- **Ciampi Rendo** — 13,0× — 521.234 — "He Gave His Enemy One Last Chance" — 2026-09-13 — Shorts de 60s de ficção criminal com narração sintética; evidência de saturação do tema em Shorts, não do long.
- **Hidden Ops India** — 12,8× — 4.200.979 — 2026-08-27 — em hindi; confirma o cruzamento tópico organizações criminosas, fora do lane en.

## Fome do algoritmo (cluster cross-canal)

Sinal **SIM**: 3 canais diferentes com outlier ≥3× no brief (Hidden Ops India, Endless Night Files, Ashes of Empires) e 5 canais no cluster. Em EN, dois padrões distintos puxam o algoritmo: "história real por trás do filme" (Mafia Talks 28×, Ashes of Empires 8,8×) e "organização europeia em série" (Endless Night Files 21,4× mais 8,3×). São dois ângulos com fome comprovada na janela de 2 a 6 semanas.

## Convergência de formato (últimos uploads, leitura de 2026-09-22)

| Canal | Últimos 10 uploads | Duração | Convergência |
|---|---|---|---|
| Endless Night Files | 10/10 documentário de organização criminosa | 17:59 a 30:42 | total; série europeia (Albanian Parts 1 a 3, Zemun, Totò Riina, Foxtrot, PCC, 'Ndrangheta, Mocro Maffia, Kinahan); 1 por semana |
| Ashes of Empires | 10/10 documentário "real story vs movie" | 25:42 a 43:52 | total; Casino, Donnie Brasco, Untouchables, Bronx Tale, Godfather; cerca de 2,5 por semana |
| The Past Port | 10/10 Shorts de curiosidades gerais | 0:19 a 0:22 | formato incompatível com o lane |
| World Entertainment Documentaries | 1 long de 40:47 mais 9 Shorts de crime UK | 1:11 a 40:47 | sem convergência (formato misto) |
| Ciampi Rendo | 10/10 Shorts de ficção criminal | 0:53 a 1:01 | formato incompatível; 71 vídeos em 75 dias |

Conclusão de formato: o cruzamento long-form EN existe e converge em dois canais (18–35 min, voiceover, série, arquivo). Os três canais com "número grande" que não convergem são Shorts ou mistos, o que descarta o lane short-first como evidência deste modelo.

## Demanda (autocomplete — top termos)

- "organized crime documentary" (84): organized crime documentary uk · organised crime documentary uk bbc · russian organized crime documentary · canadian/montreal · organized retail crime documentary · organized crime in europe · documentary drug dealer/drugs
- "mafia documentary" (295): 5 families · italy · new york · michael franzese · roy demeo · carlo gambino · al capone · albanian mafia documentary
- "cartel documentary" (124): mexico · sinaloa · kinahan cartel documentary bbc · balkan cartel documentary · cartel documentary 2026
- "albanian mafia documentary" (75): bbc · best · crime · complete

O espaço de perguntas é profundo e durável (organização, época, cidade, país). É demanda de tema evergreen, não de notícia.

## Trends (YouTube 12m)

- "organized crime documentary": ALTA com base frágil (10,25 vs 0).
- "mafia documentary": ESTÁVEL (77 vs 74); rising "dixie mafia documentary" (+60%).
- "cartel documentary": BAIXA (17 vs 22); rising "cali cartel documentary" (+60%) e "sinaloa cartel documentary" (+40%).

## Comentários (demanda explícita)

Não coletado via API: `--comments` retornou `insufficientPermissions` (escopo `youtube.force-ssl` ausente; rodar `python scripts/yt_auth.py` para habilitar). Proxies usados:

- Contagem de comentários nos outliers: 213 (Endless Night Files, 280k views) e 78 (Ashes of Empires, 251k), números altos para canais de 2 a 3 mil inscritos.
- Evidência externa observada em espelhos de YouTube: pedido explícito de episódio sobre a Yakuza em comentário de vídeo de hierarquia da máfia; "Great documentary. Keep them coming." em documentário de 'Ndrangheta; reclamações sobre narração sintética em vídeos do tema ("despite the crappy ai narration"), o que marca a linha entre aceitação do formato e rejeição do conteúdo inautêntico.

## Fontes web

1. https://support.google.com/youtube/answer/9725604 — atualizações oficiais de diretrizes de anúncio: setembro de 2026 inclui conteúdo educativo não glorificador sobre organizações de tráfico de drogas como elegível; agosto de 2026 esclarece representação de morte em contexto documentário.
2. https://support.google.com/youtube/answer/6162278 — diretrizes advertiser-friendly; violência em contexto documentário ou jornalístico tem tratamento próprio.
3. https://longformstudio.app/articles/true-crime-youtube-channel — YPP dobra em 01/02/2027 (8.000 horas ou 20M de views de Shorts, anunciado em 10/08/2026); RPM reportado de $6–9 em true crime não gráfico [ALEGADO]; relato de limited ads aplicado retroativamente em vídeos antigos e petição de criadores.
4. https://www.seattletimes.com/business/youtube-relaxes-monetization-policy-on-videos-with-controversial-content — AP, 16/01/2026: YouTube afrouxou monetização de conteúdo sensível tratado sem descrição ou imagem gráfica.
5. https://becomeviral.com/blog/faceless-youtube-true-crime-niche — RPM de $5–15 [ALEGADO]; patrocínios de $8k–25k [ALEGADO]; formato vencedor de 15–25 min, paleta escura e narração medida.
6. https://sentrismg.com/blog/faceless-youtube-channels-2026 — operador de 4 canais faceless: Blackfiles chegou a 436k inscritos e 53M views em 126 vídeos; episódios de 20 a 37 min; 15 a 20 horas de pesquisa por história; "o playbook de automação acabou".
7. https://faceless.my/youtube/how-much-do-faceless-youtube-channels-make — faixa de RPM faceless em history/true crime de $4–10 [ALEGADO].
8. https://deadline.com/2024/11/mafia-hunters-ndrangheta-beetz-brothers-interview-1236183636 — 'Ndrangheta estimada em até €50 bilhões por ano; produtor alemão afirma que o true crime está esgotando o potencial narrativo e que o caminho é inovar o formato.
9. https://divert.stream/watch/AqYP-bi7S_U — espelho com descrição do outlier do Endless Night Files (85.969 views em 10/08/2026, disclaimer educativo e fontes públicas) · https://divert.stream/watch/rwjwxLpXQW0 — The Mafia Vault, 231.490 views em documentário de casos de informantes.
10. https://redlib.dansworld.org/r/documentaries — feed do r/Documentaries consultado; nenhuma thread específica de crime organizado na amostra (registro de ausência, sem inventar sinal).

## Saturação e riscos observados

- O cruzamento long-form EN ainda admite canal novo: os dois canais convergentes mais jovens têm menos de 90 dias e outliers de 8,8× e 21,4×, sem gigante de formato idêntico dominando o recomendador. O que existe é saturação regional forte em hindi e saturação de Shorts com narração sintética.
- Risco de inautenticidade: o tema virou ímã de Shorts padronizados (71 vídeos em 75 dias em um único canal). Isso atrai re-review de conteúdo e pode contaminar a percepção do nicho.
- Risco de advertiser: violência e drogas são as categorias sensíveis; a janela oficial de setembro de 2026 favorece quem faz análise com contexto educativo e desfavorece quem foca sangue, morte e uso.
- Risco jurídico: muitos personagens vivos. Regra do modelo: vivos = "alleged"; sem endereço ou detalhe operacional atual.

## Queries mais estreitas

Tentadas nesta coleta (as duas permitidas):

- `--brief "organized crime documentary"` → REPROVA (0 de 6 passam).
- `--cluster "mafia documentary"` → REPROVA (0 de 8 passam).

Próximas candidatas para re-scan quando houver quota (uma por vez, sem repetir as duas acima):

- "albanian mafia documentary" — 75 termos de autocomplete e um único canal EN convergente domina a evidência; é o cruzamento mais promissor.
- "ndrangheta documentary" — organização com estimativa de €50 bilhões por ano e documentário de curta duração com 188k views em 13 dias observado no snapshot web.
- "dixie mafia documentary" — única query em alta (+60%) no Trends de "mafia documentary".
- "yakuza documentary" — demanda de comentário observada e cobertura quase nula em EN long-form.
- "cartel documentary" — Trends geral em baixa, mas "cali cartel documentary" (+60%) e "sinaloa cartel documentary" (+40%) em alta; risco de advertiser maior.
