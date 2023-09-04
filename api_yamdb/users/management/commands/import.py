import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from reviews.models import (
    Categories,
    Comments,
    GenresTitles,
    Genres,
    Review,
    Titles,
)
from users.models import MyUser

User = get_user_model()

MODEL_PATH = (
    (MyUser, 'static/data/users.csv'),
    (Categories, 'static/data/category.csv'),
    (Genres, 'static/data/genre.csv'),
    (Titles, 'static/data/titles.csv'),
    (Review, 'static/data/review.csv'),
    (Comments, 'static/data/comments.csv'),
    (GenresTitles, 'static/data/genre_title.csv'),
)


class Command(BaseCommand):
    help = 'Импорт данных из csv в базу данных.'

    def handle(self, *args, **kwargs):
        """Импорт данных.
        """
        for model, path in MODEL_PATH:
            with open(
                path,
                newline='',
                encoding='utf8'
            ) as csv_file:
                for data in csv.DictReader(csv_file):
                    print(model)
                    print(data)
                    if data.get('category') is not None:
                        data['category'] = Categories.objects.get(
                            id=data['category']
                        )
                    if data.get('author') is not None:
                        data['author'] = MyUser.objects.get(
                            id=data['author']
                        )
                    if data.get('title') is not None:
                        data['title'] = Titles.objects.get(
                            id=data['title']
                        )
                    if (data.get('title_id') is not None
                       and data.get('genre_id') is not None):
                        data['title_id'] = Titles.objects.get(
                            id=data['title_id']
                        )
                        data['genre_id'] = Genres.objects.get(
                            id=data['genre_id']
                        )
                    print(data)
                    model.objects.create(**data)
        self.stdout.write(
            'Загрузка завершена'
        )
