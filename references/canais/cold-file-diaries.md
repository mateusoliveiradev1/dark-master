# Canal — Cold File Diaries

**Canal prioritário (já no ar).** Toda a operação tem regras TRAVADAS no projeto.
Fonte autoritativa: `C:\Users\Liiiraa\Downloads\canal dark1\00_CANAL\`.

## Identidade
- Nome: **Cold File Diaries** · handle **@ColdFileDiaries** (fallback @ColdFileDiariesUS).
- Idioma: **inglês** · Gênero: **true crime faceless**.
- Posicionamento (1 frase): *"Unsolved American cold cases, retold calmly for adults who remember them."*
- Público: **45+, EUA**, vê TV à noite; quer calma + respeito; odeia gritaria e gore.
- Não confundir com "Cold Case Files" (A&E). Nunca usar esse nome em título/thumb.

## Branding (travado)
- Paleta: fundo `#0A0A0C` · acento `#B91C1C` · texto `#F5F5F4` · detalhe `#8A8A93`.
- Fonte thumbs: **Bebas Neue** / Oswald Bold; branco + palavra-chave em vermelho.
- Thumb: fundo cinematográfico escuro + **3–5 palavras máx** + 1 elemento de mistério (casa, estrada, pasta). **Nunca**: rosto gritando, seta amarela gigante, sangue, >5 palavras.
- Logo: pasta carimbada "COLD" + lupa. Vinheta 3s (pasta abrindo). Outro 20s com tela final.
- **4 séries**: **VANISHED · SMALL TOWN SECRETS · HEISTS & LIES · KILLERS UNKNOWN** (thumb com tarja da série).

## Voz
- **edge-tts `en-US-ChristopherNeural`, SEMPRE a mesma** (não trocar).
- Rate/pitch por série: KILLERS -8%/-5Hz · VANISHED/SMALL TOWN -5%/-3Hz · HEISTS -3%/-1Hz · hook -8%/-5Hz · outro -4%/-2Hz.
- Compensar robô com gaps 0.35/0.15 + bed ambiente. Drama via pausa, não via trocar voz.
- Próximo passo: migrar para **ElevenLabs** (mesma voz clonada).

## Calendário (lançamento 14/09/2026)
- **LANÇAMENTO: 14/09/2026 (SEG)**. **1 LONG + 1 SHORT por dia, mesmo caso, 30 dias seguidos.**
- **Grade fixa diária:**
  - **12:00 BRT / 11:00 EDT / 08:00 PDT = SHORT** (teaser 30s vertical do LONG da noite).
  - **21:00 BRT / 20:00 EDT / 17:00 PDT = LONG** (premiere nos 7 primeiros, depois agendado).
  - **Domingo 18:00 BRT = COMMUNITY POST** da semana.
- **Ritmo semanal de séries:** SEG VANISHED · TER SMALL TOWN · QUA HEISTS · QUI KILLERS · SEX VANISHED · SÁB SMALL TOWN · DOM HEIST/KILLER alternando.
- **Regra rolante:** todo dia produzir o vídeo do **dia+1**. **Nunca abaixo de 7 agendados**; se cair pra 3, fim de semana duplo.
- Premiere mantida **D1–D7**, depois agendado.

### Tabela dia-a-dia (14/09 → 13/10)
| Dia | Data | videoNN | Caso | Série |
|---|---|---|---|---|
| D1 | 14/09 | video01 | Sodder 1945 | VANISHED |
| D2 | 15/09 | video02 | D.B. Cooper 1971 | HEISTS |
| D3 | 16/09 | video03 | Springfield Three 1992 | VANISHED |
| D4 | 17/09 | video04 | Zodiac | KILLERS |
| D5 | 18/09 | video05 | Yuba Five 1978 | VANISHED |
| D6 | 19/09 | video06 | Gardner 1990 | HEISTS |
| D7 | 20/09 | video07 | Black Dahlia 1947 | KILLERS |
| D8 | 21/09 | video08 | Circleville | SMALL TOWN |
| D9 | 22/09 | video09 | Maura Murray | VANISHED |
| D10 | 23/09 | video10 | Axeman | KILLERS |
| D11 | 24/09 | video11 | Earhart | VANISHED |
| D12 | 25/09 | video12 | Fort Worth Three | VANISHED |
| D13 | 26/09 | video13 | Alcatraz | HEISTS |
| D14 | 27/09 | video14 | Cleveland Torso | KILLERS |
| D15 | 28/09 | video15 | Johnny Gosch | VANISHED |
| D16 | 29/09 | video16 | Max Headroom | SMALL TOWN |
| D17 | 30/09 | video17 | Texarkana | SMALL TOWN |
| D18 | 01/10 | video18 | Brian Shaffer | VANISHED |
| D19 | 02/10 | video19 | Oakland County | KILLERS |
| D20 | 03/10 | video20 | Asha Degree | VANISHED |
| D21 | 04/10 | video21 | I-70 | KILLERS |
| D22 | 05/10 | video22 | Brandon Lawson | VANISHED |
| D23 | 06/10 | video23 | Servant Girl | KILLERS |
| D24 | 07/10 | video24 | Dorothy Arnold | VANISHED |
| D25 | 08/10 | video25 | Doodler | KILLERS |
| D26 | 09/10 | video26 | Hinterkaifeck | SMALL TOWN |
| D27 | 10/10 | video27 | Hoffa | HEISTS |
| D28 | 11/10 | video28 | Alphabet | KILLERS |
| D29 | 12/10 | video29 | Mad Gasser | SMALL TOWN |
| D30 | 13/10 | video30 | Colonial Parkway | KILLERS |

> Verifique o status atual em `00_CANAL/CALENDARIO_30.txt` (a tabela evolui).

## Projeto no disco
`C:\Users\Liiiraa\Downloads\canal dark1`
- `00_CANAL/` — branding, calendário, regras, protocolos, assets.
- `scripts/` (~27 .py) — orquestrador `build_video.py`.
- `videoNN/` — `01_roteiro`, `02_audio`, `03_imagens`, `04_video_final` + `youtube_package.txt`.

## Operação (metadata, PORTE, padrões de Short, anti-inauthentic)
→ **`canais/cold-file-diaries-operacao.md`** (ler antes de gerar qualquer coisa).

## Status
- Estoque fechado (≥17 prontos em 15/09); em produção video18+.
- Outliers de Short: **Cooper (video02 ~1.213) · Springfield (video03 ~1.210) · Yuba (video05 ~1.2K)**.
- **"PADRÃO SHORT 2 VENCEDOR (não mexer no video02)"** — não reabrir shorts 01–22 viralizados.

## Prioridade
**Empurrar 4.000h / 10M antes de 01/02/2027** (canal já no ar, com tração).
Long-form = dinheiro (RPM true crime $8–15); Short = alcance.
