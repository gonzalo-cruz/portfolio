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
  paper: '#f9f8f4',          // Aged Ivory
  'paper-border': '#e3e1da', 
  rust: '#4e8087',           // Muted Retro Teal
  ink: '#222f33',            // Deep Slate Ink
  'ink-light': '#546a70',    // Slate Grey
  parchment: '#f0efea',      
  warm: {
    surface: '#161a1b',      // Deep Slate Off-Black (Dark Mode BG)
    border: '#2a3438',       
    text: '#e6eaea',         // Off-white slate text
    subtext: '#8ca3a8',      // Muted blue-grey subtext
    black: '#0b0d0e'         
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
