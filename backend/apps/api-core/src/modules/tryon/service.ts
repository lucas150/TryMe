import type { TryOnRequest, TryOnResponse } from "./schema.js";
import { nanoBananaModel } from "../../infra/gemini.js";

export async function runTryOn(
  input: TryOnRequest
): Promise<TryOnResponse> {
  const { avatarImageUrl, garmentImageUrl, style } = input;

  // Later:
  // 1. Load avatar embedding
  // 2. Segment garment
  // 3. Call Nano Banana
  // 4. Store result
  // 5. Deduct credits

  /**
   * TEMPORARY:
   * For now, we assume avatarId is actually an image URL.
   * Later this will resolve from storage / embeddings.
   */
  // const avatarImageUrl = avatarId;

  const prompt = `
You are a virtual try-on AI.

TASK:
Apply the garment from the garment image onto the person in the avatar image.

CRITICAL CONSTRAINTS (MUST FOLLOW):
- Preserve the original image framing exactly
- DO NOT crop, zoom, or reframe the image
- Keep the full head-to-torso/body visible as in the original avatar image
- Keep the face, hair, pose, and body shape unchanged
- Replace ONLY the clothing item

REALISM:
- Match lighting direction and intensity
- Match shadows on skin and fabric
- Maintain realistic fabric drape and folds

OUTPUT:
- Photorealistic
- Same aspect ratio as the avatar image
- Same camera distance as the avatar image

STYLE:
${style ?? "studio"}
`;


  const result = await nanoBananaModel.generateContent([
    prompt,
    {
      inlineData: {
        mimeType: "image/jpeg",
        data: await fetchImageBase64(avatarImageUrl),
      },
    },
    {
      inlineData: {
        mimeType: "image/jpeg",
        data: await fetchImageBase64(garmentImageUrl),
      },
    },
  ]);

const part = result.response.candidates?.[0]?.content?.parts?.[0];

if (!isInlineImagePart(part)) {
  throw new Error("Nano Banana did not return an image");
}

const base64Image = part.inlineData.data;

  // For now, return a data URL
  // Later: upload to Cloudinary
  return {
    imageUrl: `data:image/png;base64,${base64Image}`,
    creditsUsed: 1,
  };
}

function isInlineImagePart(
  part: unknown
): part is { inlineData: { data: string } } {
  return (
    typeof part === "object" &&
    part !== null &&
    "inlineData" in part &&
    typeof (part as any).inlineData?.data === "string"
  );
}


async function fetchImageBase64(url: string): Promise<string> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch image: ${url}`);
  }

  const arrayBuffer = await res.arrayBuffer();
  return Buffer.from(arrayBuffer).toString("base64");
}
