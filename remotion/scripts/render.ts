import { mkdirSync } from "node:fs";
import { dirname } from "node:path";

import { renderMedia } from "@remotion/renderer";

import { getComposition, outputPath, readPlan } from "./shared";

const plan = readPlan();
const format = process.argv[2] ?? plan.format;
const compositionId = format === "short" ? "DarkMasterShort" : "DarkMasterLong";
const output = outputPath(process.env.DARK_MASTER_OUTPUT, `out/${plan.episode}-${format}.mp4`);
mkdirSync(dirname(output), { recursive: true });
const { serveUrl, composition } = await getComposition(plan, compositionId);
await renderMedia({
  serveUrl,
  composition,
  codec: plan.render.codec,
  audioCodec: plan.render.audioCodec,
  crf: plan.render.crf,
  imageFormat: plan.render.imageFormat,
  jpegQuality: plan.render.jpegQuality,
  outputLocation: output,
  inputProps: { plan },
});
process.stdout.write(`${output}\n`);
