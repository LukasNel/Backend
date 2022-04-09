from django.db import models
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
    availability = models.OneToMany(
        base_field = 
        size = 
    )
    subjects = models.OneToMany(
        base_field = models.CharField(max_length = 50),
        size = 
    )
    bio = models.CharField(max_length=200)

class Tutee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    picture = models.ImageField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    rating = models.FloatField()
    numRatings = models.IntegerField()
    bio = models.CharField(max_length=200)


    pub_date = models.DateTimeField('date published')

