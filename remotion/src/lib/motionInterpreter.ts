import type { CSSProperties } from "react";

import type { MotionOperator } from "../schema";
import { normalizeMotionOperator } from "../schema";

export const MOTION_EASINGS = {
  linear: (value: number) => value,
  easeOutCubic: (value: number) => 1 - (1 - value) ** 3,
  easeInOutCubic: (value: number) => (value < 0.5 ? 4 * value ** 3 : 1 - (-2 * value + 2) ** 3 / 2),
  easeOutQuint: (value: number) => 1 - (1 - value) ** 5,
} as const;

export type MotionEasingName = keyof typeof MOTION_EASINGS;

export type MotionCalculationContext = {
  progress: number;
  stateProgress: number;
  intensity: number;
  ratio: number;
  focalPoint: [number, number];
  width: number;
  height: number;
  visibleLayers: string[];
  reason: string;
};

export type MotionValues = {
  scale: number;
  x: number;
  y: number;
  rotate: number;
  opacity: number;
  clipPath: string;
  filter: string;
  drawProgress: number;
  textProgress: number;
  brightness: number;
  layerOffsets: Record<string, { x: number; y: number; scale: number }>;
};

export type OperatorDefinition = {
  name: MotionOperator;
  reason: string;
  intensityRatio: number;
  easing: MotionEasingName;
  calculate: (context: MotionCalculationContext) => MotionValues;
};

export type MotionInput = {
  operator?: string | null;
  intensity?: number;
  progress: number;
  stateProgress?: number;
  focalPoint?: readonly [number, number];
  width?: number;
  height?: number;
  visibleLayers?: string[];
  reason?: string;
};

export type MotionFrame = MotionValues & {
  operator: MotionOperator | null;
  rawOperator: string;
  intensity: number;
  intensityRatio: number;
  appliedIntensity: number;
  reason: string;
  easing: MotionEasingName | null;
  progress: number;
  stateProgress: number;
  easedStateProgress: number;
  focalPoint: [number, number];
};

export type MotionError = MotionValues & {
  operator: null;
  rawOperator: string;
  intensity: number;
  intensityRatio: 0;
  appliedIntensity: 0;
  reason: string;
  easing: null;
  progress: number;
  stateProgress: number;
  easedStateProgress: number;
  focalPoint: [number, number];
  error: string;
};

export type MotionInterpretation = MotionFrame | MotionError;

const clamp = (value: number, minimum = 0, maximum = 1): number =>
  Math.min(maximum, Math.max(minimum, Number.isFinite(value) ? value : minimum));

const baseValues = (): MotionValues => ({
  scale: 1,
  x: 0,
  y: 0,
  rotate: 0,
  opacity: 1,
  clipPath: "inset(0% 0% 0% 0%)",
  filter: "none",
  drawProgress: 0,
  textProgress: 0,
  brightness: 1,
  layerOffsets: {},
});

const layerSeed = (layer: string): number => {
  let value = 0;
  for (const character of layer) value = (value * 31 + character.charCodeAt(0)) % 997;
  return value / 997;
};

const withParallax = (
  context: MotionCalculationContext,
  amount: number,
): Record<string, { x: number; y: number; scale: number }> =>
  Object.fromEntries(
    context.visibleLayers.map((layer) => {
      const seed = layerSeed(layer) * 2 - 1;
      return [
        layer,
        {
          x: seed * amount,
          y: (1 - layerSeed(`${layer}-y`)) * amount * 0.35,
          scale: 1 + Math.abs(seed) * amount * 0.08,
        },
      ];
    }),
  );

const definitions: Record<MotionOperator, OperatorDefinition> = {
  "static-hold": {
    name: "static-hold",
    reason: "preserve the declared state without inventing camera movement",
    intensityRatio: 0,
    easing: "linear",
    calculate: () => baseValues(),
  },
  "slow-push": {
    name: "slow-push",
    reason: "make the state change legible through a restrained forward camera move",
    intensityRatio: 0.42,
    easing: "easeOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1 + amount * 0.08,
        x: (0.5 - context.focalPoint[0]) * amount * 0.025,
        y: (0.5 - context.focalPoint[1]) * amount * 0.018,
      };
    },
  },
  "lateral-drift": {
    name: "lateral-drift",
    reason: "shift the reading axis while keeping the declared focal point stable",
    intensityRatio: 0.36,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const direction = context.focalPoint[0] < 0.5 ? 1 : -1;
      const amount = context.ratio * (context.stateProgress - 0.5) * 2;
      return {
        ...baseValues(),
        x: direction * amount * 0.055,
        y: (0.5 - context.focalPoint[1]) * context.ratio * 0.012,
        scale: 1 + context.ratio * 0.018,
      };
    },
  },
  "crop-shift": {
    name: "crop-shift",
    reason: "reframe around a state-specific focal point without changing the asset",
    intensityRatio: 0.48,
    easing: "easeOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.01 + amount * 0.07,
        x: (0.5 - context.focalPoint[0]) * amount * 0.16,
        y: (0.5 - context.focalPoint[1]) * amount * 0.1,
      };
    },
  },
  "detail-inspection": {
    name: "detail-inspection",
    reason: "inspect a bounded detail while preserving surrounding context",
    intensityRatio: 0.62,
    easing: "easeOutQuint",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.03 + amount * 0.17,
        x: (0.5 - context.focalPoint[0]) * amount * 0.2,
        y: (0.5 - context.focalPoint[1]) * amount * 0.12,
      };
    },
  },
  "controlled-crop": {
    name: "controlled-crop",
    reason: "hold editorial framing while the declared focal point becomes primary",
    intensityRatio: 0.44,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.015 + amount * 0.065,
        x: (0.5 - context.focalPoint[0]) * amount * 0.12,
        y: (0.5 - context.focalPoint[1]) * amount * 0.075,
      };
    },
  },
  "pull-out": {
    name: "pull-out",
    reason: "return visual emphasis to the surrounding case context",
    intensityRatio: 0.4,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.1 - amount * 0.07,
        x: (context.focalPoint[0] - 0.5) * amount * 0.12,
        y: (context.focalPoint[1] - 0.5) * amount * 0.08,
      };
    },
  },
  "masked-reveal": {
    name: "masked-reveal",
    reason: "reveal only the state-bearing region with a deterministic mask",
    intensityRatio: 0.52,
    easing: "easeOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        clipPath: `inset(0% ${(1 - amount) * 100}% 0% 0%)`,
        scale: 1.01 + amount * 0.04,
      };
    },
  },
  "line-draw": {
    name: "line-draw",
    reason: "construct a chronological relation through a visible line",
    intensityRatio: 0.58,
    easing: "easeOutCubic",
    calculate: (context) => ({
      ...baseValues(),
      drawProgress: context.ratio * context.stateProgress,
      scale: 1.01,
    }),
  },
  "timeline-build": {
    name: "timeline-build",
    reason: "build the timeline as a left-to-right state relation",
    intensityRatio: 0.58,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        drawProgress: amount,
        x: (amount - 0.5) * 0.035,
        scale: 1.01 + amount * 0.02,
      };
    },
  },
  "route-draw": {
    name: "route-draw",
    reason: "trace a route in the direction declared by the spatial state",
    intensityRatio: 0.56,
    easing: "easeOutCubic",
    calculate: (context) => ({
      ...baseValues(),
      drawProgress: context.ratio * context.stateProgress,
      scale: 1.008,
    }),
  },
  "document-dive": {
    name: "document-dive",
    reason: "move into the document surface while keeping its source context visible",
    intensityRatio: 0.38,
    easing: "easeOutQuint",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.02 + amount * 0.1,
        y: (0.5 - context.focalPoint[1]) * amount * 0.12,
        x: (0.5 - context.focalPoint[0]) * amount * 0.04,
      };
    },
  },
  "evidence-lens": {
    name: "evidence-lens",
    reason: "isolate evidence with a bounded lens and stable crop",
    intensityRatio: 0.66,
    easing: "easeOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      const radius = 22 + amount * 24;
      return {
        ...baseValues(),
        scale: 1.04 + amount * 0.13,
        x: (0.5 - context.focalPoint[0]) * amount * 0.16,
        y: (0.5 - context.focalPoint[1]) * amount * 0.11,
        clipPath: `inset(${Math.max(0, 10 - amount * 8)}% ${Math.max(0, 50 - radius)}% ${Math.max(0, 10 - amount * 8)}% ${Math.max(0, 50 - radius)}%)`,
        filter: `brightness(${1 + amount * 0.06}) contrast(${1 + amount * 0.08})`,
      };
    },
  },
  parallax: {
    name: "parallax",
    reason: "separate declared visual layers along a controlled depth axis",
    intensityRatio: 0.34,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const amount = context.ratio * (context.stateProgress - 0.5) * 2;
      return {
        ...baseValues(),
        x: amount * 0.028,
        y: amount * 0.012,
        scale: 1.015,
        layerOffsets: withParallax(context, amount * 0.045),
      };
    },
  },
  "match-cut": {
    name: "match-cut",
    reason: "carry a declared visual anchor across a state boundary",
    intensityRatio: 0.46,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        x: (0.5 - amount) * 0.12,
        y: (context.focalPoint[1] - 0.5) * amount * 0.06,
        scale: 1.01 + amount * 0.045,
      };
    },
  },
  "luminance-dissolve": {
    name: "luminance-dissolve",
    reason: "change luminance to mark a state transition without a generic fade",
    intensityRatio: 0.32,
    easing: "easeInOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        brightness: 0.86 + amount * 0.22,
        filter: `brightness(${0.86 + amount * 0.22}) saturate(${0.72 + amount * 0.34})`,
        scale: 1.01 + amount * 0.025,
      };
    },
  },
  "negative-space-pullout": {
    name: "negative-space-pullout",
    reason: "withdraw toward negative space to expose consequence without invention",
    intensityRatio: 0.4,
    easing: "easeOutCubic",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.09 - amount * 0.08,
        x: (amount - 0.5) * 0.12,
        y: (0.5 - context.focalPoint[1]) * amount * 0.05,
      };
    },
  },
  "archive-title-object": {
    name: "archive-title-object",
    reason: "separate the archival object from its title through spatial hierarchy",
    intensityRatio: 0.36,
    easing: "easeOutQuint",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      return {
        ...baseValues(),
        scale: 1.02 + amount * 0.06,
        y: (0.5 - amount) * 0.08,
        x: (0.5 - context.focalPoint[0]) * amount * 0.05,
      };
    },
  },
  "typewriter-interference": {
    name: "typewriter-interference",
    reason: "reveal typed information with deterministic interference, not random noise",
    intensityRatio: 0.3,
    easing: "linear",
    calculate: (context) => {
      const amount = context.ratio * context.stateProgress;
      const seed = context.visibleLayers.join(":").length % 7;
      return {
        ...baseValues(),
        textProgress: amount,
        x: Math.sin(seed + context.stateProgress * Math.PI * 2) * amount * 0.012,
        filter: `contrast(${1 + amount * 0.08})`,
      };
    },
  },
};

export const getMotionDefinition = (operator: MotionOperator): OperatorDefinition =>
  definitions[operator];

export const getMotionOperators = (): readonly OperatorDefinition[] => Object.values(definitions);
export const getMotionOperatorNames = (): readonly MotionOperator[] =>
  Object.keys(definitions) as MotionOperator[];

const normalizePoint = (value: readonly [number, number] | undefined): [number, number] => [
  clamp(value?.[0] ?? 0.5),
  clamp(value?.[1] ?? 0.5),
];

export class MotionInterpreter {
  interpret(input: MotionInput): MotionInterpretation {
    const rawOperator = input.operator?.trim() ?? "";
    const operator = normalizeMotionOperator(rawOperator);
    const intensity = clamp(input.intensity ?? 0, 0, 4);
    const progress = clamp(input.progress);
    const stateProgress = clamp(input.stateProgress ?? progress);
    const focalPoint = normalizePoint(input.focalPoint);
    if (!operator) {
      return {
        ...baseValues(),
        operator: null,
        rawOperator,
        intensity,
        intensityRatio: 0,
        appliedIntensity: 0,
        reason: input.reason?.trim() || "motion operator is not declared",
        easing: null,
        progress,
        stateProgress,
        easedStateProgress: stateProgress,
        focalPoint,
        error: `unknown motion operator: ${rawOperator || "<empty>"}`,
      };
    }
    const definition = definitions[operator];
    const easedStateProgress = clamp(MOTION_EASINGS[definition.easing](stateProgress));
    const ratio = (intensity / 4) * definition.intensityRatio;
    const context: MotionCalculationContext = {
      progress,
      stateProgress: easedStateProgress,
      intensity,
      ratio,
      focalPoint,
      width: Math.max(1, input.width ?? 1920),
      height: Math.max(1, input.height ?? 1080),
      visibleLayers: input.visibleLayers ?? [],
      reason: input.reason?.trim() || definition.reason,
    };
    const values = intensity === 0 ? baseValues() : definition.calculate(context);
    return {
      ...values,
      operator,
      rawOperator,
      intensity,
      intensityRatio: definition.intensityRatio,
      appliedIntensity: ratio,
      reason: context.reason,
      easing: definition.easing,
      progress,
      stateProgress,
      easedStateProgress,
      focalPoint,
    };
  }
}

export const motionInterpreter = new MotionInterpreter();

export const interpretMotion = (input: MotionInput): MotionInterpretation =>
  motionInterpreter.interpret(input);

export const motionStyle = (frame: MotionFrame, width: number, height: number): CSSProperties => ({
  opacity: frame.opacity,
  clipPath: frame.clipPath,
  filter: frame.filter === "none" ? undefined : frame.filter,
  transform: `translate3d(${frame.x * width}px, ${frame.y * height}px, 0) scale(${frame.scale}) rotate(${frame.rotate}deg)`,
  transformOrigin: `${frame.focalPoint[0] * 100}% ${frame.focalPoint[1] * 100}%`,
  willChange: "transform, opacity, clip-path, filter",
});

export const mediaMotionStyle = (
  frame: MotionFrame,
  width: number,
  height: number,
  layer?: string,
): CSSProperties => {
  const base = motionStyle(frame, width, height);
  if (frame.operator === "typewriter-interference") {
    return {
      ...base,
      clipPath: "none",
      transform: "none",
    };
  }
  const offset = layer ? frame.layerOffsets[layer] : undefined;
  if (!offset) return base;
  return {
    ...base,
    transform: `${base.transform} translate3d(${offset.x * 100}vw, ${offset.y * 100}vh, 0) scale(${offset.scale})`,
  };
};

export const annotationMotionStyle = (
  frame: MotionFrame,
  _width: number,
  _height: number,
): CSSProperties => ({
  opacity: frame.opacity,
  willChange: "opacity",
});

export const vectorMotionStyle = (
  frame: MotionFrame,
  width: number,
  height: number,
): CSSProperties => ({
  opacity: frame.opacity,
  clipPath: frame.clipPath === "inset(0% 0% 0% 0%)" ? undefined : frame.clipPath,
  transform: `translate3d(${frame.x * width * 0.25}px, ${frame.y * height * 0.25}px, 0)`,
  willChange: "transform, opacity, clip-path",
});

export const textMotionStyle = (
  frame: MotionFrame,
  width: number,
  height: number,
): CSSProperties => {
  if (frame.operator !== "typewriter-interference") return {};
  return {
    clipPath: `inset(0 ${(1 - frame.textProgress) * 100}% 0 0)`,
    transform: `translate3d(${frame.x * width}px, ${frame.y * height}px, 0)`,
    willChange: "transform, clip-path",
  };
};

export const layerMotionStyle = (frame: MotionFrame, layer: string): CSSProperties => {
  const offset = frame.layerOffsets[layer];
  if (!offset) return {};
  return {
    transform: `translate3d(${offset.x * 100}vw, ${offset.y * 100}vh, 0) scale(${offset.scale})`,
  };
};
