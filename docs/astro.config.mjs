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
        "./src/index.css",
        "./src/tailwind.css",
      ],
      social: {
        github: "https://github.com/flojoy-ai",
        discord: "https://discord.gg/7HEBr7yG8c",
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
          collapsed: false,
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
  markdown: {
    shikiConfig: {
      // Choose from Shiki's built-in themes (or add your own)
      // https://github.com/shikijs/shiki/blob/main/docs/themes.md
      theme: "dracula",
      // Add custom languages
      // Note: Shiki has countless langs built-in, including .astro!
      // https://github.com/shikijs/shiki/blob/main/docs/languages.md
      langs: ["python"],
      // Enable word wrap to prevent horizontal scrolling
      wrap: true,
    },
  },
  vite: {
    resolve: {
      alias: {
        "@blocks": path.resolve("../blocks/"),
      },
    },
  },
});
