"use client";
import { useEffect, useRef, useState } from "react";

type Tok = { t: string; c?: "k" | "g" | "m" };
const SCRIPT: Tok[][] = [
  [{ t: "$ ", c: "m" }, { t: "python scripts/yt_scan_outliers.py --watch" }],
  [{ t: "" }],
  [{ t: "ALERTA  ", c: "k" }, { t: "Cold File Diaries   mediana 26 views" }],
  [{ t: "  48.6x   1240   " , c: "g" }, { t: "Yuba County Five" }],
  [{ t: "  46.7x   1190   ", c: "g" }, { t: "D.B. Cooper — Never Found" }],
  [{ t: "  46.3x   1180   ", c: "g" }, { t: "Springfield Three" }],
  [{ t: "" }],
  [{ t: "corrente:  ", c: "m" }, { t: "video23 -> And tomorrow — Dorothy Arnold" }],
  [{ t: "  ... 3 outliers gravados em Neon Postgres", c: "m" }],
];

export function Terminal() {
  const total = SCRIPT.reduce((n, l) => n + l.reduce((m, k) => m + k.t.length, 0), 0);
  const [n, setN] = useState(0);
  const reduce = useRef(false);

  useEffect(() => {
    reduce.current = matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce.current) { setN(total); return; }
    let id: number;
    const tick = () => {
      setN((v) => {
        if (v >= total) return v;
        id = window.setTimeout(tick, 8 + Math.random() * 16);
        return v + 1;
      });
    };
    id = window.setTimeout(tick, 700);
    return () => clearTimeout(id);
  }, [total]);

  // render partial
  let budget = n;
  const out: React.ReactNode[] = [];
  SCRIPT.forEach((line, i) => {
    const nodes: React.ReactNode[] = [];
    line.forEach((tok, j) => {
      if (budget <= 0) return;
      const take = Math.min(tok.t.length, budget);
      budget -= take;
      const text = tok.t.slice(0, take);
      nodes.push(tok.c ? <span key={j} className={tok.c}>{text}</span> : <span key={j}>{text}</span>);
    });
    out.push(<div key={i}>{nodes.length ? nodes : "\u00A0"}</div>);
  });

  return (
    <div className="terminal" aria-hidden="true">
      <div className="bar"><i /><i /><i /><span>~/dark-master</span></div>
      <pre>
        {out}
        {n < total && <span className="caret" />}
      </pre>
    </div>
  );
}
