import type { CSSProperties, FC, ReactNode } from "react";

import { Img, staticFile } from "remotion";

export const AssetImage: FC<{
  src?: string;
  objectPosition?: string;
  opacity?: number;
  filter?: string;
}> = ({ src, objectPosition = "center", opacity = 1, filter }) => {
  if (!src) {
    return (
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(135deg, #24242a 0%, #0a0a0c 70%)",
          opacity,
        }}
      />
    );
  }

  return (
    <Img
      src={staticFile(src)}
      style={{
        position: "absolute",
        inset: 0,
        width: "100%",
        height: "100%",
        objectFit: "cover",
        objectPosition,
        opacity,
        filter,
      }}
    />
  );
};

export const Paper: FC<{
  children: ReactNode;
  color: string;
  accent: string;
  style?: CSSProperties;
}> = ({ children, color, accent, style }) => (
  <div
    style={{
      position: "relative",
      background: color,
      color: "#18181B",
      padding: 28,
      borderLeft: `8px solid ${accent}`,
      boxShadow: "0 18px 50px rgba(0,0,0,0.34)",
      ...style,
    }}
  >
    {children}
  </div>
);
