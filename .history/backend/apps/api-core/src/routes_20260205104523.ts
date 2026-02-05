import { FastifyInstance } from "fastify";
import { tryOnRoutes } from "./modules/tryon/routes.js";

export async function registerRoutes(app: FastifyInstance) {
  app.register(tryOnRoutes, { prefix: "/tryon" });
}
