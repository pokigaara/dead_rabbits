from rest_framework import serializers
from activity.models import *


class ActivityDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ActivityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
