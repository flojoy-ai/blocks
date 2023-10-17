import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import tailwind from "@astrojs/tailwind";
import path from "path";
import react from "@astrojs/react";

// https://astro.build/config
export default defineConfig({
  site: "https://blocks.flojoy.ai",
  integrations: [
    starlight({
      title: "Flojoy Docs",
      customCss: [
        // Path to your Tailwind base styles:
        "./src/tailwind.css",
      ],
      social: {
        github: "https://github.com/flojoy-ai",
      },
      lastUpdated: true,
      sidebar: [
        {
          label: "Flojoy Studio",
          autogenerate: {
            directory: "studio",
          },
        },
        {
          label: "Flojoy Blocks",
          autogenerate: {
            directory: "blocks",
            collapsed: true,
          },
        },
        {
          label: "Instruments Database",
          autogenerate: {
            directory: "instruments",
            collapsed: true,
          },
        },
      ],
      defaultLocale: "root",
      locales: {
        root: {
          lang: "en",
          label: "English",
        },
        fr: {
          label: "Français",
        },
        "zh-cn": {
          label: "简体中文",
          lang: "zh-CN",
        },
      },
    }),
    tailwind({
      // Disable the default base styles:
      applyBaseStyles: false,
    }),
    react(),
  ],
  vite: {
    resolve: {
      alias: {
        "@blocks": path.resolve("../blocks/"),
      },
    },
  },
});
