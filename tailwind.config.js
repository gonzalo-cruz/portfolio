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
  paper: '#efede6',          // Antique Paper
  'paper-border': '#dcd8cd', 
  rust: '#a36a2c',           // Muted Bronze / Saddle Brown
  ink: '#292524',            // Warm Stone Ink
  'ink-light': '#57534e',    // Stone Grey
  parchment: '#e7e5e4',      
  warm: {
    surface: '#1c1917',      // Warm Stone 900 (Dark Mode BG)
    border: '#44403c',       
    text: '#f5f5f4',         // Stone 100 text
    subtext: '#a8a29e',      // Stone 400 subtext
    black: '#0c0a09'         
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
