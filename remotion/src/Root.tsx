import type { FC } from "react";
import type { CalculateMetadataFunction } from "remotion";
import { Composition } from "remotion";

import { EditorialVideo } from "./compositions/EditorialVideo";
import {
  type CompositionProps,
  CompositionSchema,
  defaultRenderPlan,
  type RenderPlan,
} from "./schema";

const calculateMetadata: CalculateMetadataFunction<CompositionProps> = ({ props }) => ({
  durationInFrames: Math.max(
    1,
    Math.round(props.plan.video.durationSeconds * props.plan.video.fps),
  ),
  width: props.plan.video.width,
  height: props.plan.video.height,
  fps: props.plan.video.fps,
});

const defaultShortPlan: RenderPlan = {
  ...defaultRenderPlan,
  format: "short",
  video: { width: 1080, height: 1920, fps: 30, durationSeconds: 8 },
  scenes: defaultRenderPlan.scenes.map((scene) => ({
    ...scene,
    durationSeconds: scene.durationSeconds / 2,
  })),
};

export const Root: FC = () => (
  <>
    <Composition
      id="DarkMasterLong"
      component={EditorialVideo}
      durationInFrames={240}
      fps={30}
      width={1920}
      height={1080}
      schema={CompositionSchema}
      defaultProps={{ plan: defaultRenderPlan }}
      calculateMetadata={calculateMetadata}
    />
    <Composition
      id="DarkMasterShort"
      component={EditorialVideo}
      durationInFrames={240}
      fps={30}
      width={1080}
      height={1920}
      schema={CompositionSchema}
      defaultProps={{ plan: defaultShortPlan }}
      calculateMetadata={calculateMetadata}
    />
  </>
);
