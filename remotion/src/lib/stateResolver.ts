import {
  type AssetRef,
  type MotionOperator,
  normalizeMotionOperator,
  type RenderPlan,
  SCENE_TYPES,
} from "../schema";
import type { LayoutFormat, LayoutProfile } from "./layout";
import { getLayoutProfile } from "./layout";
import type { MotionFrame, MotionInterpretation } from "./motionInterpreter";
import { MOTION_EASINGS, motionInterpreter } from "./motionInterpreter";

export type Scene = RenderPlan["scenes"][number];
export type SceneState = Scene["states"][number];
export type MotionState = NonNullable<Scene["motionPrompt"]>["states"][number];

export type ResolvedSceneState = {
  frame: number;
  progress: number;
  stateProgress: number;
  stateIndex: number;
  state: SceneState | null;
  stateRange: [number, number];
  stateTransitionProgress: number;
  stateBoundaryProgress: number;
  previousState: SceneState | null;
  nextState: SceneState | null;
  nextStateId: string | null;
  motionState: MotionState | null;
  visibleLayers: string[];
  hiddenLayers: string[];
  assetIds: string[];
  assets: AssetRef[];
  primaryAsset: AssetRef | null;
  supportingAsset: AssetRef | null;
  focalPoint: [number, number];
  annotation: string | null;
  transition: string | null;
  audioCue: string | null;
  rawMotion: string;
  operator: MotionOperator | null;
  intensity: number;
  reason: string;
  motion: MotionInterpretation;
  format: LayoutFormat;
  layout: LayoutProfile;
  errors: string[];
};

const clamp = (value: number, minimum = 0, maximum = 1): number =>
  Math.min(maximum, Math.max(minimum, Number.isFinite(value) ? value : minimum));

const unique = (values: string[]): string[] => [...new Set(values.filter(Boolean))];

const sceneProgress = (frame: number, durationInFrames: number): number =>
  clamp(frame / Math.max(1, durationInFrames - 1));

const stateAt = <T extends { timeRange: [number, number] }>(
  value: number,
  states: T[],
): T | null => {
  if (!states.length) return null;
  const selected = states.find(
    (state) => value >= state.timeRange[0] && value < state.timeRange[1],
  );
  return selected ?? states[states.length - 1];
};

const stateIndexAt = <T extends { timeRange: [number, number] }>(
  value: number,
  states: T[],
): number => {
  const index = states.findIndex(
    (state) => value >= state.timeRange[0] && value < state.timeRange[1],
  );
  return index < 0 ? Math.max(0, states.length - 1) : index;
};

const resolveVisibleLayers = (
  scene: Scene,
  state: SceneState | null,
  motionState: MotionState | null,
): string[] => {
  const stateLayers = state?.visibleLayers ?? [];
  const motionLayers = motionState?.visibleLayers ?? [];
  const fallback = stateLayers.length
    ? stateLayers
    : motionLayers.length
      ? motionLayers
      : scene.layers.length
        ? scene.layers
        : scene.imagePrompt?.layers.length
          ? scene.imagePrompt.layers
          : (scene.motionPrompt?.layers ?? []);
  const hidden = unique([...(state?.hiddenLayers ?? []), ...(motionState?.hiddenLayers ?? [])]);
  const visible = unique(fallback).filter((layer) => !hidden.includes(layer));
  return visible.length ? visible : [];
};

const resolveAssetIds = (state: SceneState | null, motionState: MotionState | null): string[] => {
  const explicit = state?.assetIds?.length ? state.assetIds : (motionState?.assetIds ?? []);
  return unique(explicit);
};

const resolveAssets = (
  plan: RenderPlan,
  scene: Scene,
  state: SceneState | null,
  motionState: MotionState | null,
): { assets: AssetRef[]; errors: string[] } => {
  const requestedIds = resolveAssetIds(state, motionState);
  const blocked = new Set(plan.blockedAssetIds);
  const ledgerAssets = plan.assetLedger.filter(
    (asset) => asset.promptId === scene.promptId && asset.shotId === scene.shotId,
  );
  const byId = new Map<string, AssetRef>();
  for (const asset of ledgerAssets) byId.set(asset.assetId, asset);
  for (const asset of scene.assets) byId.set(asset.assetId, asset);
  const errors: string[] = [];
  const selected: AssetRef[] = [];
  for (const assetId of requestedIds) {
    const asset = byId.get(assetId);
    if (!asset) {
      errors.push(`assetId not found: ${assetId}`);
      continue;
    }
    if (asset.blocked || blocked.has(assetId)) {
      errors.push(`assetId is blocked: ${assetId}`);
      continue;
    }
    selected.push(asset);
  }
  if (!selected.length && !requestedIds.length) {
    const available = [...byId.values()]
      .filter((asset) => !asset.blocked && !blocked.has(asset.assetId))
      .sort((left, right) => left.assetId.localeCompare(right.assetId));
    selected.push(...available.filter((asset) => asset.role === "primary"));
    if (!selected.length) selected.push(...available);
  }
  return { assets: selected, errors };
};

const cameraFocalPoint = (scene: Scene, progress: number): [number, number] | undefined => {
  const keyframes = [...(scene.motionPrompt?.cameraPath.keyframes ?? [])].sort(
    (left, right) => left.at - right.at,
  );
  if (!keyframes.length) return undefined;
  const at = clamp(progress) * 100;
  const first = keyframes[0];
  const last = keyframes[keyframes.length - 1];
  if (at <= first.at) return [clamp(first.focalPoint[0]), clamp(first.focalPoint[1])];
  if (at >= last.at) return [clamp(last.focalPoint[0]), clamp(last.focalPoint[1])];
  for (let index = 1; index < keyframes.length; index += 1) {
    const previous = keyframes[index - 1];
    const next = keyframes[index];
    if (at > next.at) continue;
    const span = Math.max(0.0001, next.at - previous.at);
    const local = clamp((at - previous.at) / span);
    const eased = MOTION_EASINGS.easeInOutCubic(local);
    return [
      clamp(previous.focalPoint[0] + (next.focalPoint[0] - previous.focalPoint[0]) * eased),
      clamp(previous.focalPoint[1] + (next.focalPoint[1] - previous.focalPoint[1]) * eased),
    ];
  }
  return undefined;
};

const resolveFocalPoint = (
  scene: Scene,
  state: SceneState | null,
  motionState: MotionState | null,
  layout: LayoutProfile,
  progress: number,
): [number, number] => {
  const cameraPoint = cameraFocalPoint(scene, progress);
  const point =
    state?.focalPoint ??
    motionState?.focalPoint ??
    (layout.format === "short"
      ? layout.focalPoint
      : (cameraPoint ??
        (typeof scene.imagePrompt?.composition === "object"
          ? scene.imagePrompt.composition.focalPoint
          : undefined) ??
        layout.focalPoint));
  return [clamp(point[0]), clamp(point[1])];
};

export class StateResolver {
  resolve(
    plan: RenderPlan,
    scene: Scene,
    frame: number,
    fps: number,
    width = plan.video.width,
    height = plan.video.height,
  ): ResolvedSceneState {
    const durationInFrames = Math.max(1, Math.round(scene.durationSeconds * fps));
    const progress = sceneProgress(frame, durationInFrames);
    const state = stateAt(progress, scene.states);
    const stateIndex = state ? stateIndexAt(progress, scene.states) : -1;
    const motionState = stateAt(progress * 100, scene.motionPrompt?.states ?? []);
    const resolvedStateProgress = state
      ? clamp(
          (progress - state.timeRange[0]) /
            Math.max(0.0001, state.timeRange[1] - state.timeRange[0]),
        )
      : progress;
    const nextStateId = stateIndex >= 0 ? (scene.states[stateIndex + 1]?.id ?? null) : null;
    const previousState = stateIndex > 0 ? (scene.states[stateIndex - 1] ?? null) : null;
    const nextState = stateIndex >= 0 ? (scene.states[stateIndex + 1] ?? null) : null;
    const stateBoundaryProgress = clamp((resolvedStateProgress - 0.82) / 0.18);
    const layout = getLayoutProfile(plan, width, height, scene);
    const visibleLayers = resolveVisibleLayers(scene, state, motionState);
    const assetResult = resolveAssets(plan, scene, state, motionState);
    const focalPoint = resolveFocalPoint(scene, state, motionState, layout, progress);
    const rawMotion = state?.motion ?? motionState?.motion ?? scene.motionVariant;
    const intensity = motionState?.intensity ?? scene.motionPrompt?.intensity ?? (state ? 1 : 0);
    const reason = state?.intent ?? motionState?.intent ?? scene.motionIntent;
    const operator = normalizeMotionOperator(rawMotion);
    const errors = [...assetResult.errors];
    if (!SCENE_TYPES.includes(scene.type)) errors.push(`unknown scene type: ${String(scene.type)}`);
    if (!operator) errors.push(`unknown motion operator: ${rawMotion || "<empty>"}`);
    const motion = motionInterpreter.interpret({
      operator: rawMotion,
      intensity,
      progress,
      stateProgress: resolvedStateProgress,
      focalPoint,
      width,
      height,
      visibleLayers,
      reason,
    });
    return {
      frame,
      progress,
      stateProgress: resolvedStateProgress,
      stateIndex,
      state,
      stateRange: state?.timeRange ?? [progress, progress],
      stateTransitionProgress: resolvedStateProgress,
      stateBoundaryProgress,
      previousState,
      nextState,
      nextStateId,
      motionState,

      visibleLayers,
      hiddenLayers: unique([...(state?.hiddenLayers ?? []), ...(motionState?.hiddenLayers ?? [])]),
      assetIds: resolveAssetIds(state, motionState),
      assets: assetResult.assets,
      primaryAsset:
        assetResult.assets.find((asset) => asset.role === "primary") ??
        assetResult.assets[0] ??
        null,
      supportingAsset: assetResult.assets.find((asset) => asset.role === "supporting") ?? null,
      focalPoint,
      annotation: state?.annotation ?? motionState?.annotation ?? null,
      transition: motionState?.transition ?? null,
      audioCue: motionState?.audioCue ?? scene.motionPrompt?.audioCues[0] ?? null,
      rawMotion,
      operator,
      intensity,
      reason,
      motion,
      format: layout.format,
      layout,
      errors,
    };
  }
}

export const stateResolver = new StateResolver();

export const resolveSceneState = (
  plan: RenderPlan,
  scene: Scene,
  frame: number,
  fps: number,
  width = plan.video.width,
  height = plan.video.height,
): ResolvedSceneState => stateResolver.resolve(plan, scene, frame, fps, width, height);

export const resolveState = resolveSceneState;

export const isMotionFrame = (value: MotionInterpretation): value is MotionFrame =>
  value.operator !== null;
