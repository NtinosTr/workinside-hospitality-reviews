from django.contrib import admin
from .models import Hotel, Department, Review


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name", "location")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("hotel", "department", "rating", "email", "created_at", "is_verified", "is_sensitive")
    list_filter = ("hotel", "department", "rating", "is_verified", "is_sensitive")
    search_fields = ("hotel__name", "department__name", "comment", "email", "name")
    ordering = ("-created_at",)
