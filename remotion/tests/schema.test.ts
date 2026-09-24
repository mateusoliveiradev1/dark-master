import { describe, expect, it } from "vitest";

import { defaultRenderPlan, RenderPlanSchema } from "../src/schema";

describe("render plan schema", () => {
  it("accepts the default plan", () => {
    expect(RenderPlanSchema.parse(defaultRenderPlan).version).toBe(1);
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
  });
});
