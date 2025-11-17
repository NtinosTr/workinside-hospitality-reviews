"use client";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";

export default function SubmitReview() {
  const { id } = useParams<{ id: string }>();
  // Σε κάποιες περιπτώσεις το useParams μπορεί να δώσει array.
  const hotelId = Array.isArray(id) ? id[0] : id;

  const [departments, setDepartments] = useState<any[]>([]);
  const [department, setDepartment] = useState("");
  const [rating, setRating] = useState("");
  const [comment, setComment] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!hotelId) return;
    fetch(`http://127.0.0.1:8000/api/hotels/${hotelId}/departments/`)
      .then((res) => res.json())
      .then((data) => setDepartments(data))
      .catch((err) => console.error("Departments fetch error:", err))
      .finally(() => setLoading(false));
  }, [hotelId]);

  const submit = async () => {
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/hotels/${hotelId}/reviews/add/`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ rating, comment, department }),
        }
      );

      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        alert(`❌ Failed to submit review.${err?.error ? " " + err.error : ""}`);
        return;
      }

      alert("✅ Review submitted!");
      location.href = `/hotels/${hotelId}`;
    } catch (e) {
      console.error(e);
      alert("❌ Failed to submit review.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center text-center gap-4 px-4">
      <h1 className="text-3xl font-bold mb-2">Submit your review</h1>

      {loading ? (
        <p>Loading departments…</p>
      ) : (
        <>
          <select
            className="text-black p-2 rounded"
            value={department}
            onChange={(e) => setDepartment(e.target.value)}
          >
            <option value="">Select department</option>
            {departments.map((d) => (
              <option key={d.id} value={d.id}>
                {d.name}
              </option>
            ))}
          </select>

          <input
            type="number"
            placeholder="Rating (1 - 10)"
            className="text-black p-2 rounded"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
            min={1}
            max={10}
          />

          <textarea
            placeholder="Your experience..."
            className="text-black p-2 rounded w-80 h-32"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
          />

          <button
            onClick={submit}
            className="px-5 py-2 rounded bg-purple-500 hover:bg-purple-600 transition text-white"
            disabled={!department || !rating || !comment}
          >
            Submit Review
          </button>
        </>
      )}
    </div>
  );
}
