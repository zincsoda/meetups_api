from django.db import models

class Meetup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField()
    postcode = models.CharField(max_length=12)
    organiser = models.CharField(max_length=200)
    organiser_contact = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    image_url = models.CharField(max_length=1000)
