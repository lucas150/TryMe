import type { TryOnRequest, TryOnResponse } from "./schema.js";

export async function runTryOn(
  input: TryOnRequest
): Promise<TryOnResponse> {

  // Later:
  // 1. Load avatar embedding
  // 2. Segment garment
  // 3. Call Nano Banana
  // 4. Store result
  // 5. Deduct credits

  return {
    imageUrl: "https://example.com/mock-tryon.png",
    creditsUsed: 1,
  };
}
