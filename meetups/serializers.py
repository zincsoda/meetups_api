from rest_framework import serializers
from meetups.models import *

class MeetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetup
        fields = ('id','name','description')

