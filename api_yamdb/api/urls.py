from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from .views import UsersViewSet, CommentsViewSet, ReviewViewSet

v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
v1_router.register(
    r'users',
    UsersViewSet,
    basename='users'
)
v1_router.register(
    r'categories',
    CategoriesViewSet,
    basename='categories'
)
v1_router.register(
    r'genres',
    GenresViewSet,
    basename='genres'
)
v1_router.register(
    r'titles',
    TitlesViewSet,
    basename='titles'
)

urlpatterns = [
    path('v1/', include(v1_router.urls))
]

