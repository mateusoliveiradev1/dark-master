# 09 — Monetização e compliance

O que decide se você pode monetizar e o que faz perder a monetização. Fonte: YouTube Help / Creator Insider. [OFICIAL]

## Requisitos do YPP (2026)

| Faixa | Inscritos | Uploads | Watch time / Shorts | Libera |
|---|---|---|---|---|
| **Entrada** | 500 | 3 em 90 dias | 3.000h (365d) **ou** 3M views Shorts (90d) | memberships, Super Chat/Thanks, Shopping |
| **Completa** | 1.000 | — | 4.000h (365d) **ou** 10M views Shorts (90d) | Watch Page Ads, Shorts Feed Ads, Premium |

Outros requisitos: país elegível, sem strike ativo, 2FA ligado, recursos avançados, AdSense vinculado.

### Manutenção mínima (não cair do YPP) [PRATICANTE relatando OFICIAL 10/08/2026]
`1.000h/365d OU 1M Shorts/90d OU 2 longs ou 5 Shorts/90d`. 6 meses sem vídeo/post = remoção. De 01/02/2027, Shorts exige `10M/90d rolantes` para seguir no revenue-share de Shorts (caiu = segue no YPP e no long, volta sozinho ao recruzarem).
Calcule com `python scripts/ypp_check.py --subs N --hours H [--short-views V] [--longs-90d L --shorts-90d S]`.

### ⚠️ O prazo que muda tudo
**YouTube confirmou (10/08/2026): a partir de 01/02/2027 os requisitos dobram para novos inscritos** — **8.000h** ou **20M views de Shorts**. Quem já está no programa não é afetado. **Conclusão: entrar antes de fev/2027 vale o dobro.** Canal do zero em ~4 meses provavelmente não pega o prazo antigo → priorize o canal que já tem tração.

### Detalhes que pegam criadores
- Só contam: vídeos **públicos** (long-form) e lives públicas arquivadas. **Shorts não contam** para as 4.000h.
- Janela **rolante de 365 dias**: horas antigas expiram.
- Tornar público→privado **remove retroativamente** as horas.
- Shorts: **engaged views** (não o número bruto) contam para YPP/receita.

## Política de conteúdo inautêntico [OFICIAL — atualizada 15/07/2025, detalhada 16/07/2026]

A regra: **"o formato pode repetir; a substância não".** Três baldes NÃO monetizáveis:

1. **Genérico / repetitivo / template** — parece feito com template, intercambiável entre vídeos, "slideshow de imagem", "roteiro com find-and-replace", IA com template genérico sem insight próprio.
2. **Insatisfatório / desagradável** — fórmula emocionalmente manipuladora, formato copiado ao ponto de parecer intercambiável, choque só para views. Ex.: temas perturbadores repetidos sem arco coeso.
3. **Personas de IA em temas sensíveis** — "especialistas" sintéticos dando conselho de **saúde, finanças, direito ou política/segurança**.

**Enforcement é no canal**, olhando os últimos ~30 uploads. Em jan/2026 foi terminada uma leva de canais (16 canais, 35M inscritos). Faceless **é permitido** — faceless vazio não é.

### O que continua permitido
- Personagens/apresentadores recorrentes, intros/outros/lower-thirds consistentes.
- Narração faceless sobre footage licenciado.
- IA para roteiro, voz, edição, thumbnail.
- Formatos de série com estrutura repetida, **se cada episódio entrega valor distinto**.

### Testes de sanidade antes de publicar
- Se eu trocar o roteiro do vídeo A pelo B, ainda faz sentido? → problema de template.
- Cada vídeo tem ≥1 fato/número/exemplo/opinião que não aparece em nenhum outro?
- A promessa do thumbnail é entregue e cedo?
- Assistindo 3 vídeos seguidos, o 3º parece informação nova ou remix?

### Antídotos (obrigatórios para dark)
- **1 peça de pesquisa primária por vídeo** (uma linha do tempo montada por você, um dado compilado, uma comparação).
- **Tome posição** (contenha uma frase discutível).
- Varie hooks/estrutura entre episódios (não só o tema).
- Não reutilize metadados idênticos; audite títulos/descrições duplicados.
- Volte e **limpe o back catalog** (títulos/descrições/what não entrega valor).

## Advertiser-friendly (monetização de anúncios)

- **Imagem gráfica na thumb ou nos primeiros 15s** → Limited Ads (mesmo com roteiro educacional).
- Cobertura educacional/documental de tragédia **é monetizável**; gore explícito não.
- **Forensic-focus** (DNA/balística/patologia explicados) tem o **menor risco** de yellow icon.
- Evite: thumb com crime scene, primeiros 15s com violência, temas sensíveis (abuso infantil, autolesão, transtornos alimentares) permanecem restritos.

## Divulgação de IA [OFICIAL]

- Marcar `Sim` em `Studio > AI use` quando realista: pessoa real parecendo dizer/fazer o que não fez; evento/lugar real alterado; cena realista que não ocorreu.
- Não precisa marcar: roteiro/voz clonada própria/título/thumb/legenda/upscale por IA, grade, blur, backdrop IA em movimento.
- YouTube marca automaticamente (C2PA, SynthID) e desde 05/2026 pode etiquetar sozinho. Omitir = label forçado, remoção, suspensão YPP.
- Marcar como IA **não** penaliza alcance/monetização por si só; o problema é conteúdo massificado.

## Reused content (compilação/documentário) [OFICIAL — FAQ reused]

- Reprovado: compilação sem narrativa, reação muda, só leitura de site/feed, mesma música com pitch mudado, download sem mudança. **Permissão ≠ salvo; sem claim ≠ salvo.**
- Aprovado: crítica com clips, reação com comentário, storyline editado, remix com áudio/vídeo próprio, edição substantiva.
- Gate dark: `>50% narração/análise própria + fontes na descrição + transformação visível` (timeline, mapa, comparação, reconstituição licenciada).

## Palavrão, violência e controversos [OFICIAL]

- Palavrão (29/07/2025): forte nos 1os 7s = full ads; moderado/forte em título/thumb ou alta frequência = limited; slur = sem ads.
- Violência sem contexto = sem ads; com contexto news/edu/doc = monetizável.
- Controversos (vigor 13/01/2026): cobertura **não-gráfica** de abuso doméstico, self-harm, suicídio, abuso sexual adulto, aborto, assédio + relato preventivo/jornalístico = full. Restritos: abuso infantil, exploração infantil, eating disorders.
- True crime na prática [PRATICANTE]: onda de `limited` em 2026 mesmo com tratamento respeitoso. Gates: thumb sem crime scene/sangue; 0-15s sem gore/agonia; linguagem forense > gore; self-certification honesta + revisão humana (até 24h).

## Checklist de compliance (rodar antes de publicar)

- [ ] Sem template intercambiável (substância varia).
- [ ] Pesquisa/insight próprio presente.
- [ ] Sem imagem gráfica na thumb/primeiros 15s.
- [ ] Pessoas vivas tratadas como "suspeito/acusado".
- [ ] Divulgação de IA se voz/visual sintético.
- [ ] Metadados não duplicados.
- [ ] Canal ainda ativo (não 6 meses parado).
