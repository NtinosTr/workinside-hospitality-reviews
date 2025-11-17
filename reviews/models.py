from django.db import models


# ---------------------------
# DEPARTMENT MODEL
# ---------------------------
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ---------------------------
# HOTEL MODEL (only ONE!)
# ---------------------------
class Hotel(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)

    # MANY TO MANY to departments
    departments = models.ManyToManyField(Department, related_name="hotels")

    def __str__(self):
        return self.name


# ---------------------------
# REVIEW MODEL
# ---------------------------
class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    rating = models.IntegerField()
    comment = models.TextField()
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_verified = models.BooleanField(default=False)
    is_sensitive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hotel.name} - {self.rating}/10"
