# Modelo — Aviação e acidentes (acidentes aéreos, desaparecimentos e investigações)

> Categoria: Sobrevivência · Subnicho: acidentes aéreos, desaparecimentos e investigações de aviação · Slug: `survival-aviation`
> Lane: long-first · Idioma: en (docs PT-BR) · RPM (classe): $8–14 [ALEGADO]
> Validação: **PARCIAL** em 2026-09-22 (ver `evidencia.md`). O scan bruto `aviation disaster documentary` deu **REPROVA** nos gates rígidos (1/8 canais passa — Koda Aviation, 42d); o retry `plane crash documentary` repetiu 1/5 (mesmo canal). Fome em 3 canais (outliers de 33,9×, 18,8× e 6,1×) e 3 emergentes de 79–89 dias sustentam a watchlist. Revalidar em 2–4 semanas antes de escalar.
> Diferenciação: este modelo cobre **aviação** (acidente, desaparecimento, investigação, fator humano e segurança operacional). Fenômeno aéreo inexplicado/UFO pertence a `mystery-sky`; naufrágio a `survival-shipwrecks`; desastre industrial a `dark-history-disasters`. Não sobrepor os três.

## 1. Posicionamento (1 frase)

Anatomia documental de acidentes aéreos e desaparecimentos — a cadeia de causas, a investigação oficial e o que mudou na segurança depois — para espectadores de 25 a 54 anos que querem o relatório, não o espetáculo.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália). Entusiasta de aviação, passageiro frequente e consumidor de documentário não gráfico. Já consome Mentour Pilot, Green Dot Aviation, Mayday: Air Disaster e as análises escritas da Admiral Cloudberg; lê relatório do NTSB/ATSB por hobby. Observação da coleta: as âncoras do nicho são seniores e de long-form; os rompimentos pequenos da coleta são majoritariamente short-form — o lane long-first EN tem âncoras fortes e poucos entrantes recentes.
- **Promessa do canal:** em cada episódio, o arco completo — o voo normal, a cadeia de falhas, o que os investigadores provaram e o que a indústria mudou por causa disso.
- **Inimigo da promessa:** especulação vendida como fato, "veja acontecer", imagem de vítima, gore, reencenação de TV reutilizada, culpa individual sem relatório final, número sem fonte.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Acidentes icônicos e a investigação (Tenerife, JAL 123, AF447, Concorde, 737 MAX) | alta — "air crash investigation" é termo de topo no autocomplete | alta no formato reenactment/repost; média no formato análise técnica | cadeia de causas + achado do relatório + mudança regulatória |
| Desaparecimentos aéreos (MH370, Star Dust, voos sem rastro) | alta e durável | média, com muito conteúdo especulativo | o que a investigação provou × o que é teoria ([FATO]/[REPORTADO]/[LENDA]) |
| Falhas sistêmicas e de projeto (rudder hardover, fadiga de metal, MCAS, fogo de carga) | média-alta | baixa em EN com animação de sistemas | engenharia explicada em diagrama + AD/boletim de serviço |
| Sobrevivência e resgate (pouso forçado, amaragem, sobreviventes) | média-alta — outlier de 18,8× em "He Survived a Plane Crash…" | média | fator humano + ciência da sobrevivência + resgate |
| Segurança operacional moderna (quase-acidentes, incursões de pista, por que voar é seguro) | média | baixa em long-form | dado oficial + o sistema que impede a repetição (arco de segurança) |

## 4. Lane e formato

- **Lane:** long-first — justificativa com número: as âncoras EN do nicho são long-form (Mentour Pilot 25–51 min; Green Dot Aviation 14–43 min; Mayday 44:33) e há um entrante novo declarado de long-form em 2026 (Planes Gone Wrong). O rompimento pequeno da coleta é majoritariamente short-form (Koda Aviation, 42d, outlier 33,9×; It's Aviation, mediana ~9,9M views/vídeo) — oportunidade de aquisição, não de receita. Ver `evidencia.md`.
- **Duração alvo:** long 18–24 min (flagship 30–45 min) · short 20–28s. **Cadência:** 1 long/semana + 1 short a cada 2–3 semanas.
- **Mix:** ≤20% Shorts (lane long-first, `30`). Short é sempre teaser do episódio (aponta para o long do dia) e o funil é medido (`21`); se não medir, cortar Shorts.

## 5. Fingerprint de formato (o que o recomendador lê)

Long 16:9, 18–24 min, cadência semanal estável; thumbnail de arquivo dessaturada com 1 elemento de aeronave (silhueta, cockpit, instrumento, rota no mapa) + 1 número/ano + 3–5 palavras; narração em voiceover, tom contido, ritmo pausado; diagramas e animações próprios de sistemas (o diferencial visível da Green Dot); descrição com capítulos e fontes citando o relatório; série nomeada ("The Chain 04: …" ou equivalente); zero footage de reencenação de TV; Short 9:16 ocasional com o mesmo enquadramento e identidade visual.

## 6. Estrutura de roteiro

- **Beats:** `models/survival-aviation/beats.json` (gênero `survival-aviation`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). FINO (1.900–2.400) para incidentes menores; RICO (3.400–3.800) para flagships de 24–27 min.
- **Dispositivos:** re-hook a cada 2–4 min (nova peça do relatório); re-engage ~3 e ~6 min; 3–5 open loops nos primeiros 20s; pattern interrupt a cada 30–90s (arquivo → diagrama animado → transcrição → mapa de rota); pergunta central (por que a cadeia não foi interrompida) resolvida só no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: relatório final (NTSB, BEA, AAIB, ATSB, TSB, CENIPA, MAK), transcrição de CVR/FDR, docket do NTSB, Airworthiness Directive (FAA/EASA), boletim de serviço do fabricante, dado de segurança (IATA/ICAO). Nada entra sem 2 fontes cruzadas e camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada do registro (manutenção, instrumento, transcrição) + relógio (minutos exatos até o impacto).
- **Exemplos:**
  1. "Both engines were still running when the crew shut one down. The recorder shows why they were sure."
  2. "The pitot tubes froze at cruise altitude. Four minutes and twenty-three seconds later, the aircraft was in the Atlantic."
  3. "A tail strike was patched in 1978. Seven years later, the patch failed at 24,000 feet."
- **Proibido:** data/local antes do gancho; gore; imagem ou último momento de vítima; culpar pessoa viva sem "alleged"; teoria como fato; meta-linguagem ("in this video").

## 8. Thumbnail

- **Composição:** 1 elemento de aeronave (silhueta, cockpit, instrumento, rota no mapa) + 1 número/ano + 3–5 palavras. O número carrega a promessa; a aeronave dá o contexto.
- **Paleta:** dessaturada (cinza-slate, azul-noite) com um único acento (âmbar de instrumento ou vermelho de alerta). **Fonte:** condensed sans bold, alto contraste, legível a 120px.
- **Nunca:** cena de impacto, fogo com pessoas, corpos, vítimas identificáveis, footage de reencenação de TV, sensacionalismo ("SHOCKING"), repetir as palavras do título.

## 9. Monetização

- **AdSense (classe):** $8–14 [ALEGADO]. Em `references/10`, Documentário aparece em ~$12,6 e Dark History em ~$11–13 [ALEGADO]; a AIR Media-Tech mede mediana real de $2,30 em 300 canais e alerta que a dispersão dentro do nicho é maior que entre nichos [PRATICANTE] — a classe depende de execução não gráfica, público Tier-1 e ad-load. O contexto documentário é fator explícito de elegibilidade (YouTube Help) e a política de ago/2026 passou a permitir monetização de conteúdo educacional/documentário que retrata morte [OFICIAL/REPORTADO] — mas imagem gráfica na thumb/15s derruba para limited ads. Anunciantes plausíveis: companhia aérea/turismo, seguro, educação, streaming e VPN (patrocínio recorrente no nicho) [ALEGADO/REPORTADO].
- **Produto digital:** tripwire de $9–19 — dossiê em PDF com linha do tempo, diagramas do sistema, trechos do relatório e bibliografia.
- **Patreon/membros:** acesso antecipado, corte estendido da investigação e leitura guiada do relatório final.
- **Afiliado:** livros de aviação, história e fator humano.
- **Rota no funil (`21`):** short → inscrito → episódio long → dossiê/produto → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 10–16 h de pesquisa/roteiro + 6–10 h de montagem/animação. **Assets:** dockets e relatórios de agência (obra do governo dos EUA é domínio público; demais agências: checar termos caso a caso), fotos de Wikimedia Commons/Library of Congress/NARA (licença por arquivo), diagramas, mapas de rota e animações de sistema próprios; transcrições oficiais em vez de áudio de ATC de terceiros; **nunca** footage de reencenação de TV (Mayday/National Geographic/Discovery).
- **Voz:** TTS de qualidade (edge-tts no protótipo, ElevenLabs na publicação), ritmo pausado (~140–150 palavras por minuto). Divulgação de IA no pacote quando voz/visual forem sintéticos.
- **GATE 100%:** sem todas as imagens/diagramas aprovados, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** morte é o núcleo do tema. Mitigação: foco em causa, investigação e resposta; zero gore; zero imagem de vítima; thumb sem cena de impacto; casos com suicídio ou terrorismo entram como alto risco e não viram flagship; relatório preliminar é tratado como preliminar.
- **Conteúdo inautêntico:** o nicho tem muito repost de TV e slideshow TTS genérico — exatamente o perfil que a política mira. O modelo se protege com 1 peça primária por episódio (relatório/docket/transcrição), animação própria e estrutura que varia entre episódios.
- **Vítimas e famílias:** sem imagem de vítima, sem áudio de gritos, sem reconstituição do último minuto de vida; números só com fonte; memória tratada com respeito (o "arco de segurança" é a homenagem).
- **Direitos:** reencenação de TV, áudio de ATC de terceiros e imagens de radar/ADS-B têm licença restrita — usar transcrição oficial, dado aberto e arte própria.
- **Pessoas vivas:** pilotos e mecânicos citados apenas com "according to the report/alleged" até decisão final; nunca afirmar culpa individual sem relatório ou tribunal.
- **Especulação:** MH370 e afins exigem separação explícita entre o que o relatório provou e o que é teoria; nada de teoria como isca.

## 12. 10 ideias-semente (títulos)

1. Tenerife 1977: The Clearance That Never Came
2. Japan Air 123: The Repair That Waited Seven Years
3. Air France 447: Four Minutes and Twenty-Three Seconds
4. The Gimli Glider: The Fuel Math That Was Half Wrong
5. Qantas 72: The Computer That Pitched the Plane Down
6. MH370: The Seven Hours of Handshakes
7. Alaska 261: The Tail That Ran Out of Grease
8. Helios 522: The Ghost Flight Over the Aegean
9. United 232: Flying a DC-10 With Throttles Alone
10. British Midland 92: The Engine They Switched Off

> Todo número, data e afirmação desses títulos precisa de fonte primária na pesquisa do episódio (relatório final, docket, transcrição). Nenhum entra no roteiro sem 2 fontes.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVD/AVP lidos contra a referência de mercado [PRATICANTE, ref `01`]; CTR comparado à mediana da própria conta.
- **D+7:** episódio novo acumulando ≥1.000 views/dia; inscritos crescendo acima de 1% dos views; se houver Short, cliques no long medidos (funil).
- **Meta de validação em 30 dias:** 4 longs publicados; soma dos 5 primeiros ≥10.000 views; 2+ episódios com outlier ≥5× contra a mediana do canal → o formato confirma e o modelo pode subir para PASSA em novo scan (com novos entrantes ≤45d).
