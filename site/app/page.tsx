import { Nav } from "@/components/Nav";
import { Hero } from "@/components/Hero";
import { Marquee } from "@/components/Marquee";
import { Reveal } from "@/components/Reveal";
import { TiltCard } from "@/components/TiltCard";
import { Counter } from "@/components/Counter";
import { Logo } from "@/components/Logo";
import { MagneticButton } from "@/components/MagneticButton";

const FEATURES = [
  ["01", "Algoritmo & retenção", "Shorts (engaged views, swipe-away, loops) e long-form (CTR, AVD, AVP, 1º minuto, por minuto)."],
  ["02", "Roteiro & hooks", "Y1–Y11 de títulos, cold open, promise stack, escalada, rehooks a cada 2–4 min, final abrupto."],
  ["03", "Thumbnails & A/B", "Psicologia de clique, composição legível a 120px, 3 variantes para Test & Compare."],
  ["04", "Monetização", "Trilha 0→YPP, playbook das 4.000h, funil Short→long, produto digital $7–27."],
  ["05", "Auto-evolução", "Puxa métricas reais, detecta outliers e propõe mudanças com evidência. Nada muda sem seu OK."],
  ["06", "Entende o canal", "Lê calendário, regras travadas e a corrente de teaser antes de gerar qualquer coisa."],
] as const;

const CMDS = [
  ["/dark-canal", "Lê o projeto: calendário, regras e corrente de teaser."],
  ["/dark", "Ideia → título → thumb → roteiro → checklist."],
  ["/dark-build", "Roda o pipeline de produção do canal alvo."],
  ["/dark-audit", "Gate anti-inauthentic + YPP + divulgação de IA."],
  ["/dark-scan", "Varre canais e alerta outliers acima da baseline."],
  ["/dark-revisar", "Loop semanal: métricas → aprendizados → propostas."],
  ["/dark-monetizar", "Trilha 0→YPP com metas e checkpoints."],
] as const;

const AGENTS = [
  ["strategist", "Ideação, packaging e diagnóstico por métrica."],
  ["roteirista", "Long-form (5 atos) e Shorts (hook + loop)."],
  ["packager", "Títulos, capítulos e plano de A/B."],
  ["auditor", "Compliance YPP e conteúdo inautêntico."],
  ["produtor", "Executa imagens, voz e motion por canal."],
  ["analyst", "Lê métricas e propõe evolução com evidência."],
  ["scout", "Nichos, subnichos e outliers de concorrentes."],
] as const;

export default function Page() {
  return (
    <>
      <Nav />
      <main id="top">
        <Hero />
        <Marquee />

        <section id="capacidades">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div>
                  <p className="eyebrow">Capacidades</p>
                  <h2>Um sistema, não um prompt.</h2>
                </div>
                <p>Cada peça da operação de um canal dark — do gancho à esteira de produção — destilada, testada e ligada aos seus próprios pipelines.</p>
              </div>
            </Reveal>
            <div className="feat">
              {FEATURES.map(([n, t, d], i) => (
                <Reveal key={n} delay={i * 0.05}>
                  <TiltCard>
                    <article>
                      <span className="n">{n}</span>
                      <h3>{t}</h3>
                      <p>{d}</p>
                    </article>
                  </TiltCard>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        <section id="fluxo">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">Fluxo</p><h2>Comandos que operam o canal.</h2></div>
                <p>Setar o foco, entender o canal, produzir, auditar e revisar — tudo por comando.</p>
              </div>
            </Reveal>
            <div className="rows">
              <Reveal>
                <ul className="list">
                  {CMDS.map(([c, d]) => (<li key={c}><code>{c}</code><span>{d}</span></li>))}
                </ul>
              </Reveal>
              <Reveal delay={0.08}>
                <ul className="list">
                  {AGENTS.map(([c, d]) => (<li key={c}><code>{c}</code><span>{d}</span></li>))}
                </ul>
              </Reveal>
            </div>
          </div>
        </section>

        <section id="dados">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">Motor de dados</p><h2>Métricas reais, memória que cresce.</h2></div>
                <p>Conecta à YouTube Analytics API via OAuth, grava snapshots em Postgres (Neon) e alimenta um loop de melhoria contínua. Sem banco pago, sem chute.</p>
              </div>
            </Reveal>
            <div className="stats">
              <Reveal><div><b><Counter to={30} /></b><small>references</small></div></Reveal>
              <Reveal delay={0.05}><div><b><Counter to={10} /></b><small>comandos</small></div></Reveal>
              <Reveal delay={0.1}><div><b><Counter to={7} /></b><small>subagentes</small></div></Reveal>
              <Reveal delay={0.15}><div><b><Counter to={9} /></b><small>scripts</small></div></Reveal>
            </div>
          </div>
        </section>

        <section id="seguranca" style={{ borderBottom: "none" }}>
          <div className="wrap split">
            <Reveal>
              <p className="eyebrow">Segurança</p>
              <h2>Suas chaves, sua máquina.</h2>
              <p className="lead" style={{ marginTop: 18 }}>
                As credenciais do Google e a string de banco ficam <em>fora do repositório</em>, numa pasta local de segredos.
                O token só acessa <em>leitura</em> do seu próprio canal.
              </p>
            </Reveal>
            <Reveal delay={0.1}>
              <div className="terminal">
                <div className="bar"><i /><i /><i /><span>secrets/</span></div>
                <pre>
                  <div><span className="m">~/.config/opencode/secrets/</span></div>
                  <div>  client_secrets.json   <span className="m"># OAuth (Desktop)</span></div>
                  <div>  yt-token.json         <span className="m"># leitura do canal</span></div>
                  <div>  dark.env              <span className="m"># DATABASE_URL (Neon)</span></div>
                  <div>{"\u00A0"}</div>
                  <div><span className="k">.gitignore</span> protege:</div>
                  <div>  vendors/*/   data/dark.db</div>
                </pre>
              </div>
            </Reveal>
          </div>
        </section>
      </main>

      <footer>
        <div className="wrap foot">
          <div>
            <a className="brand" href="#top" style={{ marginBottom: 14 }}><Logo /> dark-master</a>
            <p>Skill open-source para planejar, produzir e monetizar canais dark no YouTube. Feita para rodar dentro do opencode, sobre os seus próprios pipelines.</p>
          </div>
          <div className="cta">
            <MagneticButton href="https://github.com/mateusoliveiradev1/dark-master">GitHub</MagneticButton>
            <MagneticButton href="/privacy">Privacidade</MagneticButton>
          </div>
        </div>
      </footer>
    </>
  );
}
