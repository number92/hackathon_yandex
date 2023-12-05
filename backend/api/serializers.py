from rest_framework import serializers
from direction.models import Direction, Profession, Course
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


# class SecondStepSerializer(serializers.Serializer):
#     class Meta:
#         fields = ("courses", )
#
#     courses = serializers.SerializerMethodField()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("name", "professions")

    def get_courses(self, obj):
        return serializer.data