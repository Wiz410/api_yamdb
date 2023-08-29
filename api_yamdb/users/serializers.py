from rest_framework.serializers import ModelSerializer
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
