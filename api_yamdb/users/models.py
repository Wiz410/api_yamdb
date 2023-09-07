from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

USER: str = 'user'
MODERATOR: str = 'moderator'
ADMIN: str = 'admin'

CHOISE: tuple[tuple[str, str]] = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Админ'),
)


class MyUser(AbstractUser):
    """Модель пользователя."""
    username = models.CharField(
        'Имя пользователя',
        unique=True,
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='Некорректный ввод'
            )
        ]
    )
    email = models.EmailField(
        'Адрес электронной почты',
        unique=True,
        max_length=254,
    )
    role = models.CharField(
        'Роль',
        max_length=50,
        null=True,
        choices=CHOISE,
        default=USER,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
        max_length=512,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', 'username')

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN

    def __srt__(self):
        return self.username
