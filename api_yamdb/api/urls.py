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

router = routers.DefaultRouter()
router.register(r'^categories/(?P<slug>[-a-zA-Z0-9_]+)/$',
                CategoriesViewSet, basename='categories')
router.register(r'^genres/(?P<slug>[-a-zA-Z0-9_]+)/$',
                GenresViewSet, basename='genres')
router.register(r'titles', TitlesViewSet, basename='titles')

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
