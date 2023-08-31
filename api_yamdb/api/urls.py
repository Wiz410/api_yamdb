from rest_framework import routers
from django.urls import path, include

from api.views import CategoriesViewSet, GenresViewSet, TitlesViewSet

router = routers.DefaultRouter()
router.register(r'^categories/(?P<slug>[-a-zA-Z0-9_]+)/$',
                CategoriesViewSet, basename='categories')
router.register(r'^genres/(?P<slug>[-a-zA-Z0-9_]+)/$',
                GenresViewSet, basename='genres')
router.register(r'titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
]