from django.shortcuts import render
from rest_framework import generics
from reservation.serializers import *


# Create your views here.
class ReservCreateUser(generics.CreateAPIView):
    serializer_class = ReservCreatUserSerial


class ReservUpdateAdmin(generics.RetrieveUpdateAPIView):
    serializer_class = ReservUptadeAdminSerial
    queryset = Reserv.objects.all()
