import type { CSSProperties } from "react";

import type { RenderPlan } from "../schema";

export type LayoutFormat = "long" | "short";
export type SafeAreaKind = "action" | "captions" | "watermark";
export type NormalizedRect = [number, number, number, number];

export type CropChoice = {
  focalPoint: [number, number];
  actionSafe: NormalizedRect;
  captionAvoid: NormalizedRect;
  dedicatedReframeRequired: boolean;
};

export type LayoutProfile = {
  format: LayoutFormat;
  width: number;
  height: number;
  scale: number;
  safeArea: NormalizedRect;
  actionSafe: NormalizedRect;
  captionSafe: NormalizedRect;
  watermarkSafe: NormalizedRect;
  focalPoint: [number, number];
  dedicatedReframeRequired: boolean;
};

export const DEFAULT_SAFE_AREAS: Record<LayoutFormat, Record<SafeAreaKind, NormalizedRect>> = {
  long: {
    action: [0.05, 0.05, 0.9, 0.78],
    captions: [0.06, 0.78, 0.88, 0.16],
    watermark: [0.88, 0.04, 0.08, 0.08],
  },
  short: {
    action: [0.1, 0.1, 0.8, 0.72],
    captions: [0.08, 0.78, 0.84, 0.16],
    watermark: [0.84, 0.04, 0.1, 0.08],
  },
};

export const DEFAULT_CROP_POLICIES: Record<LayoutFormat, CropChoice> = {
  long: {
    focalPoint: [0.5, 0.5],
    actionSafe: DEFAULT_SAFE_AREAS.long.action,
    captionAvoid: DEFAULT_SAFE_AREAS.long.captions,
    dedicatedReframeRequired: false,
  },
  short: {
    focalPoint: [0.5, 0.42],
    actionSafe: DEFAULT_SAFE_AREAS.short.action,
    captionAvoid: DEFAULT_SAFE_AREAS.short.captions,
    dedicatedReframeRequired: true,
  },
};

const clamp = (value: number, minimum = 0, maximum = 1): number =>
  Math.min(maximum, Math.max(minimum, Number.isFinite(value) ? value : minimum));

export const resolveLayoutFormat = (
  width: number,
  height: number,
  requested: LayoutFormat,
): LayoutFormat => {
  if (requested === "short") return "short";
  return height > width ? "short" : "long";
};

export const normalizeRect = (
  value: readonly number[] | undefined,
  fallback: NormalizedRect,
): NormalizedRect => {
  if (!value || value.length < 4) return fallback;
  const x = clamp(value[0]);
  const y = clamp(value[1]);
  const width = clamp(value[2], 0.001, 1 - x);
  const height = clamp(value[3], 0.001, 1 - y);
  return [x, y, width, height];
};

const sceneSafeArea = (
  scene: RenderPlan["scenes"][number] | undefined,
  format: LayoutFormat,
  kind: SafeAreaKind,
): NormalizedRect | undefined => {
  const value =
    scene?.safeAreas?.[format]?.[kind] ?? scene?.imagePrompt?.safeAreas?.[format]?.[kind];
  return value ? normalizeRect(value, DEFAULT_SAFE_AREAS[format][kind]) : undefined;
};

const visualSafeArea = (
  plan: RenderPlan,
  format: LayoutFormat,
  kind: SafeAreaKind,
): NormalizedRect | undefined => {
  const safeAreas = plan.visualBible?.safeAreas;
  if (!safeAreas || typeof safeAreas !== "object") return undefined;
  const formatAreas = (safeAreas as Record<string, unknown>)[format];
  if (!formatAreas || typeof formatAreas !== "object") return undefined;
  const value = (formatAreas as Record<string, unknown>)[kind];
  return Array.isArray(value) ? normalizeRect(value, DEFAULT_SAFE_AREAS[format][kind]) : undefined;
};

const cropChoice = (
  scene: RenderPlan["scenes"][number] | undefined,
  format: LayoutFormat,
): CropChoice => {
  const fallback = DEFAULT_CROP_POLICIES[format];
  if (format === "short") {
    const policy =
      scene?.cropPolicy?.short ??
      scene?.imagePrompt?.cropPolicy?.short ??
      scene?.motionPrompt?.cropPolicy?.short;
    return {
      focalPoint: [
        clamp(policy?.focalPoint[0] ?? fallback.focalPoint[0]),
        clamp(policy?.focalPoint[1] ?? fallback.focalPoint[1]),
      ],
      actionSafe: normalizeRect(policy?.actionSafe, fallback.actionSafe),
      captionAvoid: normalizeRect(policy?.captionAvoid, fallback.captionAvoid),
      dedicatedReframeRequired:
        policy?.dedicatedReframeRequired ?? fallback.dedicatedReframeRequired,
    };
  }
  const policy =
    scene?.cropPolicy?.long ??
    scene?.imagePrompt?.cropPolicy?.long ??
    scene?.motionPrompt?.cropPolicy?.long;
  return {
    focalPoint: [
      clamp(policy?.focalPoint[0] ?? fallback.focalPoint[0]),
      clamp(policy?.focalPoint[1] ?? fallback.focalPoint[1]),
    ],
    actionSafe: normalizeRect(policy?.actionSafe, fallback.actionSafe),
    captionAvoid: normalizeRect(policy?.captionAvoid, fallback.captionAvoid),
    dedicatedReframeRequired: false,
  };
};

export const getLayoutProfile = (
  plan: RenderPlan,
  width = plan.video.width,
  height = plan.video.height,
  scene?: RenderPlan["scenes"][number],
): LayoutProfile => {
  const format = resolveLayoutFormat(width, height, plan.format);
  const crop = cropChoice(scene, format);
  const actionSafe =
    sceneSafeArea(scene, format, "action") ??
    visualSafeArea(plan, format, "action") ??
    crop.actionSafe;
  const captionSafe =
    sceneSafeArea(scene, format, "captions") ??
    visualSafeArea(plan, format, "captions") ??
    crop.captionAvoid;
  const watermarkSafe =
    sceneSafeArea(scene, format, "watermark") ??
    visualSafeArea(plan, format, "watermark") ??
    DEFAULT_SAFE_AREAS[format].watermark;
  const safeArea: NormalizedRect = [
    clamp(plan.theme.safeArea.x / Math.max(1, width)),
    clamp(plan.theme.safeArea.y / Math.max(1, height)),
    clamp(1 - (plan.theme.safeArea.x * 2) / Math.max(1, width), 0.001, 1),
    clamp(1 - (plan.theme.safeArea.y * 2) / Math.max(1, height), 0.001, 1),
  ];
  return {
    format,
    width,
    height,
    scale: Math.min(width, height) / 1080,
    safeArea,
    actionSafe,
    captionSafe,
    watermarkSafe,
    focalPoint: crop.focalPoint,
    dedicatedReframeRequired: crop.dedicatedReframeRequired,
  };
};

export const rectToPixels = (rect: NormalizedRect, width: number, height: number) => ({
  left: rect[0] * width,
  top: rect[1] * height,
  width: rect[2] * width,
  height: rect[3] * height,
});

export const rectStyle = (rect: NormalizedRect, width: number, height: number): CSSProperties => {
  const pixels = rectToPixels(rect, width, height);
  return {
    left: pixels.left,
    top: pixels.top,
    width: pixels.width,
    height: pixels.height,
  };
};
