# Modelo — Surtos e bio-riscos (investigação de surtos modernos)

> Categoria: Forense/médico · Subnicho: investigação de surtos modernos e bio-riscos · Slug: `forensic-epidemics`
> Lane: long-first · Idioma: en (docs PT-BR) · RPM (classe): $10–18 [ALEGADO]
> Validação: **REPROVA** em 2026-09-22 (ver `evidencia.md`). 0/15 canais pequenos passaram os 3 gates nas duas coletas; 1 outlier micro (5,7×) e nenhum emergente. Não lançar como canal amplo de "outbreak investigation"; revalidar com caso nomeado (janela Ebola RDC 2026) em 2–4 semanas.
> **Diferenciação obrigatória:** o modelo vizinho `dark-history-pandemics` (pandemias históricas) REPROVA. Este modelo é investigação de surto **moderna** — epidemiologia de campo, caça ao caso índice, genômica, resposta institucional. Nunca história de pragas (Peste Negra, cólera vitoriana, gripe de 1918) como eixo.

## 1. Posicionamento (1 frase)

Reconstrução forense de surtos modernos, do caso índice ao boletim oficial, para espectadores de 25 a 54 anos que querem o método da investigação (linha do tempo, curva epidêmica, rastreamento de contatos, genômica) em tom científico, sem pânico.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália). Consome FRONTLINE/PBS, Radiolab, podcasts de saúde pública (`Patient Zero`, `Febrile`, `Epidemic`), noticiário de surtos e cursos de epidemiologia; inclui estudantes de medicina, enfermagem e saúde pública e profissionais de vigilância.
- **Promessa do canal:** em cada episódio, a anatomia de uma investigação de surto real — quanto tempo o sistema demorou a enxergar, como a linha do tempo foi montada, o que o laboratório provou, onde a resposta falhou e o que mudou na vigilância depois.
- **Inimigo da promessa:** pânico ("a próxima pandemia vai matar…"), previsão apocalíptica, culpa a "paciente zero", estigma a comunidades, sensacionalismo, conselho médico, origem política afirmada como fato.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Caça ao caso índice / "patient zero" (Ebola 2014 e RDC 2026; AIDS e a reatribuição genômica) | média — cluster mediu 18 canais, quase todos micro; termo vive de ficção e podcast | baixa-média | linha do tempo da investigação + genômica que confirmou ou derrubou o culpado |
| Anatomia de superespalhamento (ensaio de coro, funerais, corredor de hotel, cruzeiros) | média — coberto por BBC/FRONTLINE; autocomplete puxa "episode 1 / part 1 / full" | baixa | reconstrução pessoa-lugar-tempo + o que tornou o evento supercrítico |
| Resposta institucional e falhas (demora da OMS, atraso de diagnóstico, ativação do EOC) | média-alta — termo contaminado por "covid" e notícia | alta | avaliação com documento oficial, sem politiqueiro |
| Acidentes de laboratório e biossegurança (Birmingham 1978, Sverdlovsk, incidentes do CDC) | baixa-média (não medida — revalidar) | baixa | níveis BSL, relatório de incidente, o que a norma mudou |
| Salto zoonótico e emergência (Nipah, MERS, H5N1, mpox) | média (não medida — revalidar) | baixa-média | a cadeia do spillover + One Health, com fonte por etapa |

> "Demanda" e "saturação" marcadas como leitura qualitativa da coleta de 2026-09-22 (`evidencia.md`); só o autocomplete do termo principal foi medido (96 termos, catálogo poluído).

## 4. Lane e formato

- **Lane:** long-first — decisão de desenho somada ao formato do nicho adjacente: a reconstrução exige 15–22 min, e o documentário-investigação longo é a referência que performa (FRONTLINE "Outbreak", 4,4M views no YouTube). A coleta **não** trouxe sinal short-first, e nenhum canal pequeno passou os gates — a lane fica como decisão de projeto a validar, não como leitura de dados.
- **Duração alvo:** 15–22 min (PADRÃO); 12–15 min (FINO) para surtos menores; 24–27 min no flagship com arquivo denso. **Cadência:** 1 long por semana + 1 short-teaser na semana do flagship.
- **Mix:** até 20% Shorts. Short é teaser do long do dia; só manter o funil se a conversão estiver medida (`references/21`).

## 5. Fingerprint de formato (o que o recomendador lê)

16:9, 15–22 min, cadência semanal. Voiceover sem rosto, tom de briefing (não de narrativa de horror). Visual recorrente: mapa com pin, curva epidêmica desenhada na tela, line list anonimizada, documento oficial (MMWR/WHO) em close, arte de arquivo dessaturada. Sem trilha épica; drone mínimo ou silêncio. Thumbnail documental com 1 número. Episódios em "files" numerados ("Outbreak File 04: …"). Descrição com capítulos, fontes e camadas [FATO]/[REPORTADO].

## 6. Estrutura de roteiro

- **Beats:** `models/forensic-epidemics/beats.json` (gênero `forensic-epidemics`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). FINO (1.900–2.400) para 12–15 min; RICO (3.400–3.800) para flagships de 24–27 min.
- **Dispositivos:** re-hook a cada 2–4 min, re-engage por volta de 3 min e de 6 min, 3 a 5 open loops nos primeiros 20s, pattern interrupt a cada 30–90s (mapa → curva → documento → entrevista), pergunta central (de onde veio / por que demorou) que só se resolve no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: linha do tempo compilada a partir de relatórios oficiais (MMWR, situação WHO, boletins de ministério), estudo genômico com sequências depositadas, relatório de investigação de campo, inquérito ou auditoria. Nada entra sem 2 fontes e camada [FATO]/[REPORTADO].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** contradição verificada no registro da investigação + relógio do atraso + objeto-símbolo (caixão, lista de convidados, tubo de amostra).
- **Exemplos:**
  1. "The outbreak had been spreading for months, and the only record of it was a guest list at a funeral."
  2. "Fifty-three of the sixty-one people in the room got sick. None of them touched each other."
  3. "The test that would have caught it took two hours. It took five months for anyone to order it."
- **Proibido:** pânico, previsão de próxima pandemia, culpar pessoa ou comunidade, data ou local antes do gancho, abstração, meta-linguagem ("in this video"), conselho médico.

## 8. Thumbnail

- **Composição:** 1 elemento forte (mapa com pin, curva epidêmica, documento em close) + 1 número ou 2–3 palavras + um acento de cor.
- **Paleta:** arquivo dessaturado (cinza, sépia, azul-noite) com um único acento vermelho ou âmbar. **Fonte:** condensed sans bold, legível a 120px.
- **Nunca:** imagem de paciente ou hospital, caveira/praga de pânico, promessa de "próxima pandemia", repetir as palavras do título, foto de pessoa identificável doentes.

## 9. Monetização

- **AdSense (classe):** $10–18 [ALEGADO]. Faixa de saúde/documentário nas estimativas de mercado: wellness $8–18, medical/clinical $15–35 (exige autoridade), média de nichos faceless $11,10 e mediana $10,10, documentário $12,6 em `references/10` [ALEGADO]. A barra depende de execução não-pânico e de não dar conselho médico. Anunciantes plausíveis: seguradoras, telemedicina, streaming documentário, educação [qualitativo, sem número].
- **Produto digital:** dossiê "case file" em PDF ($9–19) com linha do tempo, curva epidêmica, line list anonimizada, documentos oficiais e bibliografia.
- **Patreon/membros:** fontes e documentos antes do vídeo, episódio estendido, votação do próximo caso.
- **Afiliado:** livros de epidemiologia, saúde pública e história das doenças (títulos de editora).
- **Rota no funil (`21`):** short-teaser → inscrito → long → dossiê → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 12–18 h de pesquisa e roteiro + 4–8 h de montagem. Verificação de fonte por etapa é o gargalo real do nicho.
- **Assets:** documentos públicos (CDC MMWR, WHO, boletins de ministério), Wikimedia, arquivos nacionais; mapas, curvas e diagramas procedurais próprios. Footage de agência (Reuters, BBC, AP) exige licença — checar caso a caso antes de entrar no corte.
- **Voz:** edge-tts no protótipo, ElevenLabs na publicação, ritmo pausado (140–150 palavras por minuto). Divulgação de mídia sintética no pacote quando voz ou visual forem gerados.
- **GATE 100%:** sem todas as imagens aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** política de desinformação médica (prevenção, tratamento, negação; exceção educacional/documental) e o balde "persona de IA em temas sensíveis" — um "especialista" sintético dando conselho de saúde não monetiza `[OFICIAL — ref 09]`. O canal é documental por construção: reporta o que a autoridade de saúde disse, nunca recomenda.
- **Pânico / off-putting:** o balde de conteúdo insatisfatório/desagradável mira "temas perturbadores repetidos sem arco coeso" — cada episódio precisa de arco, contexto e conclusão.
- **Pessoas e estigma:** nunca tratar "paciente zero" como culpado. O caso Gaetan Dugas é o estudo de caso do dano (rótulo desmentido por genômica em 2016); comunidades e países nunca são culpados. Pessoas vivas = "according to the report / alleged".
- **Surto em curso (Ebola RDC 2026):** números mudam; carimbar data e fonte em cada dado. Origem política (lab leak, etc.) entra apenas como [REPORTADO], nunca como fato.
- **Inautenticidade:** doença/surto é um dos padrões mais massificados por IA; proteger com 1 peça primária por vídeo, estrutura variável entre episódios e POV próprio.
- **Direitos:** footage de agência de notícia é o maior custo e o maior risco de copyright do nicho.

## 12. 10 ideias-semente (títulos)

1. The Coffin on the Rocky Road: Hunting Patient Zero in Congo's 2026 Ebola Outbreak
2. The Choir Rehearsal: 61 Singers, 53 Infections, Zero Contact
3. The Last Smallpox Death on Earth: Birmingham, 1978
4. The Wind From Compound 19: Anthrax in Sverdlovsk
5. The Label That Was Wrong: AIDS, Patient Zero, and the Man Who Wasn't
6. Nipah: The Pig Farm Virus That Went on the WHO Watchlist
7. The Corridor That Went Global: SARS and the Metropole Hotel
8. MERS: One Camel Lineage, One Hospital, One Long Year
9. The Letters: 2001 and the Anthrax Investigation That Started With a Mailbox
10. H5N1 in the Dairy Barn: The Outbreak That Was Already Underway

> Todo número, data e afirmação desses títulos precisa de fonte primária na pesquisa do episódio (MMWR/WHO/estudo/relatório de inquérito). Nenhum entra no roteiro sem 2 fontes.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVD/AVP lidos contra a referência de mercado de ~23,7% de retenção média [PRATICANTE, ref `01`]; CTR comparado à mediana da própria conta (o YouTube não publica meta de CTR).
- **D+7:** episódio novo acumulando pelo menos 1.000 views/dia no canal; inscritos crescendo acima de 1% dos views do episódio.
- **Meta de validação em 30 dias:** 3 episódios publicados, cada um com 8.000+ views e soma dos 5 primeiros acima de 10.000. Se 2 ou mais episódios derem outlier de 5× ou mais contra a mediana do canal, o formato está confirmado e o modelo pode ser promovido em novo scan com caso nomeado.
