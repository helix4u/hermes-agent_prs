import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const webRoot = path.resolve(__dirname, "..");

const copies = [
  {
    from: path.join(webRoot, "node_modules", "@nous-research", "ui", "dist", "fonts"),
    to: path.join(webRoot, "public", "fonts"),
  },
  {
    from: path.join(webRoot, "node_modules", "@nous-research", "ui", "dist", "assets"),
    to: path.join(webRoot, "public", "ds-assets"),
  },
];

for (const { to } of copies) {
  fs.rmSync(to, { force: true, recursive: true });
}

for (const { from, to } of copies) {
  if (!fs.existsSync(from)) {
    throw new Error(`Missing source asset directory: ${from}`);
  }
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.cpSync(from, to, { recursive: true });
}
