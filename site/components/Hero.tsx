"use client";
import { motion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";
import { Terminal } from "./Terminal";
import { MagneticButton } from "./MagneticButton";

const line = {
  hidden: { y: "110%" },
  show: (i: number) => ({
    y: "0%",
    transition: { duration: 0.95, ease: [0.16, 0.84, 0.44, 1] as const, delay: 0.08 * i },
  }),
};

export function Hero() {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
  const y = useTransform(scrollYProgress, [0, 1], [0, 120]);
  const opacity = useTransform(scrollYProgress, [0, 0.8], [1, 0]);

  return (
    <motion.div ref={ref} style={{ y, opacity }} className="wrap hero">
      <div className="hero-grid">
        <div>
          <motion.span className="tag" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 }}>
            <i /> skill para canais dark / faceless
          </motion.span>

          <h1>
            <span className="line-mask">
              <motion.span style={{ display: "block" }} variants={line} custom={0} initial="hidden" animate="show">Da ideia</motion.span>
            </span>
            <span className="line-mask">
              <motion.span style={{ display: "block" }} variants={line} custom={1} initial="hidden" animate="show">
                ao <span className="redact">arquivo</span> que
              </motion.span>
            </span>
            <span className="line-mask">
              <motion.span style={{ display: "block" }} variants={line} custom={2} initial="hidden" animate="show">se paga.</motion.span>
            </span>
          </h1>

          <motion.p className="lead" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.6, duration: 0.7 }}>
            Um cérebro único que funde o algoritmo do YouTube, o guia de produção do MrBeast,
            os dados de 2026 e os seus canais. Planeja, empacota, roteiriza, produz — e aprende com o resultado.
          </motion.p>

          <motion.div className="cta" initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.75 }}>
            <MagneticButton href="https://github.com/mateusoliveiradev1/dark-master" primary>Ver no GitHub →</MagneticButton>
            <MagneticButton href="#fluxo">Como funciona</MagneticButton>
          </motion.div>
        </div>

        <motion.div initial={{ opacity: 0, y: 30, rotateX: 8 }} animate={{ opacity: 1, y: 0, rotateX: 0 }} transition={{ delay: 0.5, duration: 0.9, ease: [0.16, 0.84, 0.44, 1] }}>
          <Terminal />
        </motion.div>
      </div>
    </motion.div>
  );
}
