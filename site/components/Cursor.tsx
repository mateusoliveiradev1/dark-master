"use client";
import { useEffect, useState } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";

export function Cursor() {
  const [enabled, setEnabled] = useState(false);
  const x = useMotionValue(-100);
  const y = useMotionValue(-100);
  const rx = useSpring(x, { stiffness: 320, damping: 28, mass: 0.6 });
  const ry = useSpring(y, { stiffness: 320, damping: 28, mass: 0.6 });

  useEffect(() => {
    if (matchMedia("(hover:none)").matches || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    setEnabled(true);
    document.body.style.cursor = "none";
    const move = (e: MouseEvent) => { x.set(e.clientX); y.set(e.clientY); };
    addEventListener("mousemove", move, { passive: true });
    return () => { removeEventListener("mousemove", move); document.body.style.cursor = ""; };
  }, [x, y]);

  if (!enabled) return null;
  return (
    <>
      <motion.div className="cursor-ring" style={{ x: rx, y: ry, translateX: "-50%", translateY: "-50%" }} />
      <motion.div className="cursor-dot" style={{ x, y, translateX: "-50%", translateY: "-50%" }} />
    </>
  );
}
