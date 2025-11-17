from django.urls import path
from . import views_views

urlpatterns = [
    path("", views_views.hotel_reviews_page, name="hotel-reviews"),
]
