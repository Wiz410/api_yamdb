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

router = routers.DefaultRouter()
router.register(r'^categories/(?P<slug>[-a-zA-Z0-9_]+)/$',
                CategoriesViewSet, basename='categories')
router.register(r'^genres/(?P<slug>[-a-zA-Z0-9_]+)/$',
                GenresViewSet, basename='genres')
router.register(r'titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(v1_router.urls))
]

