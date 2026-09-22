# 13 — Imagens e voz

Backends padronizados: **Nano Banana manual + Pollinations (fallback)** para imagem; **edge-tts + ElevenLabs** para voz.

## Imagem

### Nano Banana (padrão, manual)
- O usuário escreve prompts por cena num `03_imagens/PROMPTS.md` e gera externamente, revisando cada imagem.
- Vantagem: controle artístico + evita "cara de IA genérica" (importante p/ anti-inauthentic).
- Regra: **GATE 100%** — todas as imagens antes de gerar voz.

Estilo por canal (prefixo travado):
- **Cold File Diaries / Laudo Final:** dark cinematic forensic illustration, desaturated cold tones, deep blacks, subtle red accent, volumetric fog, 16:9, no text, no watermark, no blood, no gore, no real face, silhouettes from behind.
- **Financial Crime Files:** photorealistic documentary reconstruction, natural proportions, plausible lighting, no teal-orange, no lens flare, documentary photo language.
- **Midnight Archive:** arte procedural (código) + Wikimedia Commons PD/CC.

### Pollinations (fallback gratuito, automatizável)
```
https://image.pollinations.ai/prompt/{prompt_urlencoded}?width=1920&height=1080&nologo=true&model=flux
```
- Escreva só se `len(bytes) > 10000` (buffer até completar).
- Use para testes/volume quando não quiser gastar Nano Banana.

### QA de imagem
- Gerar **1 imagem teste** e aprovar o estilo antes de gerar todas.
- Auditar: ≥1280px, aspecto 1.70–1.85, ≥50KB, sem rosto real/gore/texto legível.
- Montar contact sheet para revisão humana.

## Voz

### edge-tts (grátis, padrão de produção)

Escolha **uma voz e trave-a** para o canal (identidade de marca). Sugestões por tom:

| Tom | Voz sugerida (edge-tts) |
|---|---|
| Documentário EN (grave, medido) | `en-US-ChristopherNeural` (rate -8% a -12%) |
| Investigativo EN (neutro) | `en-US-GuyNeural` |
| PT-BR | `pt-BR-AntonioNeural` ou `fr-FR-RemyMultilingualNeural` |

> A voz por canal fica no playbook (`playbooks/<canal>/`). **Canal novo define a própria** — não copie a de outro canal.

- Prosódia por sentença (variação de rate/pitch), pausas 0.35s/0.15s, trim de silêncio.
- Bed musical por série com ducking (sidechain) + `loudnorm I=-16` (ou -14 onde o projeto usa).
- Legenda karaokê via faster-whisper (word timings) alinhada ao roteiro.

### ElevenLabs (premium, naturalidade)
- Melhor para storytelling/documentário dramático. **Professional Voice Clone** dá voz de marca consistente.
- Uso: quando a voz é parte da marca e uma leitura fraca prejudica o vídeo.
- Custo: Starter pago libera licença comercial; Creator ~$22/mês.
- Cuidado: créditos acabam rápido em long-form.

### Critério de escolha
- Voz é a marca (documentário dramático) → **ElevenLabs / clone**.
- Volume alto, custo controlado → **edge-tts** (grátis).
- Multi-idioma → auto-dub do YouTube (`11`) ou clone multilíngue.

### Qualidade de narração (regras)
- Combine a voz com o formato: calma/medida para documentário; energia só onde cabe.
- Legenda é camada de compreensão, não conserto de fala ruim.
- Renderize 200 palavras de teste com nomes/preços/lista antes de fechar a voz.
- Voze consistente por canal (reconhecimento de marca).

## Checklist imagem/voz
- [ ] 1 imagem teste aprovada antes de lotear.
- [ ] GATE 100% (todas imagens prontas).
- [ ] Voz oficial do canal aplicada.
- [ ] Teste de 200 palavras (pronúncia/ritmo).
- [ ] loudnorm no alvo do projeto.
- [ ] Captions alinhadas ao roteiro.
