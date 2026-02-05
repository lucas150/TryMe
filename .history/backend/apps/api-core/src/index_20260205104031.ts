import { buildApp } from "./server/app";

const app = buildApp();

app.listen({ port: 3000 }, (err, address) => {
  if (err) {
    app.log.error(err);
    process.exit(1);
  }

  console.log(`🚀 API Core listening at ${address}`);
});
