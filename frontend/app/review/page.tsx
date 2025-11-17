"use client";
import { useState, useEffect } from "react";

export default function ReviewFormPage() {
  const [hotels, setHotels] = useState<any[]>([]);
  const [departments, setDepartments] = useState<any[]>([]);
  const [selectedHotel, setSelectedHotel] = useState("");
  const [selectedDepartment, setSelectedDepartment] = useState("");
  const [rating, setRating] = useState("");
  const [comment, setComment] = useState("");

  // Load hotels
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/hotels/")
      .then((res) => res.json())
      .then((data) => setHotels(data));
  }, []);

  // Load departments when hotel is selected
  useEffect(() => {
    if (!selectedHotel) return;
    fetch(`http://127.0.0.1:8000/api/hotels/${selectedHotel}/departments/`)
      .then((res) => res.json())
      .then((data) => setDepartments(data));
  }, [selectedHotel]);

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    const reviewData = {
      hotel: selectedHotel,
      department: selectedDepartment,
      rating: Number(rating),
      comment,
      author: "Anonymous",
    };

    const response = await fetch("http://127.0.0.1:8000/api/reviews/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(reviewData),
    });

    if (response.ok) {
      alert("Review submitted successfully!");
      setSelectedHotel("");
      setSelectedDepartment("");
      setRating("");
      setComment("");
    } else {
      alert("Something went wrong.");
    }
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-6 text-center">
      <h1 className="text-3xl font-semibold mb-6">Submit a Review</h1>

      <form onSubmit={handleSubmit} className="w-full max-w-md space-y-4">
        <select
          value={selectedHotel}
          onChange={(e) => setSelectedHotel(e.target.value)}
          required
          className="w-full p-2 rounded bg-gray-800 border border-gray-600"
        >
          <option value="">Select Hotel</option>
          {hotels.map((hotel) => (
            <option key={hotel.id} value={hotel.id}>
              {hotel.name}
            </option>
          ))}
        </select>

        <select
          value={selectedDepartment}
          onChange={(e) => setSelectedDepartment(e.target.value)}
          required
          disabled={!departments.length}
          className="w-full p-2 rounded bg-gray-800 border border-gray-600"
        >
          <option value="">Select Department</option>
          {departments.map((dept) => (
            <option key={dept.id} value={dept.id}>
              {dept.name}
            </option>
          ))}
        </select>

        <input
          type="number"
          placeholder="Rating (1-10)"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
          min="1"
          max="10"
          required
          className="w-full p-2 rounded bg-gray-800 border border-gray-600"
        />

        <textarea
          placeholder="Share your experience..."
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="w-full p-2 rounded bg-gray-800 border border-gray-600 h-24"
        />

        <button
          type="submit"
          className="w-full py-2 bg-purple-600 hover:bg-purple-700 transition rounded text-white font-medium"
        >
          Submit Review
        </button>
      </form>
    </main>
  );
}
