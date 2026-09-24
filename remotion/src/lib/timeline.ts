import type { RenderPlan, Scene, TransitionKind } from "../schema";
import { TRANSITION_KINDS } from "../schema";

export type TimelineScene = {
  scene: Scene;
  index: number;
  from: number;
  duration: number;
  renderDuration: number;
};

export type TimelineTransition = {
  fromSceneId: string;
  toSceneId: string;
  kind: Exclude<TransitionKind, "cut" | "hold" | "none">;
  atFrame: number;
  durationInFrames: number;
};

export type TimelinePlan = {
  scenes: TimelineScene[];
  transitions: TimelineTransition[];
  totalDurationInFrames: number;
  renderDurationInFrames: number;
  errors: string[];
};

export const secondsToFrames = (seconds: number, fps: number): number =>
  Math.max(1, Math.round(seconds * fps));

export const sceneDurationFrames = (durationSeconds: number, fps: number): number =>
  secondsToFrames(durationSeconds, fps);

export const activeCaption = <T extends { startSeconds: number; endSeconds: number }>(
  captions: T[],
  seconds: number,
): T | undefined =>
  captions.find((caption) => seconds >= caption.startSeconds && seconds < caption.endSeconds);

const normalizedTransition = (value: string | undefined): TransitionKind | null => {
  if (!value) return null;
  const token = value.trim().toLowerCase().replaceAll("_", "-");
  return TRANSITION_KINDS.includes(token as TransitionKind) ? (token as TransitionKind) : null;
};

export const isRenderedTransition = (
  kind: TransitionKind | null,
): kind is Exclude<TransitionKind, "cut" | "hold" | "none"> =>
  kind !== null && kind !== "cut" && kind !== "hold" && kind !== "none";

const declaredBoundaryTransition = (
  current: Scene,
  next: Scene,
): { value: string; kind: TransitionKind | null } => {
  const currentValue = current.motionPrompt?.transitions.out ?? current.transitionOut ?? "cut";
  const nextValue = next.motionPrompt?.transitions.in ?? next.transitionIn ?? "cut";
  const currentKind = normalizedTransition(currentValue);
  const nextKind = normalizedTransition(nextValue);
  if (isRenderedTransition(currentKind)) return { value: currentValue, kind: currentKind };
  if (isRenderedTransition(nextKind)) return { value: nextValue, kind: nextKind };
  return { value: currentValue, kind: currentKind ?? nextKind };
};

const transitionDuration = (current: Scene, next: Scene, fps: number): number => {
  const seconds =
    current.motionPrompt?.transitions.durationSeconds ??
    current.transitionDurationSeconds ??
    next.motionPrompt?.transitions.durationSeconds ??
    next.transitionDurationSeconds ??
    0.35;
  return Math.max(1, Math.round(seconds * fps));
};

export const buildTimeline = (scenes: Scene[], fps: number): TimelinePlan => {
  const errors: string[] = [];
  const ranges: TimelineScene[] = [];
  let previousEnd = 0;
  scenes.forEach((scene, index) => {
    const from = Math.max(0, Math.round(scene.startSeconds * fps));
    const duration = Math.max(1, Math.round(scene.durationSeconds * fps));
    if (index === 0 && from > 0) {
      errors.push(`timeline gap before ${scene.id}`);
    }
    if (index > 0 && Math.abs(from - previousEnd) > 1) {
      errors.push(
        from > previousEnd
          ? `timeline gap before ${scene.id}`
          : `timeline overlap before ${scene.id}`,
      );
    }
    const normalizedFrom = index > 0 && Math.abs(from - previousEnd) <= 1 ? previousEnd : from;
    ranges.push({
      scene,
      index,
      from: normalizedFrom,
      duration,
      renderDuration: duration,
    });
    previousEnd = Math.max(previousEnd, normalizedFrom + duration);
  });

  const transitions: TimelineTransition[] = [];
  for (let index = 0; index < ranges.length - 1; index += 1) {
    const current = ranges[index];
    const next = ranges[index + 1];
    const declared = declaredBoundaryTransition(current.scene, next.scene);
    if (!declared.kind) {
      if (declared.value && !normalizedTransition(declared.value)) {
        errors.push(`unknown transition before ${next.scene.id}: ${declared.value}`);
      }
      continue;
    }
    if (!isRenderedTransition(declared.kind)) continue;
    const durationInFrames = transitionDuration(current.scene, next.scene, fps);
    if (durationInFrames > current.duration || durationInFrames > next.duration) {
      errors.push(`transition is longer than an adjacent scene before ${next.scene.id}`);
      continue;
    }
    transitions.push({
      fromSceneId: current.scene.id,
      toSceneId: next.scene.id,
      kind: declared.kind,
      atFrame: current.from + current.duration,
      durationInFrames,
    });
    current.renderDuration += durationInFrames;
  }

  const totalDurationInFrames = ranges.reduce(
    (maximum, range) => Math.max(maximum, range.from + range.duration),
    0,
  );
  const renderDurationInFrames = ranges.reduce(
    (maximum, range) => Math.max(maximum, range.from + range.renderDuration),
    0,
  );
  return { scenes: ranges, transitions, totalDurationInFrames, renderDurationInFrames, errors };
};

export const buildPlanTimeline = (plan: RenderPlan): TimelinePlan =>
  buildTimeline(plan.scenes, plan.video.fps);

export const activeSceneAtFrame = (plan: RenderPlan, frame: number): Scene | undefined => {
  const fps = plan.video.fps;
  const seconds = frame / fps;
  for (let index = plan.scenes.length - 1; index >= 0; index -= 1) {
    const scene = plan.scenes[index];
    if (seconds >= scene.startSeconds && seconds < scene.startSeconds + scene.durationSeconds) {
      return scene;
    }
  }
  return undefined;
};
