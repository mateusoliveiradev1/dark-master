import type { FC, ReactNode } from "react";

import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { rectStyle } from "../lib/layout";
import { annotationMotionStyle } from "../lib/motionInterpreter";
import { isMotionFrame, type ResolvedSceneState, resolveSceneState } from "../lib/stateResolver";
import type { RenderPlan } from "../schema";
import { VisualError } from "./VisualError";

export type SceneRuntimeProps = {
  plan: RenderPlan;
  scene: RenderPlan["scenes"][number];
  children: (runtime: ResolvedSceneState) => ReactNode;
};

export const useSceneRuntime = (
  plan: RenderPlan,
  scene: RenderPlan["scenes"][number],
): ResolvedSceneState => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  return resolveSceneState(plan, scene, frame, fps, width, height);
};

const StateAnnotation: FC<{ runtime: ResolvedSceneState }> = ({ runtime }) => {
  if (!runtime.annotation) return null;
  const action = runtime.layout.actionSafe;
  const left = action[0] * runtime.layout.width + runtime.layout.scale * 24;
  const bottom = (1 - action[1] - action[3]) * runtime.layout.height + runtime.layout.scale * 24;
  return (
    <div
      style={{
        position: "absolute",
        left,
        bottom,
        maxWidth: action[2] * runtime.layout.width - runtime.layout.scale * 48,
        padding: `${runtime.layout.scale * 10}px ${runtime.layout.scale * 14}px`,
        borderLeft: `${Math.max(2, runtime.layout.scale * 3)}px solid ${runtime.layout.format === "short" ? "#EBB41E" : "#B91C1C"}`,
        background: "rgba(8,8,10,0.78)",
        color: runtime.layout.format === "short" ? "#F5F5F4" : "#F5F5F4",
        fontFamily: "Arial, sans-serif",
        fontSize: Math.max(12, runtime.layout.scale * 18),
        letterSpacing: runtime.layout.scale * 0.4,
        opacity: 0.92,
        ...(runtime.motion.operator
          ? annotationMotionStyle(runtime.motion, runtime.layout.width, runtime.layout.height)
          : {}),
      }}
    >
      {runtime.annotation}
    </div>
  );
};

export const SceneRuntime: FC<SceneRuntimeProps> = ({ plan, scene, children }) => {
  const runtime = useSceneRuntime(plan, scene);
  if (runtime.errors.length || !isMotionFrame(runtime.motion)) {
    return <VisualError sceneId={scene.id} errors={runtime.errors} />;
  }
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <div
        data-state-id={runtime.state?.id ?? ""}
        data-state-transition={runtime.transition ?? ""}
        data-state-progress={runtime.stateTransitionProgress}
        data-state-boundary-progress={runtime.stateBoundaryProgress}
        data-audio-cue={runtime.audioCue ?? ""}
        data-motion-operator={runtime.operator ?? ""}
        data-motion-intensity={runtime.motion.appliedIntensity}
        data-motion-reason={runtime.reason}
        style={{
          position: "absolute",
          inset: 0,
        }}
      >
        {children(runtime)}
      </div>
      <StateAnnotation runtime={runtime} />
    </AbsoluteFill>
  );
};

export const SafeOverlay: FC<{
  runtime: ResolvedSceneState;
  children: ReactNode;
  kind?: "action" | "captions";
}> = ({ runtime, children, kind = "action" }) => {
  const rect = kind === "action" ? runtime.layout.actionSafe : runtime.layout.captionSafe;
  return (
    <div
      style={{
        position: "absolute",
        ...rectStyle(rect, runtime.layout.width, runtime.layout.height),
        pointerEvents: "none",
      }}
    >
      {children}
    </div>
  );
};
