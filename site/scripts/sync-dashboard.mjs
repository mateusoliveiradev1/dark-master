import { copyFileSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "..", "..", "data", "dashboard.json");
const dest = join(here, "..", "public", "dashboard.json");
const fallback = { generated: null, channels: [], loop_reports: [], alerts: [], ypp: {} };

mkdirSync(dirname(dest), { recursive: true });
if (existsSync(src)) {
  copyFileSync(src, dest);
  console.log(`[dashboard] synced ${src}`);
} else {
  writeFileSync(dest, JSON.stringify(fallback, null, 2));
  console.log("[dashboard] no data/dashboard.json yet — empty panel");
}
