# 34 — Voz: motor TTS (grátis e pago)

A voz é **ativo de marca**, não commodity. Regra zero: **uma voz por canal, travada no playbook** (`playbooks/<canal>/voice.json`). Trocar de voz no meio do canal quebra reconhecimento — troque o **motor** mantendo a voz sempre que possível.

> Motor unificado: `scripts/voice_engine.py` lê o contrato do canal e gera com **qualquer provider** (edge, azure, elevenlabs, fish, gemini, openai, kokoro, piper). Mesma saída: blocos + gaps + filtros + loudnorm + SRT. Teste antes de lotear: `--test`.

## Preflight e fallback gratuito

- Rode `python scripts/voice_engine.py --channel <canal> --preflight --require-free` antes de gerar; isso verifica dependências, chaves, modelo Piper e se existe um provider gratuito pronto.
- O preflight não gera áudio nem cobra API. O pipeline normal também falha antes de sintetizar quando nenhum provider está pronto; sem `--require-free`, ele apenas avisa que a cadeia é exclusivamente paga.
- O contrato de cada canal declara `lang`; o aviso de locale compara `pt-BR`/`en-US` com a voz e o gate de consistência usa esse idioma.
- O cache é escrito em arquivo temporário e só substitui o cache final após áudio válido; `--dry-run` não cria diretórios nem arquivos.
- Para o pipeline local, instale as dependências de `requirements-voice.txt`; Piper também exige um modelo `.onnx` existente no `voice_id`.

## Idioma, sotaque e consistência (a regra da voz nativa)

**Voz do canal = voz NATIVA do idioma do canal.** Voz multilíngue (Remy `fr-FR`, Andrew `en-US`) fala PT **com sotaque estrangeiro** e escorrega em palavra estrangeira — caso real: "apreendido numa blitz" saiu como *"no Mablitz"* na Remy. Multilíngue só se o **mesmo canal publica em vários idiomas** (aí use clone PT que fala os outros).

| Tier | Vozes PT-BR recomendadas |
|---|---|
| Grátis (edge) | `pt-BR-AntonioNeural` (masc., nativa) · `pt-BR-ThalitaMultilingualNeural` (fem., qualidade multilíngue com base PT) · `pt-BR-FranciscaNeural` (fem.) |
| Grátis local | Kokoro `pm_alex` / `pf_dora` · Piper `pt_BR-*` (consistência total, naturalidade menor) |
| Pago | **ElevenLabs** multilingual v2 com voz PT da library/clone PT (`language_code` em turbo/flash v2.5) · **Azure** `pt-BR-AntonioNeural` + phoneme/lexicon · **Fish** clone PT 10–30s · **Gemini** `Algenib` + style "Diga o texto a seguir em português do Brasil:" |

Como o motor trava isso:
- `"lang": "pt-BR"` no contrato → **AVISO automático** quando a voz não bate com o idioma do canal (`warn_voice_lang`); Gemini sem direção de idioma no `style` também avisa.
- Escolha da voz com evidência: `--ab "edge:pt-BR-AntonioNeural, edge:pt-BR-ThalitaMultilingualNeural, gemini:Algenib"` gera o mesmo texto em N vozes, transcreve e salva para ouvir.
- Auditoria do vídeo pronto: `--consistencia` grava `CONSISTENCIA_TTS.json` com `PASS`/`REVIEW`; `--pronounce` grava `PRONUNCIA_TTS.json` e falha se houver termos para revisar.
- **Limite honesto:** o whisper pega *troca de idioma*, **não pega sotaque** (a Remy deu 0/31 janelas "ok" mesmo com francês audível) — o gate final continua sendo a oitiva humana.

## Escolha em 30 segundos

| Situação | Use | Por quê |
|---|---|---|
| Começando, $0, validando canal | `edge` | Grátis, 400+ vozes, prosódia por bloco |
| Canal **monetizado** e quer dormir tranquilo | `azure` | Mesmas vozes do edge **com licença comercial**; 0,5M chars/mês grátis |
| $0, quer voz melhor que edge, roda local | `kokoro` | Apache 2.0 (comercial OK), 54 vozes, 8 idiomas, roda em CPU |
| Clone da **sua própria voz**, $0, local | `chatterbox` | MIT, clone com ~5s, 23 idiomas |
| Clone + naturalidade máxima, paga | `elevenlabs` | PVC (30min+) = voz de marca consistente por meses |
| Clone barato + 80+ idiomas + timestamps | `fish` | $15/1M bytes, clone 10–30s, self-host possível |
| PT-BR com direção de estilo por prompt | `gemini` | 30 vozes, estilo descrito em texto, barato (cota por request → chunk) |
| Já tem conta OpenAI | `openai` | 13 vozes, `instructions` steerable, sem clone |
| Máquina fraca / CPU-only | `piper` | ~63MB por voz, roda em qualquer PC |

## Licença e uso comercial — leia ANTES de monetizar

| Motor | Licença/uso comercial | Fonte |
|---|---|---|
| **edge-tts** | Endpoint do Bing read-aloud (consumidor). Uso **pessoal**; comercial é zona cinzenta e sem garantia de disponibilidade | [ALEGADO] — mantenedor do projeto desaconselha uso comercial |
| **Azure Speech** | Licença comercial plena; 0,5M chars/mês grátis (neural) e 5M no SKU Free web/container | [OFICIAL] |
| **Kokoro-82M** | Apache 2.0 — comercial liberado | [OFICIAL] |
| **Piper** | Código GPL-3.0; **arquivos de voz MIT** — uso comercial OK | [OFICIAL] |
| **Chatterbox** | MIT — clone e uso comercial liberados | [OFICIAL] |
| **XTTS v2** | CPML — **não-comercial** (e a Coqui fechou; sem licença comercial disponível) | [OFICIAL] |
| **F5-TTS** | Checar licença antes de monetizar (não-comercial na prática) | [ALEGADO] |
| **ElevenLabs** | Licença comercial nos planos pagos (Free não). Starter $6 → Creator $22 | [OFICIAL] |
| **Fish Audio** | Free **sem** uso comercial; Plus $11+ com licença comercial | [OFICIAL] |
| **Gemini / OpenAI TTS** | Uso via API paga conforme termos do provedor; divulgue IA ao público | [OFICIAL] |

**Regra prática:** canal monetizado com edge-tts → **migre a mesma voz para Azure** (idêntica, ex. `en-US-ChristopherNeural`) e durma tranquilo. Clone de terceiro sem consentimento = proibido em qualquer motor.

## Custo real por vídeo (~10 min ≈ 9.000 chars)

| Motor | Preço | 1 vídeo (10min) | 20 vídeos/mês |
|---|---|---|---|
| edge / kokoro / piper / chatterbox | $0 | $0 | $0 (+luz) |
| azure | ~$15/1M chars | ~$0,14 (0,5M grátis = ~55 vídeos) | ~$2,70 |
| fish | $15/1M bytes | ~$0,14 (Plus $11 ≈ 200 min) | ~$2,70 |
| gemini 2.5 flash tts | input $0,50 + output $10/1M tokens | ~$0,10–0,15 | ~$2–3 |
| openai gpt-4o-mini-tts | $0,60 + $12/1M tokens | ~$0,15–0,20 | ~$3–4 |
| elevenlabs flash/turbo | $0,05/1k chars | ~$0,45 | ~$9 |
| elevenlabs multilingual/v3 | $0,10/1k chars | ~$0,90 (Creator $22 ≈ 13 vídeos) | $22–99 plano |

> Retrabalho conta: Fish 1,5 geração/linha ainda é mais barato que ElevenLabs 1,1. Cache por hash no motor evita pagar 2x pelo mesmo bloco.

## Receitas por provider

### edge (grátis — padrão de produção)
- `pip install edge-tts`. Voz travada no contrato (`provider.voice_id`), prosódia por bloco (`rules.hook/beat/outro` + `series`).
- Vozes documentário EN: `en-US-ChristopherNeural` (-8%), `en-US-GuyNeural`. PT-BR: `pt-BR-AntonioNeural`, `pt-BR-FranciscaNeural`.
- Sem SSML custom (Microsoft bloqueia) → normalização é `normalize` (mapa no contrato) + pontuação.
- Bug conhecido: parágrafo sem caractere fálavel (`—` sozinho) → `NoAudioReceived`. O motor pula automático.

### azure (upgrade 1:1 do edge, licença comercial)
- Key em `AZURE_SPEECH_KEY`, região em `AZURE_SPEECH_REGION` (ex. `brazilsouth`). Mesmo `voice_id` do edge.
- SSML dá `rate`/`pitch`/`volume` nativos — prosódia idêntica ao edge.
- Migração de canal edge→azure: **zero mudança de som**, só o header da API.
- **Pronúncia perfeita de nome próprio:** SSML aceita `<phoneme alphabet="ipa" ph="...">` e **custom lexicon** (`.pls`/`.xml` público, suportado em pt-BR) — quando o respelling não resolve, é o recurso definitivo.

### kokoro (grátis, local, Apache 2.0)
- `pip install kokoro soundfile` + `espeak-ng` no sistema (Windows: instalar e por no PATH).
- `voice_id`: `am_michael`, `am_onyx` (EN), `pf_dora`, `pm_alex` (PT-BR). `settings.lang_code`: `a`=EN-US, `p`=PT-BR.
- Roda em CPU (RTF ~0.08), sem clone. Ideal para narração limpa em volume.

### piper (grátis, local, CPU mínimo)
- Binário + modelo `.onnx` (`settings.exe`, `voice_id` = caminho do `.onnx`).
- Qualidade abaixo de kokoro (prosódia achatada) — use onde latência/tamanho mandam.

### chatterbox / XTTS (clone local grátis)
- Chatterbox (MIT): clone de ~5s, 23 idiomas, dial de emoção. XTTS v2: melhor clone de ~6s, mas **não-comercial**.
- Referência: mono, 24kHz, 3–15s limpos, sem música/ruído. Rodar em GPU ajuda.

### elevenlabs (pago — naturalidade máxima)
- Key em `ELEVENLABS_API_KEY`. `provider.model`: `eleven_multilingual_v2` (long-form), `eleven_v3` (expressivo), `eleven_flash_v2_5` (barato).
- `voice_id` = ID da voz (library ou clone). `settings`: `stability`, `similarity_boost`, `style`, `use_speaker_boost`, `speed`.
- **IVC** = clone rápido (1min de áudio) para testar; **PVC** = 30min+ de áudio → voz de marca que se mantém por meses. Use PVC para narrador de canal.
- Créditos acabam rápido em long-form: cache + `--estimate` antes.

### fish (pago barato — clone + multilíngue)
- Key em `FISH_API_KEY`; `voice_id` = `reference_id` do clone (10–30s de áudio). `provider.model`: `s1` ou `s2-pro`.
- 80+ idiomas, code-switching, word-level timestamps (bom p/ karaokê). Limite por geração varia por plano (500 chars no free, 15k no Plus) → `settings.chunk_chars`.
- Phoneme controls (EN/ZH/JA) resolvem nome próprio que insiste em sair errado.

### gemini (pago barato — direção por prompt)
- Key em `GEMINI_API_KEY` (aceita múltiplas separadas por vírgula → rotação automática no 429). Modelo: `gemini-2.5-flash-preview-tts`.
- `voice_id` = uma das 30 vozes (`Algenib` grave, `Charon` informativo, `Kore` firme, `Puck` animado...). `settings.style` = direção em texto (ex. "Narre gravemente, ritmo lento, PT-BR").
- **Cota é por request** → chunks longos (~2000 chars) gastam menos cota E reduzem variação de tom entre takes. `settings.chunk_chars: 2000`.

### openai (pago — simples e steerable)
- Key em `OPENAI_API_KEY`. Modelo `gpt-4o-mini-tts`, vozes `onyx`/`cedar`/`marin` (melhores). `settings.instructions` = direção em texto.
- Sem clone; 2.000 tokens de input por request (≈1.400 palavras) → chunking automático.

## Clonagem de voz — regras

1. **Consentimento explícito** do dono da voz, por escrito, guardado com a data. Sem exceção.
2. Grave o dataset: sala tratada, mesmo microfone, 30min+ para PVC; 10–30s limpos para Fish/IVC.
3. Clone **da sua voz** é o caminho seguro para canal dark (você não aparece, mas a voz é sua).
4. Valide com `--test`: 200 palavras com nomes/preços/siglas **antes** de gerar o vídeo.
5. Divulgue IA ao público (política de conteúdo inautêntico + transparência — ref `09`).

## Pronúncia e normalização (o que mais estraga narração)

Duas camadas no contrato, nesta ordem:
1. **`normalize`** — troca simples: siglas faladas como letras (`FBI` → `F. B. I.`), títulos (`Mr.` → `Mister`), cargos PT (`Dr.` → `doutor`).
2. **`pronuncia`** — respellings calibrados, com fronteira de palavra (`\b`): `Samudio` → `Samúdio`, `rottweiler` → `rótiváiler`, `Vespasiano` → `Vespaziano`. **Plural antes do singular** na ordem do JSON.

**Como calibrar um respelling (método real):**
1. `python scripts/voice_engine.py videoNN --root <canal> --channel <canal> --pronounce "termo"` — gera o termo **isolado e em contexto**, transcreve com faster-whisper e flagra erro; os áudios ficam em `02_audio/_pronuncia/` para **ouvir**.
2. Ou faça A/B numerado de ouvido (ex.: `calibrar_pronuncia.py` do Laudo: baseline × grafias alternativas em um WAV com legenda).
3. Só então trave o par no `pronuncia` do playbook — um lugar só, vale para todos os vídeos do canal.

**Limites (seja honesto):** nenhum TTS é 100%; o checker é uma **rede**, não a verdade — o veredito usa o contexto (o isolado pode sair truncado no whisper small) e o gate final é a **oitiva humana** dos áudios salvos. Fish aceita phoneme controls (EN/ZH/JA) quando o respelling não resolve.

Outras regras:
- Números/anos/moeda: escreva como se fala na dúvida (`1998` → `nineteen ninety-eight`; `R$ 1,2 milhão` → `um vírgula dois milhão de reais`).
- `?` no fim de bloco ajuda prosódia no edge; vírgula vira micro-pausa; reticências viram respiro.
- Nunca conserte fala ruim com legenda — legenda é camada de compreensão (ref `13`).

## Cadeia de áudio (o que o motor faz)

```
blocos TTS → trim (0.1s / pad 0.8s) → gaps (curto 0.35s drama | normal 0.15s)
  → filtros de voz (highpass 70, lowpass 8k, compressor, gain)
  → [opcional] bed musical + ducking sidechain → loudnorm (I=-16 CFD | I=-14 Laudo)
  → voice_FINAL.wav + captions.srt
```

Quatro bugs conhecidos (já tratados no motor):
1. Bloco sem texto fálavel → pula (não chama TTS).
2. `concat -c copy` entre sample rates diferentes **dropa áudio silenciosamente** → sempre re-encode no concat.
3. Crédito/cota no meio do vídeo → cache por hash + chunking + rotação de chave.
4. Tom inconsistente entre takes → chunks longos por provider + mesma voz/settings no vídeo inteiro.

## Fallback e custo

- Cadeia `provider.fallback` no contrato: fallback com timbre diferente é bloqueado por padrão; use `--allow-voice-switch` somente após revisão humana e registre a troca no contrato.
- `--estimate` calcula chars do roteiro e o custo por provider **antes** de gastar.
- `--test` gera 200 palavras no provider real para aprovar a voz.

## QA de voz (gate antes do motion)

- [ ] `--preflight --require-free` passou com o canal correto.
- [ ] `--test` de 200 palavras aprovado (pronúncia + ritmo + tom).
- [ ] Voz é a do contrato (`--channel` certo; `_source` do contrato confere).
- [ ] `loudnorm` no alvo do projeto (-16 CFD / -14 Laudo).
- [ ] Sem clipe/estouro (limiter), sem respiro cortado no meio de frase.
- [ ] Captions no formato público e `AUDITORIA_CAPTIONS.md` sem falha.
- [ ] `PRONUNCIA_TTS.json` = `PASS` e `CONSISTENCIA_TTS.json` = `PASS`.
- [ ] Custo conferido com `--estimate` (se pago) + cache ativo.

## Checklist de decisão (canal novo)

- [ ] Idioma + tom definidos (grave/medido? energético?).
- [ ] Provider escolhido pela tabela de 30s (e pela licença, se monetiza).
- [ ] `provider` preenchido no `voice.json` do playbook (não copiar de outro canal).
- [ ] Voz travada: `voice_id` + `settings` + mapa `normalize`.
- [ ] `--test` aprovado antes de gerar o vídeo.
