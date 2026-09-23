# Playbooks — casos de estudo (NÃO são regras gerais)

Cada pasta aqui é um **playbook de um canal específico** — comportamento real, dados reais e decisões travadas daquele canal. Servem como **caso de estudo e motor de produção**, não como padrão a copiar.

## ⚠️ Regra de ouro

**Canal novo ≠ clone de um playbook.** Ao criar um canal do zero, **não** importe por padrão:
- voz / ritmo / sotaque do playbook;
- nomes de séries e formato de calendário;
- regras de metadata e fórmulas de título;
- padrões de Short (2/3/4);
- paleta e branding.

Essas decisões foram tomadas para **aquele** canal, com **aquele** público e **aquela** evidência. Um canal novo define as suas próprias a partir de pesquisa (`references/23`) e do `config/FOCUS.md`.

O que **pode** ser reaproveitado de um playbook:
- **método de produção** e mapa de scripts (engines);
- **lições** de algoritmo/aprendizado (ex.: "loop funciona") — como hipótese a testar, não lei;
- **estrutura de pastas** e organização (`references/26`).

## Playbooks existentes

| Playbook | Canal | Idioma/gênero | Serve como |
|---|---|---|---|
| `cold-file-diaries/` | Cold File Diaries | EN true crime | caso de estudo + engine de produção |
| `financial-crime-files/` | Financial Crime Files | EN crime financeiro | engine de produção |
| `laudo-final/` | Laudo Final | PT perícia | engine de produção |
| `midnight-archive/` | The Midnight Archive | EN dark history | engine de produção |

## Estrutura de um playbook

```
playbooks/<canal>/
├─ profile.md     # identidade, branding, voz, calendário, projeto no disco
├─ operacao.md    # regras travadas (metadata, roteiro, padrões, checklists) — quando houver
├─ outliers.md    # dados reais e aprendizados daquele canal — quando houver
├─ voice.json     # CONTRATO de voz: provider (motor TTS), voice id, normalize, pronuncia, regras por bloco/série, gaps, beds, ducking
├─ motion.json    # CONTRATO de motion: clip_len default e por clima/série, variantes, grade, letterbox, grain
├─ style.json     # CONTRATO de estilo: idioma, sufixo de imagem, séries, porte de imagens, thumb, short, package
└─ roteiro.json   # CONTRATO de roteiro (opcional): duração/palavras do canal quando o porte genérico não vale (ex. Laudo Final ~10min)
```

## Contrato de config do canal (anti-clone)

Os scripts de produção **não têm identidade hardcoded**: cada canal define a sua em `voice.json` / `motion.json` / `style.json` e os scripts leem daí. Canal novo ≠ clone de playbook — copie a **estrutura** do contrato, nunca os valores.

**Resolução (a primeira que existir vence):**
1. `--channel <nome|pasta|arquivo.json>` (nome resolve em `playbooks/<nome>`);
2. `DARK_CHANNEL` (env);
3. `canal.json` na raiz do projeto (com seções `voice`/`motion`/`style`);
4. `playbooks/cold-file-diaries/` (default quando existe);
5. defaults embutidos do CFD + **AVISO** (nunca silencioso).

- Playbooks procurados em `DARK_MASTER_PLAYBOOKS` ou `~/.config/opencode/skills/dark-master/playbooks`.
- Scripts que já aceitam `--channel`: `gerar_voz_v3`, `padrao_bed`, `montar_motion`, `padrao_short`, `fazer_thumb_v2`, `novo_video` (canal) e `new_video`/`prompt_builder --suffix` (skill).
- O **CFD** está migrado para o contrato: os JSONs reproduzem exatamente os valores anteriores (prova: 272 comparações dry-run, zero divergência).

### Bloco `provider` (motor TTS)

O `voice.json` aceita um bloco `provider` — o **motor** de voz, independente da voz em si:

```json
"provider": {
  "type": "edge | azure | elevenlabs | fish | gemini | openai | kokoro | piper",
  "fallback": ["azure", "kokoro"],
  "voice_id": "en-US-ChristopherNeural",
  "model": "eleven_multilingual_v2",
  "api_key_env": "ELEVENLABS_API_KEY",
  "settings": { "stability": 0.45, "similarity_boost": 0.75 }
}
```

- **Compatível para trás:** sem `provider`, o motor infere do campo `engine`/`voice` (schema antigo continua funcionando — o `gerar_voz_v3.py` do CFD não muda).
- `voice_id` ausente cai para o campo `voice` do schema antigo.
- `api_key_env` aceita múltiplas chaves separadas por vírgula (rotação automática no 429).
- `fallback`: cadeia usada quando o provider principal falha — o motor **avisa** antes de cair (nunca silencioso).
- Chaves de API **nunca** vão no JSON: só o **nome** da variável de ambiente (`api_key_env`).
- Guia completo de escolha, custos, licenças e receitas por provider: `references/34-voz-tts.md`.
- Motor unificado: `python scripts/voice_engine.py videoNN --channel <canal> [--test|--estimate|--dry-run]`.

### Bloco `roteiro` (porte do canal)

`roteiro.json` (opcional) define o **formato de roteiro** quando o porte genérico da skill não vale.

**Formato único** (canais com um só tamanho, ex. Laudo Final ~10min):
```json
{ "duracao_min": 10, "palavras": [1300, 1700], "palavras_alvo": 1500, "blocos_alvo": 40, "wpm": 145 }
```

**Múltiplos portes** (canais com fino/padrão/rico próprios, ex. CFD):
```json
{ "duracao_min": 20, "porte_default": "padrao",
  "portes": { "fino": [2300, 2700], "padrao": [2900, 3200], "rico": [3400, 3700] } }
```

- `python scripts/script_builder.py --validate <narration> --channel <canal> [--porte rico]` usa a faixa do canal (plano e validação); `--porte` escolhe o porte quando o canal tem vários.
- Sem o arquivo, o script avisa e cai no porte genérico (`fino/padrao/rico`) — nunca silencioso.
- **Sempre que possível, calibre com narrações reais** (palavras medidas), não com o que o profile promete — foi assim que Money (2479–2992 reais vs 3400 prometido) e Laudo (1540 reais) entraram na faixa certa.
