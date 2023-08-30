from rest_framework import viewsets, mixins, filters, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Categories, Genres, Titles
from api.serializers import CategoriesSerializer, GenresSerializer, TitlesSerializer


class CreateListDestroyViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('slug',)

class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('slug',)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('genre__slug', 'category__slug', 'year', 'name')
