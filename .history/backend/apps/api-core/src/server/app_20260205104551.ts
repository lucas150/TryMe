import Fastify from "fastify";
import { registerRoutes } from "../";

export function buildApp() {
  const app = Fastify({ logger: true });

  app.get("/", async () => {
    return { status: "ok", message: "API Core running" };
  });

  registerRoutes(app);

  return app;
}
