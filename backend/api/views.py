from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from backend.api.serializers import DirectionASerializer
from backend.direction.models import Course, Direction


@api_view(
    [
        "GET",
    ]
)
def userData(request):
    pass


class CourseViewSet(ModelViewSet):
    # queryset = Course.objects.all()

    @action(detail=True, methods=["GET"])
    def directionA(self, request):
        result = Direction.objects.all()
        serializer = DirectionASerializer(result)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def professionA(self, request):
        pass

    @action(detail=True, methods=["GET"])
    def levelA(self, request):
        pass

    @action(detail=True, methods=["GET"])
    def directionB(self, request):
        pass

    @action(detail=True, methods=["GET"])
    def professionB(self, request):
        pass

    @action(detail=True, methods=["GET"])
    def levelB(self, request):
        pass

    @action(detail=True, methods=["POST"])
    def directionA(self, request):
        pass

    @action(detail=True, methods=["POST"])
    def professionA(self, request):
        pass

    @action(detail=True, methods=["POST"])
    def levelA(self, request):
        pass

    @action(detail=True, methods=["POST"])
    def directionB(self, request):
        pass

    @action(detail=True, methods=["POST"])
    def professionB(self, request):
        pass

    @action(detail=True, methods=["POST"])
    def levelB(self, request):
        pass


# get
def userStatus():
    # Параметры
    # Id курса
    # Id пользователя
    # Статус в %

    # Получение статуса прохождения курсов из списка пользователя (имитируем)
    pass


# get
def showStatus():
    # Вывод статусов прохождения курсов
    pass
