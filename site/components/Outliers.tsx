"use client";
import { motion } from "framer-motion";
import { useI18n } from "@/lib/store";
import { Reveal } from "./Reveal";
import { Counter } from "./Counter";

export function Outliers() {
  const { t } = useI18n();
  const o = t.outliers;
  const max = Math.max(...o.items.map((i) => i.avp));

  return (
    <section id="casos">
      <div className="wrap">
        <Reveal>
          <div className="sec-head">
            <div>
              <p className="eyebrow">{o.eyebrow}</p>
              <h2>{o.title}</h2>
            </div>
            <p>{o.sub}</p>
          </div>
        </Reveal>

        <div className="outliers">
          {o.items.map((it, i) => (
            <Reveal key={it.name} delay={i * 0.08}>
              <div className={`ocard${i === 0 ? " best" : ""}`}>
                <div className="ocard-top">
                  <span className="fmt">{it.fmt}</span>
                  <span className="otag">{it.tag}</span>
                </div>
                <h3>{it.name}</h3>
                <div className="ometric">
                  <b><Counter to={it.views} /></b>
                  <small>{o.labels.views}</small>
                </div>
                <div className="bar-wrap" aria-hidden>
                  <motion.div
                    className="bar"
                    initial={{ width: 0 }}
                    whileInView={{ width: `${(it.avp / max) * 100}%` }}
                    viewport={{ once: true, margin: "-15%" }}
                    transition={{ duration: 1.1, ease: [0.16, 0.84, 0.44, 1], delay: 0.15 + i * 0.08 }}
                  />
                  <span className="bar-label">{it.avp}% {o.labels.avp}</span>
                </div>
                <div className="osubs"><b>{it.subs}</b> <small>{o.labels.subs}</small></div>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.1}>
          <p className="onote">{o.note} <span className="muted">{o.medianNote}</span></p>
        </Reveal>
      </div>
    </section>
  );
}
