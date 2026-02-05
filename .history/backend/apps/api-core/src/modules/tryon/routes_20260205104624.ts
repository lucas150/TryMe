import { FastifyInstance } from "fastify";
import { runTryOn } from "../tryon.service.js";

export async function tryOnRoutes(app: FastifyInstance) {
  app.post("/", async (request, reply) => {
    const result = await runTryOn(request.body);
    return result;
  });
}
