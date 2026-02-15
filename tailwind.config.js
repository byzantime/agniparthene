/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/templates/**/*.html", "./build/**/*.html"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        parchment: {
          50: '#fdfcfa',
          100: '#faf8f3',
          200: '#f5f0e6',
          300: '#ebe3d3',
          400: '#d9cdb5',
        },
        liturgical: {
          gold: '#c9a227',
          rose: '#a5b9d4',
          crimson: '#8b1538',
          navy: '#1a1a2e',
          dark: '#0f0f1a',
        },
      },
      fontFamily: {
        serif: ['"Noto Serif"', 'Georgia', 'serif'],
      },
      lineHeight: {
        'relaxed': '1.7',
        'loose': '1.85',
      },
    },
  },
  plugins: [],
}
