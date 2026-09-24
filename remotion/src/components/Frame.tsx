import type { CSSProperties, FC, PropsWithChildren } from "react";

import { AbsoluteFill } from "remotion";

export const SafeArea: FC<PropsWithChildren<{ x: number; y: number }>> = ({ x, y, children }) => (
  <AbsoluteFill style={{ padding: `${y}px ${x}px` }}>{children}</AbsoluteFill>
);

export const Backdrop: FC<
  PropsWithChildren<{
    background: string;
    surface: string;
    accent: string;
  }>
> = ({ background, surface, accent, children }) => (
  <AbsoluteFill
    style={{
      background: `radial-gradient(circle at 80% 12%, ${accent}33 0, transparent 34%), linear-gradient(135deg, ${background} 0%, ${surface} 100%)`,
      color: "#F5F5F4",
      fontFamily: "Arial, sans-serif",
    }}
  >
    {children}
  </AbsoluteFill>
);

export const vignetteStyle: CSSProperties = {
  position: "absolute",
  inset: 0,
  pointerEvents: "none",
  background: "radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,0.56) 100%)",
};
