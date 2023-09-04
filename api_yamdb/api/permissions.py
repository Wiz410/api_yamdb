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


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return (
            request.user.is_authenticated
            and (request.user.role == 'admin'
            or request.user.is_superuser)
        )  
