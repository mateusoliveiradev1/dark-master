"use client";
import Link from "next/link";
import { use, useEffect, useMemo, useState } from "react";
import { Nav } from "@/components/Nav";
import { Reveal } from "@/components/Reveal";
import { useI18n } from "@/lib/store";
import { ALERT_PT, glossSeed } from "@/lib/painel";

type Alert = { type: string; seed: string; detail: string; examples: string[];
  video_id?: string; channel?: string; niche?: string; ratio?: number };
type SeedLang = { date: string; depth: number; suggestions: string[]; trends_direction: string; rising: string[] };
type Seed = { seed: string; langs: Record<string, SeedLang> };
type Dashboard = { generated: string | null; alerts: Alert[]; seeds?: Record<string, Seed> };

const EMPTY: Dashboard = { generated: null, alerts: [], seeds: {} };

export default function AlertPage({ params }: { params: Promise<{ seed: string }> }) {
  const { seed: raw } = use(params);
  const { t, lang } = useI18n();
  const d = t.dash;
  const [data, setData] = useState<Dashboard>(EMPTY);
  useEffect(() => {
    fetch("/dashboard.json", { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : EMPTY))
      .then(setData)
      .catch(() => setData(EMPTY));
  }, []);
  const seed = decodeURIComponent(raw);
  const found = useMemo(() => {
    const bySeed = (a: Alert) => a.seed.toLowerCase() === seed.toLowerCase();
    return data.alerts.find(bySeed) ?? data.alerts.find((a) => seed.toLowerCase().includes(a.seed.toLowerCase())) ?? null;
  }, [data, seed]);
  const snap = useMemo(() => {
    if (!found) return null;
    const key = Object.keys(data.seeds ?? {}).find((k) => k.toLowerCase() === found.seed.toLowerCase());
    return (key && data.seeds?.[key]) ?? null;
  }, [data, found]);
  const g = lang === "pt" && found ? glossSeed(found.seed) : null;
  const label = found ? (lang === "pt" ? ALERT_PT[found.type]?.titulo ?? found.type : found.type) : seed;
  const queries = useMemo(() => {
    if (!snap) return found?.examples ?? [];
    const out = [...(snap.langs.en?.rising ?? []), ...(snap.langs.pt?.rising ?? []), ...(found?.examples ?? [])];
    return [...new Set(out)].slice(0, 10);
  }, [snap, found]);
  const perguntas = useMemo(() => {
    if (!snap) return [];
    const out = [...(snap.langs.en?.suggestions ?? []), ...(snap.langs.pt?.suggestions ?? [])];
    return [...new Set(out)].slice(0, 20);
  }, [snap]);

  return (
    <>
      <Nav />
      <main id="top">
        <div className="wrap" style={{ paddingTop: 48, paddingBottom: 90 }}>
          <p><Link href="/dashboard" style={{ color: "var(--red-bright)" }}>← {d.alerts}</Link></p>
          {!found ? (
            <p className="muted" style={{ marginTop: 24 }}>{d.noAlerts}</p>
          ) : (
            <>
              <Reveal>
                <p className="tag"><i />{found.type} · {d.loop} {data.generated ?? ""}</p>
                <h1 style={{ fontSize: "clamp(38px,7vw,88px)" }}>{found.seed}</h1>
                <p className="lead">{found.detail}</p>
                {g && <p><em>{g.o_que}.</em> {g.porque}.</p>}
                {lang === "pt" && ALERT_PT[found.type] && <p className="muted">{ALERT_PT[found.type].acao}</p>}
              </Reveal>
              {found.video_id && (
                <div className="stats">
                  <div><b>{found.ratio?.toFixed(1)}x</b><small>{lang === "pt" ? "múltiplo da mediana" : "median multiple"}</small></div>
                  <div><b style={{ fontSize: "clamp(20px,3vw,30px)" }}>{found.channel ?? "—"}</b><small>{lang === "pt" ? "canal" : "channel"}</small></div>
                  <div><b style={{ fontSize: "clamp(20px,3vw,30px)" }}>{found.niche ?? "—"}</b><small>nicho</small></div>
                </div>
              )}
              {snap && (
                <div className="stats">
                  {Object.entries(snap.langs).map(([l, s]) => (
                    <div key={l}><b>{s.depth}</b><small>{lang === "pt" ? `perguntas (${l})` : `questions (${l})`} · {s.trends_direction} · {s.date}</small></div>
                  ))}
                </div>
              )}
              {queries.length > 0 && (
                <>
                  <h2 style={{ marginTop: 48 }}>{lang === "pt" ? "Queries em alta" : "Rising queries"}</h2>
                  <ul className="list">
                    {queries.map((q) => (<li key={q}><code>{lang === "pt" ? "usar no título" : "use in title"}</code><span>{q}</span></li>))}
                  </ul>
                </>
              )}
              {perguntas.length > 0 && (
                <>
                  <h2 style={{ marginTop: 48 }}>{lang === "pt" ? "Perguntas reais (cada uma = um título)" : "Real questions (each = a title)"}</h2>
                  <ul className="list">
                    {perguntas.map((q) => (<li key={q}><code>autocomplete</code><span>{q}</span></li>))}
                  </ul>
                </>
              )}
              {found.video_id && (
                <p style={{ marginTop: 32 }}>
                  <a className="btn primary" href={`https://www.youtube.com/watch?v=${found.video_id}`} target="_blank" rel="noreferrer">
                    <span />{lang === "pt" ? "Ver vídeo original →" : "Watch original →"}
                  </a>
                </p>
              )}
              <h2 style={{ marginTop: 48 }}>{lang === "pt" ? "Próximos passos" : "Next steps"}</h2>
              <ul className="list">
                <li><code>1</code><span>{lang === "pt" ? "Piloto em 2 semanas com a query exata no título." : "Pilot in 2 weeks with the exact query in the title."}</span></li>
                <li><code>2</code><span>{lang === "pt" ? "Packaging com a query + thumb sem repetir palavras." : "Packaging with the query + thumb with no repeated words."}</span></li>
                <li><code>3</code><span>{lang === "pt" ? "Revalidar o nicho em 14 dias antes de escalar." : "Revalidate the niche in 14 days before scaling."}</span></li>
              </ul>
              <p className="muted" style={{ marginTop: 16 }}>
                {label} · {lang === "pt" ? "sinal de demanda com evidência datada — nunca promessa de views." : "evidence-backed demand signal — never a views promise."}
              </p>
            </>
          )}
        </div>
      </main>
    </>
  );
}
