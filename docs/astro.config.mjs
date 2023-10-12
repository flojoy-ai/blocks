import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
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
      sidebar: [
        {
          label: "Studio",
          autogenerate: {
            directory: "studio",
          },
        },
        {
          label: "Blocks",
          autogenerate: {
            directory: "blocks",
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
  ],
});
