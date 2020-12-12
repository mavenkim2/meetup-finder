from django.db import models
from django.contrib.auth.models import User
import datetime


class Event(models.Model):
    title = models.CharField('Title', max_length=200)
    day = models.DateField('Day', default=datetime.date.today, help_text='YYYY-MM-DD')
    info = models.TextField(blank=True)
    image = models.FileField(upload_to="images/", blank=True)
    location = models.CharField('Location', default='', max_length=500, blank=True)
    poster = models.CharField('Poster', default='', max_length=25)


class RegisteredEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)


class CreatedEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
