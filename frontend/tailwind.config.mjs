/** @type {import('tailwindcss').Config} */
const config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navyGray: "#1a1f2b",   // Το νέο background μας
      },
    },
  },
  plugins: [],
};

export default config;
