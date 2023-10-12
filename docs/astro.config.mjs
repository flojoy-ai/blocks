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
    }),
    tailwind({
      // Disable the default base styles:
      applyBaseStyles: false,
    }),
  ],
});
