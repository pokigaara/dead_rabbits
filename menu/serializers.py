from rest_framework import serializers
from menu.models import *


class MenuDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
