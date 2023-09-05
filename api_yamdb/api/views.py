import uuid

from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    viewsets,
    mixins,
    filters,
    status,
    views
)
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import Categories, Genres, Title, Review
from .serializers import (
    UsersSerializer,
    UserUpdateSerializer,
    CommentsSerializer,
    CategoriesSerializer,
    GenresSerializer,
    ReviewSerializer,
    TitlesReadSerializer,
    TitlesWriteSerializer,
    SignUpSerializer,
    TokenSerializer,
)
from .permissions import (
    AdminOnly,
    AdminOrReadOnly,
    AuthorModeratorAdminOrReadOnly
)
from .filters import ModelFilter


User = get_user_model()


class CreateListDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    lookup_field = ('slug')


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name',)
    lookup_field = ('slug')


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).order_by('id')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ModelFilter
    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitlesReadSerializer
        return TitlesWriteSerializer

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    """Получение списка/создание/обновление/удаление отзывов."""
    serializer_class = ReviewSerializer
    permission_classes = (AuthorModeratorAdminOrReadOnly,)

    def define_title(self):
        return get_object_or_404(Title, id=self.kwargs.get("title_id"))

    def get_queryset(self):
        title = self.define_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.define_title()
        serializer.save(author=self.request.user, title=title)

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class CommentsViewSet(ReviewViewSet):
    """Получение списка/создание/обновление/удаление комментариев."""
    serializer_class = CommentsSerializer

    def define_review(self):
        return get_object_or_404(Review, id=self.kwargs.get("review_id"))

    def get_queryset(self):
        review = self.define_review()
        return review.comments.all()

    def perform_create(self, serializer):
        review = self.define_review()
        serializer.save(author=self.request.user, review=review)

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().update(request, *args, **kwargs)


class UsersViewSet(viewsets.ModelViewSet):
    """Обработка запросов `users`.
    Запросы к `api/v1/users/` доступны
    только админу и суперпользователю.

    Запросы к `api/v1/users/me` доступны
    любому авторизованному пользователю.

    Returns:
    `api/v1/users`
        GET (json): Список всех пользователей.
        POST (json): Создание пользователя.
        GET USERNAME (json): Информация о пользователе.
        PATCH USERNAME (json): Частичное редактирование пользователя.
        DELETE USERNAME (json): Удаление пользователя.
    `api/v1/users/me`
        GET (json): Информация о пользователе.
        PATCH (json): Частичное редактирование пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AdminOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('username',)
    lookup_field = ('username')

    def update(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        user = get_object_or_404(User, username=kwargs['username'])
        serializer = self.serializer_class(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = get_object_or_404(
            User,
            username=request.user.username
        )
        if self.action == 'get':
            serializer = UserUpdateSerializer(user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        serializer = UserUpdateSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class APISingUp(views.APIView):
    """Регистрация пользователя.
    Запросы к `api/v1/auth/signup/` доступны всем пользователям.

    Returns:
        POST(json): Создание пользователя и код подтверждения для API.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            code = uuid.uuid4()
            current_user, created = User.objects.get_or_create(
                **serializer.validated_data
            )
            current_user.confirmation_code = str(code)
            current_user.save()
            send_mail(
                subject='Confirmation code YAMDB.',
                message=(
                    f'Ваш код подтверждения "{str(code)}" '
                    'для сервиса YAMDB.'
                ),
                from_email='code@yamdb.ru',
                recipient_list=[serializer.validated_data['email']],
                fail_silently=True,
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class APIToken(views.APIView):
    """Получение Токена.
    Запросы к `api/v1/auth/token/` доступны всем пользователям.

    Returns:
        POST(json): Создание токена для API.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['username']
            conf_code = serializer.validated_data['confirmation_code']
            user = get_object_or_404(
                User, username=user
            )
            if user.confirmation_code == conf_code:
                token = RefreshToken.for_user(user)
                return Response(
                    {'token': str(token.access_token)},
                    status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
