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
  paper: '#f7f3e8',          // Warm Eggshell
  'paper-border': '#e6dfd1', 
  rust: '#c77d57',           // Muted Terra Cotta / Faded Orange
  ink: '#332d2a',            // Warm Sepia Ink
  'ink-light': '#6e635b',    // Warm Brown-Grey
  parchment: '#ede7dc',      
  warm: {
    surface: '#1f1c1a',      // Warm Sepia Off-Black (Dark Mode BG)
    border: '#38312d',       
    text: '#f2ebe3',         // Cream text
    subtext: '#ada399',      // Warm subtext
    black: '#14110f'         
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
