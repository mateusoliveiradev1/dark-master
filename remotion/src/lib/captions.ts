import { type Caption, createTikTokStyleCaptions, type TikTokPage } from "@remotion/captions";

import type { RenderPlan } from "../schema";
import type { LayoutFormat } from "./layout";

export type PlanCaption = RenderPlan["captions"][number];

export const captionTokens = (captions: PlanCaption[]): Caption[] =>
  captions.flatMap((caption) => {
    const words = caption.text.trim().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    const startMs = Math.round(caption.startSeconds * 1000);
    const endMs = Math.max(startMs + 1, Math.round(caption.endSeconds * 1000));
    const duration = endMs - startMs;
    return words.map((word, index) => {
      const fromMs = startMs + Math.round((duration * index) / words.length);
      const toMs =
        index === words.length - 1
          ? endMs
          : startMs + Math.round((duration * (index + 1)) / words.length);
      return {
        text: index === 0 ? word : ` ${word}`,
        startMs: fromMs,
        endMs: Math.max(fromMs + 1, toMs),
        timestampMs: fromMs,
        confidence: null,
        pageBreakAfter: index === words.length - 1,
      };
    });
  });

export const captionPages = (captions: PlanCaption[], format: LayoutFormat): TikTokPage[] => {
  const tokens = captionTokens(captions);
  if (!tokens.length) return [];
  return createTikTokStyleCaptions({
    captions: tokens,
    combineTokensWithinMilliseconds: format === "short" ? 1000 : 1800,
  }).pages;
};

export const activeCaptionPage = (pages: TikTokPage[], seconds: number): TikTokPage | undefined => {
  const timeMs = Math.max(0, seconds * 1000);
  return pages.find((page) => timeMs >= page.startMs && timeMs < page.startMs + page.durationMs);
};

export const captionLines = (text: string, maxCharacters: number, maxLines: number): string[] => {
  const words = text.trim().split(/\s+/).filter(Boolean);
  const lines: string[] = [];
  let line = "";
  for (const word of words) {
    const candidate = line ? `${line} ${word}` : word;
    if (line && candidate.length > maxCharacters) {
      lines.push(line);
      line = word;
    } else {
      line = candidate;
    }
  }
  if (line) lines.push(line);
  return lines.slice(0, Math.max(1, maxLines));
};
