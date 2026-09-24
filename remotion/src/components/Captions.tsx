import type { FC } from "react";

import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { activeCaption } from "../lib/timeline";
import type { RenderPlan } from "../schema";

export const Captions: FC<{ plan: RenderPlan }> = ({ plan }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const seconds = frame / fps;
  const caption = activeCaption(plan.captions, seconds);
  if (!caption) return null;
  const progress = interpolate(
    frame,
    [Math.max(0, caption.startSeconds * fps), caption.endSeconds * fps],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <div
      style={{
        position: "absolute",
        left: 80,
        right: 80,
        bottom: 52,
        display: "flex",
        justifyContent: "center",
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          maxWidth: plan.format === "short" ? 760 : 1040,
          padding: "10px 20px",
          background: "rgba(8,8,10,0.78)",
          border: "1px solid rgba(255,255,255,0.12)",
          color: plan.theme.text,
          fontFamily: `${plan.theme.bodyFont}, Arial, sans-serif`,
          fontSize: plan.format === "short" ? 28 : 24,
          fontWeight: 700,
          lineHeight: 1.18,
          textAlign: "center",
          opacity: interpolate(progress, [0, 0.08, 0.92, 1], [0, 1, 1, 0]),
          transform: `translateY(${interpolate(progress, [0, 1], [8, 0])}px)`,
        }}
      >
        {caption.text}
      </div>
    </div>
  );
};
