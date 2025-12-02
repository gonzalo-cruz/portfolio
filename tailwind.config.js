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
      paper: '#fdf6e3',          // Solarized Base3
      'paper-border': '#eee8d5', 
      rust: '#cb4b16',           // Solarized Orange
      ink: '#657b83',            // Solarized Base00
      'ink-light': '#93a1a1',    
      parchment: '#eee8d5',      
      warm: {
        surface: '#002b36',      // Solarized Base03
        border: '#073642',
        text: '#839496',
        subtext: '#586e75',
        black: '#002b36'
      }
    },
    fontFamily: {
      sans: ['Lato', 'sans-serif'],
      serif: ['Lato', 'serif'],
      mono: ['Inconsolata', 'monospace'],
    },
  },
},
  plugins: [require('@tailwindcss/typography')],
}
