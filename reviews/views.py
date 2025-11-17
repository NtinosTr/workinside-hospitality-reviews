from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.signing import dumps, loads, SignatureExpired, BadSignature
from django.db.models import Avg, Count, Q, Subquery, OuterRef
from django.http import JsonResponse
from datetime import datetime, timedelta
import re

from .models import Hotel, Department, Review


# ================================ MODERATION ================================

BANNED_KEYWORDS = ["fuck", "shit", "bitch", "asshole", "cunt", "racist"]
SENSITIVE_KEYWORDS = ["abuse", "harass", "violence", "unsafe"]


def contains_sensitive(text):
    if not text:
        return False
    t = text.lower()
    return any(k in t for k in SENSITIVE_KEYWORDS)


def contains_contact(text):
    if not text:
        return False
    if "@" in text or "http" in text or "www" in text:
        return True
    if re.search(r"\b\d{8,}\b", text):
        return True
    return False


def contains_banned(text):
    if not text:
        return False
    t = text.lower()
    return any(k in t for k in BANNED_KEYWORDS)


# ================================ HOME PAGE ================================

def home_page(request):

    # Subquery: average rating only from verified reviews
    avg_rating_subquery = (
        Review.objects
        .filter(hotel=OuterRef("pk"), is_verified=True)
        .values("hotel")
        .annotate(avg=Avg("rating"))
        .values("avg")[:1]
    )

    top_hotels = (
        Hotel.objects
        .annotate(avg_rating=Subquery(avg_rating_subquery))
        .filter(avg_rating__isnull=False)
        .order_by("-avg_rating")[:10]
    )

    return render(request, "reviews/home.html", {
        "top_hotels": top_hotels,
    })


# ================================ REVIEW FORM ================================

def review_form_page(request):
    departments = Department.objects.all()

    if request.method == "POST":

        # Google Autocomplete fields
        hotel_name = request.POST.get("hotel_name")
        hotel_location = request.POST.get("hotel_address") or ""
        hotel_lat = request.POST.get("hotel_lat") or ""
        hotel_lon = request.POST.get("hotel_lon") or ""

        if not hotel_name:
            return render(request, "reviews/review_form.html", {
                "departments": departments,
                "error": "Please choose a hotel from suggestions."
            })

        # Create OR get hotel
        hotel, created = Hotel.objects.get_or_create(
            name=hotel_name,
            defaults={
                "location": hotel_location,
                "latitude": hotel_lat,
                "longitude": hotel_lon,
            }
        )

        # update only missing fields
        if not created:
            changed = False
            if not hotel.location:
                hotel.location = hotel_location
                changed = True
            if not hotel.latitude:
                hotel.latitude = hotel_lat
                changed = True
            if not hotel.longitude:
                hotel.longitude = hotel_lon
                changed = True
            if changed:
                hotel.save()

        # Review fields
        comment = request.POST.get("comment", "").strip()
        rating = request.POST.get("rating")
        name = request.POST.get("name") or "Anonymous"
        email = request.POST.get("email")

        # validation rules
        errors = []
        if len(comment) < 20:
            errors.append("Write at least 20 characters.")
        if contains_contact(comment):
            errors.append("Do not include emails, phones or links.")
        if contains_banned(comment):
            errors.append("Please avoid inappropriate language.")

        if errors:
            return render(request, "reviews/review_form.html", {
                "departments": departments,
                "error": " ".join(errors)
            })

        is_sensitive = contains_sensitive(comment)

        # Create review
        review = Review.objects.create(
            hotel=hotel,
            department_id=request.POST.get("department"),
            rating=rating,
            comment=comment,
            name=name,
            email=email,
            is_verified=False,
            is_sensitive=is_sensitive
        )

        # EMAIL CONFIRMATION
        if email:
            token = dumps({"review_id": review.id}, salt="review-confirm")
            confirm_url = request.build_absolute_uri(f"/reviews/confirm/{token}")

            send_mail(
                "Confirm Your WorkInside Review",
                "",
                "no-reply@workinside.com",
                [email],
                html_message=f"<p>Click to verify your review:</p><a href='{confirm_url}'>{confirm_url}</a>"
            )

        msg = (
            "This review contains sensitive issues and requires manual approval."
            if is_sensitive else
            "Please check your email to verify the review."
        )

        return render(request, "reviews/review_submitted.html", {"message": msg})

    # GET request
    return render(request, "reviews/review_form.html", {
        "departments": departments
    })


# ================================ CONFIRMATION ================================

def review_confirm(request, token):
    try:
        data = loads(token, salt="review-confirm", max_age=604800)
    except SignatureExpired:
        return render(request, "reviews/review_confirm.html", {"error": "Expired link."})
    except BadSignature:
        return render(request, "reviews/review_confirm.html", {"error": "Invalid link."})

    review = Review.objects.get(id=data["review_id"])
    review.is_verified = True
    review.save()

    return render(request, "reviews/review_confirm.html", {"success": "Review verified!"})


# ================================ HOTEL DETAIL ================================

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    departments = Department.objects.all()

    reviews = Review.objects.filter(
        hotel=hotel,
        is_verified=True,
        is_sensitive=False
    ).order_by("-created_at")

    stats = reviews.aggregate(avg=Avg("rating"), total=Count("id"))

    return render(request, "reviews/hotel_detail.html", {
        "hotel": hotel,
        "departments": departments,
        "reviews": reviews[:5],
        "avg_rating": stats["avg"],
        "review_count": stats["total"],
    })


# ================================ FILTER REVIEWS ================================

def filter_reviews(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    department = request.GET.get("department")
    rating = request.GET.get("rating")
    sort = request.GET.get("sort", "newest")

    reviews = Review.objects.filter(
        hotel=hotel,
        is_verified=True,
        is_sensitive=False
    )

    if department:
        reviews = reviews.filter(department_id=department)
    if rating:
        reviews = reviews.filter(rating__gte=rating)

    reviews = reviews.order_by("-created_at" if sort == "newest" else "created_at")

    return render(request, "reviews/reviews_list.html", {"reviews": reviews[:5]})


# ================================ LOAD MORE ================================

def load_more_reviews(request, hotel_id):
    offset = int(request.GET.get("offset", 0))
    reviews = Review.objects.filter(
        hotel_id=hotel_id,
        is_verified=True,
        is_sensitive=False,
    ).order_by("-created_at")[offset:offset + 5]

    return render(request, "reviews/reviews_list.html", {"reviews": reviews})


# ================================ SEARCH BAR ================================

def search_hotels(request):
    q = request.GET.get("q", "").strip()

    hotels = Hotel.objects.filter(name__icontains=q)[:10] if q else Hotel.objects.all()[:10]

    return JsonResponse({
        "results": [
            {
                "id": h.id,
                "name": h.name,
                "country": h.location or ""
            }
            for h in hotels
        ]
    })


# ================================ STATIC PAGES ================================

def privacy(request):
    return render(request, "reviews/legal/privacy.html")

def terms(request):
    return render(request, "reviews/legal/terms.html")

def cookies(request):
    return render(request, "reviews/legal/cookies.html")


# ================================ REMOVE REVIEW ================================

def remove_review_page(request):
    if request.method == "POST":
        return render(request, "reviews/legal/remove_review.html", {
            "success": "Your request was submitted."
        })
    return render(request, "reviews/legal/remove_review.html")


# ================================ CONTACT PAGE ================================

def contact_page(request):
    return render(request, "contact/contact.html")


# ================================ ADD HOTEL PAGE ================================

def add_hotel_page(request):
    return render(request, "reviews/add_hotel.html")
