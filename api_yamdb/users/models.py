from django.core.validators import RegexValidator
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
        default=CHOISE[0][0],
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
        max_length=512,
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=100,
        null=True
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', 'username')

    def __srt__(self):
        return self.username
