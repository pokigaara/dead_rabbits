from rest_framework import serializers
from menu.models import *


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


