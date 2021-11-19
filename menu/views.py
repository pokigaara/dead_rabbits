from django.shortcuts import render
from rest_framework import generics
from menu.serializers import *
from menu.models import *


class MenuCreate(generics.CreateAPIView):
    serializer_class = MenuSerializers


class MenuListView(generics.ListCreateAPIView):
    serializer_class = MenuSerializers
    queryset = Menu.objects.all()
