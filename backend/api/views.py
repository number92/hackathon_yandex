from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    FirstStepSerializer,
    CourseSerializer,
)


@api_view(["GET"])
def firststep_view(request):
    serializer = FirstStepSerializer(request)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def secondstep_view(request):
    serializer = CourseSerializer(request)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
