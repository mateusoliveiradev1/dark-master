"use client";
import { motion, useScroll, useSpring } from "framer-motion";
import { Logo } from "./Logo";

export function Nav() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 140, damping: 26, mass: 0.4 });

  return (
    <header className="top">
      <div className="wrap top-in">
        <a className="brand" href="#top"><Logo /> dark-master</a>
        <nav>
          <a href="#capacidades">Capacidades</a>
          <a href="#fluxo">Fluxo</a>
          <a href="#dados">Dados</a>
          <a href="#seguranca">Segurança</a>
          <a href="/privacy">Privacidade</a>
        </nav>
      </div>
      <motion.div className="progress" style={{ scaleX, width: "100%" }} />
    </header>
  );
}
