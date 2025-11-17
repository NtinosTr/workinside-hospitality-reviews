export default function Navbar() {
  return (
    <nav className="w-full py-4 px-6 flex justify-between items-center text-sm text-gray-300">
      <a href="/" className="font-semibold text-white hover:text-purple-300 transition">
        WorkInside
      </a>

      <div className="flex gap-6">
        <a href="/reviews" className="hover:text-purple-300 transition">
          Submit Review
        </a>
        <a href="/hotels" className="hover:text-purple-300 transition">
          View Hotels
        </a>
      </div>
    </nav>
  );
}
