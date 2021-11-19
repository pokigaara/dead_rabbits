from django.shortcuts import render
from rest_framework import generics
from activity.serializers import *


class ActivityCreate(generics.CreateAPIView):
    serializer_class = ActivityDetailSerializers


class ActivityListView(generics.ListCreateAPIView):
    serializer_class = ActivityListSerializers
    queryset = Activity.objects.all()
