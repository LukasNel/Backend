from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.conf import settings
# Create your models here.

class Tutor(models.Model):
    first_name = models.CharField(max_length=200, default = "")
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    picture = models.ImageField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    hourly_rate = models.FloatField()
    rating = models.FloatField()
    numRatings = models.IntegerField()
    availability = 
    subjects = 
    bio = models.CharField(max_length=200)


    pub_date = models.DateTimeField('date published')

class Request(models.Model):
    Tutor = models.OneToOneField(Tutee)
    zoom_link = models.urls()
    time_requested = models.FloatField()
