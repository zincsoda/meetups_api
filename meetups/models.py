from django.db import models

class Image(models.Model):
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    
    def __unicode__(self):
        return self.image_url

class Meetup(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=12, blank=True, null=True)
    speaker = models.CharField(max_length=200, blank=True, null=True)
    organiser_contact = models.CharField(max_length=200, blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

