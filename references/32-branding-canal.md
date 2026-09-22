# 32 — Branding do canal (identidade visual de verdade)

O branding é **decisão do canal** (`/dark-lancar`) e vale para tudo: thumb, banner, profile, watermark, abertura, end card. **Canal novo ≠ clone** — não copie paleta/fonte/logo de outro canal.

## Componentes

| Peça | Tamanho | Onde usar | Regra |
|---|---|---|---|
| **Logo (monograma)** | 512×512 | fonte do kit | iniciais + paleta; simples o bastante para ler a 32px |
| **Profile** | 800×800 | foto do canal | conteúdo no **círculo seguro** (o YouTube corta em círculo) |
| **Banner** | 2560×1440 | banner do canal | texto na **safe area 1235×338** (desktop/TV); mobile mostra só o centro |
| **Watermark** | 150×150 | marca d'água do vídeo | 1–2 caracteres; aparece no canto do player |
| **Thumb** | 1280×720 | por vídeo | 3–5 palavras, 1 elemento de mistério (`04`) |

> Banner oficial: 2560×1440 recomendado (mín. 2048×1152); a safe area é 1235×338 centralizada. O resto pode ser cortado.

## Paleta (4 papéis — travar)

1. **Fundo** (dark, ex.: `#0A0A0C`)
2. **Acento** (a cor da marca, usada com parcimônia)
3. **Texto** (quase-branco, ex.: `#F5F5F4`)
4. **Detalhe/muted** (cinza para apoio)

Regras: no máximo **2 cores fortes**; evitar vermelho/branco/preto puros (concorrem com a UI do YouTube); contraste ≥ 4.5:1 no texto.

## Fontes

- **1 fonte para título + 1 peso** (ex.: Bebas Neue / Oswald Bold), 1 para apoio.
- Sem serifa, condensada e bold lê melhor a 120px (thumb mobile).
- A fonte é um **arquivo** (`00_CANAL/assets/fonts/`) — versionada no contrato.

## Ferramenta — `scripts/branding_kit.py`

Gera o kit completo a partir de nome/handle/tagline/paleta/fonte:

```bash
python scripts/branding_kit.py --name "Arquivo Sombrio" --handle ArquivoSombrio \
  --tagline "Casos arquivados, contados com calma." --sub "Arquivos Perdidos" \
  --palette "#0B0B10,#C2410C,#F4F4F5,#8B8B96" \
  --font "C:/.../00_CANAL/assets/fonts/BebasNeue.ttf" \
  --out "<canal>/00_CANAL/assets/branding"
```

Saída: `logo.png` · `profile.png` · `banner.png` · `banner_guia.png` (guias da safe area — **não subir**) · `watermark.png` · `palette.json` · `BRANDING.md` (spec de uso).

## Do / Don't

- **Do:** mesma paleta em thumb/banner/profile; texto dentro da safe area; testar a thumb a 120px; 1 elemento de mistério.
- **Don't:** rosto real; gore; >5 palavras na thumb; 3+ fontes; nada no canto inferior direito da thumb (duração do YT); copiar identidade de canal existente.
- **Marca e nome:** checar disponibilidade (`27`) e registro de marca antes de escalar.

## Checklist de branding

- [ ] Nome/handle definidos e checados (`27`).
- [ ] Paleta de 4 papéis travada em `palette.json`.
- [ ] Fonte no `00_CANAL/assets/fonts/` e referenciada no kit.
- [ ] `logo.png`, `profile.png`, `banner.png` (safe area) e `watermark.png` gerados.
- [ ] Thumb style definido (`04` + `assets/template-thumb-brief.md`).
- [ ] Kit versionado (`33`) e registrado no playbook do canal.
