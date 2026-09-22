# Modelo — Crime organizado (máfia, cartéis e organizações criminosas)

> Categoria: True crime · Subnicho: máfia, cartéis e organizações criminosas · Slug: `true-crime-organized-crime`
> Lane: long-first · Idioma: en (docs em PT-BR) · RPM (classe): $8–15 [ALEGADO]
> Validação: **REPROVA** nos gates rígidos em 2026-09-22 (0/3 canais; ver `evidencia.md`).
> Sinal parcial: 2 canais EN com menos de 90 dias passando 2 dos 3 gates e outliers de 8,8× e 21,4×. Blueprint válido, lançamento condicionado a re-scan que passe os gates.

## 1. Posicionamento (1 frase)

Anatomia documental de organizações criminosas reais (máfias europeias, cartéis e irmandades de prisão) para espectadores de 25 a 54 anos que já consomem true crime e querem estrutura, fonte e número no lugar de sensacionalismo.

## 2. Público e promessa

- **Público:** 25–54, inglês (EUA, Reino Unido, Canadá, Austrália, Irlanda). Já assiste documentário longo de crime, podcast de true crime e ficção de máfia. O que os canais-evidência mostram: audiência que comenta com detalhe (213 comentários no outlier do Endless Night Files, 78 no da Ashes of Empires) e pede episódios específicos.
- **Promessa do canal:** em cada episódio, uma organização por inteiro. Origem, hierarquia, dinheiro, rotas, código interno e a operação policial que tentou desmontá-la, com documento e número.
- **Inimigo da promessa:** gore, glorificação (máfia como estilo de vida), acusação sem fonte, número sem procedência, thumbnail apelativa sem entrega.

## 3. Subnichos cobertos

| Subnicho | Demanda (autocomplete) | Saturação | Ângulo do modelo |
|---|---|---|---|
| Máfias europeias (albanesa, 'Ndrangheta, camorra, Zemun, Kinahan) | alta — 75 termos em "albanian mafia documentary" | baixa em EN (evidência: Endless Night Files) | uma organização por episódio, em série com partes |
| Máfia americana × cinema (Cosa Nostra, skim de Las Vegas, Donnie Brasco) | alta — 295 termos em "mafia documentary" | média (Ashes of Empires, Mafia Talks) | "a história real por trás do filme", com autos e números |
| Cartéis e tráfico (Sinaloa, Cali, PCC, Mocro Maffia) | média — 124 termos em "cartel documentary"; "cali cartel documentary" +60% e "sinaloa cartel documentary" +40% (Trends) | média-alta, com risco de advertiser maior | logística, rota e economia, sempre por investigação, nunca por violência |
| Organizações não ocidentais (Yakuza, tríades) | média | baixa | estrutura corporativa e declínio, ângulo pouco coberto |
| Crime organizado em negócios (lavagem, futebol, apostas, portos) | média | baixa | ponte com o RPM alto de finanças |

## 4. Lane e formato

- **Lane:** long-first. Justificativa em número: 10 de 10 uploads recentes dos dois canais-evidência EN são long-form (18–44 min). O canal pequeno mais veloz em views/dia no cluster (Ciampi Rendo, 251.072/dia) é Shorts de 53–61s com 71 vídeos em 75 dias, outro formato e outro risco. Ver `evidencia.md`.
- **Duração alvo:** 18–35 min (faixas observadas: Endless Night Files 18–31 min; Ashes of Empires 25–44 min). **Cadência:** 1 long por semana, mais 1 Short-teaser por semana quando a série tiver fôlego.
- **Mix:** até 20% Shorts. Short é teaser do episódio da série, sempre apontando para o long do dia (ref `31`).

## 5. Fingerprint de formato (o que o recomendador lê)

Duração 18–35 min, 16:9, 1080p ou mais. Cadência semanal. Thumbnail de arquivo dessaturada com um número. Narração em voiceover, sem rosto, tom contido e pausado. Episódios organizados em série numerada (Part 1, Part 2), títulos com "How / Inside / Real ." e descrição com disclaimer educativo, fontes e capítulos. Convergência confirmada nos dois canais-evidência (ver `evidencia.md`, seção de convergência).

## 6. Estrutura de roteiro

- **Beats:** `models/true-crime-organized-crime/beats.json` (gênero `true-crime-organized-crime`), usar com `--beats-file`.
- **Porte padrão:** PADRÃO, 2.900–3.300 palavras (18–21 min). RICO para caso denso com documentação primária farta (24–27 min, 3.400–3.800 palavras).
- **Dispositivos:** re-hook a cada 2–4 min, re-engage por volta de 3 min e de 6 min, 3 a 5 open loops abertos nos primeiros 20s, pattern interrupt a cada 30–90s, pergunta central que só se resolve no fim.
- **Pesquisa obrigatória:** 1 peça primária por episódio. Serve: auto de indiciamento, sentença, release de Europol/DEA/DOJ, relatório anual de apreensão, depoimento de colaborador publicado, livro de referência. Nada entra sem 2 fontes cruzadas e camada [FATO]/[REPORTADO]/[LENDA].

## 7. Hook (long-form) — fórmula

- **Arquétipo dominante:** detalhe impossível verificado + stake (o negócio fechado de dentro da cela, a rede que continuou funcionando depois da prisão do chefe).
- **Exemplos:**
  1. "The biggest cocaine deals in Europe were closed from a prison cell, on a phone the guards never found."
  2. "One cracked app handed police sixty thousand users and a hundred million messages, and half of Europe's underworld never saw it coming."
  3. "For six years, the Bonanno family treated a jewel thief like family. He was an FBI agent the whole time."
- **Proibido:** abstração, data ou local antes do gancho, meta-linguagem ("neste vídeo"), gore, glorificação.

## 8. Thumbnail

- **Composição:** 1 sujeito (silhueta, figura de arquivo, mãos algemadas) + 1 elemento de cena (mapa, mala, telefone, container) + 3–5 palavras, sempre com 1 número ou nome próprio.
- **Paleta:** dessaturada (cinza, azul-noite) com um único vermelho de acento. **Fonte:** condensed sans bold, alto contraste, legível a 120px.
- **Nunca:** gore, corpo, arma apontada para a câmera, símbolo de facção, rostos de pessoas vivas sem contexto público documentado, repetir as palavras do título.

## 9. Monetização

- **AdSense (classe):** $8–15 [ALEGADO] para crime não gráfico; documentário aparece na casa de $12,6 [ALEGADO] em `10`. O nicho fica no meio da tabela: audiência adulta e alta retenção, com risco de limited ads em violência e drogas.
- **Janela regulatória [OFICIAL]:** desde setembro de 2026, conteúdo educativo não glorificador sobre organizações de tráfico de drogas é elegível a receita de anúncios; desde agosto de 2026 as diretrizes esclarecem a monetização de representação de morte em contexto documentário. Isso favorece o formato "análise e investigação", não o formato "espetáculo de violência" (fontes em `evidencia.md`).
- **Produto digital:** tripwire de $9–19. Dossiê em PDF da organização (linha do tempo, mapa de rotas, organograma, bibliografia) vendido no fim dos episódios da série.
- **Patreon/membros:** episódio estendido, documentos e bibliografia completa, votação do próximo alvo.
- **Afiliado:** livros de referência do subnicho (Cosa Nostra, Mafia Brotherhoods, Gomorra e afins).
- **Rota no funil (`21`):** Short-teaser → inscrito → episódio long → dossiê/produto → membro.

## 10. Produção

- **Custo/tempo por vídeo:** 15–20 horas de pesquisa e roteiro por episódio, mais 4–8 horas de montagem (benchmark de operador em `evidencia.md`). Assets: arquivos públicos (National Archives, Library of Congress, Wikimedia e Europeana), releases e relatórios de Europol/DEA/DOJ, sentenças publicadas, mapas procedurais, arte de arquivo.
- **Voz:** TTS de qualidade (edge-tts para protótipo, ElevenLabs para publicação), ritmo pausado de narração dark, cerca de 150 palavras por minuto. Divulgação de IA no pacote quando voz ou visual forem sintéticos.
- **GATE 100%:** sem todas as imagens aprovadas, não gera voz nem motion.

## 11. Riscos

- **Compliance/advertiser:** violência e drogas são as duas categorias sensíveis do nicho. Mitigação: contexto educativo e documentário, foco em perícia, dinheiro e logística, zero sangue em foco, zero cena de morte, zero apologia. Autoclassificação sempre; pedir revisão humana quando cair limited ads.
- **Conteúdo inautêntico:** o subnicho está sendo inundado por Shorts de narração IA de 60s (evidência: canal de 71 vídeos em 75 dias). O modelo se protege com 1 peça primária por episódio, estrutura variável e voz/roteiro próprios.
- **Difamação e imagem:** pessoa viva = "alleged/accused"; nunca afirmar culpa não julgada; cuidado com organizações ativas: sem endereço, sem nomes de familiares, sem rotas operacionais atuais em detalhe.
- **Segurança/glorificação:** sem símbolo de facção, sem código de honra romantizado, sem material que sirva de recrutamento.

## 12. 10 ideias-semente (títulos)

1. The Albanian Network That Replaced Sicily in Europe's Cocaine Trade
2. The 'Ndrangheta's 50 Billion Euro Year, Explained
3. How Brazil's PCC Runs an Empire From Prison Paperwork
4. The Real Casino Skim: The Millions That Left the Count Room
5. Kinahan: The Cartel That Promoted Boxing Cards in Dubai
6. EncroChat: The Criminal Phone Network Police Learned to Read
7. The Zemun Clan: How Serbia's Mafia Reached Into the State
8. Yakuza, Inc.: What Happened When Japan's Syndicates Went Corporate
9. Mocro Maffia: How the Netherlands Became a Narco-State
10. Pentiti: What Actually Happens to the Men Who Talk

> Todo número citado nesses títulos (50 bilhões, ano, valores, contagens) precisa de fonte primária na pesquisa do episódio. Nenhum entra no roteiro sem 2 fontes.

## 13. Métricas de sucesso

- **D+2:** retenção de 30s acima da linha do próprio canal; AVD e AVP lidos contra a referência de mercado de cerca de 23,7% de retenção média e queda de uns 55% dos espectadores no primeiro minuto [PRATICANTE, ref `01`]; CTR comparado à mediana da própria conta, porque o YouTube não publica meta de CTR.
- **D+7:** episódio novo com pelo menos 1.000 views/dia no acumulado do canal; inscritos crescendo acima de 1% dos views do episódio.
- **Meta de validação em 30 dias:** 3 episódios publicados, com pelo menos 8.000 views cada e soma dos 5 primeiros acima de 10.000. Se 2 ou mais episódios derem outlier de 5× ou mais contra a mediana do canal, o formato está confirmado e o modelo pode ser promovido a PASSA em novo scan.
