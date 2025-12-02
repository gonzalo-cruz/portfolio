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
      paper: '#f2f5f3',          // Light Sage
      'paper-border': '#dde5e0', 
      rust: '#2d6a4f',           // Forest Green (Replacing Rust)
      ink: '#1b4332',            // Dark Green
      'ink-light': '#52796f',    
      parchment: '#e8ece9',      
      warm: {
        surface: '#1b4332',      // Dark Forest
        border: '#2d6a4f',
        text: '#d8f3dc',
        subtext: '#95d5b2',
        black: '#081c15'
      }
    },
    fontFamily: {
      sans: ['DM Sans', 'sans-serif'],
      serif: ['Lora', 'serif'],
      mono: ['Fira Code', 'monospace'],
    },
  },
},
  plugins: [require('@tailwindcss/typography')],
}
