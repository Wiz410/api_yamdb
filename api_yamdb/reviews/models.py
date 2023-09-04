from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import MyUser


class Categories(models.Model):
    name = models.CharField(
        max_length=256, verbose_name='Название')
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='Слаг')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        max_length=256, verbose_name='Название')
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='Слаг')
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
    


class Titles(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(verbose_name='Дата публикации')
    genre = models.ManyToManyField(
        Genres, through='GenresTitles', verbose_name='Жанр')
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, 
        null=True, related_name='titles', verbose_name='Категория'
    )
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenresTitles(models.Model):
    titles = models.ForeignKey(
        Titles, on_delete=models.CASCADE, verbose_name='Произведение')
    genre = models.ForeignKey(
        Genres, on_delete=models.SET_NULL, 
        null=True, verbose_name='Жанр'
    )

    def __str__(self):
        return f'{self.titles} {self.genre}'


class Review(models.Model):
    """Отзывы пользователей и рейтинг произведений"""
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField(verbose_name='Отзыв')
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
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
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата комментария'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Комментарии'
