from django.contrib.auth.models import AbstractUser
from django.db import models

CHOISE: tuple[tuple[str, str]] = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Админ'),
)


class MyUser(AbstractUser):
    """Модель пользователя."""
    username = models.CharField(
        'Имя пользователя',
        unique=True,
        max_length=150,
    )
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
        max_length=254,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
        max_length=512,
    )
    role = models.CharField(
        'Роль',
        max_length=48,
        blank=True,
        null=True,
        choices=CHOISE,
        default=CHOISE[0][0],
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=500,
        blank=True,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', 'username')

    def __srt__(self):
        return self.username
