from django.db import models
from django.conf import settings
# Create your models here.


class Tutor(models.Model):
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200,default="")
    picture = models.ImageField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    hourly_rate = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    numRatings = models.IntegerField(default=0)

    bio = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name="subjects")


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


class Request(models.Model):
    Tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
    )
    Tutee = models.ForeignKey(
        Tutee,
        on_delete=models.CASCADE,
    )
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('finished', 'Finished'),
    ]
    zoom_link = models.URLField()
    status = models.CharField(choices=STATUS_CHOICES,default="pending",max_length=200, null=True, blank=True)



class RequestTimeslot(models.Model):
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    request = models.ForeignKey(
        Request,null=True, on_delete=models.CASCADE, related_name="timeslots")

class TransactionTable(models.Model):
    Tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
    )
    Tutee = models.ForeignKey(
        Tutee,
        on_delete=models.CASCADE,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    charge = models.FloatField()
    duration = models.DateTimeField()
    status = models.IntegerField()  # states: 1.finished, 2.scheduled, 3.pending 4.invalid
