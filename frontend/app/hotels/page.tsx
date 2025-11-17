"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

export default function HotelsPage() {
  const [hotels, setHotels] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/hotels/")
      .then((res) => res.json())
      .then((data) => setHotels(data));
  }, []);

  return (
    <div className="pt-16 px-6">
      <h1 className="text-3xl font-semibold text-purple-300 text-center mb-10">
        Browse Hotels
      </h1>
<a
  href={`/hotels/${id}/review`}
  className="px-5 py-2 rounded-full bg-purple-500 hover:bg-purple-600 transition text-sm font-medium"
>
  Write a Review
</a>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {hotels.map((hotel) => (
          <Link
            key={hotel.id}
            href={`/hotels/${hotel.id}`}
            className="block p-6 rounded-xl bg-[#13141a] border border-[#2a2b31] 
            transition-all duration-300
            hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(0,0,0,0.35)]
            hover:border-purple-400"
          >
            <h2 className="text-xl font-medium text-white">{hotel.name}</h2>
            <p className="text-sm text-gray-400 mt-1">{hotel.location}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
