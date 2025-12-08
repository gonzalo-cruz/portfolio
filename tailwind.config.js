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
  paper: '#f2f0e9',          // Warm Alabaster (Not white)
  'paper-border': '#e0ded5', // Darker stone
  rust: '#c05621',           // Burnt Clay / Terra Cotta (Primary)
  ink: '#2d2a26',            // Soft Charcoal (Not black)
  'ink-light': '#5e5b56',    // Warm Grey
  parchment: '#e6e4dc',      // Secondary bg
  warm: {
    surface: '#1c1b1a',      // Warm Off-Black (Dark Mode BG)
    border: '#33302c',       // Warm Grey Border
    text: '#e8e6e3',         // Bone White (Text)
    subtext: '#a8a29e',      // Warm Grey Subtext
    black: '#121110'         // Deepest Warm Tone
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
