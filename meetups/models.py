from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    
    def __unicode__(self):
        return self.name

    def admin_thumbnail(self):
        return "<img src='%s' height='41' width='66' />" % self.image_url

    admin_thumbnail.allow_tags = True

class Meetup(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    meeting_time = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=12, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)
    website = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def admin_thumbnail(self):
        return "<img src='%s' height='41' width='66' />" % self.image.image_url
    admin_thumbnail.allow_tags = True
