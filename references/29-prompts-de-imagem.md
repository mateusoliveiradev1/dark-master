# 29 — Prompts de imagem (e scaffolding de vídeo)

Como gerar pastas e **prompts perfeitos** de imagem — consistentes, sem gore, prontos para colar no gerador.

## Anatomia de um prompt perfeito

Toda linha segue: **o que + ação + onde/quando + luz + câmera + grão/grade + guarda-corpos + aspecto**.

```
NN.jpg — BEAT: <sujeito concreto> <ação/estado>, <ambiente e época>, <luz>, <enquadramento/lente>, <grade e grão>, <guarda-corpos>, 16:9
```

1. **Sujeito concreto** — objeto/animal/lugar/pessoa de costas. Nunca vago ("uma casa" → "farmhouse de madeira 1860, uma janela acesa").
2. **Ação/estado** — o que está acontecendo (parado, chegando, aberto, vazio).
3. **Onde/quando** — lugar + época exata (evita anacronismo).
4. **Luz** — a única luz prática (lanterna, lâmpada quente, lua).
5. **Câmera** — enquadramento e lente (wide establishing, close-up de objeto, over-the-shoulder de costas).
6. **Grade/grão** — dessaturado, film grain, contraste.
7. **Guarda-corpos** — `no text, no watermark, no gore, no real photo, faces not visible`.
8. **Aspecto** — `16:9`.

## Presets de estilo (sufixo travado por canal)

Cole o **mesmo sufixo** em todas as imagens de um vídeo → consistência visual.

**True crime cinematográfico (CFD-like)**
```
cinematic documentary still, moody, desaturated, film grain, volumetric light, ultra detailed, no text, no watermark, no gore, 16:9
```

**Photoreal histórico (Hinterkaifeck-like)**
```
photoreal cinematic film still, deep blacks, film grain, desaturated cold with one warm practical light, dusk or night, no text, no signage, no letters, no readable paper, no watermark, no people close-up, faces never visible backs only, no border, no vignette frame, no gore, no real photo, 16:9
```

**Crime financeiro (documentário)**
```
photorealistic documentary reconstruction, natural proportions, plausible lighting, no teal-orange, no lens flare, documentary photo language, believable lens, no text, no watermark, 16:9
```

**Forense dark (ilustração)**
```
dark cinematic forensic illustration, desaturated cold tones, deep blacks, subtle red accent, volumetric fog, no text, no watermark, no blood, no gore, no real face, silhouettes from behind, 16:9
```

> Canal novo → defina o seu preset e trave. Não copie o de outro canal. O sufixo oficial fica no **contrato do canal** (`playbooks/<canal>/style.json` → `image_suffix`); o scaffold usa automaticamente (`novo_video.py --channel` / `new_video.py --channel` + `prompt_builder --suffix`).

## Guarda-corpos (nunca sair do prompt)

- **Sem gore/sangue/corpo** — mostre vestígio, não violência.
- **Sem rosto real** — de costas, silhueta, distante, desfocado.
- **Sem texto legível** — `no text, no signage, no letters, no readable paper`.
- **Sem anacronismo** — declare a época e proíba o que não existia.
- **Sem marca/logo/watermark.**
- **Sem acusar vivo** — cenas de "teoria" são simbólicas, sem rosto.

## Storyboard (beats) — ordem que conta a história

`estabelecedor → cotidiano → pressão → o dia/noite → descoberta → busca → pista → perícia → investigação → família → mídia → teorias ×3 → laudo → legado → teaser`

Distribua as imagens por esses beats. Cada imagem = **um** momento claro.

## Consistência

- **Mesmo sufixo** em todas.
- **Ficha de personagem** mental fixa (idade, roupa, época) — o "homem de costas" é sempre o mesmo tipo.
- **Mesma época/estação** no vídeo inteiro.

## QA (obrigatório)

Depois de gerar, rode `python scripts/image_audit.py "<videoNN>/03_imagens" --sheet`:
resolução, aspecto, quase-sólida, duplicatas. Veja também o contact sheet.

## Ferramentas

```bash
# 1) criar a pasta do vídeo
python scripts/new_video.py 27 "Hoffa" HEISTS --root "<pasta do canal>"

# 2) gerar o PROMPTS.md (beats + sufixo travado)
python scripts/prompt_builder.py --style truecrime-cfd --count 34 \
  --out "<canal>/video27/03_imagens/PROMPTS.md"

# 2b) a partir de uma lista de cenas (beat + descrição por linha)
python scripts/prompt_builder.py --style photoreal --scenes cenas.txt --out PROMPTS.md

# 3) (opcional) renderizar de verdade via Pollinations
python scripts/prompt_builder.py --style truecrime-cfd --scenes cenas.txt \
  --render --outdir "<videoNN>/03_imagens"
```

> `new_video.py` cria a estrutura; `prompt_builder.py` cria os prompts; `image_audit.py` valida. O trio fecha o "scaffold perfeito".

> **Pollinations (fallback) pode devolver menos que 1920** (ex.: 1024×576). O `image_audit.py` **flag `baixa_res`** e você reusa/refaz. Para produção, prefira **Nano Banana/higgsfield** no tamanho-alvo (1280–1920).

## Manifest e retry de prompts

O GATE 100% compara a lista de prompts com os assets, não apenas a existência de uma pasta com imagens:

```bash
python scripts/asset_manifest.py \
  --images "<video>/03_imagens" \
  --out "<video>/01_roteiro/PROMPT_STATUS.json"
```

`PROMPT_STATUS.json` guarda o total esperado, os assets presentes e os IDs faltantes. Gere novamente os arquivos somente para os IDs em `missing`; não apague o manifesto para fazer o gate passar. `FAIL` bloqueia motion até todos os prompts numerados terem asset válido.
