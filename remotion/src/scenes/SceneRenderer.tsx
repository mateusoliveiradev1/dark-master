import type { FC, ReactNode } from "react";

import { AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig } from "remotion";

import { EndCard } from "../components/Brand";
import { AssetImage, Paper } from "../components/MediaLayer";
import { Body, Headline, Kicker, Metadata } from "../components/Typography";
import type { RenderPlan } from "../schema";

type Plan = RenderPlan;

const progress = (frame: number, durationInFrames: number): number =>
  interpolate(frame, [0, Math.min(18, Math.max(2, durationInFrames))], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

const Panel: FC<{ children: ReactNode; color?: string; style?: React.CSSProperties }> = ({
  children,
  color = "#17171B",
  style,
}) => (
  <div
    style={{ background: color, border: "1px solid rgba(255,255,255,0.12)", padding: 24, ...style }}
  >
    {children}
  </div>
);

const MotionLayer: FC<{ scene: Plan["scenes"][number]; children: ReactNode }> = ({
  scene,
  children,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = progress(frame, Math.round(scene.durationSeconds * fps));
  const scale =
    scene.motionVariant === "push-in"
      ? interpolate(enter, [0, 1], [1.04, 1.12])
      : scene.motionVariant === "pull-out"
        ? interpolate(enter, [0, 1], [1.12, 1.02])
        : 1;
  const x =
    scene.motionVariant === "track-left"
      ? interpolate(enter, [0, 1], [40, 0])
      : scene.motionVariant === "track-right"
        ? interpolate(enter, [0, 1], [-40, 0])
        : 0;
  return (
    <div
      style={{
        opacity: enter,
        transform: `translateX(${x}px) scale(${scale})`,
        transformOrigin: "center",
      }}
    >
      {children}
    </div>
  );
};

const Overlay: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <div
    style={{
      position: "absolute",
      inset: 0,
      display: "flex",
      flexDirection: "column",
      justifyContent: "flex-end",
      padding: 72,
      background: "linear-gradient(180deg, transparent 34%, rgba(0,0,0,0.82) 100%)",
    }}
  >
    <Kicker color={plan.theme.accent}>
      {scene.metadata.label ?? scene.purpose ?? "DOCUMENTARY"}
    </Kicker>
    <div style={{ maxWidth: 900, marginTop: 14 }}>
      <Headline style={{ color: plan.theme.text }}>{scene.headline}</Headline>
      {scene.body ? (
        <Body muted style={{ marginTop: 14 }}>
          {scene.body}
        </Body>
      ) : null}
    </div>
  </div>
);

const CinematicPhoto: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill>
    <AssetImage src={scene.asset} />
    <MotionLayer scene={scene}>
      <Overlay plan={plan} scene={scene} />
    </MotionLayer>
  </AbsoluteFill>
);

const EvidenceReveal: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill
    style={{ display: "grid", gridTemplateColumns: "1.1fr 0.9fr", gap: 24, padding: 54 }}
  >
    <Panel
      color={plan.theme.surface}
      style={{ position: "relative", overflow: "hidden", padding: 0 }}
    >
      <AssetImage src={scene.asset} />
    </Panel>
    <MotionLayer scene={scene}>
      <div
        style={{
          display: "flex",
          height: "100%",
          flexDirection: "column",
          justifyContent: "center",
          padding: 42,
        }}
      >
        <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "EVIDÊNCIA"}</Kicker>
        <Headline style={{ color: plan.theme.text, marginTop: 18 }}>{scene.headline}</Headline>
        <Body muted style={{ marginTop: 18 }}>
          {scene.body}
        </Body>
        <div style={{ marginTop: 30 }}>
          <Metadata
            label="Fonte"
            value={scene.metadata.source ?? "arquivo verificado"}
            accent={plan.theme.accent}
          />
        </div>
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const EvidenceTable: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => {
  const rows = scene.body.split("\n").filter(Boolean);
  return (
    <AbsoluteFill style={{ padding: 72, display: "flex", alignItems: "center" }}>
      <MotionLayer scene={scene}>
        <Paper
          color="#E7E2D8"
          accent={plan.theme.accent}
          style={{ width: "100%", maxWidth: 1120, color: "#18181B" }}
        >
          <div
            style={{ fontSize: 15, letterSpacing: 3, textTransform: "uppercase", opacity: 0.65 }}
          >
            {scene.metadata.label ?? "EVIDENCE LOG"}
          </div>
          <div style={{ fontSize: 42, fontWeight: 800, marginTop: 12, marginBottom: 22 }}>
            {scene.headline}
          </div>
          {rows.length ? (
            rows.map((row, index) => (
              <div
                key={row}
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  borderTop: "1px solid #18181B33",
                  padding: "14px 0",
                  fontSize: 20,
                }}
              >
                <span>{row}</span>
                <span style={{ opacity: 0.6 }}>0{index + 1}</span>
              </div>
            ))
          ) : (
            <div style={{ fontSize: 22 }}>{scene.body}</div>
          )}
        </Paper>
      </MotionLayer>
    </AbsoluteFill>
  );
};

const InvestigationBoard: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill style={{ padding: 58, background: "#16181C" }}>
    <MotionLayer scene={scene}>
      <div
        style={{
          position: "relative",
          height: "100%",
          border: `1px solid ${plan.theme.accent}55`,
          backgroundImage:
            "linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px)",
          backgroundSize: "60px 60px",
        }}
      >
        <div
          style={{
            position: "absolute",
            left: 70,
            top: 70,
            width: 350,
            height: 230,
            transform: "rotate(-5deg)",
            overflow: "hidden",
          }}
        >
          <AssetImage src={scene.asset} />
        </div>
        <div
          style={{
            position: "absolute",
            right: 86,
            top: 96,
            width: 420,
            padding: 22,
            background: "#E7E2D8",
            color: "#18181B",
            transform: "rotate(4deg)",
          }}
        >
          <div style={{ fontSize: 18, fontWeight: 800 }}>{scene.headline}</div>
          <div style={{ fontSize: 16, marginTop: 10 }}>{scene.body}</div>
        </div>
        <div
          style={{
            position: "absolute",
            left: "35%",
            bottom: 90,
            width: 320,
            borderTop: `3px solid ${plan.theme.accent}`,
            paddingTop: 14,
            color: plan.theme.text,
            fontSize: 22,
          }}
        >
          {scene.metadata.note ?? "Relacionar evidência → significado → hipótese"}
        </div>
        <svg
          viewBox="0 0 1920 1080"
          width="100%"
          height="100%"
          role="img"
          aria-label="Investigation connections"
          style={{ position: "absolute", inset: 0, pointerEvents: "none" }}
        >
          <title>Investigation connections</title>
          <path
            d="M420 250 C650 180 880 180 1210 300"
            fill="none"
            stroke={plan.theme.accent}
            strokeWidth="3"
            strokeDasharray="10 12"
          />
          <path
            d="M1180 520 C980 680 820 760 650 820"
            fill="none"
            stroke={plan.theme.text}
            strokeWidth="2"
            opacity="0.45"
          />
        </svg>
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const Timeline: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => {
  const events = scene.body.split("\n").filter(Boolean);
  return (
    <AbsoluteFill
      style={{ padding: 84, display: "flex", flexDirection: "column", justifyContent: "center" }}
    >
      <MotionLayer scene={scene}>
        <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "LINE OF TIME"}</Kicker>
        <Headline style={{ color: plan.theme.text, marginTop: 18, maxWidth: 940 }}>
          {scene.headline}
        </Headline>
        <div
          style={{
            position: "relative",
            marginTop: 70,
            height: 2,
            background: `${plan.theme.muted}77`,
          }}
        >
          {events.map((event, index) => (
            <div
              key={event}
              style={{
                position: "absolute",
                left: `${index * (100 / Math.max(1, events.length - 1))}%`,
                top: -9,
                width: 20,
                height: 20,
                borderRadius: 20,
                background: index === 0 ? plan.theme.accent : plan.theme.text,
              }}
            />
          ))}
          {events.map((event, index) => (
            <div
              key={`${event}-label`}
              style={{
                position: "absolute",
                left: `${index * (100 / Math.max(1, events.length - 1))}%`,
                top: 28,
                width: 250,
                color: plan.theme.muted,
                fontSize: 18,
                lineHeight: 1.2,
              }}
            >
              {event}
            </div>
          ))}
        </div>
      </MotionLayer>
    </AbsoluteFill>
  );
};

const Location: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill>
    <AssetImage src={scene.asset} objectPosition="center" filter="saturate(0.72) contrast(1.08)" />
    <div
      style={{
        position: "absolute",
        inset: 0,
        background: "linear-gradient(90deg, rgba(0,0,0,0.78), transparent 72%)",
      }}
    />
    <MotionLayer scene={scene}>
      <div style={{ position: "absolute", left: 72, top: 92, maxWidth: 660 }}>
        <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "LOCATION"}</Kicker>
        <Headline style={{ color: plan.theme.text, marginTop: 18 }}>{scene.headline}</Headline>
        <Body muted style={{ marginTop: 16 }}>
          {scene.body}
        </Body>
        <div style={{ marginTop: 30, color: plan.theme.text, fontSize: 16, letterSpacing: 2 }}>
          {scene.metadata.coordinates ?? "COORDINATES —"}
        </div>
      </div>
    </MotionLayer>
    <div
      style={{
        position: "absolute",
        right: 90,
        bottom: 90,
        width: 160,
        height: 160,
        border: `2px solid ${plan.theme.accent}`,
        borderRadius: 999,
        opacity: 0.8,
      }}
    />
  </AbsoluteFill>
);

const MapScene: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill style={{ padding: 72, background: "#10151A" }}>
    <MotionLayer scene={scene}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
        <div>
          <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "MAP"}</Kicker>
          <Headline style={{ color: plan.theme.text, marginTop: 16 }}>{scene.headline}</Headline>
        </div>
        <div style={{ color: plan.theme.muted, fontSize: 15, letterSpacing: 2 }}>NORTH ↑</div>
      </div>
      <div
        style={{
          position: "relative",
          flex: 1,
          marginTop: 28,
          border: "1px solid rgba(255,255,255,0.16)",
          overflow: "hidden",
        }}
      >
        <svg
          viewBox="0 0 1400 650"
          width="100%"
          height="100%"
          preserveAspectRatio="none"
          role="img"
          aria-label="Animated route"
        >
          <title>Animated route</title>
          <path
            d="M0 510 C210 430 260 230 500 260 C760 300 790 540 1020 450 C1210 370 1300 210 1400 170"
            fill="none"
            stroke="#26333D"
            strokeWidth="120"
            opacity="0.8"
          />
          <path
            d="M160 510 C330 390 420 320 610 350 C810 380 850 430 1050 420"
            fill="none"
            stroke={plan.theme.accent}
            strokeWidth="5"
            strokeDasharray="12 10"
          />
          <circle cx="160" cy="510" r="12" fill={plan.theme.accent} />
          <circle cx="1050" cy="420" r="12" fill={plan.theme.text} />
          <path
            d="M160 510 L1050 420"
            stroke={plan.theme.text}
            strokeWidth="2"
            opacity="0.45"
            strokeDasharray="6 8"
          />
        </svg>
        <div
          style={{
            position: "absolute",
            left: 36,
            bottom: 30,
            color: plan.theme.muted,
            fontSize: 18,
          }}
        >
          {scene.body}
        </div>
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const Document: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill
    style={{
      padding: 72,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      background: "#24201A",
    }}
  >
    <MotionLayer scene={scene}>
      <Paper
        color="#D8CBB2"
        accent={plan.theme.accent}
        style={{ width: 760, minHeight: 660, transform: "rotate(-2deg)" }}
      >
        <div style={{ fontSize: 14, letterSpacing: 3, textTransform: "uppercase", opacity: 0.6 }}>
          {scene.metadata.label ?? "ARCHIVE DOCUMENT"}
        </div>
        <div style={{ fontSize: 46, lineHeight: 1, fontWeight: 850, marginTop: 20 }}>
          {scene.headline}
        </div>
        <div style={{ height: 1, background: "#18181B55", margin: "28px 0" }} />
        <div style={{ fontSize: 23, lineHeight: 1.5, whiteSpace: "pre-line" }}>{scene.body}</div>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: 56,
            fontSize: 15,
            opacity: 0.6,
          }}
        >
          <span>{scene.metadata.date ?? "DATE UNKNOWN"}</span>
          <span>{scene.metadata.source ?? "SOURCE —"}</span>
        </div>
      </Paper>
    </MotionLayer>
  </AbsoluteFill>
);

const Portrait: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill
    style={{ display: "grid", gridTemplateColumns: "0.8fr 1.2fr", gap: 30, padding: 54 }}
  >
    <div style={{ position: "relative", overflow: "hidden" }}>
      <AssetImage src={scene.asset} objectPosition="center top" />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(90deg, transparent 55%, #0A0A0C)",
        }}
      />
    </div>
    <MotionLayer scene={scene}>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          paddingRight: 80,
        }}
      >
        <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "PORTRAIT"}</Kicker>
        <Headline style={{ color: plan.theme.text, marginTop: 18 }}>{scene.headline}</Headline>
        <Body muted style={{ marginTop: 18 }}>
          {scene.body}
        </Body>
        <div style={{ marginTop: 32, color: plan.theme.text, fontSize: 18, letterSpacing: 1 }}>
          {scene.metadata.person ?? "SUBJECT"}
        </div>
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const Comparison: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill style={{ padding: 54, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
    {[
      ["A", scene.asset],
      ["B", scene.secondaryAsset],
    ].map(([label, src], index) => (
      <div
        key={label}
        style={{
          position: "relative",
          overflow: "hidden",
          border: `1px solid ${index ? plan.theme.accent : plan.theme.text}55`,
        }}
      >
        <AssetImage src={src} />
        <div
          style={{
            position: "absolute",
            left: 24,
            top: 22,
            color: plan.theme.text,
            fontSize: 52,
            fontWeight: 900,
          }}
        >
          {label}
        </div>
      </div>
    ))}
    <div
      style={{
        position: "absolute",
        left: "50%",
        top: "50%",
        width: 72,
        height: 72,
        marginLeft: -36,
        marginTop: -36,
        display: "grid",
        placeItems: "center",
        borderRadius: 99,
        background: plan.theme.accent,
        color: plan.theme.text,
        fontSize: 30,
        fontWeight: 900,
      }}
    >
      VS
    </div>
    <div
      style={{
        position: "absolute",
        left: 72,
        right: 72,
        bottom: 38,
        textAlign: "center",
        color: plan.theme.text,
        fontSize: 26,
        fontWeight: 750,
      }}
    >
      {scene.headline}
    </div>
  </AbsoluteFill>
);

const Quote: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill
    style={{
      padding: 100,
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      background: "linear-gradient(135deg, #111216, #24201A)",
    }}
  >
    <MotionLayer scene={scene}>
      <div
        style={{
          fontSize: 112,
          lineHeight: 0.7,
          color: plan.theme.accent,
          fontFamily: "Georgia, serif",
        }}
      >
        “
      </div>
      <Headline style={{ color: plan.theme.text, fontSize: 70, maxWidth: 1220, marginTop: 24 }}>
        {scene.headline}
      </Headline>
      <Body muted style={{ marginTop: 26, fontSize: 25 }}>
        {scene.body}
      </Body>
      <div
        style={{
          marginTop: 34,
          color: plan.theme.accent,
          fontSize: 16,
          letterSpacing: 3,
          textTransform: "uppercase",
        }}
      >
        {scene.metadata.source ?? "SOURCE —"}
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const DataVisualization: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => {
  const values = scene.body
    .split("\n")
    .filter(Boolean)
    .map((item) => {
      const [label, raw] = item.split("|");
      return { label, value: Number(raw ?? 0) || 0 };
    });
  const max = Math.max(...values.map((item) => item.value), 1);
  return (
    <AbsoluteFill style={{ padding: 72 }}>
      <MotionLayer scene={scene}>
        <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "DATA"}</Kicker>
        <Headline style={{ color: plan.theme.text, marginTop: 16 }}>{scene.headline}</Headline>
        <div
          style={{
            display: "flex",
            alignItems: "flex-end",
            gap: 28,
            height: 500,
            marginTop: 70,
            borderBottom: "1px solid #FFFFFF33",
          }}
        >
          {values.map((item) => (
            <div
              key={item.label}
              style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "flex-end",
                height: "100%",
                width: 130,
                gap: 12,
              }}
            >
              <div
                style={{
                  height: `${(item.value / max) * 82}%`,
                  background: `linear-gradient(180deg, ${plan.theme.accent}, ${plan.theme.accent}55)`,
                  display: "flex",
                  alignItems: "flex-start",
                  justifyContent: "center",
                  paddingTop: 14,
                  color: plan.theme.text,
                  fontSize: 18,
                  fontWeight: 800,
                }}
              >
                {item.value}
              </div>
              <div style={{ color: plan.theme.muted, fontSize: 15, textAlign: "center" }}>
                {item.label}
              </div>
            </div>
          ))}
        </div>
      </MotionLayer>
    </AbsoluteFill>
  );
};

const Diagram: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => {
  const items = scene.body.split("\n").filter(Boolean);
  return (
    <AbsoluteFill style={{ padding: 72 }}>
      <MotionLayer scene={scene}>
        <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "STRUCTURE"}</Kicker>
        <Headline style={{ color: plan.theme.text, marginTop: 16 }}>{scene.headline}</Headline>
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginTop: 110,
            position: "relative",
          }}
        >
          {items.map((item, index) => (
            <div key={item} style={{ display: "flex", alignItems: "center", flex: 1 }}>
              <div
                style={{
                  width: 180,
                  height: 180,
                  borderRadius: 999,
                  display: "grid",
                  placeItems: "center",
                  padding: 20,
                  textAlign: "center",
                  background: index % 2 ? plan.theme.surface : plan.theme.accent,
                  color: plan.theme.text,
                  border: `1px solid ${plan.theme.text}55`,
                  fontSize: 19,
                  fontWeight: 750,
                }}
              >
                {item}
              </div>
              {index < items.length - 1 ? (
                <div style={{ height: 2, flex: 1, background: plan.theme.accent }} />
              ) : null}
            </div>
          ))}
        </div>
      </MotionLayer>
    </AbsoluteFill>
  );
};

const ChapterBreak: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill
    style={{ display: "grid", placeItems: "center", background: plan.theme.background }}
  >
    <MotionLayer scene={scene}>
      <div style={{ textAlign: "center" }}>
        <div style={{ color: plan.theme.accent, fontSize: 18, fontWeight: 800, letterSpacing: 5 }}>
          {scene.metadata.number ?? "CHAPTER"}
        </div>
        <Headline style={{ color: plan.theme.text, fontSize: 78, marginTop: 22, maxWidth: 1100 }}>
          {scene.headline}
        </Headline>
        <Body muted style={{ margin: "20px auto 0", textAlign: "center" }}>
          {scene.body}
        </Body>
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const Surveillance: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill style={{ padding: 58, background: "#070908" }}>
    <MotionLayer scene={scene}>
      <div
        style={{
          position: "relative",
          width: "100%",
          height: "100%",
          border: "1px solid #D6E5D655",
          overflow: "hidden",
        }}
      >
        <AssetImage
          src={scene.asset}
          objectPosition="center"
          filter="grayscale(0.6) contrast(1.25)"
        />
        <div
          style={{
            position: "absolute",
            inset: 0,
            backgroundImage:
              "repeating-linear-gradient(0deg, rgba(255,255,255,0.06) 0, rgba(255,255,255,0.06) 1px, transparent 1px, transparent 5px)",
          }}
        />
        <div
          style={{
            position: "absolute",
            top: 22,
            left: 26,
            color: "#D6E5D6",
            fontFamily: "monospace",
            fontSize: 18,
            letterSpacing: 2,
          }}
        >
          CAM 04 / {scene.metadata.timestamp ?? "00:00:00"}
        </div>
        <div
          style={{
            position: "absolute",
            right: 26,
            bottom: 22,
            color: "#D6E5D6",
            fontFamily: "monospace",
            fontSize: 16,
          }}
        >
          REC ●
        </div>
        <div
          style={{
            position: "absolute",
            left: 26,
            bottom: 22,
            color: plan.theme.accent,
            fontFamily: "monospace",
            fontSize: 18,
          }}
        >
          TRACKING SUBJECT
        </div>
      </div>
    </MotionLayer>
  </AbsoluteFill>
);

const Generic: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({ plan, scene }) => (
  <AbsoluteFill>
    <AssetImage src={scene.asset} />
    <MotionLayer scene={scene}>
      <Overlay plan={plan} scene={scene} />
    </MotionLayer>
  </AbsoluteFill>
);

export const SceneRenderer: FC<{ plan: Plan; scene: Plan["scenes"][number] }> = ({
  plan,
  scene,
}) => {
  switch (scene.type) {
    case "cinematic-photo":
      return <CinematicPhoto plan={plan} scene={scene} />;
    case "evidence-reveal":
      return <EvidenceReveal plan={plan} scene={scene} />;
    case "evidence-table":
      return <EvidenceTable plan={plan} scene={scene} />;
    case "investigation-board":
      return <InvestigationBoard plan={plan} scene={scene} />;
    case "timeline":
    case "timeline-detail":
      return <Timeline plan={plan} scene={scene} />;
    case "geographic-location":
      return <Location plan={plan} scene={scene} />;
    case "animated-map":
    case "evidence-map":
      return <MapScene plan={plan} scene={scene} />;
    case "document-report":
    case "newspaper-archive":
      return <Document plan={plan} scene={scene} />;
    case "portrait-investigation":
    case "object-detail":
      return <Portrait plan={plan} scene={scene} />;
    case "split-screen":
    case "compare-contrast":
      return <Comparison plan={plan} scene={scene} />;
    case "quote":
      return <Quote plan={plan} scene={scene} />;
    case "data-visualization":
      return <DataVisualization plan={plan} scene={scene} />;
    case "concept-diagram":
      return <Diagram plan={plan} scene={scene} />;
    case "chapter-break":
      return <ChapterBreak plan={plan} scene={scene} />;
    case "surveillance-footage":
    case "security-camera":
      return <Surveillance plan={plan} scene={scene} />;
    case "end-card-cta":
      return (
        <EndCard plan={plan} asset={scene.asset} headline={scene.headline} body={scene.body} />
      );
    default:
      return <Generic plan={plan} scene={scene} />;
  }
};
