from rest_framework import serializers
from direction.models import Direction, Profession


class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "name")


class DirectionASerializer(serializers.ModelSerializer):
    professions = ProfessionsSerializer(
        many=True, read_only=True, source="profession"
    )

    class Meta:
        model = Direction
        fields = ("id", "name", "professions")

    # def get_professions(self, obj):
    #     request = self.context["request"]
    #     print(request)
