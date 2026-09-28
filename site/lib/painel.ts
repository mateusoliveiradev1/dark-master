// Glosas PT-BR para o painel: keywords EN ficam originais (são termos de
// busca — traduzir destrói o valor), mas cada uma ganha "o que é + por que importa".
export const SEED_PT: Record<string, { o_que: string; porque: string }> = {
  "fraud documentary": { o_que: "Documentários sobre golpes financeiros", porque: "Nicho de RPM alto ($12–22); cada caso rende tese + números" },
  "heist documentary": { o_que: "Documentários sobre roubos históricos", porque: "Alto apelo visual (mapas, rotas) e arcos prontos de queda" },
  "cold case documentary": { o_que: "Casos arquivados sem solução", porque: "Evergreen por definição; pergunta central nunca expira" },
  "cybercrime documentary": { o_que: "Crimes digitais e hackers", porque: "Em ALTA no YouTube 12m; público jovem, hook técnico" },
  "crypto scam documentary": { o_que: "Golpes com criptomoedas", porque: "Em ALTA; cifras grandes + vilões nomeáveis" },
  "cult documentary": { o_que: "Seitas e cultos", porque: "Personagens extremos + arquivo abundante; queries novas surgindo" },
  "dictatorship documentary": { o_que: "Ditaduras e regimes", porque: "Em ALTA; Brasil/Espanha/Portugal têm busca própria em PT" },
  "aviation disaster documentary": { o_que: "Acidentes aéreos", porque: "Nicho denso com laudos públicos (fonte primária pronta)" },
  "archaeology mystery documentary": { o_que: "Mistérios arqueológicos", porque: "Arte procedural barata + curiosidade universal" },
  "lost civilization documentary": { o_que: "Civilizações perdidas", porque: "Em ALTA; mapas e reconstruções seguram retenção" },
  "industrial disaster documentary": { o_que: "Desastres industriais", porque: "Modelo Fascinating Horror: contido, barato, evergreen" },
  "forgotten war documentary": { o_que: "Guerras esquecidas", porque: "Em ALTA; pouca concorrência faceless em PT" },
  "deep sea mystery documentary": { o_que: "Mistérios do oceano profundo", porque: "Visual alienígena com footage de arquivo" },
  "hoax documentary": { o_que: "Farsas e boatos famosos", porque: "Estrutura pronta: crença → desmonte → reviravolta" },
  "history of pandemics documentary": { o_que: "História de pandemias", porque: "Documental puro, dados públicos (CDC/OMS)" },
  "ai failure documentary": { o_que: "Falhas de IA e tecnologia", porque: "Tema quente com pouca oferta documental séria" },
  "forensic toxicology documentary": { o_que: "Toxicologia forense", porque: "Forensic-focus = menor yellow-icon no crime" },
  "medical mystery documentary": { o_que: "Mistérios médicos", porque: "Cuidado: saúde é tema sensível p/ persona IA" },
  "corporate collapse documentary": { o_que: "Colapsos corporativos", porque: "Modelo MagnatesMedia: 1 empresa, queda nos 30s" },
};

export const ALERT_PT: Record<string, { titulo: string; acao: string }> = {
  TREND_UP: { titulo: "Em alta", acao: "Virou pauta: use a query exata no título de um piloto em 2 semanas." },
  DEMAND_DEPTH: { titulo: "Demanda", acao: "Perguntas reais do autocomplete — cada uma é um título em potencial." },
  OUTLIER_FLARE: { titulo: "Outlier", acao: "Vídeo batendo a baseline: dissecar hook, tema e thumb e replicar o eixo." },
  REVALIDATE_DUE: { titulo: "Revalidar", acao: "Nicho parado há 14+ dias: rodar novo scan antes de investir." },
  FUNNEL_GAP: { titulo: "Funil", acao: "Short sem ponte para o long: completar o SHORT_FUNNEL." },
  BASELINE: { titulo: "Base", acao: "Primeira medição: serve de régua para as próximas rodadas." },
};

export function glossSeed(seed: string): { o_que: string; porque: string } | null {
  const key = seed.trim().toLowerCase();
  return SEED_PT[key] ?? null;
}
