import { describe, expect, it } from "vitest";

import { defaultRenderPlan, RenderPlanSchema } from "../src/schema";

describe("render plan schema", () => {
  it("accepts the default plan", () => {
    expect(RenderPlanSchema.parse(defaultRenderPlan).version).toBe(2);
  });

  it("rejects unsafe and absolute asset paths", () => {
    for (const assetPath of ["../secret.png", "/secret.png"]) {
      const result = RenderPlanSchema.safeParse({
        ...defaultRenderPlan,
        scenes: [{ ...defaultRenderPlan.scenes[0], asset: assetPath }],
      });
      expect(result.success).toBe(false);
    }
  });

  it("keeps scene identity, timing and prompt contracts", () => {
    const plan = RenderPlanSchema.parse(defaultRenderPlan);
    expect(plan.scenes[0].id).toBe("scene-01");
    expect(plan.scenes[0].shotId).toBe("scene-01");
    expect(plan.scenes[0].promptId).toBe("prompt-scene-01");
    expect(plan.scenes[0].durationSeconds).toBeGreaterThan(0);
    expect(plan.scenes[0].states.length).toBeGreaterThan(0);
    expect(plan.scenes[0].imagePrompt?.full).toContain("no baked-in text");
    expect(plan.scenes[0].motionPrompt?.states[0].timeRange[0]).toBe(0);
    expect(plan.scenes[0].motionPrompt?.states.at(-1)?.timeRange[1]).toBe(100);
  });

  it("rejects v2 scenes without deterministic contracts", () => {
    const scene = { ...defaultRenderPlan.scenes[0] };
    delete (scene as Partial<typeof scene>).motionPrompt;
    const result = RenderPlanSchema.safeParse({
      ...defaultRenderPlan,
      scenes: [scene],
      video: { ...defaultRenderPlan.video, durationSeconds: scene.durationSeconds },
    });
    expect(result.success).toBe(false);
  });

  it("rejects scene gaps", () => {
    const result = RenderPlanSchema.safeParse({
      ...defaultRenderPlan,
      scenes: defaultRenderPlan.scenes.map((scene, index) =>
        index === 1 ? { ...scene, startSeconds: scene.startSeconds + 0.5 } : scene,
      ),
    });
    expect(result.success).toBe(false);
  });

  it("rejects incomplete state timelines", () => {
    const result = RenderPlanSchema.safeParse({
      ...defaultRenderPlan,
      scenes: defaultRenderPlan.scenes.map((scene, index) =>
        index === 0 ? { ...scene, states: [{ ...scene.states[0], timeRange: [0.2, 0.7] }] } : scene,
      ),
    });
    expect(result.success).toBe(false);
  });
});
