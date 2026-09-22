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
└─ outliers.md    # dados reais e aprendizados daquele canal — quando houver
```
