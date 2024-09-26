from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for soil moisture data


class SoilData(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_texture = models.CharField(max_length=100)
    rainfall = models.FloatField()
    soil_moisture = models.FloatField()
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.date} {self.time} - {self.location} - Soil Moisture: {self.soil_moisture}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

