"use client";
import { useEffect, useState } from "react";

type Alert = { type: string; seed: string; detail: string; examples: string[] };
type Channel = { handle: string; name: string; mine: boolean; nota: string };
type Ypp = { eligible_2026: boolean; eligible_2027: boolean; hours_gap_2027: number; daily_needed: number; maintenance_safe: boolean };
type Dashboard = { generated: string | null; channels: Channel[]; loop_reports: { date: string; status: string; failed_steps: string[] }[]; alerts: Alert[]; ypp: Record<string, Ypp> };

const EMPTY: Dashboard = { generated: null, channels: [], loop_reports: [], alerts: [], ypp: {} };
const ALERT_LABEL: Record<string, string> = { TREND_UP: "em alta", DEMAND_DEPTH: "demanda", OUTLIER_FLARE: "outlier", REVALIDATE_DUE: "revalidar", FUNNEL_GAP: "funil", BASELINE: "base" };

export default function DashboardPage() {
  const [data, setData] = useState<Dashboard>(EMPTY);
  const [mineOnly, setMineOnly] = useState(false);
  useEffect(() => {
    fetch("/dashboard.json", { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : EMPTY))
      .then(setData)
      .catch(() => setData(EMPTY));
  }, []);
  const channels = mineOnly ? data.channels.filter((c) => c.mine) : data.channels;
  return (
    <main id="top">
      <div className="wrap">
        <p className="eyebrow">painel · atualizado {data.generated ?? "—"}</p>
        <h1 style={{ fontSize: "clamp(2rem,5vw,3.5rem)", margin: "0 0 0.5rem" }}>Todos os canais, um arquivo.</h1>
        <p style={{ opacity: 0.75, maxWidth: "60ch" }}>
          Pesquisa automática (títulos, nichos, em alta), alertas do algoritmo e trilha YPP — alimentado pelo loop 24h. Propostas, nunca mudanças sozinhas.
        </p>
        <div style={{ display: "flex", gap: "0.75rem", margin: "1.25rem 0" }}>
          <button onClick={() => setMineOnly(false)} style={tab(!mineOnly)}>Todos</button>
          <button onClick={() => setMineOnly(true)} style={tab(mineOnly)}>Meus canais</button>
          <a href="/" style={{ ...tab(false), textDecoration: "none" }}>← site</a>
        </div>

        <h2>Alertas</h2>
        {data.alerts.length === 0 && <p style={{ opacity: 0.6 }}>Nenhum alerta na última rodada. O loop pesquisa todo domingo.</p>}
        <div className="feat">
          {data.alerts.map((a, i) => (
            <article key={i} style={card}>
              <span className="n">{ALERT_LABEL[a.type] ?? a.type}</span>
              <h3>{a.seed}</h3>
              <p>{a.detail}</p>
              {a.examples.length > 0 && <p style={{ opacity: 0.65, fontSize: "0.9em" }}>{a.examples.join(" · ")}</p>}
            </article>
          ))}
        </div>

        <h2 style={{ marginTop: "2.5rem" }}>Canais</h2>
        <div className="feat">
          {channels.map((c) => {
            const y = data.ypp[c.handle];
            return (
              <article key={c.handle} style={card}>
                <span className="n">{c.mine ? "meu" : "vigia"}</span>
                <h3>{c.name}</h3>
                <p style={{ opacity: 0.7 }}>{c.handle} · {c.nota}</p>
                {y ? (
                  <p>
                    YPP 2026: {y.eligible_2026 ? "✓" : "—"} · 2027: {y.eligible_2027 ? "✓" : `${y.hours_gap_2027}h faltando (~${y.daily_needed}h/dia)`}
                    <br />Manutenção: {y.maintenance_safe ? "✓" : "atenção"}
                  </p>
                ) : (
                  <p style={{ opacity: 0.6 }}>YPP: alimente <code>data/ypp_input.json</code> para a matemática aparecer aqui.</p>
                )}
              </article>
            );
          })}
        </div>

        <h2 style={{ marginTop: "2.5rem" }}>Loop 24h</h2>
        {data.loop_reports.map((r) => (
          <p key={r.date}>
            <strong>{r.date}</strong> — {r.status}
            {r.failed_steps.length > 0 && <span style={{ opacity: 0.7 }}> · falhou: {r.failed_steps.join(", ")}</span>}
          </p>
        ))}
      </div>
    </main>
  );
}

const card: React.CSSProperties = { border: "1px solid rgba(255,255,255,.12)", borderRadius: 12, padding: "1rem 1.1rem" };
const tab = (active: boolean): React.CSSProperties => ({
  border: "1px solid rgba(255,255,255,.2)", borderRadius: 999, padding: "0.4rem 1rem",
  background: active ? "#fff" : "transparent", color: active ? "#000" : "#fff", cursor: "pointer",
});
