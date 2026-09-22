"use client";
import { motion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";
import { Terminal } from "./Terminal";
import { MagneticButton } from "./MagneticButton";
import { useI18n } from "@/lib/store";

const EASE = [0.16, 0.84, 0.44, 1] as const;

function Word({ children, i, delay = 0 }: { children: React.ReactNode; i: number; delay?: number }) {
  return (
    <span className="word">
      <motion.span
        initial={{ y: "115%", rotate: 4 }}
        animate={{ y: "0%", rotate: 0 }}
        transition={{ duration: 0.95, ease: EASE, delay: delay + i * 0.07 }}
      >
        {children}
      </motion.span>
    </span>
  );
}

function Redact({ text, delay }: { text: string; delay: number }) {
  return (
    <span className="redact-wrap">
      <motion.span
        className="redact-bar"
        initial={{ scaleX: 1 }}
        animate={{ scaleX: [1, 1, 0, 0, 1] }}
        transition={{ duration: 6, times: [0, 0.42, 0.5, 0.78, 0.86], repeat: Infinity, ease: EASE, delay }}
      />
      <span className="redact-txt">{text}</span>
    </span>
  );
}

export function Hero() {
  const { t } = useI18n();
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
  const y = useTransform(scrollYProgress, [0, 1], [0, 140]);
  const opacity = useTransform(scrollYProgress, [0, 0.85], [1, 0]);
  const glowY = useTransform(scrollYProgress, [0, 1], [0, 220]);
  const fl1 = useTransform(scrollYProgress, [0, 1], [0, -90]);
  const fl2 = useTransform(scrollYProgress, [0, 1], [0, 70]);
  const fl3 = useTransform(scrollYProgress, [0, 1], [0, -50]);
  const termY = useTransform(scrollYProgress, [0, 1], [0, 60]);

  return (
    <motion.div ref={ref} style={{ y, opacity }} className="wrap hero">
      <motion.div className="hero-glow" style={{ y: glowY }} aria-hidden />

      {[fl1, fl2, fl3].map((yv, i) => (
        <motion.span key={i} className={`float-label fl-${i + 1}`} style={{ y: yv }} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 1 + i * 0.2 }}>
          {t.hero.floats[i]}
        </motion.span>
      ))}

      <div className="hero-grid">
        <div>
          <motion.span className="tag" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.15 }}>
            <i /> {t.hero.tag}
          </motion.span>

          <h1>
            <span className="line-mask"><Word i={0}>{t.hero.l1}</Word></span>
            <span className="line-mask" style={{ paddingTop: ".04em" }}>
              <Word i={2}>{t.hero.l2a}</Word>&nbsp;<Word i={3} delay={0.02}><Redact text={t.hero.l2redact} delay={1.1} /></Word>&nbsp;<Word i={4}>{t.hero.l2b}</Word>
            </span>
            <span className="line-mask"><Word i={5}>{t.hero.l3}</Word></span>
          </h1>

          <motion.p className="lead" initial={{ opacity: 0, y: 14 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.7, duration: 0.7, ease: EASE }}>
            {t.hero.lead}
          </motion.p>

          <motion.div className="cta" initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.85, ease: EASE }}>
            <MagneticButton href="https://github.com/mateusoliveiradev1/dark-master" primary>{t.hero.github}</MagneticButton>
            <MagneticButton href="#fluxo">{t.hero.how}</MagneticButton>
          </motion.div>

          <motion.div className="scroll-cue" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 1.5 }}>
            <span className="rail" /> {t.hero.scroll}
          </motion.div>
        </div>

        <motion.div style={{ y: termY }} initial={{ opacity: 0, y: 40, rotateX: 10 }} animate={{ opacity: 1, y: 0, rotateX: 0 }} transition={{ delay: 0.55, duration: 1, ease: EASE }}>
          <Terminal />
        </motion.div>
      </div>
    </motion.div>
  );
}
