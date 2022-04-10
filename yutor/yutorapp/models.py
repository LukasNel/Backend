from django.db import models
from django.conf import settings
from requests import request
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Tutor(models.Model):
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200, default="")
    picture = models.ImageField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    hourly_rate = models.FloatField(default=0)
    numRatings = models.IntegerField(default=0)

    bio = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Timeslot(models.Model):
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name="timeslots")



class Tutee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    picture = models.ImageField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    rating = models.FloatField()
    numRatings = models.IntegerField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Subject(models.Model):
    def __str__(self) -> str:
        return self.subject_name + ' - ' + str(self.tutor)
    subject_name = models.CharField(max_length=200, default="")
    tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE, related_name="subjects" )

class Request(models.Model):
    Tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
    )
    Tutee = models.ForeignKey(
        Tutee,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s %s - %s %s' % (self.Tutor.first_name, self.Tutor.last_name,
                                  self.Tutee.first_name, self.Tutee.last_name)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('finished', 'Finished'),
    ]
    zoom_link = models.URLField()
    status = models.CharField(
        choices=STATUS_CHOICES, default="pending", max_length=200, null=True, blank=True)
    tutor_done = models.BooleanField(default=False)
    tutee_done = models.BooleanField(default=False)


class Rating(models.Model):
    rating = models.IntegerField()
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name="ratings")
    comment = models.CharField(max_length=400, default="", blank=True)


class RequestTimeslot(models.Model):
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    zoom_link = models.URLField()

    request = models.ForeignKey(
        Request, null=True, on_delete=models.CASCADE, related_name="timeslots")


class Transaction(models.Model):
    requesttimeslot = models.ForeignKey(
        RequestTimeslot,
        on_delete=models.CASCADE,
    )
    tutor = models.ForeignKey(
        Tutor, related_name="transactions", on_delete=models.CASCADE)
    charge = models.FloatField()
