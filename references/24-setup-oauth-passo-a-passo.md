# 24 — Setup OAuth do YouTube (passo a passo)

Guia definitivo para conectar a skill às métricas do YouTube. Faça uma vez.

## Pré-requisito
Faça login no Google com a **mesma conta** que vai autorizar o canal (a que tem o canal Cold File Diaries).

## Parte 1 — Projeto e APIs
1. Abra https://console.cloud.google.com/
2. No topo, no **seletor de projeto**, escolha o projeto do seu JSON (ex.: `gen-lang-client-0322057065`). Se não existir, crie um novo ("Novo projeto").
3. Menu **☰ → "APIs e serviços" → "Biblioteca"**.
4. Procure e **habilite** as DUAS:
   - **YouTube Data API v3**
   - **YouTube Analytics API**

## Parte 2 — Tela de permissão OAuth
5. Menu **☰ → "APIs e serviços" → "Tela de permissão OAuth"**.
6. Se pedir para configurar: tipo **Externo** → Criar; preencha nome do app (`dark master`), e-mail de suporte e contato; salve e continue.
7. Em **"Usuários de teste"**, clique **"ADICIONAR USUÁRIOS"** e adicione o(s) e-mail(s) que vão autorizar. **Salvar.**
   - ⚠️ Sem isso, o login dá **`403: access_denied`**.
8. (Recomendado) Clique **"PUBLICAR APP"**. Evita o token expirar em 7 dias (app em Teste expira).

## Parte 3 — Credenciais
9. Menu **☰ → "APIs e serviços" → "Credenciais"**.
10. **"Criar credenciais" → "ID do cliente OAuth"** → tipo **"Aplicativo para computador" (Desktop app)** → Criar.
11. **Baixar o JSON**.
12. Salve o arquivo como:
    `C:\Users\Liiiraa\.config\opencode\secrets\client_secrets.json`

## Parte 4 — Autorizar (uma vez)
13. Rode: `python scripts/yt_auth.py`
14. Escolha a conta, clique **"Permitir"** (pode aparecer "app não verificado" → "Avançado" → "Acessar").

## Parte 5 — Testar
15. `python scripts/yt_db.py doctor`  → deve dizer `[OK] conexao funcionando`
16. `python scripts/yt_metrics.py`    → puxa métricas do canal
17. `python scripts/yt_scan_outliers.py --watch` → alerta de outliers

## Erros comuns
| Erro | Conserto |
|---|---|
| `403: access_denied` | Adicionar a conta em **Usuários de teste** (passo 7) ou **Publicar app** (passo 8) |
| `redirect_uri_mismatch` | Recriar o Client ID como **Desktop app** (passo 10) |
| `client_secrets.json nao encontrado` | Ver o caminho do passo 12 |
| Token expirando em 7 dias | Publicar o app (passo 8) |
| Sem receita nos reports | Normal antes de monetizar (YPP) |

## Segurança
- `client_secrets.json`, `yt-token.json` e `dark.env` ficam em `~/.config/opencode/secrets/` — **fora do repositório**.
- Nunca cole essas strings em issues/commits.

## Publicar o app (opcional) — valores de branding

Site (GitHub Pages) já no ar:
- Landing: `https://mateusoliveiradev1.github.io/dark-master/`
- Privacidade: `https://mateusoliveiradev1.github.io/dark-master/privacy.html`

Preencha na **Tela de permissão OAuth**:
| Campo | Valor |
|---|---|
| Página inicial do aplicativo | `https://mateusoliveiradev1.github.io/dark-master/` |
| Link da Política de Privacidade | `https://mateusoliveiradev1.github.io/dark-master/privacy.html` |
| Link dos Termos de Serviço | `https://github.com/mateusoliveiradev1/dark-master` |
| Domínios autorizados | `mateusoliveiradev1.github.io` |

Depois clique em **"Publicar app"**. Assim o refresh token **não expira em 7 dias**.
(Publicar com escopos sensíveis mostra o aviso "app não verificado" — normal para uso pessoal.)
