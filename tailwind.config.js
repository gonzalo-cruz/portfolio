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
  paper: '#eaeaeb',          // Mist Grey (Not white)
  'paper-border': '#d4d4d8', // Zinc 300
  rust: '#e4e4e7',           // Zinc 200 (High contrast highlight for Dark Mode)
  ink: '#27272a',            // Soft Black (Zinc 800)
  'ink-light': '#52525b',    // Zinc 600
  parchment: '#f4f4f5',      // Zinc 100
  warm: {
    surface: '#18181b',      // Zinc 900 (Soft Industrial Dark BG)
    border: '#27272a',       
    text: '#f4f4f5',         // Zinc 100 text
    subtext: '#a1a1aa',      // Zinc 400 subtext
    black: '#09090b'         // Zinc 950
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
