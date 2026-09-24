import { z } from "zod";

export const MOTION_OPERATORS = [
  "static-hold",
  "slow-push",
  "lateral-drift",
  "crop-shift",
  "detail-inspection",
  "controlled-crop",
  "pull-out",
  "masked-reveal",
  "line-draw",
  "timeline-build",
  "route-draw",
  "document-dive",
  "evidence-lens",
  "parallax",
  "match-cut",
  "luminance-dissolve",
  "negative-space-pullout",
  "archive-title-object",
  "typewriter-interference",
] as const;

export type MotionOperator = (typeof MOTION_OPERATORS)[number];
export const MotionOperatorSchema = z.enum(MOTION_OPERATORS);

const MOTION_ALIASES = {
  "archive-title": "archive-title-object",
  "archive-title-object": "archive-title-object",
  "controlled-crop": "controlled-crop",
  "crop-shift": "crop-shift",
  "detail-inspection": "detail-inspection",
  "detail-reveal": "detail-inspection",
  "document-dive": "document-dive",
  drift: "lateral-drift",
  "drift-with-purpose": "lateral-drift",
  "evidence-lens": "evidence-lens",
  fade: "static-hold",
  hold: "static-hold",
  "hold-and-transition": "static-hold",
  "lateral-drift": "lateral-drift",
  "line-draw": "line-draw",
  "line-drawing": "line-draw",
  "luminance-dissolve": "luminance-dissolve",
  "match-cut": "match-cut",
  "masked-reveal": "masked-reveal",
  "negative-space": "negative-space-pullout",
  "negative-space-pullout": "negative-space-pullout",
  parallax: "parallax",
  "pull-out": "pull-out",
  "push-in": "slow-push",
  route: "route-draw",
  "route-draw": "route-draw",
  "slow-push": "slow-push",
  "slow-spatial-entry": "slow-push",
  "static-hold": "static-hold",
  timeline: "timeline-build",
  "timeline-build": "timeline-build",
  "track-left": "lateral-drift",
  "track-right": "lateral-drift",
  typewriter: "typewriter-interference",
  "typewriter-interference": "typewriter-interference",
} as const satisfies Record<string, MotionOperator>;

export const normalizeMotionOperator = (
  value: string | null | undefined,
): MotionOperator | null => {
  if (!value) return null;
  const token = value.trim().toLowerCase().replaceAll("_", "-");
  return MOTION_ALIASES[token as keyof typeof MOTION_ALIASES] ?? null;
};

export const isKnownMotionToken = (value: string | null | undefined): boolean =>
  normalizeMotionOperator(value) !== null;
export const MotionTokenSchema = z.string().min(1).refine(isKnownMotionToken, {
  message: "motion must resolve to a declared operator",
});

const CAMERA_ONLY_MOTION = new Set<MotionOperator>([
  "slow-push",
  "lateral-drift",
  "crop-shift",
  "detail-inspection",
  "controlled-crop",
  "pull-out",
  "negative-space-pullout",
  "archive-title-object",
  "match-cut",
]);

const isCameraOnlyMotion = (value: string | null | undefined): boolean => {
  const operator = normalizeMotionOperator(value);
  return operator === null || CAMERA_ONLY_MOTION.has(operator);
};

export const SCENE_TYPES = [
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
] as const;

export type SceneType = (typeof SCENE_TYPES)[number];
export const SceneTypeSchema = z.enum(SCENE_TYPES);

export const TRANSITION_KINDS = [
  "cut",
  "hold",
  "none",
  "dissolve",
  "fade",
  "slide",
  "wipe",
  "match-cut",
  "luminance-dissolve",
] as const;

export type TransitionKind = (typeof TRANSITION_KINDS)[number];
export const TransitionKindSchema = z.enum(TRANSITION_KINDS);
export const normalizeTransitionKind = (
  value: string | null | undefined,
): TransitionKind | null => {
  if (!value) return null;
  const token = value.trim().toLowerCase().replaceAll("_", "-");
  return TransitionKindSchema.safeParse(token).success ? (token as TransitionKind) : null;
};
export const TransitionTokenSchema = z
  .string()
  .min(1)
  .refine((value) => normalizeTransitionKind(value) !== null, {
    message: "transition must be a declared transition kind",
  });

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
    (value) =>
      !value.includes("..") &&
      !value.includes("\\") &&
      !/^[a-z]+:/i.test(value) &&
      !value.startsWith("/"),
    "asset path must be relative and portable",
  );

export const AssetRefSchema = z.object({
  assetId: z.string().min(1),
  promptId: z.string().optional(),
  shotId: z.string().optional(),
  path: AssetPathSchema,
  role: z.string().min(1).default("primary"),
  layer: z.string().min(1).optional(),
  kind: z.string().default("image"),
  origin: z.string().default("synthetic-or-licensed"),
  rightsStatus: z.string().default("pending"),
  hash: z.string().nullable().optional(),
  blocked: z.boolean().default(false),
  sourceBlockIds: z.array(z.string()).default([]),
});

export const CropPolicySchema = z.object({
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

const SafeAreasSchema = z.record(z.string(), z.record(z.string(), z.array(z.number()).length(4)));

export const CompositionContractSchema = z.object({
  description: z.string().default(""),
  focalPoint: z.tuple([z.number(), z.number()]),
  shotScale: z.string().default(""),
  camera: z.string().default(""),
  lighting: z.string().default(""),
});

export const ImagePromptSchema = z.object({
  contractVersion: z.literal(1),
  promptId: z.string().min(1),
  shotId: z.string().min(1),
  purpose: z.string().min(1),
  question: z.string().min(1),
  stateChange: z.string().min(1),
  classification: z.string().min(1),
  subject: z.string().min(1),
  setting: z.string().min(1),
  composition: CompositionContractSchema,
  layers: z.array(z.string().min(1)).min(1),
  cropPolicy: CropPolicySchema,
  safeAreas: SafeAreasSchema,
  continuity: z.record(z.string(), z.unknown()),
  negativeGuards: z.array(z.string().min(1)).min(1),
  full: z.string().min(1),
});

export const MotionPromptStateSchema = z.object({
  id: z.string().min(1),
  timeRange: z.tuple([z.number().min(0), z.number().min(0).max(100)]),
  intent: z.string().min(1),
  visibleLayers: z.array(z.string().min(1)).min(1),
  hiddenLayers: z.array(z.string().min(1)).optional(),
  assetIds: z.array(z.string().min(1)).optional(),
  focalPoint: z.tuple([z.number(), z.number()]).optional(),
  annotation: z.string().optional(),
  motion: MotionTokenSchema,
  transition: TransitionTokenSchema,
  audioCue: z.string().min(1),
  intensity: z.number().min(0).max(4).optional(),
});

export const MotionPromptSchema = z.object({
  contractVersion: z.literal(1),
  promptId: z.string().min(1),
  shotId: z.string().min(1),
  intensity: z.number().int().min(0).max(4),
  layers: z.array(z.string().min(1)).min(1),
  states: z.array(MotionPromptStateSchema).min(1),
  cameraPath: z.object({
    kind: MotionTokenSchema,
    description: z.string().min(1),
    keyframes: z
      .array(
        z.object({
          at: z.number().min(0).max(100),
          focalPoint: z.tuple([z.number(), z.number()]),
        }),
      )
      .default([]),
  }),
  cropPolicy: CropPolicySchema,
  transitions: z.object({
    in: TransitionTokenSchema,
    out: TransitionTokenSchema,
    rationale: z.string().min(1),
    durationSeconds: z.number().positive().max(3).optional(),
  }),
  audioCues: z.array(z.string().min(1)).min(1),
  staticException: z.object({
    allowed: z.boolean(),
    reason: z.string().min(1),
  }),
  negativeMotion: z.array(z.string().min(1)).min(1),
  full: z.string().min(1),
});

export const SceneStateSchema = z.object({
  id: z.string().min(1),
  timeRange: z.tuple([z.number().min(0), z.number().min(0).max(1)]),
  intent: z.string().min(1),
  visibleLayers: z.array(z.string()).default([]),
  hiddenLayers: z.array(z.string()).default([]),
  assetIds: z.array(z.string()).default([]),
  motion: MotionTokenSchema.default("drift-with-purpose"),
  focalPoint: z.tuple([z.number(), z.number()]).optional(),
  annotation: z.string().optional(),
});

export const SceneSchema = z.object({
  id: z.string().min(1),
  shotId: z.string().optional(),
  type: z.enum(SCENE_TYPES),
  purpose: z.string().default(""),
  question: z.string().default(""),
  stateChange: z.string().default(""),
  classification: z.string().default(""),
  subject: z.string().default(""),
  setting: z.string().default(""),
  composition: z.union([z.string(), CompositionContractSchema]).default(""),
  layers: z.array(z.string()).default([]),
  startSeconds: z.number().nonnegative(),
  durationSeconds: z.number().positive(),
  sourceBlockIds: z.array(z.string()).default([]),
  claimIds: z.array(z.string()).default([]),
  sourceIds: z.array(z.string()).default([]),
  promptId: z.string().optional(),
  safeAreas: SafeAreasSchema.default({}),
  negativeGuards: z.array(z.string()).default([]),
  continuity: z.record(z.string(), z.unknown()).default({}),
  imagePrompt: ImagePromptSchema.optional(),
  motionPrompt: MotionPromptSchema.optional(),
  asset: AssetPathSchema.optional(),
  secondaryAsset: AssetPathSchema.optional(),
  assets: z.array(AssetRefSchema).default([]),
  states: z.array(SceneStateSchema).default([]),
  cropPolicy: CropPolicySchema.optional(),
  headline: z.string().default(""),
  body: z.string().default(""),
  metadata: z.record(z.string(), z.string()).default({}),
  motionVariant: MotionTokenSchema.default("drift"),
  motionIntent: z.string().default("purposeful"),
  transitionIn: TransitionTokenSchema.default("cut"),
  transitionOut: TransitionTokenSchema.default("cut"),
  transitionDurationSeconds: z.number().positive().max(3).optional(),
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
  blockedAssetIds: z.array(z.string()).default([]),
  scenes: z.array(SceneSchema).min(1),
  sources: z.record(z.string(), z.string()).default({}),
});

export const RenderPlanSchema = RenderPlanBaseSchema.superRefine((plan, context) => {
  const sceneIds = new Set<string>();
  const promptIds = new Set<string>();
  const v2RequiredFields = [
    "shotId",
    "promptId",
    "sourceBlockIds",
    "claimIds",
    "sourceIds",
    "purpose",
    "question",
    "stateChange",
    "classification",
    "subject",
    "setting",
    "composition",
    "layers",
    "cropPolicy",
    "safeAreas",
    "negativeGuards",
    "continuity",
    "states",
  ] as const;
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
    if (plan.version === 2) {
      for (const field of v2RequiredFields) {
        const value = scene[field] as unknown;
        const empty =
          value === undefined ||
          value === null ||
          value === "" ||
          (Array.isArray(value) && value.length === 0) ||
          (typeof value === "object" && !Array.isArray(value) && Object.keys(value).length === 0);
        if (empty) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, field],
            message: `${field} is required for render plan v2`,
          });
        }
      }
      if (scene.shotId !== scene.id) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "shotId"],
          message: "shotId must match scene id",
        });
      }
      if (!scene.promptId || promptIds.has(scene.promptId)) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "promptId"],
          message: "promptId must be present and unique",
        });
      }
      if (scene.promptId) promptIds.add(scene.promptId);
      if (!scene.imagePrompt || !scene.motionPrompt) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index],
          message: "image and motion prompt contracts are required for render plan v2",
        });
      } else {
        if (
          scene.imagePrompt.promptId !== scene.promptId ||
          scene.imagePrompt.shotId !== scene.shotId
        ) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "imagePrompt"],
            message: "image prompt identity does not match scene",
          });
        }
        if (!scene.imagePrompt.full.toLowerCase().includes("no baked-in text")) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "imagePrompt", "full"],
            message: "image prompt must forbid baked-in text",
          });
        }
        if (
          scene.motionPrompt.promptId !== scene.promptId ||
          scene.motionPrompt.shotId !== scene.shotId
        ) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "motionPrompt"],
            message: "motion prompt identity does not match scene",
          });
        }
        const firstMotionState = scene.motionPrompt.states[0];
        const lastMotionState = scene.motionPrompt.states[scene.motionPrompt.states.length - 1];
        if (
          !firstMotionState ||
          !lastMotionState ||
          firstMotionState.timeRange[0] !== 0 ||
          lastMotionState.timeRange[1] !== 100
        ) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "motionPrompt", "states"],
            message: "motion states must cover 0 to 100",
          });
        }
        if (
          !scene.motionPrompt.cameraPath.description.includes(scene.subject) ||
          !scene.motionPrompt.cameraPath.description.includes(scene.stateChange)
        ) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "motionPrompt", "cameraPath"],
            message: "camera path must be bound to subject and state change",
          });
        }
        if (!isKnownMotionToken(scene.motionVariant)) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "motionVariant"],
            message: "motionVariant must resolve to a declared operator",
          });
        }
        const transitionValues = [
          ["transitionIn", scene.transitionIn],
          ["transitionOut", scene.transitionOut],
          ["motionPrompt.transitions.in", scene.motionPrompt.transitions.in],
          ["motionPrompt.transitions.out", scene.motionPrompt.transitions.out],
        ] as const;
        for (const [field, value] of transitionValues) {
          if (!normalizeTransitionKind(value)) {
            context.addIssue({
              code: "custom",
              path: ["scenes", index, ...field.split(".")],
              message: "transition must be a declared transition kind",
            });
          }
        }
        if (!isKnownMotionToken(scene.motionPrompt.cameraPath.kind)) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "motionPrompt", "cameraPath", "kind"],
            message: "camera path kind must resolve to a declared operator",
          });
        }
        let previousMotionEnd = 0;
        for (const [motionStateIndex, motionState] of scene.motionPrompt.states.entries()) {
          if (!isKnownMotionToken(motionState.motion)) {
            context.addIssue({
              code: "custom",
              path: ["scenes", index, "motionPrompt", "states", motionStateIndex, "motion"],
              message: "motion state must resolve to a declared operator",
            });
          }
          if (motionState.timeRange[0] < previousMotionEnd - 0.01) {
            context.addIssue({
              code: "custom",
              path: ["scenes", index, "motionPrompt", "states", motionStateIndex, "timeRange"],
              message: "motion states cannot overlap",
            });
          }
          if (motionState.timeRange[0] > previousMotionEnd + 0.01) {
            context.addIssue({
              code: "custom",
              path: ["scenes", index, "motionPrompt", "states", motionStateIndex, "timeRange"],
              message: "motion states cannot have gaps",
            });
          }
          previousMotionEnd = motionState.timeRange[1];
        }
        if (
          !scene.motionPrompt.staticException.allowed &&
          scene.motionPrompt.states.every((motionState) => isCameraOnlyMotion(motionState.motion))
        ) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "motionPrompt", "staticException"],
            message: "non-static scenes require at least one semantic motion operator",
          });
        }
      }
      for (const [stateIndex, state] of scene.states.entries()) {
        if (!isKnownMotionToken(state.motion)) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "states", stateIndex, "motion"],
            message: "scene state must resolve to a declared operator",
          });
        }
        for (const [assetIdIndex, assetId] of state.assetIds.entries()) {
          const asset =
            scene.assets.find((candidate) => candidate.assetId === assetId) ??
            plan.assetLedger.find(
              (candidate) =>
                candidate.assetId === assetId &&
                candidate.promptId === scene.promptId &&
                candidate.shotId === scene.shotId,
            );
          if (!asset || asset.blocked || plan.blockedAssetIds.includes(assetId)) {
            context.addIssue({
              code: "custom",
              path: ["scenes", index, "states", stateIndex, "assetIds", assetIdIndex],
              message: "state assetId must resolve to an unblocked scene asset",
            });
          }
        }
      }
      for (const [assetIndex, asset] of scene.assets.entries()) {
        if (
          asset.promptId !== scene.promptId ||
          asset.shotId !== scene.shotId ||
          asset.blocked ||
          plan.blockedAssetIds.includes(asset.assetId)
        ) {
          context.addIssue({
            code: "custom",
            path: ["scenes", index, "assets", assetIndex],
            message: "asset identity must match scene and blocked assets cannot render",
          });
        }
      }
    }
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
    if (plan.version === 2 && index === 0 && scene.startSeconds > 0.05) {
      context.addIssue({
        code: "custom",
        path: ["scenes", index, "startSeconds"],
        message: "v2 scenes cannot start after a leading timeline gap",
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
    let previousStateEnd = 0;
    for (const [stateIndex, state] of scene.states.entries()) {
      if (state.timeRange[0] >= state.timeRange[1]) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "states", stateIndex, "timeRange"],
          message: "state range must be increasing",
        });
      }
      if (state.timeRange[0] < previousStateEnd - 0.01) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "states", stateIndex, "timeRange"],
          message: "state timeline cannot overlap",
        });
      }
      if (state.timeRange[0] > previousStateEnd + 0.01 && stateIndex > 0) {
        context.addIssue({
          code: "custom",
          path: ["scenes", index, "states", stateIndex, "timeRange"],
          message: "state timeline cannot have gaps",
        });
      }
      previousStateEnd = state.timeRange[1];
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
  if (plan.version === 2) {
    for (const [index, asset] of plan.assetLedger.entries()) {
      if (asset.blocked || !asset.promptId || !asset.shotId) {
        context.addIssue({
          code: "custom",
          path: ["assetLedger", index],
          message: "render plan v2 assets require identity and cannot be blocked",
        });
      }
    }
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

export type AssetRef = z.infer<typeof AssetRefSchema>;
export type CropPolicy = z.infer<typeof CropPolicySchema>;
export type ImagePrompt = z.infer<typeof ImagePromptSchema>;
export type MotionPrompt = z.infer<typeof MotionPromptSchema>;
export type MotionPromptState = z.infer<typeof MotionPromptStateSchema>;
export type SceneState = z.infer<typeof SceneStateSchema>;
export type Scene = z.infer<typeof SceneSchema>;
export type RenderPlan = z.infer<typeof RenderPlanSchema>;

export const CompositionSchema = z.object({ plan: RenderPlanSchema });
export type CompositionProps = z.infer<typeof CompositionSchema>;

const defaultCropPolicy: z.infer<typeof CropPolicySchema> = {
  masterAspect: "16:9",
  long: {
    focalPoint: [0.5, 0.5],
    actionSafe: [0.05, 0.05, 0.9, 0.78],
    captionAvoid: [0.06, 0.78, 0.88, 0.16],
  },
  short: {
    focalPoint: [0.5, 0.42],
    actionSafe: [0.1, 0.1, 0.8, 0.72],
    captionAvoid: [0.08, 0.78, 0.84, 0.16],
    dedicatedReframeRequired: true,
  },
};

const defaultSafeAreas = {
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

const defaultSceneContract = (
  shotId: string,
  promptId: string,
  sourceBlockId: string,
  claimId: string,
  sourceId: string,
  question: string,
  stateChange: string,
  classification: string,
  subject: string,
  setting: string,
  purpose: string,
) => {
  const layers = ["environment", "subject", "state-change", "continuity"];
  const composition = `${subject} arranged to make ${stateChange} visible`;
  const continuity = {
    palette: { background: "#0A0A0C", accent: "#B91C1C" },
    era: "documented case chronology",
    geography: setting,
    evidenceTreatment: classification,
  };
  const negativeGuards = [
    "no baked-in text",
    "no watermark",
    "no unsupported factual detail",
    "no gore",
  ];
  return {
    shotId,
    promptId,
    sourceBlockIds: [sourceBlockId],
    claimIds: [claimId],
    sourceIds: [sourceId],
    purpose,
    question,
    stateChange,
    classification,
    subject,
    setting,
    composition,
    layers,
    cropPolicy: defaultCropPolicy,
    safeAreas: defaultSafeAreas,
    negativeGuards,
    continuity,
    imagePrompt: {
      contractVersion: 1 as const,
      promptId,
      shotId,
      purpose,
      question,
      stateChange,
      classification,
      subject,
      setting,
      composition: {
        description: composition,
        focalPoint: [0.5, 0.45] as [number, number],
        shotScale: "case-specific documentary scale",
        camera: "purposeful case-bound camera position",
        lighting: "motivated low-key documentary light",
      },
      layers,
      cropPolicy: defaultCropPolicy,
      safeAreas: defaultSafeAreas,
      continuity,
      negativeGuards,
      full: `IMAGE_PROMPT[${promptId}/${shotId}] | Editorial purpose: ${purpose} | Scene question: ${question} | State change: ${stateChange} | Classification: ${classification} | Subject: ${subject} | Setting: ${setting} | Composition: ${composition} | Focal point: 0.5,0.45 | Crop: 16:9 master | Safe areas: long and short declared | Continuity: case-bound palette, era and geography | Negative guards: ${negativeGuards.join("; ")} | Output: 16:9; no baked-in text.`,
    },
    motionPrompt: {
      contractVersion: 1 as const,
      promptId,
      shotId,
      intensity: classification === "HIPOTESE" ? 3 : 2,
      layers,
      states: [
        {
          id: "entry",
          timeRange: [0, 20] as [number, number],
          intent: `establish ${subject}`,
          visibleLayers: layers,
          motion: "slow-spatial-entry",
          transition: "hold",
          audioCue: `low emphasis before ${question}`,
        },
        {
          id: "focus",
          timeRange: [20, 80] as [number, number],
          intent: `make ${stateChange} legible`,
          visibleLayers: layers,
          motion: "controlled-crop",
          transition: "hold",
          audioCue: `evidence texture resolves at ${stateChange}`,
        },
        {
          id: "exit",
          timeRange: [80, 100] as [number, number],
          intent: `preserve ${stateChange} for the next scene`,
          visibleLayers: layers,
          motion: "hold-and-transition",
          transition: "hold",
          audioCue: `low cut aligned to ${question}`,
        },
      ],
      cameraPath: {
        kind: "controlled-crop",
        description: `Start on ${subject}; move only to make ${stateChange} legible while answering ${question}.`,
        keyframes: [
          { at: 0, focalPoint: [0.5, 0.45] as [number, number] },
          { at: 50, focalPoint: [0.5, 0.44] as [number, number] },
          { at: 100, focalPoint: [0.5, 0.45] as [number, number] },
        ],
      },
      cropPolicy: defaultCropPolicy,
      transitions: {
        in: "cut",
        out: "cut",
        rationale: `transition only after ${stateChange} resolves ${question}`,
      },
      audioCues: [`low emphasis at ${stateChange}`, `quiet resolve for ${question}`],
      staticException: {
        allowed: false,
        reason: `${stateChange} must remain visibly distinct`,
      },
      negativeMotion: [
        "no generic zoom used as the only motion",
        "no generic fade used as the only transition",
        "no random parallax",
      ],
      full: `MOTION_PROMPT[${promptId}/${shotId}] | Intensity 2/4 | States 0-100 | Camera path bound to ${subject} and ${stateChange} | Case-specific crop and transition | Audio cues and static exception declared | Negative motion enforced.`,
    },
  };
};

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
  blockedAssetIds: [],
  scenes: [
    {
      ...defaultSceneContract(
        "scene-01",
        "prompt-scene-01",
        "B001",
        "C001",
        "S001",
        "O que torna o detalhe impossível?",
        "A contradição entra no enquadramento.",
        "FATO",
        "um detalhe de arquivo sem texto legível",
        "sala de arquivo documentada no caso",
        "estabelecer a contradição",
      ),
      id: "scene-01",
      type: "cinematic-photo",
      purpose: "hook",
      startSeconds: 0,
      durationSeconds: 2.8,
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
      ...defaultSceneContract(
        "scene-02",
        "prompt-scene-02",
        "B002",
        "C002",
        "S002",
        "Qual prova muda a leitura?",
        "A mesma evidência recebe outra interpretação.",
        "REPORTADO",
        "a evidência isolada sobre a mesa",
        "laboratório linked ao caso",
        "revelar a mudança de leitura",
      ),
      id: "scene-02",
      type: "evidence-reveal",
      purpose: "evidence",
      startSeconds: 2.8,
      durationSeconds: 2.6,
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
      ...defaultSceneContract(
        "scene-03",
        "prompt-scene-03",
        "B003",
        "C003",
        "S003",
        "Como o tempo reorganiza a prova?",
        "A sequência temporal altera a hierarquia dos eventos.",
        "FATO",
        "a linha do tempo materializada por objetos do caso",
        "arquivo cronológico ligado à pesquisa",
        "construir a relação temporal",
      ),
      id: "scene-03",
      type: "timeline",
      purpose: "context",
      startSeconds: 5.4,
      durationSeconds: 2.6,
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
