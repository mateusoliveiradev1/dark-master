import { readFileSync } from "node:fs";

import { describe, expect, it } from "vitest";

import { captionLines, captionPages } from "../src/lib/captions";
import { getLayoutProfile } from "../src/lib/layout";
import { getMotionDefinition, MotionInterpreter } from "../src/lib/motionInterpreter";
import { resolveSceneState } from "../src/lib/stateResolver";
import { buildPlanTimeline } from "../src/lib/timeline";
import { MOTION_OPERATORS, RenderPlanSchema } from "../src/schema";
import fixture from "./fixtures/runtime-contract.json";

const plan = RenderPlanSchema.parse(fixture);

describe("visual runtime contracts", () => {
  it("keeps an absolute contiguous timeline and preserves transition duration", () => {
    const timeline = buildPlanTimeline(plan);

    expect(timeline.errors).toEqual([]);
    expect(timeline.scenes.map((scene) => scene.from)).toEqual([0, 60]);
    expect(timeline.transitions).toHaveLength(1);
    expect(timeline.totalDurationInFrames).toBe(120);
    expect(timeline.renderDurationInFrames).toBe(timeline.totalDurationInFrames);
  });

  it("resolves layers and assets by state identity instead of array order", () => {
    const scene = plan.scenes[0];
    const alternate = {
      ...scene,
      assets: [
        {
          ...scene.assets[0],
          assetId: "asset-first-alternate",
          path: "images/alternate.jpg",
        },
        scene.assets[0],
      ],
    };
    const state = resolveSceneState(
      { ...plan, scenes: [alternate, plan.scenes[1]] },
      alternate,
      45,
      30,
      1080,
      1920,
    );

    expect(state.state?.id).toBe("focus");
    expect(state.visibleLayers).toEqual(["subject", "evidence"]);
    expect(state.hiddenLayers).toEqual(["environment"]);
    expect(state.focalPoint).toEqual([0.7, 0.3]);
    expect(state.annotation).toBe("evidência localizada");
    expect(state.assets.map((asset) => asset.assetId)).toEqual(["asset-first"]);
  });

  it("does not create a transition when the boundary is explicitly cut", () => {
    const cutPlan = {
      ...plan,
      scenes: plan.scenes.map((scene) => ({
        ...scene,
        transitionIn: "cut",
        transitionOut: "cut",
        motionPrompt: scene.motionPrompt
          ? {
              ...scene.motionPrompt,
              transitions: {
                ...scene.motionPrompt.transitions,
                in: "cut",
                out: "cut",
              },
            }
          : scene.motionPrompt,
      })),
    };

    expect(buildPlanTimeline(cutPlan).transitions).toHaveLength(0);
  });

  it("executes every declared operator with an explicit reason and intensity", () => {
    const interpreter = new MotionInterpreter();

    for (const operator of MOTION_OPERATORS) {
      const result = interpreter.interpret({
        operator,
        intensity: 3,
        progress: 0.4,
        stateProgress: 0.7,
        visibleLayers: ["environment", "evidence"],
      });
      expect(result.operator).toBe(operator);
      expect("error" in result).toBe(false);
      if ("error" in result) continue;
      expect(result.reason).toBe(getMotionDefinition(operator).reason);
      expect(result.easing).not.toBeNull();
      expect(result.appliedIntensity).toBeGreaterThanOrEqual(0);
    }
  });

  it("uses the short crop policy for portrait dimensions", () => {
    const profile = getLayoutProfile(plan, 1080, 1920, plan.scenes[0]);

    expect(profile.format).toBe("short");
    expect(profile.focalPoint).toEqual([0.7, 0.3]);
    expect(profile.dedicatedReframeRequired).toBe(true);
    const sceneWithoutStateFocal = {
      ...plan.scenes[0],
      states: plan.scenes[0].states.map((state) => {
        const next = { ...state };
        delete next.focalPoint;
        return next;
      }),
    };
    expect(resolveSceneState(plan, sceneWithoutStateFocal, 0, 30, 1080, 1920).focalPoint).toEqual([
      0.7, 0.3,
    ]);
  });

  it("holds static frames without camera movement", () => {
    const interpreter = new MotionInterpreter();
    const first = interpreter.interpret({
      operator: "static-hold",
      intensity: 4,
      progress: 0,
      stateProgress: 0,
    });
    const last = interpreter.interpret({
      operator: "static-hold",
      intensity: 4,
      progress: 1,
      stateProgress: 1,
    });

    expect(first.operator).toBe("static-hold");
    expect(last.scale).toBe(first.scale);
    expect(last.x).toBe(first.x);
    expect(last.y).toBe(first.y);
    expect(last.clipPath).toBe(first.clipPath);
  });

  it("keeps scene motion targetable instead of applying it to the whole frame", () => {
    const source = readFileSync(
      new URL("../src/components/SceneRuntime.tsx", import.meta.url),
      "utf8",
    );
    const primitives = readFileSync(
      new URL("../src/scenes/ScenePrimitives.tsx", import.meta.url),
      "utf8",
    );

    expect(source).not.toContain("...motionStyle(runtime.motion");
    expect(source).toContain("data-state-boundary-progress");
    expect(primitives).toContain("mediaMotionStyle");
    expect(primitives).toContain("textMotionStyle");
  });

  it("returns a visible error result for an unknown operator", () => {
    const result = new MotionInterpreter().interpret({
      operator: "unknown-camera",
      intensity: 2,
      progress: 0.5,
    });

    expect("error" in result).toBe(true);
  });

  it("blocks unknown scene, motion and transition types in v2", () => {
    const unknownMotion = {
      ...plan,
      scenes: plan.scenes.map((scene, index) =>
        index === 0
          ? {
              ...scene,
              states: scene.states.map((state, stateIndex) =>
                stateIndex === 0 ? { ...state, motion: "unknown-camera" } : state,
              ),
            }
          : scene,
      ),
    };
    const unknownType = {
      ...plan,
      scenes: plan.scenes.map((scene, index) =>
        index === 0 ? { ...scene, type: "unknown-scene" } : scene,
      ),
    };
    const unknownTransition = {
      ...plan,
      scenes: plan.scenes.map((scene, index) =>
        index === 0 ? { ...scene, transitionOut: "unknown-transition" } : scene,
      ),
    };

    expect(RenderPlanSchema.safeParse(unknownMotion).success).toBe(false);
    expect(RenderPlanSchema.safeParse(unknownType).success).toBe(false);
    expect(RenderPlanSchema.safeParse(unknownTransition).success).toBe(false);
  });

  it("creates caption pages and limits rendered lines", () => {
    const pages = captionPages(plan.captions, "short");
    const lines = captionLines("uma prova longa precisa permanecer dentro da area segura", 18, 2);

    expect(pages.length).toBeGreaterThan(0);
    expect(lines.length).toBeLessThanOrEqual(2);
  });

  it("has no silent fallback renderer", () => {
    const source = readFileSync(
      new URL("../src/scenes/SceneRenderer.tsx", import.meta.url),
      "utf8",
    );

    expect(source).not.toContain("Generic");
  });
});
