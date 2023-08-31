from django.contrib.admin import register
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model

OBJECT_PER_PAGE: int = 10
User = get_user_model()


@register(User)
class UserAdmin(ModelAdmin):
    """Регистрация модели `MyUser` для админки."""
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    ]
    list_editable = [
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    ]
    list_per_page = OBJECT_PER_PAGE
    ordering = [
        'id',
        'username',
    ]
