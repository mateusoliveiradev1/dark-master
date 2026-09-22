"use client";
import { useEffect, useRef } from "react";

export function Background() {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const c = ref.current;
    if (!c) return;
    const ctx = c.getContext("2d");
    if (!ctx) return;
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    const dpr = Math.min(devicePixelRatio || 1, 2);
    let w = 0, h = 0;
    type P = { x: number; y: number; r: number; vx: number; vy: number; a: number };
    let parts: P[] = [];
    let scan = 0;

    const size = () => {
      w = c.width = innerWidth * dpr;
      h = c.height = innerHeight * dpr;
      c.style.width = innerWidth + "px";
      c.style.height = innerHeight + "px";
      const n = Math.min(110, Math.round(innerWidth / 15));
      parts = Array.from({ length: n }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        r: (Math.random() * 1.5 + 0.3) * dpr,
        vx: (Math.random() - 0.5) * 0.14 * dpr,
        vy: (-Math.random() * 0.18 - 0.02) * dpr,
        a: Math.random() * 0.5 + 0.1,
      }));
    };

    let mx = 0.5, my = 0.5;
    const move = (e: MouseEvent) => { mx = e.clientX / innerWidth; my = e.clientY / innerHeight; };
    addEventListener("mousemove", move, { passive: true });

    let raf = 0;
    const frame = () => {
      ctx.clearRect(0, 0, w, h);
      const ox = (mx - 0.5) * 34 * dpr;
      const oy = (my - 0.5) * 34 * dpr;
      for (const p of parts) {
        p.x += p.vx; p.y += p.vy;
        if (p.y < -12) { p.y = h + 12; p.x = Math.random() * w; }
        if (p.x < -12) p.x = w + 12;
        if (p.x > w + 12) p.x = -12;
        ctx.beginPath();
        ctx.arc(p.x + ox, p.y + oy, p.r, 0, 6.283);
        ctx.fillStyle = `rgba(226,59,59,${p.a * 0.5})`;
        ctx.fill();
      }
      scan += 0.5 * dpr;
      if (scan > h + 200) scan = -200;
      const g = ctx.createLinearGradient(0, scan - 60, 0, scan + 60);
      g.addColorStop(0, "rgba(226,59,59,0)");
      g.addColorStop(0.5, "rgba(226,59,59,0.045)");
      g.addColorStop(1, "rgba(226,59,59,0)");
      ctx.fillStyle = g;
      ctx.fillRect(0, scan - 60, w, 120);
      raf = requestAnimationFrame(frame);
    };

    size();
    addEventListener("resize", size);
    if (!reduce) frame();
    return () => {
      cancelAnimationFrame(raf);
      removeEventListener("resize", size);
      removeEventListener("mousemove", move);
    };
  }, []);

  return (
    <div className="fx" aria-hidden="true">
      <canvas ref={ref} />
      <div className="grid" />
      <div className="vignette" />
      <div className="grain" />
    </div>
  );
}
