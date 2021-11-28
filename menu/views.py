from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from menu.serializers import *
from menu.models import *


class MenuView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = MenuSerializers
    queryset = Menu.objects.all()


class CetegorView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategorSerializers
    queryset = Categories.objects.all()


# class MenuListView(generics.ListCreateAPIView):
#     serializer_class = MenuSerializers
#     queryset = Menu.objects.all()

#
# class MenuDetailView(generics.RetrieveDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = MenuSerializers
#     queryset = Menu.objects.all()
#
#
# class MenuUpdateView(generics.RetrieveUpdateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = MenuSerializers
#     queryset = Menu.objects.all()
