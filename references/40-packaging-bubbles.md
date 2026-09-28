# 40 — Motor universal de packaging + bolhas (qualquer nicho, PT+EN)

Núcleo fixo + adaptador de nicho. Título e thumb nascem como **par** e só avançam com gate 10/10 de **processo** (não promessa de CTR).

## 1. Arquitetura

- **Núcleo (não muda por vídeo):** `03` (Y1–Y11 + pareamento + micro-regras), `04` (5 inegociáveis + 120px + 2–3 variantes 1-eixo), `01` (CTR×retenção), `02` (Shorts), `05/b/c/e` (retenção MrBeast, parafraseado).
- **Adaptador (única parte que muda):** `models/<slug>/profile.md + hooks.md + beats.json + evidencia.md` + `playbooks/<canal>/style.json + voice.json + motion.json`. Scripts leem via `--channel`; sem config = aviso explícito, nunca fallback silencioso.
- **Localização, não tradução:** keyword PT via autocomplete/Trends PT, keyword EN via autocomplete/Trends EN. Overlay ≤4 palavras por idioma.

## 2. Artefatos obrigatórios por vídeo

| Arquivo | O que é | Gate |
|---|---|---|
| `01_roteiro/PACKAGING.json` | 3–5 pares `{titulo PT/EN, thumb text PT/EN + conceito, hook30s + short3s, formula Y, goal browse\|search, evidencia URLs}` + decisão humana (winner + 1–2 alts Test & Compare) | `packaging_audit.py` — FAIL bloqueia |
| `01_roteiro/THUMB_BRIEF.json` | 2–3 conceitos × 6 campos + eixo variante + nota 120px (+ `image` opcional) | `thumb_audit.py` — FAIL bloqueia |
| `01_roteiro/TITLE_RESEARCH.md/.json` | tema/subtema/ângulo/idioma/mercado/formato + candidatos + URLs datadas + autocomplete + Trends + comentários + limitações | `title_research.py` — FAIL/ausente bloqueia |
| `01_roteiro/ROTATION_AUDIT.json` | título+hook+beats+CTA vs últimos 3 | FAIL/ausente bloqueia |
| `01_roteiro/SHORT_QA.json` | hook ≤8, blocos ≤4, frame1 texto ≤6, sem saudação/logo, funil válido, loop ≥0.55 quando há vídeo | FAIL bloqueia; sem vídeo = REVIEW |
| `youtube_package.txt` | escolha humana final + alts | presença obrigatória |

Templates: `templates/packaging.json`, `templates/thumb_brief.json`. Schema: `schemas/packaging.schema.json`.

## 3. Rubrica 10/10 de processo (FAIL se qualquer eixo <10)

**Título:** curiosidade+concreto · 1 número específico · keyword real do dossiê · 40–60 chars (hard <100) · front-load · honesto vs 30s/3s · diferenciado do adjacente.
**Thumb:** 1 foco · legível a 120px · contraste BOGY vs UI · ≤4 palavras · emoção = vídeo · sem gore (`09`).
**Par:** split de carga (título = contexto/número/busca; thumb = rosto/emoção/resultado) · zero palavras repetidas em PT e EN · hook casado (Y1/Y7, Y3/Y8, Y2/Y9, Y5/Y8, Y6/Y9, Y11/Y8, Short/Y10).
**Regra 50/50 (MrBeast):** trecho com 50% de chance = reescrever. Sem dull moments, fim abrupto + overdeliver, 1 wow/episódio, simples p/50M, viewer médio do canal, últimos ~50 do nicho estudados, baseline dos 9 anteriores (nunca benchmark genérico).

## 4. Playbook de bolhas (modelo mental [PRATICANTE], não limiar oficial)

**[OFICIAL]:** Shorts = sistema separado, explore→exploit em ondas; sinais = Viewed vs Swiped, AVD/AVP, engaged views, satisfação. Long = teste por semanas, satisfação > watch time. Lag Analytics 48–72h.
**[PRATICANTE]:** B1 (300–2k, 30min–3h) → B2 (10k→30k→50k, públicos parecidos + frios) → B3 (~200k+) → B4 (global). Reteste 3–7 dias possível; números tipo "80%/70%/15–25%" são referência, não garantia.

**Pré-bolha:** `SHORT_QA.json` bloqueante + `SHORT_FUNNEL.md` (1 claim verificada + ponte + loop + fixado/related). Short bom sozinho, long valioso sozinho.
**Durante (D+2/D+7, nunca nas 3h):** `channel_scan + yt_metrics + yt_analysis` (snapshots, traffic_sources, retention 100pts, engaged views, subs/1k). Diagnóstico `02`: shown baixo = tema; chose baixo = frame1; AVD fraco = corpo; sem like/sub = conexão. Ausente = desconhecido, nunca zero. Travou ~1k? espera 7d, 1 variável por vez.
**Pós:** outlier = bate baseline própria (3x/5x/10x flare); cross-canal 2–3 = fome. Hipótese com 4–6 comparáveis; regra só com repetição + aprovação. Re-otimiza back catalog. Short→Long só via `RELATED_VIDEO/END_SCREEN`.
