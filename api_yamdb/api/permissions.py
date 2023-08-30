from rest_framework.permissions import BasePermission


class AdminOnly(BasePermission):
    """Разрешение для админов и суперпользователя.

    Returns:
        has_permission (bool): True если
        пользователь авторизован
        и является админом или суперпользователем.
    """
    def has_permission(self, request, view) -> bool:
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
            or request.user.is_superuser
        )
