from django.urls import path, re_path
from . import views

urlpatterns = [

    # 🏠 Home Page
    path("", views.home_page, name="home"),

    # ✍️ Submit Review Page
    path("submit/", views.review_form_page, name="review_form"),

    # 📩 Email Confirmation (token)
    re_path(r"^confirm/(?P<token>.+)/$", views.review_confirm, name="review_confirm"),

    # 🏨 Hotel Detail Page
    path("hotel/<int:hotel_id>/", views.hotel_detail, name="hotel_detail"),

    # 🔍 Filter Reviews
    path("hotel/<int:hotel_id>/filter/", views.filter_reviews, name="filter_reviews"),

    # 📜 Load More Reviews
    path("hotel/<int:hotel_id>/load-more/", views.load_more_reviews, name="load_more_reviews"),

    # 🔎 Local DB Hotel Search (άνω μπάρα)
    path("search/", views.search_hotels, name="search_hotels"),

    # 🌍 OSM/Google API Autocomplete for review form

    # 📄 Legal pages
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("cookies/", views.cookies, name="cookies"),

    # ⚖️ Remove Review Request Page
    path("remove-review/", views.remove_review_page, name="remove_review"),

    # 📩 Contact page
    path("contact/", views.contact_page, name="contact"),

    # ➕ Add hotel manually (dev tool)
    path("add-hotel/", views.add_hotel_page, name="add_hotel"),
]
