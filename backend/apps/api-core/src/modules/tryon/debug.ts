import type { FastifyBaseLogger } from "fastify";

export function debugLog(
  logger: FastifyBaseLogger,
  enabled: boolean,
  message: string,
  data?: unknown
) {
  if (!enabled) return;

  logger.info(
    data ? { msg: message, data } : { msg: message }
  );
}
