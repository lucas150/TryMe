import { FastifyInstance } from "fastify";
import { runTryOn } from "./service.js";
import { TryOnRequestSchema } from "./schema.js";

export async function tryOnRoutes(app: FastifyInstance) {
  app.post(
    "/",
    async (request, reply) => {
      // 🔐 Validate input at runtime
      const parsed = TryOnRequestSchema.safeParse(request.body);

      if (!parsed.success) {
        return reply.status(400).send({
          error: "Invalid try-on request",
          details: parsed.error.flatten(),
        });
      }

      const data = parsed.data;

      // ✅ centralized debug logging
      if (data.debug) {
        app.log.info({
          msg: "Try-on request received",
          avatar: data.avatarImageUrl,
          garment: data.garmentImageUrl,
        });
      }

      const result = await runTryOn(data, app.log);

      return result;
    }
  );
}
