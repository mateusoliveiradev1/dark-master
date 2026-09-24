import { createTikTokStyleCaptions } from "@remotion/captions";
import type { FC } from "react";
import { useMemo } from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { activeCaptionPage, captionLines, captionPages } from "../lib/captions";
import { getLayoutProfile, rectStyle } from "../lib/layout";
import type { RenderPlan } from "../schema";

export const Captions: FC<{ plan: RenderPlan; scene?: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const layout = getLayoutProfile(plan, width, height, scene);
  const pages = useMemo(
    () => captionPages(plan.captions, layout.format),
    [plan.captions, layout.format],
  );
  const page = activeCaptionPage(pages, frame / fps);
  if (!page) return null;
  const maxCharacters = Math.max(
    18,
    Math.floor((layout.format === "short" ? 30 : 46) * layout.scale),
  );
  const maxLines = layout.format === "short" ? 3 : 2;
  const lines = captionLines(page.text, maxCharacters, maxLines);
  return (
    <div
      style={{
        position: "absolute",
        ...rectStyle(layout.captionSafe, width, height),
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          width: "100%",
          padding: `${Math.max(8, layout.scale * 10)}px ${Math.max(14, layout.scale * 20)}px`,
          background: "rgba(8,8,10,0.86)",
          border: "1px solid rgba(255,255,255,0.14)",
          color: plan.theme.text,
          fontFamily: `${plan.theme.bodyFont}, Arial, sans-serif`,
          fontSize: Math.max(16, (layout.format === "short" ? 28 : 24) * layout.scale),
          fontWeight: 700,
          lineHeight: 1.16,
          textAlign: "center",
          overflow: "hidden",
        }}
      >
        {lines.map((line) => (
          <div key={line}>{line}</div>
        ))}
      </div>
    </div>
  );
};

export { createTikTokStyleCaptions };
