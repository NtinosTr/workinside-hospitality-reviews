"use client";

import { useState } from "react";

export default function SearchBar() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);

  const search = async (value: string) => {
    setQuery(value);
    if (value.length < 3) return;

    const res = await fetch(`http://127.0.0.1:8000/api/hotels/search?q=${value}`);
    const data = await res.json();
    setResults(data);
  };

  return (
    <div className="w-full max-w-xl mx-auto mt-16">
      <input
        type="text"
        placeholder="Search hotels..."
        value={query}
        onChange={(e) => search(e.target.value)}
        className="w-full p-3 rounded-md border border-gray-600 bg-black text-white"
      />

      {results.length > 0 && (
        <ul className="mt-3 bg-gray-900 rounded-lg shadow-lg border border-gray-700">
          {results.map((hotel, index) => (
            <li
              key={index}
              className="p-3 hover:bg-gray-800 cursor-pointer"
            >
              {hotel.name} — {hotel.city}, {hotel.country}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
