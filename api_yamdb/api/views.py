from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Titles, Review
from .serializers import CommentsSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Получение списка/создание/обновление/удаление отзывов."""
    serializer_class = ReviewSerializer

    def define_title(self):
        return get_object_or_404(Titles, id=self.kwargs.get("title_id"))

    def get_queryset(self):
        title = self.define_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.define_title()
        serializer.save(author=self.request.user, title=title)


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
