from django.contrib import admin
from django.urls import path, include
from reviews import views as review_views

urlpatterns = [

    # 👉 Redirect root "/" -> "/reviews/"
    path("", review_views.home_page, name="root_home"),

    # 👉 Reviews app
    path("reviews/", include("reviews.urls")),

    # 👉 Admin panel
    path("admin/", admin.site.urls),
]

# ❌ Remove custom handlers (they don't exist yet)
# handler404 = "reviews.views.error_404"
# handler500 = "reviews.views.error_500"
