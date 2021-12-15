from rest_framework import serializers
from home.models import *


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

