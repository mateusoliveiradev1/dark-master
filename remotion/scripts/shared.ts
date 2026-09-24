import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

import { bundle } from "@remotion/bundler";
import { getCompositions } from "@remotion/renderer";

import { type RenderPlan, RenderPlanSchema } from "../src/schema";

export const readPlan = (): RenderPlan => {
  const value = process.env.DARK_MASTER_RENDER_PLAN;
  if (!value) throw new Error("DARK_MASTER_RENDER_PLAN is required");
  const plan = JSON.parse(readFileSync(resolve(value), "utf8")) as unknown;
  return RenderPlanSchema.parse(plan);
};

export const getComposition = async (plan: RenderPlan, compositionId: string) => {
  const publicDir = process.env.DARK_MASTER_PUBLIC_DIR;
  const serveUrl = await bundle({
    entryPoint: resolve(process.cwd(), "src/index.ts"),
    publicDir: publicDir && existsSync(publicDir) ? publicDir : undefined,
  });
  const compositions = await getCompositions({ serveUrl, inputProps: { plan } });
  const composition = compositions.find((item) => item.id === compositionId);
  if (!composition) throw new Error(`Composition not found: ${compositionId}`);
  return { serveUrl, composition };
};

export const outputPath = (value: string | undefined, fallback: string): string =>
  resolve(value ?? fallback);
