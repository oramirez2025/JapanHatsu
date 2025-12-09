from django.db import models
from trips_app.models import Trip


# Create your models here.
class PreTripTask(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    helpful_link = models.CharField(max_length=500, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
