// tailwind.config.cjs
const starlightPlugin = require("@astrojs/starlight-tailwind");
const colors = require("tailwindcss/colors");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        // Your preferred accent color. Indigo is closest to Starlight’s defaults.
        accent: colors.indigo,
        // Your preferred gray scale. Zinc is closest to Starlight’s defaults.
        gray: colors.zinc,
      },
      fontFamily: {
        // Your preferred text font. Starlight uses a system font stack by default.
        sans: ['"Atkinson Hyperlegible"'],
        // Your preferred code font. Starlight uses system monospace fonts by default.
        mono: ['"IBM Plex Mono"'],
      },
    },
  },
  plugins: [starlightPlugin()],
};
