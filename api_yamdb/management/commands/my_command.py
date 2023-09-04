from django.core.management.base import BaseCommand

from import_sqlite3 import import_csv


class Command(BaseCommand):
    help = 'Импорт csv файлов в базу данных'
    DICT_FILES = {
    'category': ' reviews_categories',
    'genre': ' reviews_genres',
    'genre_title': ' reviews_genrestitles',
    'titles': ' reviews_titles',
    'users': ' users_myuser',
    'comments': ' reviews_comments',
    'review': ' reviews_review',
    }
    DB_NAME = 'db.sqlite3'

    def handle(self):
        import_csv(dict_files=self.DICT_FILES, db_name=self.DB_NAME)
