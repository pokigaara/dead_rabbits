from rest_framework import serializers
from home.models import Home


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'