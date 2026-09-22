# 23 — Nichos, subnichos e outliers

Método para achar o que fazer em seguida. Base: pesquisa 2026 (OutlierKit, vidIQ, 1of10, NicheBreakout). [PRATICANTE]

## O conceito de outlier

**Outlier = vídeo que bate a própria baseline do canal** (não views absolutas). Um vídeo de 1M views num canal que faz 500k é 2x; um de 10k num canal que faz 1k é 10x — o segundo é o sinal forte e reproduzível.

Brackets mentais: **2x** interessante · **5x** forte · **10x** = flare no céu.

**Por que importa:** o algoritmo lê o outlier como sinal de qualidade e empurra para além dos inscritos. A demanda reprimida aparece. A janela entre o outlier e a saturação é de **2–6 semanas**.

## Os 3 checks de nicho (antes de comprometer)

1. **Canais pequenos ganham ali.** Canais **<20k inscritos** fazendo **5–20x** o normal = tópico aberto. Só gigantes = tópico fechado.
2. **Paga o suficiente.** Finance/business/education > entretenimento. Decida o RPM necessário **antes**.
3. **Você consegue fazer 50 vídeos.** Escreva 20 ideias agora; se não conseguir, é estreito demais.

## Validar demanda pela recência

- Vídeo **recente** (dias/semanas) com views = tema **em alta**. Vídeo antigo rankeado = tema esfriou.
- Métrica melhor: **views/dia** (não views totais).
- Cross-channel: **2–3 outliers do mesmo tema em canais diferentes** = o algoritmo está com fome daquele tema.

## Como extrair um outlier (loop)

1. Achar o overperformer (≥3x; ideal ≥5x).
2. Comparar com a baseline (medir o gap real).
3. Desmontar: **título, thumb, tema, formato, timing**.
4. Isolar a **estrutura transferível** (não os detalhes que só funcionaram por causa do canal deles).
5. Refazer **na sua voz**, para a sua audiência. Nunca clonar (a cópia perde para o original).

> Gap mais valioso: quando o **tema mais frequente** do concorrente NÃO é o que mais performa. O público já mostrou a lacuna.

## Formato vs. tópico

- **Tópico** = sobre o quê. **Formato** = como é construído (vertical TTS short, documentário long-form, voiceover+b-roll…).
- O mesmo tópico pode bombar num formato e morrer em outro. Saturação é do **cruzamento formato×tópico**, não do tópico pai.
- Cuidado com "parece fácil": **baixo custo de produção ≠ baixa saturação** (é o oposto).

## Monitoramento (o "avisa quando alguém posta outlier")

- `scripts/yt_scan_outliers.py --watch` roda a lista `monitor/channels.json`.
- Ele calcula a mediana do canal e marca vídeos ≥ `ratio` (default 3x), grava em `data/dark.db` e imprime o alerta.
- **Ritmo:** semanal (a janela é 2–6 semanas; perder uma semana = entrar atrasado).
- Fluxo: alerta → `dark-scout` desmonta o padrão → sugere adaptação → `/dark` gera o vídeo.

## Como treinar o algoritmo a te achar

- Postar em horário consistente; o público dark consome à noite (20h–23h local) [PRATICANTE].
- Shorts viram porta de entrada **se** ligados ao long (teaser + comentário fixado); Short desconectado = inscrito que não assiste.
- Após um viral, a queda é normal; **não mude tudo** — continue o padrão vencedor por 5–10 vídeos.

## Não fazer

- Rankear concorrentes por views absolutas (premia canal grande, não a ideia).
- Escolher nicho por CPM sem validar demanda.
- Reabrir formato saturado sem ângulo novo.
- Copiar o vídeo outlier em vez da estrutura.

## Checklist

- [ ] Nicho passa os 3 checks.
- [ ] Outliers mapeados (≥3x) em ≥3 canais pequenos.
- [ ] Padrão extraído (título/thumb/formato/timing).
- [ ] Ângulo ainda não coberto escolhido.
- [ ] Monitor rodando semanalmente (`--watch`).
- [ ] Registrado em `data/nichos.md` e `data/outliers.json`.
