import datetime as dt

from rest_framework import serializers
from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model

from reviews.models import Categories, Genres, Titles, Review, Comments


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


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user
        if Review.objects.filter(title=title_id, author=author).exists():
            raise serializers.ValidationError(
                'Уже существует отзыв от пользователя к данному произведению'
            )
        return data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('title',)


class UsersSerializer(serializers.ModelSerializer):
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


class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор модели `MyUser` для обновления данных."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        read_only_fields = ('role',)


class SignUpSerializer(serializers.Serializer):
    """Сериализатор модели `MyUser` для регистрации."""
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z',
        max_length=150,
        required=True
    )
    email = serializers.EmailField(max_length=254, required=True)

    class Meta:
        fields = (
            'username',
            'email'
        )

    def validate(self, value):
        user = value['username']
        mail = value['email']
        if User.objects.filter(
            username=user,
            email=mail
        ):
            return value
        if user == 'me':
            raise serializers.ValidationError(
                'Имя пользователя me запрещено!'
            )
        if User.objects.filter(username=value['username']):
            raise serializers.ValidationError(
                f'Пользователь с именем {user} уже есть!'
            )
        if User.objects.filter(email=value['email']):
            raise serializers.ValidationError(
                f'Пользователь с почтой {mail} уже есть!'
            )
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализатор модели `MyUser` для получения токена."""
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=100,
        required=True
    )

    class Meta:
        fields = (
            'username',
            'confirmation_code'
        )
