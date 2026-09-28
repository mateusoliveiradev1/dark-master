"use client";
import Link from "next/link";
import { use, useEffect, useMemo, useState } from "react";
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

function words(s: string): Set<string> {
  return new Set((s.toLowerCase().match(/[a-z]{4,}/g) ?? []).filter((w) => !["documentary", "documentaries", "com"].includes(w)));
}

function relatedAlerts(channel: Channel, alerts: Alert[]) {
  const ctx = words(`${channel.name} ${channel.nota}`);
  return alerts
    .map((a) => ({ a, score: [...words(a.seed)].filter((w) => ctx.has(w)).length }))
    .filter((x) => x.score > 0)
    .sort((x, y) => y.score - x.score)
    .map((x) => x.a);
}

export default function ChannelPage({ params }: { params: Promise<{ handle: string }> }) {
  const { handle } = use(params);
  const { t, lang } = useI18n();
  const d = t.dash;
  const [data, setData] = useState<Dashboard>(EMPTY);
  useEffect(() => {
    fetch("/dashboard.json", { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : EMPTY))
      .then(setData)
      .catch(() => setData(EMPTY));
  }, []);
  const channel = useMemo(() => {
    const h = decodeURIComponent(handle).toLowerCase();
    return data.channels.find((c) => c.handle.toLowerCase() === h || c.handle.toLowerCase() === `@${h}`) ?? null;
  }, [data, handle]);
  const alerts = useMemo(() => (channel ? relatedAlerts(channel, data.alerts) : []), [channel, data]);

  return (
    <>
      <Nav />
      <main id="top">
        <div className="wrap" style={{ paddingTop: 48 }}>
          <p><Link href="/dashboard" style={{ color: "var(--red-bright)" }}>← {d.channels}</Link></p>
          {!channel ? (
            <p className="muted" style={{ marginTop: 24 }}>{d.awaiting}</p>
          ) : (
            <>
              <Reveal>
                <p className="tag"><i />{channel.handle} · {channel.mine ? d.mine : "vigia"}</p>
                <h1 style={{ fontSize: "clamp(40px,8vw,96px)" }}>{channel.name}</h1>
                <p className="lead">{channel.nota}</p>
              </Reveal>
              {(() => {
                const det = data.details?.[channel.handle];
                const y = data.ypp[channel.handle];
                if (!det || det.status !== "ok") return <p className="muted">{d.awaiting}</p>;
                const max = Math.max(1, ...(det.series ?? []).map((p) => p.views));
                return (
                  <div className="stats">
                    <div><b>{det.views_30d?.toLocaleString("pt-BR")}</b><small>{d.views30d}</small></div>
                    <div><b>{det.engaged_rate}%</b><small>{d.engaged}</small></div>
                    <div><b>{det.top?.[0] ? `${Math.round(((det.top[0].views ?? 0) / Math.max(1, det.views_30d ?? 1)) * 100)}%` : "—"}</b><small>{d.bestOutlier}</small></div>
                    <div><b style={{ fontSize: "clamp(20px,3vw,30px)" }}>{y ? (y.eligible_2027 ? d.ok : `${y.hours_gap_2027}h`) : "—"}</b><small>{d.ypp2027}</small></div>
                  </div>
                );
              })()}
              {(() => {
                const det = data.details?.[channel.handle];
                if (!det?.top?.length) return null;
                return (
                  <>
                    <h2 style={{ marginTop: 48 }}>Top vídeos</h2>
                    <ul className="list">
                      {det.top.map((v, i) => (
                        <li key={i}><code>{Number(v.views).toLocaleString("pt-BR")} views</code><span>{v.title} <span className="muted">· {v.format}</span></span></li>
                      ))}
                    </ul>
                  </>
                );
              })()}
              <h2 style={{ marginTop: 48 }}>{d.alerts} {lang === "pt" ? "do nicho" : "for this niche"} ({alerts.length})</h2>
              {alerts.length === 0 && <p className="muted">{d.noAlerts}</p>}
              <div className="outliers">
                {alerts.map((a, i) => {
                  const g = lang === "pt" ? glossSeed(a.seed) : null;
                  return (
                    <article key={i} className="ocard">
                      <div className="ocard-top"><span className="fmt">{a.type}</span><span className="otag">{lang === "pt" ? ALERT_PT[a.type]?.titulo ?? a.type : a.type}</span></div>
                      <h3>{a.seed}</h3>
                      <p className="muted">{a.detail}</p>
                      {g && <p><em>{g.o_que}.</em> {g.porque}.</p>}
                    </article>
                  );
                })}
              </div>
            </>
          )}
        </div>
      </main>
    </>
  );
}
