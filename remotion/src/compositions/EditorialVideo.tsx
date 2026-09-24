import { Audio } from "@remotion/media";
import type { FC } from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  Series,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { ChannelBrand } from "../components/Brand";
import { Captions } from "../components/Captions";
import { Backdrop, vignetteStyle } from "../components/Frame";
import { secondsToFrames } from "../lib/timeline";
import { SceneRenderer } from "../scenes/SceneRenderer";
import type { RenderPlan } from "../schema";

const SceneFrame: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const duration = Math.max(1, secondsToFrames(scene.durationSeconds, fps));
  const edgeFrames = Math.min(18, Math.max(5, Math.round(duration * 0.12)));
  const entering = interpolate(frame, [0, edgeFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const leaving = interpolate(frame, [duration - edgeFrames, duration], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const transition = scene.transitionIn || "dissolve";
  const opacity = transition === "cut" ? 1 : entering * leaving;
  const translateX =
    transition === "slide"
      ? interpolate(entering, [0, 1], [plan.format === "short" ? 90 : 160, 0])
      : 0;
  return (
    <AbsoluteFill style={{ opacity, transform: `translateX(${translateX}px)`, overflow: "hidden" }}>
      <SceneRenderer plan={plan} scene={scene} />
    </AbsoluteFill>
  );
};

export const EditorialVideo: FC<{ plan: RenderPlan }> = ({ plan }) => {
  const { fps } = useVideoConfig();
  return (
    <Backdrop
      background={plan.theme.background}
      surface={plan.theme.surface}
      accent={plan.theme.accent}
      bodyFont={plan.theme.bodyFont}
      headingFont={plan.theme.headingFont}
    >
      <Series>
        {plan.scenes.map((scene) => (
          <Series.Sequence
            key={scene.id}
            offset={secondsToFrames(scene.startSeconds, fps)}
            durationInFrames={secondsToFrames(scene.durationSeconds, fps)}
            layout="none"
          >
            <SceneFrame plan={plan} scene={scene} />
          </Series.Sequence>
        ))}
      </Series>
      {plan.audio ? <Audio src={staticFile(plan.audio.src)} volume={plan.audio.volume} /> : null}
      <ChannelBrand plan={plan} />
      <Captions plan={plan} />
      <AbsoluteFill style={vignetteStyle} />
    </Backdrop>
  );
};
