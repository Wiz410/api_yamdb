from pathlib import Path
import subprocess

def import_csv(dict_files: dict, db_name: str): 
    file_name = 'static/data/{name}.csv'
    db = Path(db_name).resolve()
    for data_csv, tabl in dict_files.items():
        csv_file = Path(file_name.format(name=data_csv)).resolve()
        result = subprocess.run(
            ['sqlite3',
            str(db),
            '-cmd',
            '.mode csv',
            '.import --skip 1 ' + str(csv_file).replace('\\','\\\\')
            +tabl],
            capture_output=True
        )

dict_files = {
    'category': ' reviews_categories',
    'genre': ' reviews_genres',
    'genre_title': ' reviews_genrestitles',
    'titles': ' reviews_titles',
    'users': ' users_myuser',
    'comments': ' reviews_comments',
    'review': ' reviews_review',
    }
db_name = 'db.sqlite3'

import_csv(dict_files, db_name)
