"use client";
import { Nav } from "@/components/Nav";
import { Hero } from "@/components/Hero";
import { Marquee } from "@/components/Marquee";
import { Reveal } from "@/components/Reveal";
import { TiltCard } from "@/components/TiltCard";
import { Counter } from "@/components/Counter";
import { Logo } from "@/components/Logo";
import { MagneticButton } from "@/components/MagneticButton";
import { Outliers } from "@/components/Outliers";
import { VideoSection } from "@/components/VideoSection";
import { useI18n } from "@/lib/store";

export default function Page() {
  const { t } = useI18n();

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
                  <p className="eyebrow">{t.cap.eyebrow}</p>
                  <h2>{t.cap.title}</h2>
                </div>
                <p>{t.cap.sub}</p>
              </div>
            </Reveal>
            <div className="feat">
              {t.cap.items.map(([title, desc], i) => (
                <Reveal key={title} delay={i * 0.05}>
                  <TiltCard>
                    <article>
                      <span className="n">{String(i + 1).padStart(2, "0")}</span>
                      <h3>{title}</h3>
                      <p>{desc}</p>
                    </article>
                  </TiltCard>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        <Outliers />
        <VideoSection />

        <section id="fluxo">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">{t.fluxo.eyebrow}</p><h2>{t.fluxo.title}</h2></div>
                <p>{t.fluxo.sub}</p>
              </div>
            </Reveal>
            <div className="rows">
              <Reveal>
                <ul className="list">
                  {t.fluxo.cmds.map(([c, d]) => (<li key={c}><code>{c}</code><span>{d}</span></li>))}
                </ul>
              </Reveal>
              <Reveal delay={0.08}>
                <ul className="list">
                  {t.fluxo.agents.map(([c, d]) => (<li key={c}><code>{c}</code><span>{d}</span></li>))}
                </ul>
              </Reveal>
            </div>
          </div>
        </section>

        <section id="dados">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">{t.dados.eyebrow}</p><h2>{t.dados.title}</h2></div>
                <p>{t.dados.sub}</p>
              </div>
            </Reveal>
            <div className="stats">
              <Reveal><div><b><Counter to={32} /></b><small>{t.dados.stats[0]}</small></div></Reveal>
              <Reveal delay={0.05}><div><b><Counter to={12} /></b><small>{t.dados.stats[1]}</small></div></Reveal>
              <Reveal delay={0.1}><div><b><Counter to={7} /></b><small>{t.dados.stats[2]}</small></div></Reveal>
              <Reveal delay={0.15}><div><b><Counter to={12} /></b><small>{t.dados.stats[3]}</small></div></Reveal>
            </div>
          </div>
        </section>

        <section id="seguranca" style={{ borderBottom: "none" }}>
          <div className="wrap split">
            <Reveal>
              <p className="eyebrow">{t.seg.eyebrow}</p>
              <h2>{t.seg.title}</h2>
              <p className="lead" style={{ marginTop: 18 }}>
                {t.seg.body1} <em>{t.seg.bodyEm1}</em>{t.seg.body2} <em>{t.seg.bodyEm2}</em> {t.seg.body3}
              </p>
            </Reveal>
            <Reveal delay={0.1}>
              <div className="terminal">
                <div className="bar"><i /><i /><i /><span>secrets/</span></div>
                <pre>
                  <div><span className="m">~/.config/opencode/secrets/</span></div>
                  <div>  client_secrets.json   <span className="m"># OAuth (Desktop)</span></div>
                  <div>  yt-token.json         <span className="m"># read-only token</span></div>
                  <div>  dark.env              <span className="m"># DATABASE_URL (Neon)</span></div>
                  <div>{"\u00A0"}</div>
                  <div><span className="k">.gitignore</span> protects:</div>
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
            <a className="brand" href="/" style={{ marginBottom: 14 }}><Logo /> dark-master</a>
            <p>{t.footer.text}</p>
          </div>
          <div className="cta">
            <MagneticButton href="https://github.com/mateusoliveiradev1/dark-master">{t.footer.github}</MagneticButton>
            <MagneticButton href="/privacy">{t.footer.privacy}</MagneticButton>
          </div>
        </div>
      </footer>
    </>
  );
}
