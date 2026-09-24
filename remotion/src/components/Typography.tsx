import type { CSSProperties, FC, PropsWithChildren } from "react";

export const Kicker: FC<PropsWithChildren<{ color: string }>> = ({ color, children }) => (
  <div
    style={{
      color,
      fontSize: 16,
      fontWeight: 700,
      letterSpacing: 4,
      textTransform: "uppercase",
    }}
  >
    {children}
  </div>
);

export const Headline: FC<{ children: React.ReactNode; style?: CSSProperties }> = ({
  children,
  style,
}) => (
  <div
    style={{
      fontSize: 58,
      fontWeight: 800,
      lineHeight: 0.98,
      letterSpacing: -1.8,
      textWrap: "balance",
      ...style,
    }}
  >
    {children}
  </div>
);

export const Body: FC<{ children: React.ReactNode; muted?: boolean; style?: CSSProperties }> = ({
  children,
  muted = false,
  style,
}) => (
  <div
    style={{
      color: muted ? "#A1A1AA" : "#F5F5F4",
      fontSize: 24,
      lineHeight: 1.3,
      maxWidth: 660,
      ...style,
    }}
  >
    {children}
  </div>
);

export const Metadata: FC<{ label: string; value: string; accent: string }> = ({
  label,
  value,
  accent,
}) => (
  <div style={{ display: "flex", alignItems: "center", gap: 12, fontSize: 15, letterSpacing: 1.5 }}>
    <span style={{ width: 30, height: 3, background: accent }} />
    <span style={{ color: "#A1A1AA" }}>{label.toUpperCase()}</span>
    <span style={{ color: "#F5F5F4" }}>{value}</span>
  </div>
);
