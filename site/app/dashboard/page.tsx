"use client";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { Nav } from "@/components/Nav";
import { Reveal } from "@/components/Reveal";
import { useI18n } from "@/lib/store";
import { ALERT_PT, glossSeed } from "@/lib/painel";

type Alert = { type: string; seed: string; detail: string; examples: string[] };
type Channel = { handle: string; name: string; mine: boolean; nota: string };
type Detail = { status: string; videos?: number; views_30d?: number; engaged_30d?: number; engaged_rate?: number;
  top?: { title: string; views: number; format: string }[]; series?: { date: string; views: number }[];
  last_capture?: string };
type Ypp = { eligible_2026: boolean; eligible_2027: boolean; hours_gap_2027: number; daily_needed: number; maintenance_safe: boolean };
type Dashboard = { generated: string | null; channels: Channel[]; details?: Record<string, Detail>;
  loop_reports: { date: string; status: string; failed_steps: string[] }[]; alerts: Alert[]; ypp: Record<string, Ypp> };

const EMPTY: Dashboard = { generated: null, channels: [], loop_reports: [], alerts: [], ypp: {} };

function Spark({ series }: { series: { date: string; views: number }[] }) {
  const max = Math.max(1, ...series.map((p) => p.views));
  const pts = series.map((p, i) => `${(i / Math.max(1, series.length - 1)) * 100},${28 - (p.views / max) * 26}`).join(" ");
  return (
    <svg viewBox="0 0 100 30" style={{ width: "100%", height: 34 }} aria-hidden>
      <polyline points={pts} fill="none" stroke="var(--red-bright)" strokeWidth="1.6" />
    </svg>
  );
}

export default function DashboardPage() {
  const { t, lang } = useI18n();
  const d = t.dash;
  const [data, setData] = useState<Dashboard>(EMPTY);
  const [mineOnly, setMineOnly] = useState(false);
  useEffect(() => {
    fetch("/dashboard.json", { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : EMPTY))
      .then(setData)
      .catch(() => setData(EMPTY));
  }, []);
  const channels = useMemo(() => (mineOnly ? data.channels.filter((c) => c.mine) : data.channels), [data, mineOnly]);
  const mineCount = data.channels.filter((c) => c.mine).length;
  const pick = (mine: boolean) => {
    setMineOnly(mine);
    requestAnimationFrame(() => document.getElementById("canais")?.scrollIntoView({ behavior: "smooth" }));
  };
  const gloss = (seed: string) => (lang === "pt" ? glossSeed(seed) : null);

  return (
    <>
      <Nav />
      <main id="top">
        <section className="hero">
          <div className="wrap">
            <Reveal>
              <p className="tag"><i />{d.eyebrow} · {data.generated ?? "—"}</p>
              <h1>{d.titleA}<br />{d.titleB}</h1>
              <p className="lead">{d.sub}</p>
              <div className="cta" role="tablist" aria-label={d.channels}>
                <button role="tab" aria-selected={!mineOnly} className={`btn${!mineOnly ? " primary" : ""}`} onClick={() => pick(false)}>
                  <span />{d.all} ({data.channels.length})
                </button>
                <button role="tab" aria-selected={mineOnly} className={`btn${mineOnly ? " primary" : ""}`} onClick={() => pick(true)}>
                  <span />{d.mine} ({mineCount})
                </button>
                <Link className="btn" href="/"><span />{d.back}</Link>
              </div>
            </Reveal>
          </div>
        </section>

        <section id="alertas">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">{d.alerts}</p><h2>{d.alerts}</h2></div>
                <p>{data.alerts.length} {lang === "pt" ? "sinais acionáveis da última pesquisa" : "actionable signals from the last research"}</p>
              </div>
            </Reveal>
            {data.alerts.length === 0 && <p className="muted">{d.noAlerts}</p>}
            <div className="outliers">
              {data.alerts.map((a, i) => {
                const g = gloss(a.seed);
                const label = lang === "pt" ? ALERT_PT[a.type]?.titulo ?? a.type : a.type;
                return (
                  <Reveal key={`${a.type}-${a.seed}-${i}`} delay={Math.min(i, 5) * 0.04}>
                    <article className={`ocard${i === 0 ? " best" : ""}`}>
                      <div className="ocard-top"><span className="fmt">{a.type}</span><span className="otag">{label}</span></div>
                      <h3>{a.seed || "—"}</h3>
                      <p className="muted">{a.detail}</p>
                      {g && <p><em>{g.o_que}.</em> {g.porque}.</p>}
                      {lang === "pt" && ALERT_PT[a.type] && <p className="muted">{ALERT_PT[a.type].acao}</p>}
                      {a.examples.length > 0 && <p className="muted" style={{ fontSize: "13px" }}>{a.examples.join(" · ")}</p>}
                    </article>
                  </Reveal>
                );
              })}
            </div>
          </div>
        </section>

        <section id="canais">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">{d.channels}</p><h2>{d.channels} ({channels.length})</h2></div>
              </div>
            </Reveal>
            {channels.length === 0 && <p className="muted">{d.emptyMine}</p>}
            <div className="outliers">
              {channels.map((c, i) => {
                const det = data.details?.[c.handle];
                const y = data.ypp[c.handle];
                return (
                  <Reveal key={c.handle} delay={Math.min(i, 5) * 0.04}>
                    <article className={`ocard${c.mine ? " best" : ""}`}>
                      <div className="ocard-top"><span className="fmt">{c.handle}</span><span className="otag">{c.mine ? d.mine : "vigia"}</span></div>
                      <h3>{c.name}</h3>
                      {det?.status === "ok" ? (
                        <>
                          <div className="ometric"><b>{det.views_30d?.toLocaleString("pt-BR")}</b><small>{d.views30d} · {det.videos} vídeos</small></div>
                          {det.series && det.series.length > 1 && <Spark series={det.series} />}
                          <p className="muted" style={{ fontSize: "13px" }}>
                            {d.engaged} {det.engaged_rate}% · {d.lastCapture} {det.last_capture ?? "—"}
                          </p>
                        </>
                      ) : (
                        <p className="muted">{d.awaiting}</p>
                      )}
                      {y && (
                        <p style={{ fontSize: "13.5px" }}>
                          {d.ypp2026}: {y.eligible_2026 ? d.ok : "—"} · {d.ypp2027}: {y.eligible_2027 ? d.ok : `${y.hours_gap_2027}h (~${y.daily_needed}h/dia)`}
                          <br />{d.maintenance}: {y.maintenance_safe ? d.ok : d.attention}
                        </p>
                      )}
                      <p><Link href={`/dashboard/${encodeURIComponent(c.handle.replace(/^@/, ""))}`} style={{ color: "var(--red-bright)" }}>{d.open}</Link></p>
                    </article>
                  </Reveal>
                );
              })}
            </div>
          </div>
        </section>

        <section id="loop">
          <div className="wrap">
            <Reveal>
              <div className="sec-head">
                <div><p className="eyebrow">{d.loop}</p><h2>{d.howTitle}</h2></div>
              </div>
            </Reveal>
            <ul className="list">
              {d.how.map(([t, s]) => (
                <li key={t}><code>{t}</code><span>{s}</span></li>
              ))}
            </ul>
            <div className="stats">
              {data.loop_reports.slice(-4).map((r) => (
                <div key={r.date}><b style={{ fontSize: "clamp(28px,4vw,44px)" }}>{r.status}</b><small>{r.date}{r.failed_steps.length > 0 ? ` · ${r.failed_steps.length} falhas` : ""}</small></div>
              ))}
            </div>
          </div>
        </section>
      </main>
    </>
  );
}
