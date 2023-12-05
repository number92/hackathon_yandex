from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import FirstStepSerializer, UserGradeSerializer
from users.models import UserGradeMap


class FirstStepView(APIView):
    """Шаг 1."""

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
