from rest_framework import serializers
from ..models import Direction, CurrentProfession


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class CurrentProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentProfession
        fields = '__all__'
