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
      paper: '#282a36',          // Dracula Background
      'paper-border': '#44475a', 
      rust: '#ff79c6',           // Dracula Pink
      ink: '#f8f8f2',            // Off White
      'ink-light': '#bd93f9',    // Dracula Purple
      parchment: '#44475a',      // Selection Color
      warm: {
        surface: '#282a36',      
        border: '#6272a4',
        text: '#f8f8f2',
        subtext: '#8be9fd',      // Cyan
        black: '#21222c'
      }
    },
    fontFamily: {
      sans: ['Fira Sans', 'sans-serif'],
      serif: ['Fira Sans', 'sans-serif'],
      mono: ['Fira Code', 'monospace'],
    },
  },
},
  plugins: [require('@tailwindcss/typography')],
}
