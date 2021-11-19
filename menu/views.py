from django.shortcuts import render
from rest_framework import generics
from menu.serializers import *
from menu.models import *


class MenuCreate(generics.CreateAPIView):
    serializer_class = MenuDetailSerializers


class MenuListView(generics.ListCreateAPIView):
    serializer_class = MenuListSerializers
    queryset = Menu.objects.all()
