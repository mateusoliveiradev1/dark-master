export const secondsToFrames = (seconds: number, fps: number): number =>
  Math.max(1, Math.round(seconds * fps));

export const sceneDurationFrames = (durationSeconds: number, fps: number): number =>
  secondsToFrames(durationSeconds, fps);

export const activeCaption = <T extends { startSeconds: number; endSeconds: number }>(
  captions: T[],
  seconds: number,
): T | undefined =>
  captions.find((caption) => seconds >= caption.startSeconds && seconds < caption.endSeconds);
