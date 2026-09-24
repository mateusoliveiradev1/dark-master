import type { FC } from "react";

import { AbsoluteFill, Img, staticFile } from "remotion";

import type { RenderPlan } from "../schema";

export const ChannelBrand: FC<{ plan: RenderPlan }> = ({ plan }) => (
  <AbsoluteFill style={{ pointerEvents: "none" }}>
    <div
      style={{
        position: "absolute",
        top: 30,
        left: 34,
        display: "flex",
        alignItems: "center",
        gap: 10,
        color: plan.theme.text,
        fontFamily: `${plan.theme.headingFont}, Arial, sans-serif`,
        fontSize: 15,
        fontWeight: 800,
        letterSpacing: 2.4,
        textTransform: "uppercase",
      }}
    >
      <span style={{ width: 8, height: 8, borderRadius: 99, background: plan.theme.accent }} />
      {plan.channel}
    </div>
    <div
      style={{
        position: "absolute",
        right: 34,
        bottom: 24,
        width: 25,
        height: 25,
        border: `2px solid ${plan.theme.text}`,
        borderRadius: 7,
        opacity: 0.72,
      }}
    />
  </AbsoluteFill>
);

export const EndCard: FC<{ plan: RenderPlan; asset?: string; headline: string; body: string }> = ({
  plan,
  asset,
  headline,
  body,
}) => (
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
        maxWidth: 920,
        textAlign: "center",
        padding: 54,
        background: "rgba(8,8,10,0.78)",
        border: `1px solid ${plan.theme.accent}66`,
      }}
    >
      <div
        style={{
          color: plan.theme.accent,
          fontSize: 17,
          fontWeight: 800,
          letterSpacing: 4,
          textTransform: "uppercase",
        }}
      >
        {plan.channel}
      </div>
      <div
        style={{
          color: plan.theme.text,
          fontSize: 66,
          fontWeight: 850,
          lineHeight: 0.95,
          marginTop: 18,
        }}
      >
        {headline}
      </div>
      <div style={{ color: plan.theme.muted, fontSize: 24, marginTop: 20 }}>{body}</div>
    </div>
  </AbsoluteFill>
);
