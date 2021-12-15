from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from home.serializers import *
from home.models import *


# Create your views here.

class HomeView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = HomeSerializers
    queryset = Home.objects.all()


class PhotoView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PhotoSerializers
    queryset = Photo.objects.all()
