import { Audio } from "@remotion/media";
import type { FC } from "react";
import { AbsoluteFill, Series, staticFile, useVideoConfig } from "remotion";
import { ChannelBrand } from "../components/Brand";
import { Captions } from "../components/Captions";
import { Backdrop, vignetteStyle } from "../components/Frame";
import { secondsToFrames } from "../lib/timeline";
import { SceneRenderer } from "../scenes/SceneRenderer";
import type { RenderPlan } from "../schema";

export const EditorialVideo: FC<{ plan: RenderPlan }> = ({ plan }) => {
  const { fps } = useVideoConfig();
  return (
    <Backdrop
      background={plan.theme.background}
      surface={plan.theme.surface}
      accent={plan.theme.accent}
    >
      <Series>
        {plan.scenes.map((scene) => (
          <Series.Sequence
            key={scene.id}
            offset={secondsToFrames(scene.startSeconds, fps)}
            durationInFrames={secondsToFrames(scene.durationSeconds, fps)}
            layout="none"
          >
            <SceneRenderer plan={plan} scene={scene} />
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
