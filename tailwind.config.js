/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
  extend: {
    colors: {
      paper: '#000000',          // Pure Black
      'paper-border': '#333333', 
      rust: '#00ff41',           // Matrix/Neon Green
      ink: '#ffffff',            // White
      'ink-light': '#a3a3a3',    // Grey
      parchment: '#111111',      // Very Dark Grey
      warm: {
        surface: '#1a1a1a',      // Dark Mode BG (slightly lighter)
        border: '#333333',
        text: '#00ff41',         // Green Text
        subtext: '#cccccc',
        black: '#000000'
      }
    },
    fontFamily: {
      sans: ['Space Grotesk', 'sans-serif'],
      serif: ['Space Grotesk', 'sans-serif'], // Mono-vibe everywhere
      mono: ['Space Grotesk', 'monospace'],
    },
  },
},
  plugins: [require('@tailwindcss/typography')],
}
