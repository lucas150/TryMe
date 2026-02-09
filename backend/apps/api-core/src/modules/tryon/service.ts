import type { TryOnRequest, TryOnResponse } from "./schema.js";

const TRYON_ML_URL = "http://127.0.0.1:8000/tryon";

export async function runTryOn(
  input: TryOnRequest
): Promise<TryOnResponse> {
  const res = await fetch(TRYON_ML_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      avatar_image_url: input.avatarImageUrl,
      garment_image_url: input.garmentImageUrl,
    }),
  });

  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Try-on ML failed: ${err}`);
  }

  const data = await res.json();

  return {
    imageUrl: data.output_image_path, // later → signed URL
    creditsUsed: 0, // 💥 zero cost now
  };
}
