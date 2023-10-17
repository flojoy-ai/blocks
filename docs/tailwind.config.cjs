// tailwind.config.cjs
const defaultTheme = require("tailwindcss/defaultTheme");
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
        accent1: {
          DEFAULT: "rgb(var(--color-accent1) / <alpha-value>)",
          hover: "rgb(var(--color-accent1-hover) / <alpha-value>)",
        },
        accent2: "rgb(var(--color-accent2) / <alpha-value>)",
        accent3: "rgb(var(--color-accent3) / <alpha-value>)",
        accent4: "rgb(var(--color-accent4) / <alpha-value>)",
      },
      fontFamily: {
        // Your preferred text font. Starlight uses a system font stack by default.
        sans: ['"Open Sans"', "sans-serif", ...defaultTheme.fontFamily.sans],
        // Your preferred code font. Starlight uses system monospace fonts by default.
        mono: ['"IBM Plex Mono"'],
      },
    },
  },
  plugins: [starlightPlugin()],
};
