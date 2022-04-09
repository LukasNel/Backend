from django.db import models
from django.conf import settings
# Create your models here.


class Subject(models.Model):
    subject = models.CharField(max_length = 100)

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
        Timeslot,
        on_delete=models.CASCADE,
    )
    subjects = models.OneToMany(
        Subject,
        on_delete=models.CASCADE,
    )
    bio = models.CharField(max_length=200)

class Timeslot(models.Model):
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name="availability")

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

class Request(models.Model):
    Tutor = models.OneToOneField(
        Tutor,
        on_delete=models.CASCADE,
    )
    Tutee = models.OneToOneField(
        Tutee,
        on_delete=models.CASCADE,
    )
    zoom_link = models.urls()
    time_request = models.DateTimeField()