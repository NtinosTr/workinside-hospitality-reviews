from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reviews import views as review_views

urlpatterns = [

    # 👉 Redirect root "/" -> Home Page
    path("", review_views.home_page, name="root_home"),

    # 👉 Reviews app
    path("reviews/", include("reviews.urls")),

    # 👉 Admin panel
    path("admin/", admin.site.urls),
]

# 👉 Serve static files only in DEBUG mode (όχι production)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
