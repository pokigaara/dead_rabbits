from rest_framework import serializers
from reservation.models import *


class ReservCreatUserSerial(serializers.ModelSerializer):
    class Meta:
        model = Reserv
        fields = ('name', 'surname', 'phone', 'email', 'date', 'time', 'people')


class ReservUptadeAdminSerial(serializers.ModelSerializer):
    class Meta:
        model = Reserv
        fields = '__all__'
