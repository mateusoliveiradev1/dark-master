# Cold File Diaries — Operação (regras travadas)

Ler ANTES de gerar título, thumb, roteiro, Short ou pacote. Fontes: `00_CANAL/REGRA_METADATA_2026.txt`, `TEMPLATE_ROTEIRO.txt`, `PIPELINE_DIARIO.txt`, `PROTOCOLO_ANTI_INAUTHENTIC.txt`, `CHECKLIST_PERFEICAO.txt`.

## PORTE (define tamanho) — video23+
| Porte | Duração | Palavras | Imagens |
|---|---|---|---|
| FINO | 15–18 min | ~2.300–2.700 | 26–30 |
| PADRÃO (default) | 20 min | ~2.900–3.200 | 32–36 |
| RICO | 25 min | ~3.400–3.700 | 36–40 |

- 01–22 **travados**, não reabrir. Default a partir do video24 = PADRÃO.
- Regra de ouro: **nunca lançar sem 7 vídeos prontos agendados**.

## Roteiro (blocos e palavras)
HOOK 130 · CONTEXTO 500 · PRESSÃO 400 · O DIA 700 · INVESTIGAÇÃO 600 · FAMÍLIA/POS 300 · TEORIAS 400 · CHAVES+OUTRO+TEASER 200.

Regras de voz: frases **12–15 palavras**; em-dash para ênfase; números por extenso; beats curtos dramáticos; teaser do próximo no fim.
- **PROIBIDO**: "this channel", nome do canal fora do CTA, menções de duração ("twenty minutes"). O narrador **habita o arquivo** ("the file"), nunca comenta o vídeo.
- Fonte única: só existe `narration_v3.txt`.
- Checklist FATOS antes de gerar voz (vítimas/data/local/2 fontes/suspeito vivo → alleged/evitar lendas).

## Metadata — SHORT (travar)
- **Título 40–55 chars, 6–9 palavras**, SEM `#shorts`, **SEM pergunta final** (? derruba CTR -18%).
- Fórmula: `[keyword do caso nas 3 primeiras palavras] + [número/ano] + [verbo de ação] + [1 CAPS: NEVER/ZERO/LIVE/GONE/NOBODY]`.
- **Descrição 35–55 palavras**: linha 1 com keyword; `Full story: [LINK]`; `New unsolved case every day. Subscribe to Cold File Diaries.`
- **4 hashtags exatas, nessa ordem**: `#shorts #truecrime #unsolved #[Sobrenome]Case` (>15 = YouTube ignora todas).

## Metadata — LONG (travar)
- **Título 40–60 chars**, keyword nas 3 primeiras palavras/40 chars. Número na frente (**+20–36% CTR**); colchete ganha (**+27%**); 1 CAPS; sem aspas (tabloide); sem emoji; pergunta perde p/ 45+.
- Fórmula: `[CASO]: [nº + promessa tensa] [CAPS] [[Doc/Caso Real/Mistério]]`.
- **Descrição Lego 5 blocos, 250–500 palavras**: B1 hook 150 chars com keyword · B2 expansão 150–250 palavras · B3 CHAPTERS · B4 fontes numeradas + links + disclaimer IA · B5 CTA + 3–5 hashtags.
- **PROIBIDO M:SS no texto corrido** (vira link azul e quebra chapters) — escrever por extenso.
- **Chapters**: `0:00` obrigatório, mín 3, ordem crescente, 7–10 para 10–25min (1 a cada 90–120s), último **< duração real** (ffprobe). Títulos com keyword, 4–8 palavras, <35 chars. Manual sempre.
- **Tags**: 8–12, <400 chars, tag 1 = keyword exata do caso.

## Upload (todo vídeo)
- Marcar **"conteúdo alterado/IA"** + disclaimer no B4.
- Subir **não listado**, esperar **15–30 min**, agendar SHORT **12:00 BRT** / LONG **21:00 BRT**.
- Premiere **D1–D7**, depois agendado. Thumb **Test & Compare 3 variantes** (máx 3 palavras, 0 palavra igual ao título).
- Playlist da série + tela final 20s + comentário fixado EN + SHORT linkado no LONG.

## Padrões de Short (travados)
- **PADRÃO SHORT 2 (VENCEDOR — não mexer no video02):** hook 0–3s em 2ª pessoa + número impossível + pergunta aberta. Dinheiro/ação > luto. É o áudio que viraliza, não a hashtag.
- **PADRÃO SHORT 3 (conteúdo, autópsia 02/03):**
  - 0–3s: impossibilidade COMPLETA em ≤3 fragmentos curtos **ou** 1 pergunta em 2ª pessoa.
  - **PROIBIDO**: data/local antes do gancho; abstração/filosofia no hook.
  - 2ª pessoa + dinheiro/escolha, ou staccato 3x com detalhes sensoriais concretos (carros, bolsas, cigarros).
  - Karaokê tem que **contar a história no mudo**.
  - Corte 28–40s cai em **loop aberto** (pergunta sem resposta), nunca após frase que resolve.
  - Tópico: dinheiro + vítimas identificáveis + recente > caso distante.
- **PADRÃO SHORT 4 TEASE (video23+):** estrutura 32s = hook 0–8s + 2 blocos do MEIO (min 7–12, número impossível) + CTA falado 3s (mesma voz). CTA específico por caso (pergunta do PINNED). **Audio do short ≠ só os 30s iniciais**; última frase nunca conclui. Registrar os 2 blocos em `01_roteiro/tease.txt`.

## Ponte (video23+) — sem quebrar lore
PROIBIDO falar "short", "video", "channel", "subscribe" fora do CTA final. Fórmulas aprovadas: "You heard the call. You haven't heard the room." / "That was the door. Here is the house." O hook NUNCA repete as mesmas 10 palavras do tease.

## Corrente de teaser (amarra o fluxo — ler antes de mudar qualquer coisa)
Cada vídeo **anuncia o caso do dia seguinte pelo nome** no fim (ex.: video23 termina citando "Dorothy Arnold" = video24). O `tease.txt` alimenta o Short Padrão 4.
- **Mudar a ordem/inserir/remover caso exige regerar**: (1) atualizar `CALENDARIO_30.txt`; (2) refazer o **outro/teaser do vídeo anterior**; (3) refazer o `tease.txt` + Short do vídeo afetado; (4) rebuild (`build_video.py videoNN --from voz`).
- Rode `scripts/channel_scan.py "<pasta do canal>"` para ver a corrente e checar buracos.
- A corrente **não pode** ter buraco nem apontar para o caso errado.
Detalhes: `references/25-contexto-do-canal.md`.

## Anti-inauthentic (protocolo travado)
- **Variação obrigatória por vídeo**: hook (pergunta/cena/número — nunca 2 seguidos iguais); ordem de 1 bloco (par/ímpar); motion por clima (KILLERS 8.5s lento, VANISHED 7.0s, HEISTS 6.0s); thumb (L1/L2 alternando cor + com/sem número, máx 5 palavras); título (numero/pergunta/aspas — nunca 3 seguidos iguais).
- **Camada humana sem voz EN**: marcar IA, descrição com fontes, comentário fixado EN, captions revisadas, 1x/semana community com bastidor.
- **Multi-canal**: nunca postar mesmo roteiro/imagem/voz em 2 canais.
- **GATE 100%**: imagens <100% = não gera voz/motion.

## Checklist PERFEIÇÃO (nada sobe sem passar)
- **Voz**: mapa por série; gaps 0.35/0.15; sem efeito "voz diminuída".
- **Música**: bed `_1↔_2` crossfade 4s; autoteste de emenda; ducking -10dB; loudnorm I=-16 TP=-1.5; fade in 2s/out 3s.
- **LONG**: `_parts` refeitos quando a voz muda; FINAL voz==vídeo no décimo; YOUTUBE CRF23 veryfast aac 128k; respiro final (última palavra +1.5–2s bed + fade-out 1.2s + hold preto); `captions.srt` NORMA (42ch/2 linhas) + `captions_full.srt`.
- **SHORT**: pré-requisito `captions.srt` NORMA + `captions_full.srt`; corte na 1ª frase completa após 28s (teto ~40s) + respiro + fade 0.6s; karaokê sem interpolação; vertical 1080x1920; legenda lower-third.
- **Upload**: título/desc/chapters/tags conforme acima; Ctrl+F ":" na descrição = zero M:SS fora de chapters; último chapter < duração.

## Escala
1º investimento ao faturar: **ElevenLabs** (voz). 2º: **editor humano de thumbs**. Voz e thumb são os 2 gargalos.
