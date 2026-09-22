# FOCUS — objetivo atual da skill

> **Este arquivo manda em tudo.** Todo comando/agente lê o FOCUS ANTES de agir. Revise semanalmente (`/dark-revisar`).

## Foco vigente

- **Data de referência:** 2026-09-22
- **Canal alvo:** **Cold File Diaries** — existente (EN true crime · `playbooks/cold-file-diaries/`)
- **Objetivo:** monetizar (**YPP**) + crescer inscritos, destravando o tráfego para o long-form
- **Métrica norte:** **watch hours** (long) + **conversão Short→long** (e inscritos como proxy de alcance)
- **Horizonte:** 30 dias de execução · **prazo duro: 01/02/2027** (requisitos dobram: 8.000h / 20M)
- **Orçamento:** free tier (edge-tts + imagens procedurais; ElevenLabs quando validar)
- **Idioma:** en (auto-dub nos 2–3 idiomas dominantes)
- **Formato (lane):** **mixed** — Short = aquisição, long = receita; manter só se o funil estiver **medido**
- **Playbook do canal:** `playbooks/cold-file-diaries/` (profile + operacao + outliers)

## Diagnóstico / baseline (evidência em `data/`)

- **Loop vence:** Springfield Three (Short, AVP **136%**) → 7,25h e 4 inscritos vs Yuba (AVP 43%) → 1 inscrito. Meta: AVP > 100%.
- **Long retém quem chega, mas não recebe tráfego:** Zodiac long AVD 907s com **66 views**; Sodder long 5 inscritos com 20 views. O gargalo é **tráfego**, não conteúdo.
- Shorts vencedores ~1,2K views (Cooper, Springfield, Yuba); longs ~22 views → precisa **~1.300× mais views/long** ou um breakout.
- Hook abstrato/filosófico derrubou alcance (video01) → **proibido abstração no hook** (regra aprendida).
- Padrões travados: **SHORT 2** (2ª pessoa + número impossível + pergunta) e **SHORT 3** (karaokê narrando no mudo + loop aberto) — não reabrir shorts 01–22 viralizados.

## Prioridades (ordem)

1. **Funil Short→long montado e medido**: Related Video + comentário fixado + CTA falado específico do caso; medir % de views do long vindas do Short (traffic source).
2. **Escalar o loop (AVP >100%)** em todo Short novo, replicando o padrão vencedor (não a frase).
3. **Cadência de lançamento**: 1 LONG + 1 SHORT/dia (mesmo caso), nunca abaixo de 7 agendados; registrar D+2/D+7.
4. **Auto-dub + títulos traduzidos** ligados (alcance grátis) e 1 live/semana para horas.
5. **Revalidar nichos adjacentes** via `/dark-nicho` (models/ já traz evidência: cold cases, heists, crime organizado e serial killers com fome cross-canal).

## Regras do foco

- Nunca sacrificar **compliance** (conteúdo inautêntico/YPP) por velocidade.
- **Travas absolutas** (não mudar sem aprovação explícita): `REGRA_METADATA*`, padrões de Short, arquivos do projeto, este `FOCUS.md`.
- Proposta de evolução precisa de **evidência** (`data/`) e melhora a métrica norte sem quebrar baseline.
- Roteiro sempre com pesquisa (`references/30` + subagentes) e anti-IA (`17`); Short segue `31`.

## Troca de foco

Quando o objetivo for atingido ou expirar, rode `/dark-focus` e reavalie (próximo canal, novo idioma, produto, etc.).
