# 23 — Pesquisa de nicho e outliers (método real)

**Não existe lista pronta.** Pesquisa de nicho é uma **tarefa de pesquisa**, não brainstorming. O resultado não é um nome de nicho — é um nome **com evidência de canal**. Base: NicheBreakout, OutlierKit, vidIQ (jun/2026). [PRATICANTE]

## Conceito central: formato × tópico

- **Tópico** = sobre o quê. **Formato** = como é construído (vertical TTS short, documentário long-form, voiceover+b-roll…).
- O recomendador lê **formato** (duração, aspecto, cadência, thumb) e casa com audiência. O mesmo tópico pode bombar num formato e morrer em outro.
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

Nicho passa se **3 canais** diferentes passarem os 3 gates. "Romper" tem que ter **número**, não "parece promissor".

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

## Ferramentas
- `scripts/niche_scan.py` — varre canais/vídeos e calcula gates e outliers (Data API).
- `dark-scout` amarra: web + API + Trends/Reddit.
- Comando: `/dark-nicho discover` e `/dark-nicho verify <nicho>`.
