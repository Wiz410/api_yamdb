import datetime as dt

from rest_framework import serializers

from reviews.models import Categories, Genres, Titles


class CategoriesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(max_length=50)
    name = serializers.CharField(max_length=256)

    class Meta:
        model = Categories
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(max_length=50)
    name = serializers.CharField(max_length=256)

    class Meta:
        model = Genres
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    categories = CategoriesSerializer()

    class Meta:
        model = Titles
        fields = '__all__'
    
    def validate_year(self, value):
        """
        Проверка года выпуска
        """
        if value > dt.datetime.now().year:
            raise serializers.ValidationError('Неправильно указан год выпуска')
        return value
