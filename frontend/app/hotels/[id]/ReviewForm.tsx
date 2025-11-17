"use client";

import { useState } from "react";

export default function ReviewForm({ hotelId, departments }) {
  const [rating, setRating] = useState("");
  const [comment, setComment] = useState("");

  const submitReview = async () => {
    const res = await fetch(`http://127.0.0.1:8000/api/hotels/${hotelId}/add-review/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ rating, comment }),
    });

    if (res.ok) {
      alert("Review submitted successfully!");
      location.reload();
    } else {
      alert("Failed to submit review.");
    }
  };

  return (
    <div className="space-y-3 bg-white p-4 border border-gray-200 rounded-xl shadow-sm">
      <h3 className="font-medium">Write a Review</h3>

      <input
        type="number"
        placeholder="Rating (1-10)"
        value={rating}
        onChange={(e) => setRating(e.target.value)}
        className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm"
      />

      <textarea
        placeholder="Your comment..."
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm"
      />

      <button
        onClick={submitReview}
        className="bg-[#6d28d9] text-white rounded-lg px-4 py-2 text-sm hover:bg-[#5b21b6]"
      >
        Submit Review
      </button>
    </div>
  );
}
