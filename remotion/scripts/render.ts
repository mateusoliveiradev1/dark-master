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
  codec: "h264",
  audioCodec: "aac",
  crf: 18,
  imageFormat: "jpeg",
  jpegQuality: 92,
  outputLocation: output,
  inputProps: { plan },
});
process.stdout.write(`${output}\n`);
