from rest_framework import serializers
from direction.models import Direction, Profession
from users.models import UserGradeMap
from .utils import level_b_json, level_a_json


class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "name")


class DirectionASerializer(serializers.ModelSerializer):
    professions = ProfessionsSerializer(
        read_only=True, many=True, source="profession"
    )

    class Meta:
        model = Direction
        fields = ("id", "name", "professions")


class FirstStepSerializer(serializers.Serializer):
    directions = serializers.SerializerMethodField()
    level_a = serializers.SerializerMethodField()
    level_b = serializers.SerializerMethodField()

    class Meta:
        fields = ("directions", "level_a", "level_b")

    def get_level_a(self, obj):
        return level_a_json()

    def get_level_b(self, obj):
        return level_b_json()

    def get_directions(self, obj):
        serializer = DirectionASerializer(Direction.objects.all(), many=True)
        return serializer.data


class UserGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGradeMap
        fields = (
            "user",
            "start_level",
            "end_level",
            "start_prof",
            "end_prof",
            "data_joined",
        )

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return UserGradeMap.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start_level = validated_data.get(
            "start_level", instance.start_level
        )
        instance.end_level = validated_data.get(
            "end_level", instance.end_level
        )
        instance.start_prof = validated_data.get(
            "start_prof", instance.start_prof
        )
        instance.end_prof = validated_data.get("end_prof", instance.end_prof)
        return instance
