from django.urls import path, include
from rest_framework import routers

from .views import (
    CategoriesViewSet,
    GenresViewSet,
    TitlesViewSet,
    CommentsViewSet,
    ReviewViewSet,
    UsersViewSet,
    APISingUp,
    APIToken
)

v1_router = routers.DefaultRouter()
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

auth_patterns = [
    path(
        'signup/',
        APISingUp.as_view(),
        name='signup'
    ),
    path(
        'token/',
        APIToken.as_view(),
        name='token'
    )
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(auth_patterns)),
]
