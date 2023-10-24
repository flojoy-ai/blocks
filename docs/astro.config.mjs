import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import tailwind from "@astrojs/tailwind";
import path from "path";
import react from "@astrojs/react";

import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

// https://astro.build/config
export default defineConfig({
  site: "https://blocks.flojoy.ai",
  integrations: [
    starlight({
      title: "Flojoy Docs",
      customCss: [
        // Path to your Tailwind base styles:
        "./src/tailwind.css",
        // Some reactflow styles
        "./src/index.css",
        // Joey: Please do not add any more custom css files
      ],
      social: {
        github: "https://github.com/flojoy-ai",
        discord: "https://discord.gg/7HEBr7yG8c",
      },
      lastUpdated: true,
      head: [
        {
          // Tag to support Latex display
          tag: "link",
          attrs: {
            rel: "stylesheet",
            href: "https://cdn.jsdelivr.net/npm/katex@0.15.1/dist/katex.css",
            integrity:
              "sha384-WsHMgfkABRyG494OmuiNmkAOk8nhO1qE+Y6wns6v+EoNoTNxrWxYpl5ZYWFOLPCM",
            crossorigin: "anonymous",
          },
        },
      ],
      sidebar: [
        // Joey: IMPORTANT, always use autogenerate unless
        // there is a very good reason not to use it
        {
          label: "🕹️ Flojoy Studio",
          autogenerate: {
            directory: "studio",
          },
        },
        {
          label: "🔮 Flojoy Blocks",
          collapsed: false,
          autogenerate: {
            directory: "blocks",
            collapsed: true,
          },
        },
        {
          label: "📚 Contribution Guide",
          items: [
            {
              label: "Contribute to Blocks",
              autogenerate: {
                directory: "contribution/blocks",
                collapsed: true,
              },
            },
            {
              label: "Contribute to Docs",
              autogenerate: {
                directory: "contribution/docs",
                collapsed: true,
              },
            },
          ],
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
        // "zh-cn": {
        //   label: "简体中文",
        //   lang: "zh-CN",
        // },
      },
    }),
    tailwind({
      // Disable the default base styles, otherwise CSS will break
      applyBaseStyles: false,
    }),
    react(),
  ],
  markdown: {
    shikiConfig: {
      theme: "dracula",
      langs: ["python"],
      wrap: true, // Enable word wrap to prevent horizontal scrolling
    },
    // 2 plugins for math support
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  vite: {
    resolve: {
      // Very import alias to make @blocks work for rollup
      alias: {
        "@blocks": path.resolve("../blocks/"),
      },
    },
  },
});
