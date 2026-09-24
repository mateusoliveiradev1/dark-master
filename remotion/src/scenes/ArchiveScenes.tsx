import type { FC } from "react";

import { AbsoluteFill } from "remotion";

import { EndCard } from "../components/Brand";
import { AssetImage } from "../components/MediaLayer";
import { SceneRuntime } from "../components/SceneRuntime";
import { Body, Headline, Kicker } from "../components/Typography";
import { motionStyle, textMotionStyle } from "../lib/motionInterpreter";
import { isMotionFrame } from "../lib/stateResolver";
import type { RenderPlan } from "../schema";
import { RuntimeAsset, ScenePaper } from "./ScenePrimitives";

export const Document: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill
        style={{
          padding: runtime.layout.scale * 72,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          background: "#24201A",
        }}
      >
        <ScenePaper
          plan={plan}
          scene={scene}
          style={{
            maxWidth: "78%",
            minHeight: "62%",
            ...(isMotionFrame(runtime.motion)
              ? {
                  ...motionStyle(runtime.motion, runtime.layout.width, runtime.layout.height),
                  transform: `rotate(-2deg) ${motionStyle(runtime.motion, runtime.layout.width, runtime.layout.height).transform}`,
                }
              : {}),
          }}
        >
          <div
            style={{
              height: 1,
              background: "#18181B55",
              margin: `${runtime.layout.scale * 28}px 0`,
            }}
          />
          <div
            style={{
              position: "relative",
              fontSize: Math.max(16, runtime.layout.scale * 23),
              lineHeight: 1.5,
              whiteSpace: "pre-line",
            }}
          >
            {scene.body}
            <div
              style={{
                position: "absolute",
                left: "-2%",
                right: "-2%",
                top: `${Math.min(72, 18 + runtime.stateProgress * 44)}%`,
                height: `${Math.max(2, runtime.layout.scale * 3)}px`,
                background: plan.theme.accent,
                opacity: 0.78,
                transform: `scaleX(${Math.min(1, Math.max(0, (runtime.stateProgress - 0.18) / 0.35))})`,
                transformOrigin: "left center",
              }}
            />
          </div>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              marginTop: runtime.layout.scale * 56,
              fontSize: Math.max(10, runtime.layout.scale * 15),
              opacity: 0.6,
            }}
          >
            <span>{scene.metadata.date ?? "DATE UNKNOWN"}</span>
            <span>{scene.metadata.source ?? "SOURCE —"}</span>
          </div>
        </ScenePaper>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const Portrait: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill
        style={{
          display: "grid",
          gridTemplateColumns: runtime.format === "short" ? "1fr" : "0.8fr 1.2fr",
          gridTemplateRows: runtime.format === "short" ? "1fr 1fr" : "1fr",
          gap: runtime.layout.scale * 30,
          padding: runtime.layout.scale * 54,
        }}
      >
        <div style={{ position: "relative", overflow: "hidden" }}>
          <RuntimeAsset runtime={runtime} scene={scene} />
          <div
            style={{
              position: "absolute",
              inset: 0,
              background:
                runtime.format === "short"
                  ? "linear-gradient(180deg, transparent 55%, #0A0A0C)"
                  : "linear-gradient(90deg, transparent 55%, #0A0A0C)",
            }}
          />
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            paddingRight: runtime.layout.scale * 80,
          }}
        >
          <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "PORTRAIT"}</Kicker>
          <Headline style={{ color: plan.theme.text, marginTop: runtime.layout.scale * 18 }}>
            {scene.headline}
          </Headline>
          <Body muted style={{ marginTop: runtime.layout.scale * 18 }}>
            {scene.body}
          </Body>
          <div
            style={{
              marginTop: runtime.layout.scale * 32,
              color: plan.theme.text,
              fontSize: Math.max(12, runtime.layout.scale * 18),
              letterSpacing: 1,
            }}
          >
            {scene.metadata.person ?? "SUBJECT"}
          </div>
        </div>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const Comparison: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
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
      return (
        <AbsoluteFill
          style={{
            padding: runtime.layout.scale * 54,
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: runtime.layout.scale * 16,
          }}
        >
          {[
            ["A", primary, scene.asset],
            ["B", supporting, scene.secondaryAsset],
          ].map(([label, asset, legacy], index) => {
            const typedAsset = asset as RenderPlan["scenes"][number]["assets"][number] | null;
            const source = typeof legacy === "string" ? legacy : undefined;
            return (
              <div
                key={label as string}
                style={{
                  position: "relative",
                  overflow: "hidden",
                  border: `1px solid ${index ? plan.theme.accent : plan.theme.text}55`,
                  opacity: Math.min(1, Math.max(0, (runtime.stateProgress - index * 0.28) / 0.32)),
                }}
              >
                {typedAsset ? (
                  <AssetImage
                    asset={typedAsset}
                    objectPosition={`${runtime.focalPoint[0] * 100}% ${runtime.focalPoint[1] * 100}%`}
                    visibleLayers={runtime.visibleLayers}
                    hiddenLayers={runtime.hiddenLayers}
                  />
                ) : (
                  <AssetImage
                    src={source}
                    objectPosition={`${runtime.focalPoint[0] * 100}% ${runtime.focalPoint[1] * 100}%`}
                    visibleLayers={runtime.visibleLayers}
                    hiddenLayers={runtime.hiddenLayers}
                  />
                )}
                <div
                  style={{
                    position: "absolute",
                    left: runtime.layout.scale * 24,
                    top: runtime.layout.scale * 22,
                    color: plan.theme.text,
                    fontSize: Math.max(28, runtime.layout.scale * 52),
                    fontWeight: 900,
                  }}
                >
                  {label as string}
                </div>
              </div>
            );
          })}
          <div
            style={{
              position: "absolute",
              left: "50%",
              top: "50%",
              width: runtime.layout.scale * 72,
              height: runtime.layout.scale * 72,
              marginLeft: -runtime.layout.scale * 36,
              marginTop: -runtime.layout.scale * 36,
              display: "grid",
              placeItems: "center",
              borderRadius: 99,
              background: plan.theme.accent,
              color: plan.theme.text,
              fontSize: Math.max(18, runtime.layout.scale * 30),
              fontWeight: 900,
            }}
          >
            VS
          </div>
          <div
            style={{
              position: "absolute",
              left: runtime.layout.scale * 72,
              right: runtime.layout.scale * 72,
              bottom: runtime.layout.scale * 38,
              textAlign: "center",
              color: plan.theme.text,
              fontSize: Math.max(16, runtime.layout.scale * 26),
              fontWeight: 750,
              opacity: Math.min(1, Math.max(0, (runtime.stateProgress - 0.45) / 0.3)),
            }}
          >
            {scene.headline}
          </div>
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const Quote: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill
        style={{
          padding: runtime.layout.scale * 100,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          background: "linear-gradient(135deg, #111216, #24201A)",
        }}
      >
        <div
          style={{
            fontSize: Math.max(64, runtime.layout.scale * 112),
            lineHeight: 0.7,
            color: plan.theme.accent,
            fontFamily: "Georgia, serif",
          }}
        >
          “
        </div>
        <Headline
          style={{
            color: plan.theme.text,
            fontSize: Math.max(34, runtime.layout.scale * 70),
            maxWidth: "82%",
            marginTop: runtime.layout.scale * 24,
            ...(isMotionFrame(runtime.motion)
              ? textMotionStyle(runtime.motion, runtime.layout.width, runtime.layout.height)
              : {}),
          }}
        >
          {scene.headline}
        </Headline>
        <Body
          muted
          style={{
            marginTop: runtime.layout.scale * 26,
            fontSize: Math.max(16, runtime.layout.scale * 25),
          }}
        >
          {scene.body}
        </Body>
        <div
          style={{
            marginTop: runtime.layout.scale * 34,
            color: plan.theme.accent,
            fontSize: Math.max(10, runtime.layout.scale * 16),
            letterSpacing: 3,
            textTransform: "uppercase",
          }}
        >
          {scene.metadata.source ?? "SOURCE —"}
        </div>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const DataVisualization: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const values = scene.body
        .split("\n")
        .filter(Boolean)
        .map((item) => {
          const [label, raw] = item.split("|");
          return { label, value: Number(raw ?? 0) || 0 };
        });
      const max = Math.max(...values.map((item) => item.value), 1);
      return (
        <AbsoluteFill style={{ padding: runtime.layout.scale * 72 }}>
          <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "DATA"}</Kicker>
          <Headline style={{ color: plan.theme.text, marginTop: runtime.layout.scale * 16 }}>
            {scene.headline}
          </Headline>
          <div
            style={{
              display: "flex",
              alignItems: "flex-end",
              gap: runtime.layout.scale * 28,
              height: "54%",
              marginTop: runtime.layout.scale * 70,
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
                  width: "18%",
                  gap: runtime.layout.scale * 12,
                }}
              >
                <div
                  style={{
                    height: `${(item.value / max) * 82 * runtime.stateProgress}%`,
                    background: `linear-gradient(180deg, ${plan.theme.accent}, ${plan.theme.accent}55)`,
                    display: "flex",
                    alignItems: "flex-start",
                    justifyContent: "center",
                    paddingTop: runtime.layout.scale * 14,
                    color: plan.theme.text,
                    fontSize: Math.max(12, runtime.layout.scale * 18),
                    fontWeight: 800,
                  }}
                >
                  {item.value}
                </div>
                <div
                  style={{
                    color: plan.theme.muted,
                    fontSize: Math.max(10, runtime.layout.scale * 15),
                    textAlign: "center",
                  }}
                >
                  {item.label}
                </div>
              </div>
            ))}
          </div>
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const Diagram: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => {
      const items = scene.body.split("\n").filter(Boolean);
      return (
        <AbsoluteFill style={{ padding: runtime.layout.scale * 72 }}>
          <Kicker color={plan.theme.accent}>{scene.metadata.label ?? "STRUCTURE"}</Kicker>
          <Headline style={{ color: plan.theme.text, marginTop: runtime.layout.scale * 16 }}>
            {scene.headline}
          </Headline>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              marginTop: runtime.layout.scale * 110,
              position: "relative",
            }}
          >
            {items.map((item, index) => (
              <div key={item} style={{ display: "flex", alignItems: "center", flex: 1 }}>
                <div
                  style={{
                    width: runtime.layout.scale * 180,
                    height: runtime.layout.scale * 180,
                    borderRadius: 999,
                    display: "grid",
                    placeItems: "center",
                    padding: runtime.layout.scale * 20,
                    textAlign: "center",
                    background: index % 2 ? plan.theme.surface : plan.theme.accent,
                    color: plan.theme.text,
                    border: `1px solid ${plan.theme.text}55`,
                    fontSize: Math.max(12, runtime.layout.scale * 19),
                    fontWeight: 750,
                  }}
                >
                  {item}
                </div>
                {index < items.length - 1 ? (
                  <div
                    style={{
                      height: 2,
                      flex: 1,
                      background: plan.theme.accent,
                      opacity: Math.min(
                        1,
                        Math.max(0, (runtime.stateProgress - index * 0.2) / 0.35),
                      ),
                      transform: `scaleX(${Math.min(1, Math.max(0, (runtime.stateProgress - index * 0.2) / 0.35))})`,
                      transformOrigin: "left center",
                    }}
                  />
                ) : null}
              </div>
            ))}
          </div>
        </AbsoluteFill>
      );
    }}
  </SceneRuntime>
);

export const ChapterBreak: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill
        style={{ display: "grid", placeItems: "center", background: plan.theme.background }}
      >
        <div style={{ textAlign: "center", maxWidth: "82%" }}>
          <div
            style={{
              color: plan.theme.accent,
              fontSize: Math.max(12, runtime.layout.scale * 18),
              fontWeight: 800,
              letterSpacing: 5,
            }}
          >
            {scene.metadata.number ?? "CHAPTER"}
          </div>
          <Headline
            style={{
              color: plan.theme.text,
              fontSize: Math.max(30, runtime.layout.scale * 78),
              marginTop: runtime.layout.scale * 22,
            }}
          >
            {scene.headline}
          </Headline>
          <Body
            muted
            style={{ margin: `${runtime.layout.scale * 20}px auto 0`, textAlign: "center" }}
          >
            {scene.body}
          </Body>
        </div>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const Surveillance: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <AbsoluteFill style={{ padding: runtime.layout.scale * 58, background: "#070908" }}>
        <div
          style={{
            position: "relative",
            width: "100%",
            height: "100%",
            border: "1px solid #D6E5D655",
            overflow: "hidden",
          }}
        >
          <RuntimeAsset runtime={runtime} scene={scene} />
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
              top: runtime.layout.scale * 22,
              left: runtime.layout.scale * 26,
              color: "#D6E5D6",
              fontFamily: "monospace",
              fontSize: Math.max(11, runtime.layout.scale * 18),
              letterSpacing: 2,
            }}
          >
            CAM 04 / {scene.metadata.timestamp ?? "00:00:00"}
          </div>
          <div
            style={{
              position: "absolute",
              right: runtime.layout.scale * 26,
              bottom: runtime.layout.scale * 22,
              color: "#D6E5D6",
              fontFamily: "monospace",
              fontSize: Math.max(10, runtime.layout.scale * 16),
            }}
          >
            REC ●
          </div>
          <div
            style={{
              position: "absolute",
              left: runtime.layout.scale * 26,
              bottom: runtime.layout.scale * 22,
              color: plan.theme.accent,
              fontFamily: "monospace",
              fontSize: Math.max(11, runtime.layout.scale * 18),
            }}
          >
            TRACKING SUBJECT
          </div>
        </div>
      </AbsoluteFill>
    )}
  </SceneRuntime>
);

export const EndCardScene: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <SceneRuntime plan={plan} scene={scene}>
    {(runtime) => (
      <EndCard
        plan={plan}
        scene={scene}
        asset={runtime.primaryAsset?.path ?? scene.asset}
        headline={scene.headline}
        body={scene.body}
      />
    )}
  </SceneRuntime>
);
