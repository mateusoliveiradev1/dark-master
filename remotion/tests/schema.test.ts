import { describe, expect, it } from "vitest";

import { defaultRenderPlan, RenderPlanSchema } from "../src/schema";

describe("render plan schema", () => {
  it("accepts the default plan", () => {
    expect(RenderPlanSchema.parse(defaultRenderPlan).version).toBe(2);
  });

  it("rejects unsafe asset paths", () => {
    const result = RenderPlanSchema.safeParse({
      ...defaultRenderPlan,
      scenes: [{ ...defaultRenderPlan.scenes[0], asset: "../secret.png" }],
    });
    expect(result.success).toBe(false);
  });

  it("keeps scene identity and timing", () => {
    const plan = RenderPlanSchema.parse(defaultRenderPlan);
    expect(plan.scenes[0].id).toBe("scene-01");
    expect(plan.scenes[0].durationSeconds).toBeGreaterThan(0);
    expect(plan.scenes[0].states.length).toBeGreaterThan(0);
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
