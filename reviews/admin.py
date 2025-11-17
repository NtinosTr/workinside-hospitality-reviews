from django.contrib import admin
from .models import Hotel, Department, Review


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("hotel", "department", "rating", "email", "created_at")
    list_filter = ("hotel", "department", "rating")
    search_fields = ("hotel__name", "department__name", "comment", "email")
