import type { CSSProperties, FC, ReactNode } from "react";

import { Img, staticFile } from "remotion";

import type { AssetRef } from "../schema";

export type AssetImageProps = {
  src?: string;
  asset?: AssetRef;
  objectPosition?: string;
  opacity?: number;
  filter?: string;
  layer?: string;
  visibleLayers?: string[];
  hiddenLayers?: string[];
  style?: CSSProperties;
};

export const AssetImage: FC<AssetImageProps> = ({
  src,
  asset,
  objectPosition = "center",
  opacity = 1,
  filter,
  layer,
  visibleLayers,
  hiddenLayers,
  style,
}) => {
  const source = asset?.path ?? src;
  const effectiveLayer = layer ?? asset?.layer;
  const isVisible =
    !effectiveLayer ||
    (hiddenLayers?.includes(effectiveLayer) !== true &&
      (!visibleLayers || visibleLayers.includes(effectiveLayer)));
  if (!isVisible) return null;
  if (!source) {
    return (
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(135deg, #24242a 0%, #0a0a0c 70%)",
          opacity,
          ...style,
        }}
      />
    );
  }
  return (
    <Img
      src={staticFile(source)}
      style={{
        position: "absolute",
        inset: 0,
        width: "100%",
        height: "100%",
        objectFit: "cover",
        objectPosition,
        opacity,
        filter,
        ...style,
      }}
    />
  );
};

export const AssetStack: FC<{
  assets: AssetRef[];
  focalPoint: [number, number];
  visibleLayers?: string[];
  hiddenLayers?: string[];
  opacity?: number;
}> = ({ assets, focalPoint, visibleLayers, hiddenLayers, opacity = 1 }) => (
  <>
    {assets.map((asset) => (
      <AssetImage
        key={asset.assetId}
        asset={asset}
        objectPosition={`${focalPoint[0] * 100}% ${focalPoint[1] * 100}%`}
        layer={asset.layer}
        visibleLayers={visibleLayers}
        hiddenLayers={hiddenLayers}
        opacity={opacity}
      />
    ))}
  </>
);

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
