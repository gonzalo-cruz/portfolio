/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
        serif: ['Lora', 'serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      colors: {
        'warm-black': '#191714',
        'warm-surface': '#262320',
        'warm-border': '#3A3632',
        'warm-text': '#F0EFEA',
        'warm-subtext': '#B0AEA5',
        'parchment': '#FDF9F3',
        'paper': '#FFFFFF',
        'paper-border': '#E0DCD4',
        'ink': '#191714',
        'ink-light': '#4A4540',
        'rust': '#D97757',
        'sage': '#788C5D',
        'slate': '#6A9BCC',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
