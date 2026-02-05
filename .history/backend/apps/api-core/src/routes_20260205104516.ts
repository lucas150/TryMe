import { FastifyInstance } from "fastify";
import { tryOnRoutes } from "./modules/tryon/";

export async function registerRoutes(app: FastifyInstance) {
  app.register(tryOnRoutes, { prefix: "/tryon" });
}
