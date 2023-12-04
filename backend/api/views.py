from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from api.serializers import DirectionASerializer
from direction.models import Course, Direction, Profession


# @api_view(
#     [
#         "GET",
#     ]
# )
# def userData(request):
#     pass


class FirstStepView(ListModelMixin, GenericViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionASerializer


# # get
# def userStatus():
#     # Параметры
#     # Id курса
#     # Id пользователя
#     # Статус в %

#     # Получение статуса прохождения курсов из списка пользователя (имитируем)
#     pass


# # get
# def showStatus():
#     # Вывод статусов прохождения курсов
#     pass
