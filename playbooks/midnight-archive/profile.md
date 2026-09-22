# Canal — The Midnight Archive (a criar do zero)

## Identidade
- Nome: **The Midnight Archive — History's darkest chapters**
- Idioma: **inglês** · Gênero: **dark history documental**
- Tese: capítulos mais sombrios da história, 22–45 min, ~1 vídeo/semana.

## Diferencial (menor risco de conteúdo inautêntico)
- Visuais **100% procedurais** (arte gerada por código: fog, neve, céu, cabanas, dunas…) — **não** slideshow de IA genérica.
- Fotos de **domínio público/CC do Wikimedia Commons** com créditos (`image_credits.txt`).
- Motion próprio: **letterbox 2.39:1**, grão animado, vignette, grade, legendas animadas, **cortes sincronizados na narração**.

## Voz
- **edge-tts `en-US-ChristopherNeural`**, rate **-12%**, pitch **-6Hz**.
- Prosódia por sentença (varia rate/pitch), pausas humanas.

## Formato
- Episódio 1 (piloto): Donner Party (já produzido em `C:\Users\Liiiraa\Downloads\canal-dark`).
- Fechamento reflexivo fixo: pergunta ao espectador ("could you have survived that winter?…").

## Biblioteca de código (reaproveitar, NÃO alterar)
`C:\Users\Liiiraa\Downloads\canal-dark`
- `scripts/tts.py` · `visuals.py` · `fetch_images.py` · `music.py` · `motion.py` · `render.py` · `branding.py` · `seo.py`
- `content/ep1/script.py` (roteiro) · `content/backlog.md` (36 ideias ranqueadas)

## Plano de lançamento (do zero)
1. Definir nome/handle/descriptions (ver `18`).
2. Branding (logo/banner/thumb) — reaproveitar `branding.py`.
3. Calendário: 1 long-form/semana + 3–5 Shorts.
4. Settings do canal (`18`).
5. Publicar o piloto (Donner Party) + shorts derivados.

## Estratégia
- **Projeto de longo prazo** (em paralelo ao Cold File Diaries).
- Nicho estreito + tom contido + biblioteca evergreen → RPM dark history ~$11–13.
- Usar Shorts derivados para descoberta; long-form para autoridade/receita.
