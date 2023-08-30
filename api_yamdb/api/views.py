from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED
from rest_framework.viewsets import ModelViewSet

from .permissions import AdminOnly
from .serializers import UsersSerializer
from .serializers import UserUpdateSerializer

User = get_user_model()


class UsersViewSet(ModelViewSet):
    """Обработка запросов `users`.
    Запросы к `api/v1/users/` доступны
    только админу и суперпользователю.

    Запросы к `api/v1/users/me` доступны
    любому авторизованному пользователю.

    Returns:
    `api/v1/users`
        GET (json): Список всех пользователей.
        POST (json): Создание пользователя.
        GET USERNAME (json): Информация о пользователе.
        PATCH USERNAME (json): Частичное редактирование пользователя.
        DELETE USERNAME (json): Удаление пользователя.
    `api/v1/users/me`
        GET (json): Информация о пользователе.
        PATCH (json): Частичное редактирование пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AdminOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('username',)
    lookup_field = ('username')

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
        user = get_object_or_404(User, username=kwargs['username'])
        serializer = self.serializer_class(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = get_object_or_404(User, username=request.user.username)
        if self.action == 'get':
            serializer = UserUpdateSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        serializer = UserUpdateSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
