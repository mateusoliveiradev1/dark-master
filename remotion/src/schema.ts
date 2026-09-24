import { z } from "zod";

const ColorSchema = z.string().regex(/^#[0-9a-f]{6,8}$/i);
const defaultTheme = {
  background: "#0A0A0C",
  surface: "#17171B",
  text: "#F5F5F4",
  muted: "#A1A1AA",
  accent: "#B91C1C",
  headingFont: "Arial",
  bodyFont: "Arial",
  safeArea: { x: 72, y: 54 },
};
const AssetPathSchema = z
  .string()
  .refine(
    (value) => !value.includes("..") && !value.includes("\\") && !/^[a-z]+:/i.test(value),
    "asset path must be relative and portable",
  );

const AssetRefSchema = z.object({
  assetId: z.string().min(1),
  path: AssetPathSchema,
  role: z.string().min(1).default("primary"),
  kind: z.string().default("image"),
  origin: z.string().default("synthetic-or-licensed"),
  rightsStatus: z.string().default("pending"),
  hash: z.string().optional(),
});

const CropPolicySchema = z.object({
  masterAspect: z.string().default("16:9"),
  long: z
    .object({
      focalPoint: z.tuple([z.number(), z.number()]).default([0.5, 0.5]),
      actionSafe: z.array(z.number()).length(4).optional(),
      captionAvoid: z.array(z.number()).length(4).optional(),
    })
    .optional(),
  short: z
    .object({
      focalPoint: z.tuple([z.number(), z.number()]).default([0.5, 0.42]),
      actionSafe: z.array(z.number()).length(4).optional(),
      captionAvoid: z.array(z.number()).length(4).optional(),
      dedicatedReframeRequired: z.boolean().default(false),
    })
    .optional(),
});

const SceneStateSchema = z.object({
  id: z.string().min(1),
  timeRange: z.tuple([z.number().min(0), z.number().min(0).max(1)]),
  intent: z.string().min(1),
  visibleLayers: z.array(z.string()).default([]),
  hiddenLayers: z.array(z.string()).default([]),
  assetIds: z.array(z.string()).default([]),
  motion: z.string().default("drift-with-purpose"),
  focalPoint: z.tuple([z.number(), z.number()]).optional(),
  annotation: z.string().optional(),
});

const SceneSchema = z.object({
  id: z.string().min(1),
  type: z.enum([
    "cinematic-photo",
    "evidence-reveal",
    "evidence-table",
    "investigation-board",
    "timeline",
    "geographic-location",
    "animated-map",
    "document-report",
    "newspaper-archive",
    "portrait-investigation",
    "split-screen",
    "compare-contrast",
    "quote",
    "data-visualization",
    "concept-diagram",
    "chapter-break",
    "object-detail",
    "surveillance-footage",
    "security-camera",
    "timeline-detail",
    "evidence-map",
    "end-card-cta",
    "forensic-reveal",
    "evidence-focus",
    "document-dive",
    "timeline-build",
    "location-sequence",
    "photo-reconstruction",
    "split-evidence",
    "detail-extraction",
    "negative-space-beat",
    "hypothesis-comparator",
    "archive-end-card",
  ]),
  purpose: z.string().default(""),
  startSeconds: z.number().nonnegative(),
  durationSeconds: z.number().positive(),
  sourceBlockIds: z.array(z.string()).default([]),
  claimIds: z.array(z.string()).default([]),
  sourceIds: z.array(z.string()).default([]),
  promptId: z.string().optional(),
  asset: AssetPathSchema.optional(),
  secondaryAsset: AssetPathSchema.optional(),
  assets: z.array(AssetRefSchema).default([]),
  states: z.array(SceneStateSchema).default([]),
  cropPolicy: CropPolicySchema.optional(),
  headline: z.string().default(""),
  body: z.string().default(""),
  metadata: z.record(z.string(), z.string()).default({}),
  motionVariant: z.string().default("drift"),
  motionIntent: z.string().default("purposeful"),
  transitionIn: z.string().default("dissolve"),
  transitionOut: z.string().default("dissolve"),
});

const RenderPlanBaseSchema = z.object({
  version: z.union([z.literal(1), z.literal(2)]).default(2),
  channel: z.string().min(1),
  episode: z.string().min(1),
  format: z.enum(["long", "short"]),
  video: z.object({
    width: z.number().int().positive(),
    height: z.number().int().positive(),
    fps: z.number().int().positive(),
    durationSeconds: z.number().positive(),
  }),
  audio: z
    .object({
      src: AssetPathSchema,
      volume: z.number().min(0).max(2).default(1),
    })
    .optional(),
  captions: z
    .array(
      z.object({
        startSeconds: z.number().nonnegative(),
        endSeconds: z.number().positive(),
        text: z.string().min(1),
        blockId: z.string().optional(),
        claimIds: z.array(z.string()).default([]),
      }),
    )
    .default([]),
  theme: z
    .object({
      background: ColorSchema.default("#0A0A0C"),
      surface: ColorSchema.default("#17171B"),
      text: ColorSchema.default("#F5F5F4"),
      muted: ColorSchema.default("#A1A1AA"),
      accent: ColorSchema.default("#B91C1C"),
      headingFont: z.string().default("Arial"),
      bodyFont: z.string().default("Arial"),
      safeArea: z
        .object({
          x: z.number().nonnegative().default(72),
          y: z.number().nonnegative().default(54),
        })
        .default({ x: 72, y: 54 }),
    })
    .default(defaultTheme),
  visualBible: z.record(z.string(), z.unknown()).optional(),
  render: z
    .object({
      codec: z.enum(["h264", "h265", "vp8", "prores"]).default("h264"),
      audioCodec: z.enum(["aac", "mp3", "opus", "pcm-16"]).default("aac"),
      crf: z.number().int().min(0).max(51).default(18),
      imageFormat: z.enum(["jpeg", "png"]).default("jpeg"),
      jpegQuality: z.number().int().min(1).max(100).default(92),
    })
    .default({ codec: "h264", audioCodec: "aac", crf: 18, imageFormat: "jpeg", jpegQuality: 92 }),
  branding: z
    .object({
      watermark: AssetPathSchema.optional(),
      watermarkOpacity: z.number().min(0).max(1).default(0.32),
      tagline: z.string().default(""),
      endCard: z.string().default("archive-end-card"),
    })
    .default({ watermarkOpacity: 0.32, tagline: "", endCard: "archive-end-card" }),
  contractVersions: z.record(z.string(), z.string()).default({}),
  assetLedger: z.array(AssetRefSchema).default([]),
  scenes: z.array(SceneSchema).min(1),
  sources: z.record(z.string(), z.string()).default({}),
});

export const RenderPlanSchema = RenderPlanBaseSchema.superRefine((plan, context) => {
  const sceneIds = new Set<string>();
  let previousEnd = 0;
  for (const [index, scene] of plan.scenes.entries()) {
    if (sceneIds.has(scene.id)) {
      context.addIssue({
        code: "custom",
        path: ["scenes", index, "id"],
        message: "scene id must be unique",
      });
    }
    sceneIds.add(scene.id);
    if (
      scene.startSeconds > plan.video.durationSeconds ||
      scene.startSeconds + scene.durationSeconds > plan.video.durationSeconds + 0.05
    ) {
      context.addIssue({
        code: "custom",
        path: ["scenes", index],
        message: "scene exceeds video duration",
      });
    }
    if (index > 0 && scene.startSeconds < previousEnd - 0.05) {
      context.addIssue({
        code: "custom",
        path: ["scenes", index, "startSeconds"],
        message: "scene overlap is too large",
      });
    }
    if (index > 0 && scene.startSeconds > previousEnd + 0.05) {
      context.addIssue({
        code: "custom",
        path: ["scenes", index, "startSeconds"],
        message: "scene gap is not allowed",
      });
    }
    for (const [stateIndex, state] of scene.states.entries()) {
      if (state.timeRange[0] >= state.timeRange[1]) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "states", stateIndex, "timeRange"],
          message: "state range must be increasing",
        });
      }
    }
    if (scene.states.length > 0) {
      const first = scene.states[0].timeRange[0];
      const last = scene.states[scene.states.length - 1].timeRange[1];
      if (Math.abs(first) > 0.01 || Math.abs(last - 1) > 0.01) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "states"],
          message: "state timeline must cover 0 to 1",
        });
      }
    }
    previousEnd = Math.max(previousEnd, scene.startSeconds + scene.durationSeconds);
  }
  for (const [index, caption] of plan.captions.entries()) {
    if (caption.startSeconds < 0 || caption.endSeconds > plan.video.durationSeconds + 0.05) {
      context.addIssue({
        code: "custom",
        path: ["captions", index],
        message: "caption exceeds video duration",
      });
    }
    if (caption.endSeconds <= caption.startSeconds) {
      context.addIssue({
        code: "custom",
        path: ["captions", index],
        message: "caption must have positive duration",
      });
    }
  }
});

export type RenderPlan = z.infer<typeof RenderPlanSchema>;

export const CompositionSchema = z.object({ plan: RenderPlanSchema });
export type CompositionProps = z.infer<typeof CompositionSchema>;

export const defaultRenderPlan: RenderPlan = {
  version: 2,
  channel: "fixture",
  episode: "video01",
  format: "long",
  video: { width: 1920, height: 1080, fps: 30, durationSeconds: 8 },
  theme: { ...defaultTheme, safeArea: { x: 72, y: 54 } },
  captions: [
    { startSeconds: 0, endSeconds: 2.4, text: "A primeira pergunta aparece.", claimIds: [] },
    { startSeconds: 2.4, endSeconds: 5.2, text: "A evidência muda o caminho.", claimIds: [] },
    { startSeconds: 5.2, endSeconds: 8, text: "O arquivo ainda tem uma resposta.", claimIds: [] },
  ],
  render: { codec: "h264", audioCodec: "aac", crf: 18, imageFormat: "jpeg", jpegQuality: 92 },
  branding: { watermarkOpacity: 0.32, tagline: "", endCard: "archive-end-card" },
  contractVersions: {},
  assetLedger: [],
  scenes: [
    {
      id: "scene-01",
      type: "cinematic-photo",
      purpose: "hook",
      startSeconds: 0,
      durationSeconds: 2.8,
      sourceBlockIds: ["B001"],
      claimIds: [],
      sourceIds: [],
      assets: [],
      headline: "O detalhe impossível",
      body: "A história começa antes da resposta.",
      motionVariant: "push-in",
      motionIntent: "establish the contradiction",
      transitionIn: "dissolve",
      transitionOut: "dissolve",
      states: [
        {
          id: "entry",
          timeRange: [0, 0.2],
          intent: "entry",
          visibleLayers: ["background"],
          hiddenLayers: [],
          assetIds: [],
          motion: "slow-spatial-entry",
        },
        {
          id: "focus",
          timeRange: [0.2, 0.7],
          intent: "focus",
          visibleLayers: ["background", "evidence"],
          hiddenLayers: [],
          assetIds: [],
          motion: "controlled-crop",
        },
        {
          id: "exit",
          timeRange: [0.7, 1],
          intent: "exit",
          visibleLayers: ["background", "evidence"],
          hiddenLayers: [],
          assetIds: [],
          motion: "hold-and-transition",
        },
      ],
      metadata: { label: "COLD OPEN" },
    },
    {
      id: "scene-02",
      type: "evidence-reveal",
      purpose: "evidence",
      startSeconds: 2.8,
      durationSeconds: 2.6,
      sourceBlockIds: ["B002"],
      claimIds: [],
      sourceIds: [],
      assets: [],
      headline: "A prova muda o caso",
      body: "A mesma evidência, outra leitura.",
      motionVariant: "track-left",
      motionIntent: "move focus to the evidence",
      transitionIn: "dissolve",
      transitionOut: "dissolve",
      states: [
        {
          id: "entry",
          timeRange: [0, 0.2],
          intent: "entry",
          visibleLayers: ["background"],
          hiddenLayers: [],
          assetIds: [],
          motion: "slow-spatial-entry",
        },
        {
          id: "focus",
          timeRange: [0.2, 0.7],
          intent: "focus",
          visibleLayers: ["background", "evidence"],
          hiddenLayers: [],
          assetIds: [],
          motion: "detail-reveal",
        },
        {
          id: "exit",
          timeRange: [0.7, 1],
          intent: "exit",
          visibleLayers: ["evidence"],
          hiddenLayers: [],
          assetIds: [],
          motion: "hold-and-transition",
        },
      ],
      metadata: { label: "EVIDÊNCIA" },
    },
    {
      id: "scene-03",
      type: "timeline",
      purpose: "context",
      startSeconds: 5.4,
      durationSeconds: 2.6,
      sourceBlockIds: ["B003"],
      claimIds: [],
      sourceIds: [],
      assets: [],
      headline: "O tempo reorganiza tudo",
      body: "A sequência revela a mudança de estado.",
      motionVariant: "timeline",
      motionIntent: "build the relationship between events",
      transitionIn: "dissolve",
      transitionOut: "dissolve",
      states: [
        {
          id: "entry",
          timeRange: [0, 0.2],
          intent: "entry",
          visibleLayers: ["background"],
          hiddenLayers: [],
          assetIds: [],
          motion: "slow-spatial-entry",
        },
        {
          id: "focus",
          timeRange: [0.2, 0.7],
          intent: "focus",
          visibleLayers: ["timeline"],
          hiddenLayers: [],
          assetIds: [],
          motion: "line-drawing",
        },
        {
          id: "exit",
          timeRange: [0.7, 1],
          intent: "exit",
          visibleLayers: ["timeline"],
          hiddenLayers: [],
          assetIds: [],
          motion: "hold-and-transition",
        },
      ],
      metadata: { label: "CONTEXTO" },
    },
  ],
  sources: {},
};
