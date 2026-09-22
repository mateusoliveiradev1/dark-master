# 17 — Anti-IA (tirar cara de texto gerado)

Destilado de `pedronauck/humanizer` (MIT) + voice rules do `sergebulaev/youtube-skills` (MIT). Protege contra a política de conteúdo inautêntico e melhora a voz.

## Regra

Escreva como **uma pessoa, para uma pessoa**. Cada frase mantida deve adicionar algo que o leitor ainda não tinha. Um "tell" conta na proporção de quão raramente um bom escritor o faria de propósito.

## Proibido sempre (1 hit já é tell)

- "Não é só X, é Y" / "not just X, it's Y" / "não apenas... mas".
- "No mundo de hoje" / "in today's fast-paced world".
- "game-changer", "deep dive", "no fim do dia", "needle-mover".
- "sem mais delongas", "neste vídeo nós vamos", "deixe o like".
- Aberturas de sinceridade: "vou ser honesto", "real talk", "opinião impopular" (numa opinião popular).

## Padrões fortes (agi na 1ª ocorrência)

1. **Not-X-but-Y** — negue apenas crença real, senão diga direto.
2. **Closer de uma linha / fragmento dramático** — "That is the real win.", "Read that again."
3. **Frases "profundas"** — "a real questão é", "no fundo", "X é a Y de Z", "X vira armadilha".
4. **Run-up** — "vamos mergulhar", "here's what you need to know", "honestly?".
5. **Argumentar com ninguém** — "não é sobre", "to be clear", "don't get me wrong".

## Ritmo

6. **Triads forçadas** — três itens para parecer completo.
7. **Aberturas repetidas** de frase.
8. **Travessões como conector universal** (ver voice rule: ≤1 por 100 palavras).
9. **Qualificadores empilhados** ("could potentially possibly").
10. **Hífens em pares** em todo lugar.
11. **Voz passiva** escondendo o sujeito.

## Inflação

12. **Palavras de IA** — actually, crucial, delve, robust, seamless, leverage, foster, landscape, tapestry, testament, underscore, meticulous, pivotal, showcase, vibrant…
13. **Significância inflada** — "marca um momento pivotal", "deixa um legado", "the future looks bright".
14. **Conexão vaga** — "associado a", "ligado a" sem dizer como.
15. **Riders -ing** — "highlighting…, underscoring…, reflecting…".
16. **Linguagem de venda** — "vibrant", "nestled in the heart of", "breathtaking", "renowned".
17. **Autoridade emprestada** — "especialistas dizem", "segundo relatos".
18. **Evitar is/are/has** — usar "serve como", "representa", "conta com".

## Formatação

19. **Bold decorativo** e listas com rótulo em negrito pra tudo.
20. **Headings decorativos** com emoji/setas, Title Case, regras horizontais.
21. **Aspas curvas** onde o formato usa retas.

## Sobras de chat

22. **Resíduo de chatbot** — "Espero que ajude!", "Ótima pergunta!", "Quer que eu…".
23. **Disclaimers de limite de conhecimento** — "até meu último treinamento".
24. **Heading repetido** na 1ª frase do parágrafo.
25. **Escrever sobre a versão anterior** (em conteúdo que não é changelog).

## Voice rules do YouTube (complemento)

- Travessão ≤1/100 palavras; use `..` como pausa.
- Capitalize nomes.
- **Números específicos** > adjetivos.
- Diga o payoff.
- Título e thumb são um par, não repetem palavras.
- Não keyword-stuff.
- Título ≤100 chars (ideal 40–60); descrição ≤5.000 (1ªs 150 visíveis).

## Como aplicar (fluxo)

1. Marque os tells (do mais forte ao mais fraco).
2. Reescreva mantendo cada fato; não invente detalhe.
3. Cheque os 5 que mais sobrevivem: not-X-but-Y, closer, travessão, triad, bold.
4. Leia em voz alta; varie o comprimento das frases.

## Nota

Uma pessoa pode fazer qualquer um desses de propósito — o tell é a **densidade**. Vários juntos no mesmo trecho = reescreva.
