from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

v1_router = DefaultRouter()
v1_router.register(
    r'users',
    UsersViewSet,
    basename='users'
)

urlpatterns = [
    path('', include(v1_router.urls))
]
