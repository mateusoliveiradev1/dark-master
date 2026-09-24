import { Audio } from "@remotion/media";
import { linearTiming, type TransitionPresentation, TransitionSeries } from "@remotion/transitions";
import { crossZoom } from "@remotion/transitions/cross-zoom";
import { dissolve } from "@remotion/transitions/dissolve";
import { slide } from "@remotion/transitions/slide";
import { wipe } from "@remotion/transitions/wipe";
import type { FC, ReactNode } from "react";
import { AbsoluteFill, Easing, Sequence, staticFile, useCurrentFrame } from "remotion";

import { ChannelBrand } from "../components/Brand";
import { Captions } from "../components/Captions";
import { Backdrop, vignetteStyle } from "../components/Frame";
import { VisualError } from "../components/VisualError";
import { activeSceneAtFrame, buildPlanTimeline } from "../lib/timeline";
import { SceneRenderer } from "../scenes/SceneRenderer";
import type { RenderPlan, TransitionKind } from "../schema";

const SceneFrame: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => (
  <AbsoluteFill style={{ overflow: "hidden" }}>
    <SceneRenderer plan={plan} scene={scene} />
  </AbsoluteFill>
);

const asTransitionPresentation = (
  value: unknown,
): TransitionPresentation<Record<string, unknown>> =>
  value as TransitionPresentation<Record<string, unknown>>;

const transitionPresentation = (
  kind: Exclude<TransitionKind, "cut" | "hold" | "none">,
): TransitionPresentation<Record<string, unknown>> => {
  switch (kind) {
    case "slide":
      return asTransitionPresentation(slide({ direction: "from-right" }));
    case "wipe":
      return asTransitionPresentation(wipe({ direction: "from-left" }));
    case "match-cut":
      return asTransitionPresentation(crossZoom({ strength: 0.18 }));
    case "luminance-dissolve":
      return asTransitionPresentation(dissolve({ intensity: 0.36 }));
    case "fade":
    case "dissolve":
      return asTransitionPresentation(dissolve({ intensity: 0.18 }));
  }
};

const AbsoluteScenes: FC<{ plan: RenderPlan; timeline: ReturnType<typeof buildPlanTimeline> }> = ({
  plan,
  timeline,
}) => (
  <>
    {timeline.scenes.map((range) => (
      <Sequence
        key={range.scene.id}
        from={range.from}
        durationInFrames={range.duration}
        layout="none"
        name={range.scene.id}
      >
        <SceneFrame plan={plan} scene={range.scene} />
      </Sequence>
    ))}
  </>
);

const TransitionScenes: FC<{
  plan: RenderPlan;
  timeline: ReturnType<typeof buildPlanTimeline>;
}> = ({ plan, timeline }) => {
  const first = timeline.scenes[0];
  const last = timeline.scenes.at(-1);
  if (!first || !last) return null;
  const contentDuration = last.from + last.renderDuration - first.from;
  return (
    <Sequence
      from={first.from}
      durationInFrames={contentDuration}
      layout="none"
      name="declared-transitions"
    >
      <TransitionSeries>
        {timeline.scenes.flatMap((range) => {
          const transition = timeline.transitions.find(
            (candidate) => candidate.fromSceneId === range.scene.id,
          );
          const nodes: ReactNode[] = [
            <TransitionSeries.Sequence
              key={`${range.scene.id}-sequence`}
              durationInFrames={range.renderDuration}
              layout="none"
              name={range.scene.id}
            >
              <SceneFrame plan={plan} scene={range.scene} />
            </TransitionSeries.Sequence>,
          ];
          if (transition) {
            nodes.push(
              <TransitionSeries.Transition
                key={`${transition.fromSceneId}-${transition.toSceneId}`}
                presentation={transitionPresentation(transition.kind)}
                timing={linearTiming({
                  durationInFrames: transition.durationInFrames,
                  easing: Easing.bezier(0.22, 1, 0.36, 1),
                })}
              />,
            );
          }
          return nodes;
        })}
      </TransitionSeries>
    </Sequence>
  );
};

export const EditorialVideo: FC<{ plan: RenderPlan }> = ({ plan }) => {
  const frame = useCurrentFrame();
  const timeline = buildPlanTimeline(plan);
  const activeScene = activeSceneAtFrame(plan, frame);
  return (
    <Backdrop
      background={plan.theme.background}
      surface={plan.theme.surface}
      accent={plan.theme.accent}
      bodyFont={plan.theme.bodyFont}
      headingFont={plan.theme.headingFont}
    >
      {timeline.transitions.length ? (
        <TransitionScenes plan={plan} timeline={timeline} />
      ) : (
        <AbsoluteScenes plan={plan} timeline={timeline} />
      )}
      {timeline.errors.length ? <VisualError sceneId="timeline" errors={timeline.errors} /> : null}
      {plan.audio ? <Audio src={staticFile(plan.audio.src)} volume={plan.audio.volume} /> : null}
      <ChannelBrand plan={plan} scene={activeScene} />
      <Captions plan={plan} scene={activeScene} />
      <AbsoluteFill style={vignetteStyle} />
    </Backdrop>
  );
};
