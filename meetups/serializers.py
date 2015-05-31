from rest_framework import serializers
from meetups.models import *

class MeetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetup
        fields = ('id','name','description','date','start_time','end_time','location','postcode','speaker','speaker','organiser_contact','image')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','image_url')

