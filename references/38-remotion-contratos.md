# 38 — Contratos visuais e direção de arte

## Fontes de verdade

- `profile.md` define identidade, público, tom e operação.
- `style.json` define idioma, branding, imagem, tipografia, captions, safe areas e tokens visuais.
- `motion.json` define engine, tamanho, FPS, duração, motion, transições e render.
- `ROTEIRO_MAP.json` define semântica, ordem e estado de cada bloco.
- `RENDER_PLAN` combina esses dados sem modificar o roteiro.

## Visual Bible

Toda direção visual deve resolver:

- identidade e mood;
- paleta e contraste;
- headline, metadata, body e captions;
- safe areas e hierarquia;
- imagem, crop, portrait, documento, map, evidence, timeline e comparação;
- transições, câmera, parallax, motion blur, grain, texture e vignette;
- captions, watermark, end card e sound direction;
- padrões proibidos e limites de texto.

A Visual Bible é específica do canal e pode ter overrides por série. Ela nunca herda paleta, fonte, voz ou motion de outro canal.

## Escolha de cena

A escolha é por função editorial:

- `cinematic-photo`: estabelecer lugar e tensão;
- `evidence-reveal`: mostrar prova e leitura;
- `evidence-table`: organizar dados;
- `investigation-board`: conectar relações;
- `timeline` e `timeline-detail`: estabelecer passagem do tempo;
- `geographic-location` e mapas: orientar o espaço;
- documentos e archive: tratar fonte e contexto;
- portrait e object-detail: humanizar ou materializar;
- split-screen e compare-contrast: criar contraste;
- quote: amplificar uma afirmação;
- data-visualization: explicar relação mensurável;
- concept-diagram: explicar estrutura;
- chapter-break: marcar mudança de estado;
- surveillance e security-camera: tratar câmera como evidência;
- end-card-cta: fechar identidade e ação.

## Contrato v2 do RenderPlan

Novos episódios usam `RenderPlan.version: 2`. O plano deve carregar:

- `visualBible` e hashes dos contratos;
- `claimIds`, `sourceBlockIds` e `sourceIds` por cena;
- `promptId` e `assetLedger` com origem, direitos e hash;
- `states` com `timeRange`, `intent`, camadas, assets, anotação e movimento;
- `cropPolicy` para Long e Short;
- transições interpretadas pelo runtime;
- captions dentro da duração do plano.

O schema aceita planos v1 apenas para compatibilidade legada. Novos planos não podem usar o fallback silencioso de imagem por índice, asset sem manifest, claim sem fonte ou cena sem rastro de estado.

A pontuação vai de 0 a 100 e cobre clareza, marca, hierarquia, tipografia, composição, crop, repetição, motion, captions, pacing, assets, sync e segurança. O render só é aprovado sem BLOCKER/MAJOR e com score mínimo 92. A revisão independente é obrigatória; o diretor de arte não se autoaprove.

## Imagens geradas por IA

Imagens IA entram como assets de cena, nunca como slideshow automático. A skill pode usar imagens para fundos, plates, retratos, documentos, mapas, texturas, objetos e reconstruções. O Remotion responde por crop, parallax, composição, overlays, motion, captions, áudio, sincronização e export. Assets externos/sintéticos devem ter origem e status de direitos registrados no ledger do canal.
