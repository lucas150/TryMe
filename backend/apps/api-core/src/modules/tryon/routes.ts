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

      const result = await runTryOn(parsed.data);
      return result;
    }
  );
}
