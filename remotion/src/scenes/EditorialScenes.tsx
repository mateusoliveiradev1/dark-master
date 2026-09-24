import type { FC } from "react";

import { AbsoluteFill } from "remotion";

import { SceneRuntime } from "../components/SceneRuntime";
import { Body, Headline, Kicker } from "../components/Typography";
import type { RenderPlan } from "../schema";
import { MetadataLine, Panel, RuntimeAsset, ScenePaper, TextOverlay } from "./ScenePrimitives";

export const CinematicPhoto: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const markerProgress = Math.min(1, Math.max(0, (runtime.stateProgress - 0.22) / 0.45));
      const markerLeft = `${runtime.focalPoint[0] * 100}%`;
      const markerTop = `${runtime.focalPoint[1] * 100}%`;
      return (
        <AbsoluteFill>
          <RuntimeAsset runtime={runtime} scene={scene} />
          <AbsoluteFill
            style={{
              background:
                "linear-gradient(90deg, rgba(4,5,7,0.08) 0%, transparent 52%, rgba(4,5,7,0.74) 100%), linear-gradient(0deg, rgba(4,5,7,0.86) 0%, transparent 52%)",
            }}
          />
          <div
            style={{
              position: "absolute",
              left: markerLeft,
              top: markerTop,
              width: `${Math.max(8, 22 - markerProgress * 4)}%`,
              aspectRatio: "1.45",
              transform: `translate(-50%, -50%) scale(${0.72 + markerProgress * 0.28})`,
              border: `${Math.max(2, runtime.layout.scale * 3)}px solid ${plan.theme.accent}`,
              boxShadow: `0 0 0 ${runtime.layout.scale * 2}px rgba(0,0,0,0.25)`,
              opacity: markerProgress * 0.92,
            }}
          >
            <div
              style={{
                position: "absolute",
                left: -runtime.layout.scale * 18,
                top: "50%",
                width: runtime.layout.scale * 18,
                height: Math.max(2, runtime.layout.scale * 3),
                background: plan.theme.accent,
              }}
            />
            <div
              style={{
                position: "absolute",
                right: runtime.layout.scale * 22,
                top: runtime.layout.scale * 18,
                padding: `${runtime.layout.scale * 6}px ${runtime.layout.scale * 10}px`,
                background: plan.theme.accent,
                color: plan.theme.text,
                fontSize: Math.max(9, runtime.layout.scale * 14),
                fontWeight: 800,
                letterSpacing: 1.5,
                textTransform: "uppercase",
              }}
            >
              EVIDÊNCIA
            </div>
          </div>
          <div
            style={{
              position: "absolute",
              left: runtime.layout.scale * 54,
              bottom: runtime.layout.scale * 46,
              padding: `${runtime.layout.scale * 10}px ${runtime.layout.scale * 14}px`,
              borderTop: `${Math.max(2, runtime.layout.scale * 2)}px solid ${plan.theme.accent}`,
              background: "rgba(8,8,10,0.76)",
              color: plan.theme.muted,
              fontSize: Math.max(10, runtime.layout.scale * 16),
              letterSpacing: 1.4,
              opacity: Math.min(1, markerProgress * 1.25),
            }}
          >
            {scene.metadata.source ?? "FONTE VERIFICADA"}
          </div>
          <TextOverlay plan={plan} scene={scene} runtime={runtime} />
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const EvidenceReveal: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const primary = runtime.primaryAsset ?? runtime.assets[0] ?? null;
      const supporting =
        runtime.supportingAsset ??
        runtime.assets.find((asset) => asset.assetId !== primary?.assetId) ??
        null;
      const lensProgress = Math.min(1, Math.max(0, (runtime.stateProgress - 0.18) / 0.5));
      return (
        <AbsoluteFill
          style={{
            display: "grid",
            gridTemplateColumns: runtime.format === "short" ? "1fr" : "1.1fr 0.9fr",
            gridTemplateRows: runtime.format === "short" ? "1.1fr 0.9fr" : "1fr",
            gap: runtime.layout.scale * 24,
            padding: runtime.layout.scale * 54,
          }}
        >
          <Panel
            color={plan.theme.surface}
            style={{ position: "relative", overflow: "hidden", padding: 0 }}
          >
            <RuntimeAsset runtime={runtime} scene={scene} asset={primary} />
            <div
              style={{
                position: "absolute",
                left: `${runtime.focalPoint[0] * 100}%`,
                top: `${runtime.focalPoint[1] * 100}%`,
                width: `${Math.max(12, 28 - lensProgress * 5)}%`,
                aspectRatio: "1.25",
                transform: `translate(-50%, -50%) scale(${0.7 + lensProgress * 0.3})`,
                border: `${Math.max(2, runtime.layout.scale * 3)}px solid ${plan.theme.accent}`,
                boxShadow: `0 0 0 ${runtime.layout.scale * 3}px rgba(0,0,0,0.28)`,
                opacity: lensProgress,
              }}
            />
            <div
              style={{
                position: "absolute",
                left: runtime.layout.scale * 28,
                top: runtime.layout.scale * 28,
                color: plan.theme.text,
                fontSize: Math.max(10, runtime.layout.scale * 16),
                letterSpacing: 2,
                opacity: Math.min(1, runtime.stateProgress * 1.5),
              }}
            >
              PLATE / {String(scene.promptId ?? "DOC").toUpperCase()}
            </div>
          </Panel>
          <div
            style={{
              display: "flex",
              height: "100%",
              flexDirection: "column",
              justifyContent: "center",
              padding: runtime.layout.scale * 42,
            }}
          >
            <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "EVIDÊNCIA"}</Kicker>
            <Headline
              style={{
                color: plan.theme.text,
                marginTop: runtime.layout.scale * 18,
                fontSize: Math.max(26, runtime.layout.scale * 58),
              }}
            >
              {scene.headline}
            </Headline>
            <Body muted style={{ marginTop: runtime.layout.scale * 18 }}>
              {scene.body}
            </Body>
            {supporting ? (
              <div
                style={{
                  position: "relative",
                  height: "26%",
                  minHeight: runtime.layout.scale * 130,
                  marginTop: runtime.layout.scale * 24,
                  overflow: "hidden",
                  border: `1px solid ${plan.theme.text}55`,
                  opacity: Math.min(1, Math.max(0, (runtime.stateProgress - 0.28) / 0.35)),
                }}
              >
                <RuntimeAsset runtime={runtime} scene={scene} asset={supporting} />
                <div
                  style={{
                    position: "absolute",
                    left: runtime.layout.scale * 14,
                    bottom: runtime.layout.scale * 12,
                    padding: `${runtime.layout.scale * 6}px ${runtime.layout.scale * 10}px`,
                    background: "rgba(8,8,10,0.82)",
                    color: plan.theme.text,
                    fontSize: Math.max(9, runtime.layout.scale * 14),
                    letterSpacing: 1.2,
                    textTransform: "uppercase",
                  }}
                >
                  CONTEXTO / DETALHE
                </div>
              </div>
            ) : null}
            <MetadataLine plan={plan} scene={scene} />
          </div>
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const EvidenceTable: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const rows = scene.body.split("\n").filter(Boolean);
      return (
        <AbsoluteFill
          style={{ padding: runtime.layout.scale * 72, display: "flex", alignItems: "center" }}
        >
          <ScenePaper plan={plan} scene={scene}>
            {rows.length ? (
              rows.map((row, index) => {
                const start = (index / Math.max(1, rows.length)) * 0.7;
                const end = start + 0.2;
                const localProgress = Math.min(
                  1,
                  Math.max(0, (runtime.stateProgress - start) / (end - start)),
                );
                return (
                  <div
                    key={row}
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      borderTop: "1px solid #18181B33",
                      padding: `${runtime.layout.scale * 14}px 0`,
                      fontSize: Math.max(14, runtime.layout.scale * 20),
                      opacity: localProgress,
                      transform: `translateX(${(1 - localProgress) * runtime.layout.scale * 18}px)`,
                    }}
                  >
                    <span>{row}</span>
                    <span style={{ opacity: 0.6 }}>{String(index + 1).padStart(2, "0")}</span>
                  </div>
                );
              })
            ) : (
              <div style={{ fontSize: Math.max(16, runtime.layout.scale * 22) }}>{scene.body}</div>
            )}
          </ScenePaper>
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const InvestigationBoard: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill style={{ padding: runtime.layout.scale * 58, background: "#16181C" }}>
        <div
          style={{
            position: "relative",
            height: "100%",
            border: `1px solid ${plan.theme.accent}55`,
            backgroundImage:
              "linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px)",
            backgroundSize: `${runtime.layout.scale * 60}px ${runtime.layout.scale * 60}px`,
            overflow: "hidden",
          }}
        >
          <div
            style={{
              position: "absolute",
              left: runtime.layout.scale * 70,
              top: runtime.layout.scale * 70,
              width: "34%",
              height: "38%",
              transform: `rotate(-5deg) scale(${0.92 + runtime.stateProgress * 0.08})`,
              overflow: "hidden",
              opacity: Math.min(1, runtime.stateProgress / 0.35),
            }}
          >
            <RuntimeAsset runtime={runtime} scene={scene} />
          </div>
          <div
            style={{
              position: "absolute",
              right: runtime.layout.scale * 86,
              top: runtime.layout.scale * 96,
              width: "32%",
              padding: runtime.layout.scale * 22,
              background: "#E7E2D8",
              color: "#18181B",
              transform: `rotate(4deg) scale(${0.94 + runtime.stateProgress * 0.06})`,
              opacity: Math.min(1, Math.max(0, (runtime.stateProgress - 0.2) / 0.35)),
            }}
          >
            <div style={{ fontSize: Math.max(14, runtime.layout.scale * 18), fontWeight: 800 }}>
              {scene.headline}
            </div>
            <div
              style={{
                fontSize: Math.max(12, runtime.layout.scale * 16),
                marginTop: runtime.layout.scale * 10,
              }}
            >
              {scene.body}
            </div>
          </div>
          <div
            style={{
              position: "absolute",
              left: "35%",
              bottom: runtime.layout.scale * 90,
              width: "32%",
              borderTop: `${Math.max(2, runtime.layout.scale * 3)}px solid ${plan.theme.accent}`,
              paddingTop: runtime.layout.scale * 14,
              color: plan.theme.text,
              fontSize: Math.max(14, runtime.layout.scale * 22),
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
              strokeDashoffset={220 - runtime.stateProgress * 220}
            />
            <path
              d="M1180 520 C980 680 820 760 650 820"
              fill="none"
              stroke={plan.theme.text}
              strokeWidth="2"
              strokeDasharray="6 8"
              strokeDashoffset={220 - runtime.stateProgress * 220}
              opacity="0.45"
            />
          </svg>
        </div>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const Timeline: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const events = scene.body.split("\n").filter(Boolean);
      const lineProgress =
        runtime.motion.operator === "line-draw" || runtime.motion.operator === "timeline-build"
          ? runtime.motion.drawProgress
          : runtime.stateProgress;
      const showTimeline = runtime.hiddenLayers.includes("timeline")
        ? false
        : runtime.visibleLayers.length
          ? runtime.visibleLayers.includes("timeline")
          : true;
      return (
        <AbsoluteFill
          style={{
            padding: runtime.layout.scale * 84,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
          }}
        >
          <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "LINE OF TIME"}</Kicker>
          <Headline
            style={{
              color: plan.theme.text,
              marginTop: runtime.layout.scale * 18,
              maxWidth: "72%",
            }}
          >
            {scene.headline}
          </Headline>
          {showTimeline ? (
            <div
              style={{
                position: "relative",
                marginTop: runtime.layout.scale * 70,
                height: Math.max(2, runtime.layout.scale * 2),
                background: `${plan.theme.muted}77`,
              }}
            >
              <div
                style={{
                  position: "absolute",
                  inset: 0,
                  background: plan.theme.accent,
                  transformOrigin: "left center",
                  transform: `scaleX(${lineProgress})`,
                }}
              />
              {events.map((event, index) => (
                <div
                  key={`${event}-dot`}
                  style={{
                    position: "absolute",
                    left: `${index * (100 / Math.max(1, events.length - 1))}%`,
                    top: -runtime.layout.scale * 9,
                    width: runtime.layout.scale * 20,
                    height: runtime.layout.scale * 20,
                    borderRadius: 20,
                    background: index === 0 ? plan.theme.accent : plan.theme.text,
                    opacity: Math.min(
                      1,
                      Math.max(0, (lineProgress - index / Math.max(1, events.length)) * 5),
                    ),
                  }}
                />
              ))}
              {events.map((event, index) => (
                <div
                  key={`${event}-label`}
                  style={{
                    position: "absolute",
                    left: `${index * (100 / Math.max(1, events.length - 1))}%`,
                    top: runtime.layout.scale * 28,
                    width: "25%",
                    color: plan.theme.muted,
                    fontSize: Math.max(11, runtime.layout.scale * 18),
                    lineHeight: 1.2,
                    opacity: Math.min(
                      1,
                      Math.max(0, (lineProgress - index / Math.max(1, events.length)) * 5),
                    ),
                  }}
                >
                  {event}
                </div>
              ))}
            </div>
          ) : null}
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const Location: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill>
        <RuntimeAsset runtime={runtime} scene={scene} />
        <div
          style={{
            position: "absolute",
            left: `${runtime.focalPoint[0] * 100}%`,
            top: `${runtime.focalPoint[1] * 100}%`,
            width: runtime.layout.scale * 26,
            height: runtime.layout.scale * 26,
            marginLeft: -runtime.layout.scale * 13,
            marginTop: -runtime.layout.scale * 13,
            borderRadius: "50%",
            border: `${Math.max(2, runtime.layout.scale * 3)}px solid ${plan.theme.accent}`,
            boxShadow: `0 0 0 ${runtime.layout.scale * 6}px rgba(185, 28, 28, 0.16)`,
            opacity: Math.min(1, Math.max(0, (runtime.stateProgress - 0.18) / 0.4)),
            transform: `scale(${0.7 + runtime.stateProgress * 0.3})`,
          }}
        />
        <div
          style={{
            position: "absolute",
            inset: 0,
            background: "linear-gradient(90deg, rgba(0,0,0,0.78), transparent 72%)",
          }}
        />
        <div
          style={{
            position: "absolute",
            left: runtime.layout.actionSafe[0] * runtime.layout.width + runtime.layout.scale * 20,
            top: runtime.layout.actionSafe[1] * runtime.layout.height + runtime.layout.scale * 20,
            maxWidth: "65%",
          }}
        >
          <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "LOCATION"}</Kicker>
          <Headline style={{ color: plan.theme.text, marginTop: runtime.layout.scale * 18 }}>
            {scene.headline}
          </Headline>
          <Body muted style={{ marginTop: runtime.layout.scale * 16 }}>
            {scene.body}
          </Body>
          <div
            style={{
              marginTop: runtime.layout.scale * 30,
              color: plan.theme.text,
              fontSize: Math.max(11, runtime.layout.scale * 16),
              letterSpacing: 2,
            }}
          >
            {scene.metadata.coordinates ?? "COORDINATES —"}
          </div>
        </div>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const MapScene: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const routeProgress =
        runtime.motion.operator === "route-draw" ? runtime.motion.drawProgress : 1;
      return (
        <AbsoluteFill style={{ padding: runtime.layout.scale * 72, background: "#10151A" }}>
          <div
            style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}
          >
            <div>
              <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "MAP"}</Kicker>
              <Headline style={{ color: plan.theme.text, marginTop: runtime.layout.scale * 16 }}>
                {scene.headline}
              </Headline>
            </div>
            <div
              style={{
                color: plan.theme.muted,
                fontSize: Math.max(10, runtime.layout.scale * 15),
                letterSpacing: 2,
              }}
            >
              NORTH ↑
            </div>
          </div>
          <div
            style={{
              position: "relative",
              flex: 1,
              marginTop: runtime.layout.scale * 28,
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
                strokeDasharray="1200"
                strokeDashoffset={1200 * (1 - routeProgress)}
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
                left: runtime.layout.scale * 36,
                bottom: runtime.layout.scale * 30,
                color: plan.theme.muted,
                fontSize: Math.max(12, runtime.layout.scale * 18),
              }}
            >
              {scene.body}
            </div>
          </div>
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);
