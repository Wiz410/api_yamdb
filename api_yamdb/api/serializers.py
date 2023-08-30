from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import RegexField
from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersSerializer(ModelSerializer):
    """Сериализатор модели `MyUser`."""

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User
        constraints = [
            UniqueConstraint(
                fields=['username', 'email'],
                name='usermail',
            )
        ]


class UserUpdateSerializer(ModelSerializer):
    username = RegexField(regex=r'^[\w.@+-]+\Z', max_length=150)

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        read_only_fields = ('role',)
        model = User
