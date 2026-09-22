const ITEMS = [
  "algoritmo", "hooks Y1–Y11", "thumbnails", "retenção", "shorts",
  "outliers", "monetização", "4.000 horas", "auto-dublagem",
];

export function Marquee() {
  const row = [...ITEMS, ...ITEMS];
  return (
    <div className="marquee" aria-hidden="true">
      <div className="track" style={{ animation: "mv 34s linear infinite" }}>
        {row.map((t, i) => (
          <span key={i} style={{ display: "inline-flex", gap: 46, alignItems: "center" }}>
            {t} <b>·</b>
          </span>
        ))}
      </div>
      <style>{`@keyframes mv{to{transform:translateX(calc(-50% - 23px))}}
      .marquee:hover .track{animation-play-state:paused}`}</style>
    </div>
  );
}
