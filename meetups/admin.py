from django.contrib import admin
from models import *

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail','name','description', 'contact', 'location')
    list_display_links = ('name',)
admin.site.register(Meetup, MeetupAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail','name','image_url',)
    list_display_links = ('name',)
admin.site.register(Image, ImageAdmin)
