// Renders each extracted 1000x1000 artboard HTML file to a 2000x2000 PNG
// using deviceScaleFactor: 2. Run with: NODE_PATH=$(npm root -g) node render.js
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const srcDir = path.join(__dirname, "src");
const outDir = path.join(__dirname);

async function main() {
  const files = fs.readdirSync(srcDir).filter((f) => f.endsWith(".html")).sort();
  const browser = await chromium.launch({
    executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  });
  const page = await browser.newPage({
    viewport: { width: 1000, height: 1000 },
    deviceScaleFactor: 2,
  });

  for (const file of files) {
    const name = file.replace(/\.html$/, "");
    const fileUrl = "file://" + path.join(srcDir, file);
    await page.goto(fileUrl, { waitUntil: "networkidle" });
    // give web fonts a moment to apply after networkidle
    await page.waitForTimeout(300);
    const outPath = path.join(outDir, `${name}.png`);
    await page.screenshot({ path: outPath, clip: { x: 0, y: 0, width: 1000, height: 1000 } });
    console.log(`rendered ${name}.png`);
  }

  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
