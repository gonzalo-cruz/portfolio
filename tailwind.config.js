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
  paper: '#f4f7f2',          // Sage Cream (Not white)
  'paper-border': '#e0e6dd', 
  rust: '#5a8263',           // Muted Olive / Sage Green (Primary)
  ink: '#2c332f',            // Deep Forest Charcoal
  'ink-light': '#5f6e65',    // Muted Green-Grey
  parchment: '#e9ede6',      
  warm: {
    surface: '#1a1d1b',      // Warm Green-Black (Dark Mode BG)
    border: '#2f3832',       
    text: '#e8ece9',         // Off-white text
    subtext: '#9ca8a1',      // Sage subtext
    black: '#0f1210'         // Deepest tone
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
