import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import { resolve } from "node:path";

const commandVersion = (command: string): string | null => {
  try {
    return execFileSync(command, ["-version"], { encoding: "utf8" }).trim().split("\n")[0];
  } catch {
    return null;
  }
};

const nodeMajor = Number(process.versions.node.split(".")[0]);
const checks = {
  node: nodeMajor >= 20,
  ffmpeg: commandVersion("ffmpeg") !== null,
  ffprobe: commandVersion("ffprobe") !== null,
  remotionEntry: existsSync(resolve(process.cwd(), "src/index.ts")),
};

const result = {
  status: Object.values(checks).every(Boolean) ? "PASS" : "FAIL",
  node: process.versions.node,
  ffmpeg: commandVersion("ffmpeg"),
  ffprobe: commandVersion("ffprobe"),
  checks,
};

process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
process.exit(result.status === "PASS" ? 0 : 1);
