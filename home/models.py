from django.db import models

from django.contrib.auth.models import User


class Child(models.Model):
    parent = models.ForeignKey(User)
    rfid_tag = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    child = models.ForeignKey(Child)
    present = models.BooleanField(default=False)
    location = models.ForeignKey('Location', blank=True, null=True)
    date_present = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s activity".format(self.child)


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
