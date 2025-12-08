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
  paper: '#f3f4f6',          // Mist Grey
  'paper-border': '#e5e7eb', 
  rust: '#be123c',           // Faded Red (Primary)
  ink: '#111827',            // Soft Navy Black
  'ink-light': '#4b5563',    
  parchment: '#e5e7eb',      
  warm: {
    surface: '#18181b',      // Zinc 900 (Soft Industrial Dark)
    border: '#27272a',       
    text: '#e4e4e7',         // Zinc 200
    subtext: '#a1a1aa',      // Zinc 400
    black: '#09090b'         
  }
},
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
