from rest_framework import serializers
from direction.models import Direction, Profession
from users.models import UserGradeMap, UserCourses
from direction.models import Course
from .utils import level_b_json, level_a_json, calculating_percent


class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "name")


class DirectionASerializer(serializers.ModelSerializer):
    professions = ProfessionsSerializer(
        read_only=True, many=True, source="directions_professions"
    )

    class Meta:
        model = Direction
        fields = ("id", "name", "professions")


class FirstStepSerializer(serializers.Serializer):
    level_a = serializers.SerializerMethodField()
    level_b = serializers.SerializerMethodField()
    directions = serializers.SerializerMethodField()

    class Meta:
        fields = ("level_a", "level_b", "directions")

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
        print(validated_data)
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


class SelectCourseListSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("name", "duration", "status", "link")

    def get_status(self, obj):
        request = self.context["request"]
        user = request.user
        user_courses = user.courses.all()
        queryset_status = UserCourses.objects.filter(user=user.id)
        if user_courses.contains(obj):
            return queryset_status.get(course_id=obj.id).get_status_display()
        return "Не пройден"


class TargetSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(
        method_name="get_status_in_percent"
    )
    end_prof = serializers.CharField(source="end_prof.name")
    end_level = serializers.CharField(source="get_end_level_display")

    class Meta:
        model = UserGradeMap

        fields = ("end_level", "end_prof", "status")

    def get_status_in_percent(self, obj):
        return calculating_percent(obj)
