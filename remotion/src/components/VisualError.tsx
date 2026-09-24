import type { FC } from "react";

import { AbsoluteFill } from "remotion";

export const VisualError: FC<{ sceneId: string; errors: string[] }> = ({ sceneId, errors }) => (
  <AbsoluteFill
    style={{
      display: "grid",
      placeItems: "center",
      padding: 48,
      background: "#16070A",
      color: "#FFF1F2",
      fontFamily: "Arial, sans-serif",
    }}
  >
    <div
      style={{
        width: "min(760px, 90%)",
        border: "2px solid #FB7185",
        padding: 28,
        background: "rgba(20,4,8,0.94)",
      }}
    >
      <div style={{ fontSize: 16, letterSpacing: 3, textTransform: "uppercase", opacity: 0.72 }}>
        Runtime contract error
      </div>
      <div style={{ fontSize: 30, fontWeight: 800, marginTop: 12 }}>{sceneId}</div>
      <ul style={{ fontSize: 18, lineHeight: 1.45, paddingLeft: 24, marginBottom: 0 }}>
        {errors.map((error) => (
          <li key={error}>{error}</li>
        ))}
      </ul>
    </div>
  </AbsoluteFill>
);
