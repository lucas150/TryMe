import type { TryOnRequest, TryOnResponse } from "./schema.js";
import { debugLog } from "./debug.js";
import { FastifyBaseLogger } from "fastify";

const TRYON_ML_URL = "http://127.0.0.1:8000/tryon";
export async function runTryOn(
  input: TryOnRequest,
  logger: FastifyBaseLogger
): Promise<TryOnResponse> {

  debugLog(logger, input.debug, "Calling ML service");

  const res = await fetch(TRYON_ML_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      avatar_image_url: input.avatarImageUrl,
      garment_image_url: input.garmentImageUrl,
      debug: input.debug,
    }),
  });

  if (!res.ok) {
    const err = await res.text();
    throw new Error(`Try-on ML failed: ${err}`);
  }

  const data = await res.json();

  debugLog(logger, input.debug, "ML response received", data);

  return {
    imageUrl: data.output_image_path,
    creditsUsed: 0,
  };
}
