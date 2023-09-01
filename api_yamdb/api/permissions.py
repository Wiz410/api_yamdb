from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
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


class AuthorModeratorAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение для: авторов, модератора, админа, суперпользователя,
    аутентифицированных/неаутентифицированных пользователей.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role == 'moderator'
            or request.user.role == 'admin' or request.user.is_superuser
            or (
                request.method == 'POST'
                and request.user.is_authenticated
            )
        )
