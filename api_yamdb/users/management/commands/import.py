import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from reviews.models import (
    Categories,
    Comments,
    GenresTitles,
    Genres,
    Review,
    Title,
)

User = get_user_model()

MODEL_PATH = (
    (User, 'static/data/users.csv'),
    (Categories, 'static/data/category.csv'),
    (Genres, 'static/data/genre.csv'),
    (Title, 'static/data/titles.csv'),
    (Review, 'static/data/review.csv'),
    (Comments, 'static/data/comments.csv'),
    (GenresTitles, 'static/data/genre_title.csv'),
)


class Command(BaseCommand):
    """Импорт данных.

    Raise:
        Импорт только для пустой базы данных.
        Изменение порядка в MODEL_PATH
        приведет к ошибке импорта.

    Examples:
        >>> python manage.py migrate
        >>> python manage.py import
        >>> Загрузка завершена
    """
    help = 'Импорт данных из csv в базу данных.'

    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.SUCCESS('Импорт запушен.')
        )
        for model, path in MODEL_PATH:
            with open(
                path,
                newline='',
                encoding='utf8'
            ) as csv_file:
                for data in csv.DictReader(csv_file):
                    if data.get('category') is not None:
                        data['category'] = Categories.objects.get(
                            id=data['category']
                        )
                    if data.get('author') is not None:
                        data['author'] = User.objects.get(
                            id=data['author']
                        )
                    if data.get('title') is not None:
                        data['title'] = Title.objects.get(
                            id=data['title']
                        )
                    if (data.get('title_id') is not None
                       and data.get('genre_id') is not None):
                        data['title_id'] = Title.objects.get(
                            id=data['title_id']
                        )
                        data['genre_id'] = Genres.objects.get(
                            id=data['genre_id']
                        )
                    model.objects.create(**data)
                self.stdout.write(
                    f'Данные в модель: {model._meta.object_name} '
                    'импортированы.'
                )
        self.stdout.write(
            self.style.SUCCESS('Импорт завершен.')
        )
