import "./globals.css";
import { Plus_Jakarta_Sans } from "next/font/google";
import Navbar from "../components/Navbar";

const jakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
});

export const metadata = {
  title: "WorkInside",
  description: "Anonymous Workplace Reviews for Hotel Employees",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={jakarta.className}>
      <body className="bg-[#0f1115] text-white">
        <Navbar />
        {children}
      </body>
    </html>
  );
}
