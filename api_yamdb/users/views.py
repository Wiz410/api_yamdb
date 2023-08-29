from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from .serializers import UsersSerializer
from .permissions import AdminOnly

User = get_user_model()


class UsersViewSet(ModelViewSet):
    """Обработка запросов к `users`.
    Запросы к `api/v1/users/` доступны
    только админу и суперпользователю.

    Note:
        Не работают запросы к `api/v1/users/{username}`

    Returns:
        GET (json): Список всех пользователей.
        POST (json): Создание пользователя.
        GET USERNAME (json): Информация о пользователе.
        PUT USERNAME (json): Редактирование пользователя.
        PATCH USERNAME (json): Частичное редактирование пользователя.
        DELETE USERNAME (json): Удаление пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AdminOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('username',)


class UsersMeViewSet(ModelViewSet):
    """Обработка запросов к `users/me`.
    Запросы к `api/v1/users/me` доступны
    любому авторизованному пользователю.

    Note:
        Не работает

    Returns:
        GET (json): Информация о пользователе.
        PATCH (json): Частичное редактирование пользователя.
    """
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_object_or_404(User, username=self.request.user.username)
