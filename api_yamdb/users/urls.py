from django.urls import path
from django.urls import include
from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet
from .views import UsersMeViewSet

User = get_user_model()

v1_router = DefaultRouter()
v1_router.register(
    r'users',
    UsersViewSet,
    basename='users'
)

v1_router.register(
    r'users/me',
    UsersMeViewSet,
    basename='me'
)

urlpatterns = [
    path('', include(v1_router.urls))
]
