"use client";
import { use, useState, useEffect } from "react";

export default function HotelPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params); // ✅ σωστό ξετύλιγμα promise

  const [hotel, setHotel] = useState<any>(null);
  const [reviews, setReviews] = useState<any[]>([]);
  const [departments, setDepartments] = useState<any[]>([]);

  useEffect(() => {
    // Fetch hotel info
    fetch(`http://127.0.0.1:8000/api/hotels/${id}/`)
      .then((res) => res.json())
      .then((data) => setHotel(data));

    // Fetch reviews
    fetch(`http://127.0.0.1:8000/api/hotels/${id}/reviews/`)
      .then((res) => res.json())
      .then((data) => setReviews(data));

    // Fetch departments
    fetch(`http://127.0.0.1:8000/api/hotels/${id}/departments/`)
      .then((res) => res.json())
      .then((data) => setDepartments(data));
  }, [id]);

  if (!hotel) return <p className="text-center mt-20">Loading...</p>;

  return (
    <main className="p-6 text-center">
      <h1 className="text-3xl font-semibold mb-4">{hotel.name}</h1>
      <p className="text-gray-400 mb-6">{hotel.location}</p>

      <h2 className="text-xl font-semibold mt-10 mb-3">Departments</h2>
      <ul className="space-y-1 text-purple-300">
        {departments.map((d) => (
          <li key={d.id}>{d.name}</li>
        ))}
      </ul>

      <h2 className="text-xl font-semibold mt-10 mb-3">Reviews</h2>
      {reviews.length === 0 && <p className="text-gray-500">No reviews yet.</p>}
      <ul className="space-y-4 mt-4">
        {reviews.map((r) => (
          <li key={r.id} className="bg-gray-800 p-4 rounded text-left">
            <p className="text-purple-300">{r.department_name}</p>
            <p className="text-yellow-400 font-semibold">Rating: {r.rating}/10</p>
            <p className="text-gray-300 mt-2">{r.comment}</p>
          </li>
        ))}
      </ul>
    </main>
  );
}
