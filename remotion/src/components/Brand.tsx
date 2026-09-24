import type { FC } from "react";

import { AbsoluteFill, Img, staticFile, useVideoConfig } from "remotion";

import { getLayoutProfile, rectStyle } from "../lib/layout";
import type { RenderPlan } from "../schema";

export const ChannelBrand: FC<{ plan: RenderPlan; scene?: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => {
  const { width, height } = useVideoConfig();
  const layout = getLayoutProfile(plan, width, height, scene);
  const watermark = rectStyle(layout.watermarkSafe, width, height);
  const safe = layout.safeArea;
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div
        style={{
          position: "absolute",
          top: safe[1] * height + layout.scale * 12,
          left: safe[0] * width + layout.scale * 18,
          display: "flex",
          alignItems: "center",
          gap: layout.scale * 10,
          color: plan.theme.text,
          fontFamily: `${plan.theme.headingFont}, Arial, sans-serif`,
          fontSize: Math.max(10, layout.scale * 15),
          fontWeight: 800,
          letterSpacing: layout.scale * 2.4,
          textTransform: "uppercase",
        }}
      >
        <span
          style={{
            width: Math.max(5, layout.scale * 8),
            height: Math.max(5, layout.scale * 8),
            borderRadius: 99,
            background: plan.theme.accent,
          }}
        />
        {plan.channel}
      </div>
      {plan.branding.watermark ? (
        <Img
          src={staticFile(plan.branding.watermark)}
          style={{
            position: "absolute",
            ...watermark,
            objectFit: "contain",
            opacity: plan.branding.watermarkOpacity,
          }}
        />
      ) : (
        <div
          style={{
            position: "absolute",
            ...watermark,
            border: `${Math.max(1, layout.scale * 2)}px solid ${plan.theme.text}`,
            borderRadius: Math.max(4, layout.scale * 7),
            opacity: 0.72,
          }}
        />
      )}
    </AbsoluteFill>
  );
};

export const EndCard: FC<{
  plan: RenderPlan;
  asset?: string;
  headline: string;
  body: string;
  scene?: RenderPlan["scenes"][number];
}> = ({ plan, asset, headline, body, scene }) => {
  const { width, height } = useVideoConfig();
  const layout = getLayoutProfile(plan, width, height, scene);
  return (
    <AbsoluteFill style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
      {asset ? (
        <Img
          src={staticFile(asset)}
          style={{
            position: "absolute",
            inset: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            opacity: 0.2,
          }}
        />
      ) : null}
      <div
        style={{
          position: "relative",
          width: `min(${Math.max(320, layout.actionSafe[2] * width * 0.9)}px, 86%)`,
          textAlign: "center",
          padding: Math.max(24, layout.scale * 54),
          background: "rgba(8,8,10,0.84)",
          border: `1px solid ${plan.theme.accent}66`,
        }}
      >
        <div
          style={{
            color: plan.theme.accent,
            fontSize: Math.max(12, layout.scale * 17),
            fontWeight: 800,
            letterSpacing: layout.scale * 4,
            textTransform: "uppercase",
          }}
        >
          {plan.channel}
        </div>
        <div
          style={{
            color: plan.theme.text,
            fontSize: Math.max(30, layout.scale * 66),
            fontWeight: 850,
            lineHeight: 0.95,
            marginTop: layout.scale * 18,
          }}
        >
          {headline}
        </div>
        <div
          style={{
            color: plan.theme.muted,
            fontSize: Math.max(16, layout.scale * 24),
            marginTop: layout.scale * 20,
          }}
        >
          {body}
        </div>
      </div>
    </AbsoluteFill>
  );
};
