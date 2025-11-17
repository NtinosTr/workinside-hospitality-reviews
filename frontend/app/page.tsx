export default function HomePage() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center text-center px-4">
      <h2 className="text-lg text-gray-300 mb-2">
        Your experience matters and it deserves to be heard.
      </h2>

      <h1 className="text-4xl md:text-5xl font-semibold mb-6 text-white">
        Real Stories. Real Hotels. Real People.
      </h1>

      <div className="flex items-center gap-4 mt-4">
        <a
          href="/reviews"
          className="px-5 py-2 rounded-full bg-purple-500 hover:bg-purple-600 transition text-sm font-medium"
        >
          Submit a Review
        </a>

        <a
          href="/hotels"
          className="px-5 py-2 rounded-full border border-purple-400 hover:border-purple-300 text-purple-300 hover:text-purple-200 transition text-sm font-medium"
        >
          Browse Hotels
        </a>
      </div>
    </main>
  );
}
