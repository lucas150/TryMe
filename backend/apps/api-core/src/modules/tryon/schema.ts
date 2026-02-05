import { z } from "zod";

/**
 * Input contract for a virtual try-on request
 */

export const TryOnRequestSchema = z.object({
  avatarId: z.string().uuid(),
  garmentImageUrl: z.string().url(),

  // Optional styling hint for the AI
  style: z.enum(["studio", "lifestyle", "runway"]).optional(),
});

/**
 * Output contract for a virtual try-on response
 */

export const TryOnResponseSchema = z.object({
  imageUrl: z.string().url(),
  creditsUsed: z.number().int().positive(),
});

/**
 * Inferred TypeScript types
 */
export type TryOnRequest = z.infer<typeof TryOnRequestSchema>;
export type TryOnResponse = z.infer<typeof TryOnResponseSchema>;


// TODO : Check  for depricated .string()

// Sample Usage:
// const sampleRequest: TryOnRequest = {
//   avatarId: "550e8400-e29b-41d4-a716-446655440000",
//   garmentImageUrl: "https://example.com/garment.png",
//   style: "studio",
// };

// const sampleResponse: TryOnResponse = {
//   imageUrl: "https://example.com/tryon-result.png",
//   creditsUsed: 1,
// };
