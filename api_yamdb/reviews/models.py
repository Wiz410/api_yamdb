from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import MyUser


class Review(models.Model):
    """Отзывы пользователей и рейтинг произведений"""
    text = models.TextField(verbose_name='Отзыв')
    score = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отзыва'
    )
    title = models.ForeignKey(
        'Titles',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]
        verbose_name_plural = 'Отзывы'


class Comments(models.Model):
    """Комментарии пользователей"""
    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Комментарии'


class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField('Дата публикации')
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genres, through='GenresTitles',)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, 
        null=True, related_name='titles'
    )

    def __str__(self):
        return self.name


class GenresTitles(models.Model):
    genre_id = models.ForeignKey(Genres, on_delete=models.SET_NULL,
        null=True
    )
    title_id = models.ForeignKey(Titles, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.titles}'