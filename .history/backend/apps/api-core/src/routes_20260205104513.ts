import { FastifyInstance } from "fastify";
import { tryOnRoutes } from "./";

export async function registerRoutes(app: FastifyInstance) {
  app.register(tryOnRoutes, { prefix: "/tryon" });
}
