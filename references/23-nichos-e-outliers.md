# 23 — Pesquisa de nicho e outliers (método real)

**Não existe lista pronta.** Pesquisa de nicho é uma **tarefa de pesquisa**, não brainstorming. O resultado não é um nome de nicho — é um nome **com evidência de canal**. Base: NicheBreakout, OutlierKit, vidIQ (jun/2026). [PRATICANTE]

## Conceito central: formato × tópico

- **Tópico** = sobre o quê. **Formato** = como é construído (vertical TTS short, documentário long-form, voiceover+b-roll…).
- O recomendador lê formato, duração, aspecto, cadência e thumbnail. O mesmo tópico pode bombar num formato e morrer em outro.
- O scanner separa a baseline por formato com `--format long`, `--format short` ou `--format all`; um outlier só é válido dentro do formato escolhido.
- **Saturação é do cruzamento formato×tópico**, não do tópico pai. "História" está cheio; "dark history em 20 min com arte procedural" pode estar aberto.

## Outlier (o sinal)

**Outlier = vídeo que bate a própria baseline do canal** (não views absolutas).
- Brackets: **3×** notável · **5×** forte · **10×** = flare.
- Janela de oportunidade: **2–6 semanas** entre o outlier e a saturação.
- Cross-channel: **2–3 outliers do mesmo tema em canais diferentes** = o algoritmo está com fome.

## Fluxo (8 passos)

1. **Restrições do operador** — tempo, orçamento, idioma, o que você aguenta fazer por 1 ano.
2. **Gerar candidatos por FORMato** (não por tópico solto).
3. **Achar ≥3 canais pequenos (<90 dias) rompendo** no formato.
4. **Fingerprint de formato** — checklist contra os uploads recentes (convergem?).
5. **Saturação** — o nicho ainda admite canal novo ou só alimenta os grandes?
6. **Clareza de formato** — sinal único que o recomendador lê, ou formato misturado?
7. **Armadilha do "parece fácil"** — baixo custo de produção ≠ baixa saturação (é o oposto).
8. **Gate de ação** — escolha **uma** interseção formato-tópico; publique o piloto em 2 semanas.

## Gates rígidos (reprova se falhar)

Para cada canal-candidato:
- **idade ≤ 45 dias**
- **soma dos 5 primeiros vídeos ≥ 10.000 views**
- **≥ 1.000 views/dia** de vida (views totais ÷ idade)

**INCONCLUSIVO** quando a API falhar, a amostra estiver truncada, o formato não puder ser separado ou dados essenciais estiverem ausentes. Falha operacional não é reprovação do nicho.

**Tier emergente (watchlist — NÃO aprova sozinho):** canal pequeno com **≤90 dias** + **2 dos 3 gates** (5 primeiros ≥10k e/ou ≥1k views/dia). É o caso mais comum de canais que rompem entre 45–90 dias. O scan reporta como `emerging`; revalidar em **2–4 semanas** — se cruzar o gate de idade, vira evidência.

## Checklist binário (12 checagens, ~20 min/nicho)

1. 3 canais <90d rompendo? 
2. Mesmo formato nos 3?
3. ≥1 deles <30d?
4. Todos passam os 3 gates?
5. Uploads recentes convergem no formato (últimos 5, não os 5 primeiros)?
6. Formato claro (um lane: Shorts-first / long-first / mixed)?
7. Ainda entram canais <30d no nicho (feed)?
8. Trajetória em alta (Trends/autocomplete, não só tamanho)?
9. Espaço de perguntas profundo (15 autocompletes)?
10. Dá para fazer 50 vídeos (20 ideias agora)?
11. Demanda de comentário (o público pede o que não existe)?
12. Monetização plausível qualitativa (não RPM inventado)?

**Qualquer "não" reprova.** O próximo passo é **estreitar** o cruzamento ou trocar de candidato — não insistir.

## Demanda de comentário (sub-explorada)

O que o público **pede** nos comentários (do seu canal ou de um concorrente) é o sinal de maior intenção e o menos sistematizado. Leia: pedidos recorrentes, perguntas sem resposta, "faz um vídeo sobre…".

## Fontes e o que cada uma dá

| Fonte | Dá | Cuidado |
|---|---|---|
| Busca + autocomplete do YouTube | demanda, profundidade de perguntas | viés de sessão |
| Google Trends (filtro YouTube, "Rising/Breakout") | trajetória | tamanho ≠ trajetória |
| Data API (canais/vídeos) | idade, views, cadência, outliers | não vê watch time/CTR |
| Reddit / comunidades | dor real, linguagem | nicho pode discutir e não assistir |
| Comentários de concorrentes | demanda explícita | manual |

> **RPM por nicho não é verificável de fora** (está atrás da Analytics/AdSense do dono). Trate tabelas públicas de RPM como [ALEGADO]. Monetização se avalia **qualitativamente** (tem anunciante? tem comprador?).

## Saída (brief de nicho)

Para cada nicho que passa: nome, **interseção formato-tópico**, os 3 canais-evidência (com números), outliers encontrados, anglo/lacuna não coberto, e o **piloto** sugerido. Registrar em `data/nichos.md` (sementes) e no brief.

## Ferramentas (pesquisa em tempo real)

`scripts/niche_scan.py` — tudo abaixo numa ferramenta só (Data API + autocomplete + Trends + comentários):

| Modo | O que dá | Custo |
|---|---|---|
| `--query "tema" --format long` | canais do termo + **gates** + outliers vs mediana do formato | ~100 un (search) |
| `--channel @handle` | um canal: gates + outliers | ~5 un |
| `--cluster "tema"` | **outliers cross-canal** (≥2 canais diferentes com outlier = fome) na janela de 90d | ~150 un |
| `--brief "tema"` | **BRIEF DE NICHO** (.md + .json em `data/briefs/`) com veredito, evidência, autocomplete e Trends | ~150 un |
| `--suggest "seed"` | autocomplete do YouTube (profundidade de perguntas; sem key) | HTTP livre |
| `--trends "termo"` | Google Trends filtro YouTube 12m (direção + queries em alta) | HTTP livre |
| `--comments VIDEOID` | **demanda de comentário** (perguntas/pedidos recorrentes + top likes) | ~1 un |

- `--comments` exige o escopo `youtube.force-ssl` — se der `insufficientPermissions`, rode `python scripts/yt_auth.py` de novo.
- Trends: use **termos específicos** ("industrial disaster documentary"), não genéricos ("dark history") — genérico puxa ruído (anime, marcas).
- Quota Data API: ~10.000 un/dia. `--query`/`--brief` gastam ~100–150 un cada; planeje os scans.
- `dark-scout` amarra: web + API + autocomplete + Trends + comentários.
- Comando: `/dark-nicho discover` e `/dark-nicho verify <nicho>`.
