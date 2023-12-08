from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import (
    FirstStepSerializer,
    UserGradeSerializer,
    SelectCourseListSerializer,
    TargetSerializer,
)
from users.models import UserGradeMap
from direction.models import Course

from .utils import choosen_level


class FirstStepView(APIView):
    """
    Метод get: a_b уровень навыков.
    Методы post,put,delete: создание карты уровней пользователя
    """

    permission_classes = (IsAuthenticated,)
    model = UserGradeMap
    queryset = UserGradeMap.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FirstStepSerializer(
                self.request,
            )

    def get(self, request):
        serializer = self.get_serializer_class()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        context = request.data
        context["user"] = request.user.id

        serializer = UserGradeSerializer(data=context)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        data = request.data
        usergrademap = get_object_or_404(UserGradeMap, user=request.user.id)

        serializer = UserGradeSerializer(usergrademap, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        usergrademap = get_object_or_404(UserGradeMap, user=request.user.id)
        usergrademap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SelectCourseView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Подбор курсов"""

    permission_classes = (IsAuthenticated,)
    serializer_class = SelectCourseListSerializer

    def get_queryset(self):
        usergrademap = get_object_or_404(
            UserGradeMap, user=self.request.user.id
        )
        level_range = choosen_level(usergrademap.end_level)
        queryset = []
        if type(level_range) is list:
            for i in level_range:
                query = Course.objects.filter(
                    level=i,
                    professions=usergrademap.end_prof,
                )
                queryset.extend(query)
                queryset = set(queryset)
        else:
            queryset = Course.objects.filter(
                level=usergrademap.end_level,
                professions=usergrademap.end_prof,
            )

        return queryset

    @action(
        methods=["GET"],
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def target(self, request):
        usergrademap = UserGradeMap.objects.get(user=request.user)
        serializer = TargetSerializer(
            usergrademap,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


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
