from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# jibmbe_app/models.py


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)

class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Place(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance = models.FloatField(default=0.0)

class Event(models.Model):
    # Your event model fields go here
    name = models.CharField(max_length=255)
    date = models.DateField()
    # ... other fields

    def __str__(self):
        return self.name