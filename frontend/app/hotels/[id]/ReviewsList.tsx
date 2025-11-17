export default function ReviewsList({ reviews }) {
  if (!reviews.length) {
    return <p className="text-gray-500 text-sm">No reviews yet. Be the first to write one!</p>;
  }

  return (
    <div className="space-y-4">
      {reviews.map((review) => (
        <div key={review.id} className="bg-white border border-gray-200 rounded-xl p-4 shadow-sm">
          <p className="text-sm text-gray-700">{review.comment}</p>
          <p className="text-xs text-gray-400 mt-2">
            Rating: {review.rating}/10 — {review.author}
          </p>
        </div>
      ))}
    </div>
  );
}
