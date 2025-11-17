from django.shortcuts import render, get_object_or_404
from .models import Review, Hotel

def hotel_reviews_page(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    reviews = Review.objects.filter(hotel_id=hotel_id).order_by("-id")
    return render(request, "reviews/hotel_reviews.html", {
        "hotel": hotel,
        "reviews": reviews
    })
