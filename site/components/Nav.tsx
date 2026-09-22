"use client";
import { motion, useScroll, useSpring } from "framer-motion";
import { Logo } from "./Logo";
import { Toggles } from "./Toggles";
import { useI18n } from "@/lib/store";

export function Nav() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 140, damping: 26, mass: 0.4 });
  const { t } = useI18n();

  return (
    <header className="top">
      <div className="wrap top-in">
        <a className="brand" href="/" aria-label="Início / Home"><Logo /> dark-master</a>
        <div className="nav-right">
          <nav>
            <a href="#capacidades">{t.nav.capacidades}</a>
            <a href="#casos">{t.nav.casos}</a>
            <a href="#video">{t.nav.video}</a>
            <a href="#fluxo">{t.nav.fluxo}</a>
            <a href="#dados">{t.nav.dados}</a>
            <a href="#seguranca">{t.nav.seguranca}</a>
            <a href="/privacy">{t.nav.privacidade}</a>
          </nav>
          <Toggles />
        </div>
      </div>
      <motion.div className="progress" style={{ scaleX, width: "100%" }} />
    </header>
  );
}
