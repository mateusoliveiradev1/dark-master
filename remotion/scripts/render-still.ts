import { mkdirSync } from "node:fs";
import { dirname } from "node:path";

import { renderStill } from "@remotion/renderer";

import { getComposition, outputPath, readPlan } from "./shared";

const plan = readPlan();
const format = process.argv[2] ?? plan.format;
const compositionId = format === "short" ? "DarkMasterShort" : "DarkMasterLong";
const frame = Number(process.argv[3] ?? Math.round(plan.video.fps * 0.5));
const output = outputPath(
  process.env.DARK_MASTER_STILL,
  `out/${plan.episode}-${format}-${frame}.png`,
);
mkdirSync(dirname(output), { recursive: true });
const { serveUrl, composition } = await getComposition(plan, compositionId);
await renderStill({
  serveUrl,
  composition,
  output,
  frame,
  imageFormat: "png",
  inputProps: { plan },
});
process.stdout.write(`${output}\n`);
