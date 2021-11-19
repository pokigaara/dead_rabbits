from django.shortcuts import render
from rest_framework import generics
from activity.serializers import *


class ActivityCreate(generics.CreateAPIView):
    serializer_class = ActivitySerializers


class ActivityListView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializers
    queryset = Activity.objects.all()
