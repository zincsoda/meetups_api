from django.http import HttpResponse
from meetups.models import *
from meetups.serializers import *
from rest_framework import generics

def home(request):
    return HttpResponse("<p>Hey <b>Steve</b>")


class MeetupList(generics.ListCreateAPIView):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

class MeetupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer
