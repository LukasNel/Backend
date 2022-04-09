from django.db import models
from django.conf import settings
# Create your models here.


class Tutor(models.Model):
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200,default="")
    picture = models.ImageField(null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    hourly_rate = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    numRatings = models.IntegerField(default=0)

    bio = models.CharField(max_length=200, default="")


class Subject(models.Model):
    subject = models.CharField(max_length=100)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name="subjects")


class Timeslot(models.Model):
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name="availability")


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
    zoom_link = models.URLField()
    time_request = models.DateTimeField()
    status = models.IntegerField()


class TransactionTable(models.Model):
    Tutor = models.OneToOneField(
        Tutor,
        on_delete=models.CASCADE,
    )
    Tutee = models.OneToOneField(
        Tutee,
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    charge = models.FloatField()
    duration = models.DateTimeField()
    status = models.IntegerField()  # states: 1.finished, 2.scheduled, 3.pending 4.invalid
