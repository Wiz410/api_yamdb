import django_filters

from reviews.models import Title


class ModelFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(
        field_name='genre__slug',
    )
    category = django_filters.CharFilter(
        field_name='category__slug',
    )

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')
