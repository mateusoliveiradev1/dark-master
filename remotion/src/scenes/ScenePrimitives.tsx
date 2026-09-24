import type { CSSProperties, FC, ReactNode } from "react";

import { AbsoluteFill } from "remotion";

import { AssetImage, Paper } from "../components/MediaLayer";
import { Body, Headline, Kicker, Metadata } from "../components/Typography";
import { rectStyle } from "../lib/layout";
import { mediaMotionStyle, textMotionStyle } from "../lib/motionInterpreter";
import { isMotionFrame, type ResolvedSceneState } from "../lib/stateResolver";
import type { AssetRef, RenderPlan } from "../schema";

export const Panel: FC<{ children: ReactNode; color?: string; style?: CSSProperties }> = ({
  children,
  color = "#17171B",
  style,
}) => (
  <div
    style={{
      background: color,
      border: "1px solid rgba(255,255,255,0.12)",
      padding: 24,
      ...style,
    }}
  >
    {children}
  </div>
);

const assetMotionStyle = (runtime: ResolvedSceneState, layer?: string): CSSProperties =>
  isMotionFrame(runtime.motion)
    ? mediaMotionStyle(runtime.motion, runtime.layout.width, runtime.layout.height, layer)
    : {};

export const RuntimeAsset: FC<{
  runtime: ResolvedSceneState;
  scene: RenderPlan["scenes"][number];
  asset?: AssetRef | null;
  layer?: string;
  fallback?: boolean;
  style?: CSSProperties;
}> = ({ runtime, scene, asset, layer, fallback = true, style }) => {
  const selected = asset ?? runtime.primaryAsset ?? runtime.assets[0] ?? null;
  if (selected) {
    const effectiveLayer = layer ?? selected.layer;
    return (
      <AssetImage
        asset={selected}
        objectPosition={`${runtime.focalPoint[0] * 100}% ${runtime.focalPoint[1] * 100}%`}
        layer={effectiveLayer}
        visibleLayers={runtime.visibleLayers}
        hiddenLayers={runtime.hiddenLayers}
        style={{ ...assetMotionStyle(runtime, effectiveLayer), ...style }}
      />
    );
  }
  if (!fallback) return null;
  return (
    <AssetImage
      src={scene.asset}
      objectPosition={`${runtime.focalPoint[0] * 100}% ${runtime.focalPoint[1] * 100}%`}
      layer={layer}
      visibleLayers={runtime.visibleLayers}
      hiddenLayers={runtime.hiddenLayers}
      style={{ ...assetMotionStyle(runtime, layer), ...style }}
    />
  );
};

export const TextOverlay: FC<{
  plan: RenderPlan;
  scene: RenderPlan["scenes"][number];
  runtime: ResolvedSceneState;
}> = ({ plan, scene, runtime }) => {
  const rect = runtime.layout.actionSafe;
  return (
    <div
      style={{
        position: "absolute",
        ...rectStyle(rect, runtime.layout.width, runtime.layout.height),
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-end",
        padding: Math.max(16, runtime.layout.scale * 24),
        background: "linear-gradient(180deg, transparent 30%, rgba(0,0,0,0.82) 100%)",
      }}
    >
      <Kicker color={plan.theme.accent}>
        {scene.metadata.label ?? scene.purpose ?? "DOCUMENTARY"}
      </Kicker>
      <div
        style={{
          maxWidth: "100%",
          marginTop: runtime.layout.scale * 14,
          ...(isMotionFrame(runtime.motion)
            ? textMotionStyle(runtime.motion, runtime.layout.width, runtime.layout.height)
            : {}),
        }}
      >
        <Headline
          style={{ color: plan.theme.text, fontSize: Math.max(26, runtime.layout.scale * 58) }}
        >
          {scene.headline}
        </Headline>
        {scene.body ? (
          <Body muted style={{ marginTop: runtime.layout.scale * 14, maxWidth: "100%" }}>
            {scene.body}
          </Body>
        ) : null}
      </div>
    </div>
  );
};

export const ScenePaper: FC<{
  plan: RenderPlan;
  scene: RenderPlan["scenes"][number];
  children: ReactNode;
  style?: CSSProperties;
}> = ({ plan, scene, children, style }) => (
  <Paper
    color="#E7E2D8"
    accent={plan.theme.accent}
    style={{ width: "100%", maxWidth: "92%", color: "#18181B", ...style }}
  >
    <div style={{ fontSize: 15, letterSpacing: 3, textTransform: "uppercase", opacity: 0.65 }}>
      {scene.metadata.label ?? "DOCUMENT"}
    </div>
    <div style={{ fontSize: 42, fontWeight: 800, marginTop: 12, marginBottom: 22 }}>
      {scene.headline}
    </div>
    {children}
  </Paper>
);

export const MetadataLine: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <div style={{ marginTop: 24 }}>
    <Metadata
      label="Fonte"
      value={scene.metadata.source ?? "arquivo verificado"}
      accent={plan.theme.accent}
    />
  </div>
);

export const SceneSurface: FC<{ children: ReactNode; style?: CSSProperties }> = ({
  children,
  style,
}) => <AbsoluteFill style={style}>{children}</AbsoluteFill>;
