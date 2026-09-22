/* dark-master — interações. Zero dependências. */
(function () {
  "use strict";
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Canvas: poeira/arquivo (partículas + linhas) ---------- */
  (function canvas() {
    const c = document.getElementById("fx");
    if (!c) return;
    const ctx = c.getContext("2d");
    let w, h, parts = [], dpr = Math.min(devicePixelRatio || 1, 2);
    function size() {
      w = c.width = innerWidth * dpr;
      h = c.height = innerHeight * dpr;
      c.style.width = innerWidth + "px";
      c.style.height = innerHeight + "px";
      const n = Math.min(90, Math.round(innerWidth / 16));
      parts = Array.from({ length: n }, () => ({
        x: Math.random() * w, y: Math.random() * h,
        r: (Math.random() * 1.4 + 0.3) * dpr,
        vx: (Math.random() - 0.5) * 0.12 * dpr,
        vy: (-Math.random() * 0.18 - 0.03) * dpr,
        a: Math.random() * 0.5 + 0.12,
      }));
    }
    let mx = 0.5, my = 0.5;
    addEventListener("mousemove", (e) => { mx = e.clientX / innerWidth; my = e.clientY / innerHeight; }, { passive: true });
    function frame() {
      ctx.clearRect(0, 0, w, h);
      const ox = (mx - 0.5) * 30 * dpr, oy = (my - 0.5) * 30 * dpr;
      for (const p of parts) {
        p.x += p.vx; p.y += p.vy;
        if (p.y < -10) { p.y = h + 10; p.x = Math.random() * w; }
        if (p.x < -10) p.x = w + 10; if (p.x > w + 10) p.x = -10;
        ctx.beginPath();
        ctx.arc(p.x + ox, p.y + oy, p.r, 0, 6.283);
        ctx.fillStyle = "rgba(226,59,59," + p.a * 0.5 + ")";
        ctx.fill();
      }
      requestAnimationFrame(frame);
    }
    size(); addEventListener("resize", size);
    if (!reduce) frame(); else { ctx.clearRect(0, 0, w, h); }
  })();

  /* ---------- Cursor custom ---------- */
  (function cursor() {
    if (reduce || matchMedia("(hover:none)").matches) return;
    const ring = document.querySelector(".cursor"), dot = document.querySelector(".cursor-dot");
    if (!ring || !dot) return;
    let x = innerWidth / 2, y = innerHeight / 2, rx = x, ry = y;
    document.body.classList.add("no-cursor");
    addEventListener("mousemove", (e) => { x = e.clientX; y = e.clientY; dot.style.transform = `translate(${x}px,${y}px) translate(-50%,-50%)`; }, { passive: true });
    (function loop() { rx += (x - rx) * 0.18; ry += (y - ry) * 0.18; ring.style.transform = `translate(${rx}px,${ry}px) translate(-50%,-50%)`; requestAnimationFrame(loop); })();
    document.querySelectorAll("a,button,.btn,.feat article").forEach((el) => {
      el.addEventListener("mouseenter", () => ring.classList.add("grow"));
      el.addEventListener("mouseleave", () => ring.classList.remove("grow"));
    });
  })();

  /* ---------- Scroll reveal ---------- */
  (function reveal() {
    const els = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window) || reduce) { els.forEach((e) => e.classList.add("in")); return; }
    const io = new IntersectionObserver((ents) => {
      ents.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
    els.forEach((e) => io.observe(e));
  })();

  /* ---------- Contadores ---------- */
  (function counters() {
    const nums = document.querySelectorAll("[data-count]");
    if (!nums.length) return;
    const run = (el) => {
      const to = parseFloat(el.dataset.count), dur = 1100, t0 = performance.now();
      (function step(t) {
        const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
        el.textContent = Math.round(to * e);
        if (k < 1) requestAnimationFrame(step);
      })(t0);
    };
    if (!("IntersectionObserver" in window) || reduce) { nums.forEach((e) => e.textContent = e.dataset.count); return; }
    const io = new IntersectionObserver((ents) => ents.forEach((e) => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } }), { threshold: 0.6 });
    nums.forEach((e) => io.observe(e));
  })();

  /* ---------- Barra de progresso de scroll ---------- */
  (function bar() {
    const el = document.querySelector(".scrollbar");
    if (!el) return;
    const upd = () => { const s = scrollY / (document.body.scrollHeight - innerHeight || 1); el.style.width = (s * 100).toFixed(2) + "%"; };
    addEventListener("scroll", upd, { passive: true }); upd();
  })();

  /* ---------- Terminal: digitação ---------- */
  (function term() {
    const el = document.getElementById("term");
    if (!el) return;
    const raw = el.dataset.script || "";
    if (reduce) { el.textContent = raw; return; }
    let i = 0;
    const out = [];
    (function type() {
      if (i >= raw.length) return;
      const ch = raw[i++];
      out.push(ch);
      el.textContent = out.join("");
      setTimeout(type, ch === "\n" ? 90 : 9 + Math.random() * 16);
    })();
  })();

  /* ---------- Tilt 3D nos cards ---------- */
  (function tilt() {
    if (reduce || matchMedia("(hover:none)").matches) return;
    document.querySelectorAll("[data-tilt]").forEach((card) => {
      card.addEventListener("mousemove", (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - 0.5, py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = `perspective(700px) rotateY(${px * 5}deg) rotateX(${-py * 5}deg)`;
      });
      card.addEventListener("mouseleave", () => { card.style.transform = ""; });
    });
  })();
})();
