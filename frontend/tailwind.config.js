// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
      c1: '#1e1e1e',
      c2: '#121019',
      c3: '#fd0000',
      c4: '#1e1e1e',
      c5: '#1e1e1e',
      c6: '#1e1e1e',
      },
    },
  },
  plugins: [],
}