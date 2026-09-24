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

export const RenderPlanSchema = z.object({
  version: z.literal(1),
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
      src: z.string().min(1),
      volume: z.number().min(0).max(2).default(1),
    })
    .optional(),
  captions: z
    .array(
      z.object({
        startSeconds: z.number().nonnegative(),
        endSeconds: z.number().positive(),
        text: z.string().min(1),
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
  scenes: z
    .array(
      z.object({
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
        ]),
        purpose: z.string().default(""),
        startSeconds: z.number().nonnegative(),
        durationSeconds: z.number().positive(),
        sourceBlockIds: z.array(z.string()).default([]),
        asset: AssetPathSchema.optional(),
        secondaryAsset: AssetPathSchema.optional(),
        headline: z.string().default(""),
        body: z.string().default(""),
        metadata: z.record(z.string(), z.string()).default({}),
        motionVariant: z.string().default("drift"),
        transitionIn: z.string().default("fade"),
        transitionOut: z.string().default("fade"),
      }),
    )
    .min(1),
  sources: z.record(z.string(), z.string()).default({}),
});

export type RenderPlan = z.infer<typeof RenderPlanSchema>;

export const CompositionSchema = z.object({ plan: RenderPlanSchema });
export type CompositionProps = z.infer<typeof CompositionSchema>;

export const defaultRenderPlan: RenderPlan = {
  version: 1,
  channel: "fixture",
  episode: "video01",
  format: "long",
  video: {
    width: 1920,
    height: 1080,
    fps: 30,
    durationSeconds: 8,
  },
  theme: {
    background: "#0A0A0C",
    surface: "#17171B",
    text: "#F5F5F4",
    muted: "#A1A1AA",
    accent: "#B91C1C",
    headingFont: "Arial",
    bodyFont: "Arial",
    safeArea: { x: 72, y: 54 },
  },
  captions: [
    { startSeconds: 0, endSeconds: 2.4, text: "A primeira pergunta aparece." },
    { startSeconds: 2.4, endSeconds: 5.2, text: "A evidência muda o caminho." },
    { startSeconds: 5.2, endSeconds: 8, text: "O arquivo ainda tem uma resposta." },
  ],
  scenes: [
    {
      id: "scene-01",
      type: "cinematic-photo",
      purpose: "hook",
      startSeconds: 0,
      durationSeconds: 2.8,
      sourceBlockIds: ["B001"],
      headline: "O detalhe impossível",
      body: "A história começa antes da resposta.",
      motionVariant: "push-in",
      transitionIn: "fade",
      transitionOut: "slide",
      metadata: { label: "COLD OPEN" },
    },
    {
      id: "scene-02",
      type: "evidence-reveal",
      purpose: "evidence",
      startSeconds: 2.8,
      durationSeconds: 2.6,
      sourceBlockIds: ["B002"],
      headline: "A prova muda o caso",
      body: "A mesma evidência, outra leitura.",
      motionVariant: "track-left",
      transitionIn: "slide",
      transitionOut: "fade",
      metadata: { label: "EVIDÊNCIA" },
    },
    {
      id: "scene-03",
      type: "timeline",
      purpose: "context",
      startSeconds: 5.4,
      durationSeconds: 2.6,
      sourceBlockIds: ["B003"],
      headline: "O tempo reorganiza tudo",
      body: "A sequência revela a mudança de estado.",
      motionVariant: "timeline",
      transitionIn: "fade",
      transitionOut: "fade",
      metadata: { label: "CONTEXTO" },
    },
  ],
  sources: {},
};
