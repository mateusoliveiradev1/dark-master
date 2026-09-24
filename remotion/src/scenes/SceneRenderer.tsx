import type { FC } from "react";

import { VisualError } from "../components/VisualError";
import type { RenderPlan } from "../schema";
import {
  ChapterBreak,
  Comparison,
  DataVisualization,
  Diagram,
  Document,
  EndCardScene,
  Portrait,
  Quote,
  Surveillance,
} from "./ArchiveScenes";
import {
  CinematicPhoto,
  EvidenceReveal,
  EvidenceTable,
  InvestigationBoard,
  Location,
  MapScene,
  Timeline,
} from "./EditorialScenes";

const UnknownScene: FC<{ scene: RenderPlan["scenes"][number] }> = ({ scene }) => (
  <VisualError sceneId={scene.id} errors={[`unknown scene type: ${String(scene.type)}`]} />
);

export const SceneRenderer: FC<{ plan: RenderPlan; scene: RenderPlan["scenes"][number] }> = ({
  plan,
  scene,
}) => {
  switch (scene.type) {
    case "cinematic-photo":
    case "photo-reconstruction":
      return <CinematicPhoto plan={plan} scene={scene} />;
    case "evidence-reveal":
    case "forensic-reveal":
    case "evidence-focus":
      return <EvidenceReveal plan={plan} scene={scene} />;
    case "evidence-table":
      return <EvidenceTable plan={plan} scene={scene} />;
    case "investigation-board":
      return <InvestigationBoard plan={plan} scene={scene} />;
    case "timeline":
    case "timeline-detail":
    case "timeline-build":
      return <Timeline plan={plan} scene={scene} />;
    case "geographic-location":
    case "location-sequence":
      return <Location plan={plan} scene={scene} />;
    case "animated-map":
    case "evidence-map":
      return <MapScene plan={plan} scene={scene} />;
    case "document-report":
    case "newspaper-archive":
    case "document-dive":
      return <Document plan={plan} scene={scene} />;
    case "portrait-investigation":
    case "object-detail":
    case "detail-extraction":
      return <Portrait plan={plan} scene={scene} />;
    case "split-screen":
    case "compare-contrast":
    case "split-evidence":
    case "hypothesis-comparator":
      return <Comparison plan={plan} scene={scene} />;
    case "quote":
      return <Quote plan={plan} scene={scene} />;
    case "data-visualization":
      return <DataVisualization plan={plan} scene={scene} />;
    case "concept-diagram":
      return <Diagram plan={plan} scene={scene} />;
    case "chapter-break":
    case "negative-space-beat":
      return <ChapterBreak plan={plan} scene={scene} />;
    case "surveillance-footage":
    case "security-camera":
      return <Surveillance plan={plan} scene={scene} />;
    case "end-card-cta":
    case "archive-end-card":
      return <EndCardScene plan={plan} scene={scene} />;
    default:
      return <UnknownScene scene={scene} />;
  }
};
