from django.shortcuts import render
from rest_framework import generics, permissions
from activity.serializers import *
from rest_framework import viewsets
from activity.models import *


class ActivityView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ActivitySerializers
    queryset = Activity.objects.all()


# class ActivityCreate(generics.CreateAPIView):
#     serializer_class = ActivitySerializers
#
# class ActivityListView(generics.ListCreateAPIView):
#     serializer_class = ActivitySerializers
#     queryset = Activity.objects.all()
#
#
# class ActivityDetailView(generics.RetrieveDestroyAPIView):
#     serializer_class = ActivitySerializers
#     queryset = Activity.objects.all()
#
#
# class ActivityUpdateView(generics.RetrieveUpdateAPIView):
#     serializer_class = ActivitySerializers
#     queryset = Activity.objects.all()
