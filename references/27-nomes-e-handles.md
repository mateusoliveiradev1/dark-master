# 27 — Nomes e handles (pesquisa de disponibilidade)

Como escolher e **verificar** nome de canal e @handle antes de criar. Fonte: YouTube Help + Data API. [OFICIAL/PRATICANTE]

## Regras de nome

- **Curto, pronunciável, fácil de digitar.** Evite números/letras ambíguos (0/O, 1/l).
- **Ligado ao nicho** sem ser genérico ("Arquivo X" > "Canal de Mistérios").
- **Sem confusão com marca existente.** Não use nomes de canais grandes (ex.: "Cold Case Files").
- **Combine com o formato**: dark/história/true crime → tom sóbrio; Shorts → mais direto.
- Evite **palavras sensíveis** e marcas registradas.

## @handle (regras oficiais)

- 3–30 caracteres; letras, números, `_`, `-`, `.`.
- Único no YouTube. Pode diferir do nome de exibição.
- `youtube.com/@handle`.

## Verificação de disponibilidade (dois métodos)

### 1) Data API (com OAuth já configurado)
```bash
python scripts/name_check.py "Cold File Diaries" "Arquivo Sombrio" "Dark Ledger"
```
- Busca `channels.list?forHandle=@handle` e `search.list` pelo nome.
- Reporta: handle existe? canais com nome parecido? risco de confusão.

### 2) Checagem manual
- Abra `youtube.com/@handle` — 404 = livre (provável).
- Busque o nome no YouTube e no Google.
- Veja se há marca/empresa com o nome (INPI/EUIPO para registro).

## Padrão de decisão

| Sinal | Ação |
|---|---|
| Handle existe + canal ativo no nicho | descartar |
| Nome usado por canal grande | descartar (evita A&E-style) |
| Handle livre + nome limpo | forte candidato |
| Nome genérico mas livre | ok, mas diferencie no posicionamento |

> Um nome "livre" **não** garante marca registrada. Para uso comercial sério, cheque o registro de marca.

## Saída

Registre no `config/FOCUS.md` e no playbook do canal: nome escolhido, handle, fallback (ex.: `@NomeUS`), e data da checagem.
