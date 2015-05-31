from django.contrib import admin
from models import *

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('name','speaker')
admin.site.register(Meetup, MeetupAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url',)
admin.site.register(Image, ImageAdmin)
