import csv
from users.models import MyUser

from django.core.management.base import BaseCommand

CSV_PATH = 'static/data/'
PK_FIELDS = ('category', 'author')

DICT = {
    MyUser: 'users.csv',
}


def csv_import(csv_data, model):
    objects = []
    for row in csv_data:
        for field in PK_FIELDS:
            if field in row:
                row[f'{field}_id'] = row[field]
                del row[field]
        objects.append(model(**row))
    model.objects.bulk_create(objects)


class Command(BaseCommand):
    help = 'импорт из .csv'

    def handle(self, *args, **kwargs):
        for model in DICT:
            with open(
                CSV_PATH + DICT[model],
                newline='',
                encoding='utf8'
            ) as csv_file:
                csv_import(csv.DictReader(csv_file), model)
        self.stdout.write('Импорт данных завершен.')
