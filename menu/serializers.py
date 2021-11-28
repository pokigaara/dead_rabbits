from rest_framework import serializers
from menu.models import *


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CategorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


