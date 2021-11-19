from rest_framework import serializers
from activity.models import *


class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
