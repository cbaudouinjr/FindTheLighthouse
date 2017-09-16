from django.db import models
from django.contrib.auth.models import AbstractUser


# Interest class used for tagging (by Users and Events)
class Interest(models.Model):
    name = models.CharField(max_length=20, primary_key=True)


# Extend the User class to include relation with Interests
# *** Access this class via AUTH_USER_MODEL in settings.py ***
class User(AbstractUser):
    interests = models.ManyToManyField(Interest)


# Model for an event entity
class Event(models.Model):
    title = models.CharField(max_length=75)
    startTime = models.DateTimeField
    endTime = models.DateTimeField
    description = models.TextField(max_length=1000)
    interests = models.ManyToManyField(Interest)


# Create a separated table for searching for attendees of events
class Attendee(models.Model):
    user = models.OneToOneField(User)
    event = models.OneToOneField(Event)
