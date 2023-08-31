import datetime as dt

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import RegexField
from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model

from reviews.models import Categories, Genres, Titles


User = get_user_model()


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


class UsersSerializer(ModelSerializer):
    """Сериализатор модели `MyUser`."""

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User
        constraints = [
            UniqueConstraint(
                fields=['username', 'email'],
                name='usermail',
            )
        ]


class UserUpdateSerializer(ModelSerializer):
    """Сериализатор модели `MyUser` для обновления данных."""
    username = RegexField(regex=r'^[\w.@+-]+\Z', max_length=150)

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        read_only_fields = ('role',)
        model = User
