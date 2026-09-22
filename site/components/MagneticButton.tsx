"use client";
import { useRef } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";
import type { ReactNode } from "react";

export function MagneticButton({
  children,
  href,
  primary = false,
}: {
  children: ReactNode;
  href: string;
  primary?: boolean;
}) {
  const ref = useRef<HTMLAnchorElement>(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  const sx = useSpring(x, { stiffness: 260, damping: 18 });
  const sy = useSpring(y, { stiffness: 260, damping: 18 });

  const onMove = (e: React.MouseEvent) => {
    const r = ref.current?.getBoundingClientRect();
    if (!r) return;
    x.set((e.clientX - (r.left + r.width / 2)) * 0.28);
    y.set((e.clientY - (r.top + r.height / 2)) * 0.4);
  };
  const reset = () => { x.set(0); y.set(0); };

  const external = href.startsWith("http");
  return (
    <motion.a
      ref={ref}
      href={href}
      className={`btn${primary ? " primary" : ""}`}
      onMouseMove={onMove}
      onMouseLeave={reset}
      style={{ x: sx, y: sy }}
      target={external ? "_blank" : undefined}
      rel={external ? "noopener" : undefined}
    >
      <span />
      {children}
    </motion.a>
  );
}
