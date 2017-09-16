from django.db import models
from django.contrib.auth.models import User


# Interest class used for tagging (by Users and Events)
class Interest(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=40, primary_key=True, default="None")

    def __str__(self):
        return self.name


# Extend the User class to include relation with Interests
# Only the interests field requires a lookup of the ExtUser,
# everything else can be handled
class ExtUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False)
    interests = models.ManyToManyField(Interest)
    school = models.OneToOneField(School, null=True)

    def __str__(self):
        return self.user.username


# Model for an event entity
class Event(models.Model):
    title = models.CharField(max_length=75)
    startTime = models.DateTimeField
    endTime = models.DateTimeField
    description = models.TextField(max_length=1000)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.title


# Create a separated table for searching for attendees of events
class Attendee(models.Model):
    user = models.OneToOneField(ExtUser)
    event = models.OneToOneField(Event)
