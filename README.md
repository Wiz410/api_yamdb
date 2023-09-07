# Проект YaMDb
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django?color=orange&link=https%3A%2F%2Fdocs.python.org%2F3.11%2F)


### Описание
Проект YaMDb собирает отзывы пользователей на различные произведения. Произведения делятся на категории и жанры.\
Аутентифицированные пользователи могут оставлять к произведениям отзывы, комментарии к ним, а также присваивать произведениям рейтинг от 1 до 10.\
На одно произведение пользователь может оставить только один отзыв.

Поддерживаются методы GET, POST, PATCH, DEL для пользователей, произведений, отзывов и комментариев.\
Для категорий и жанров - методы GET, POST, DEL.\
Для регистрации/аутентификации пользователей используется только метод POST.\
Аутентификация - с помощью JWT-токенов.
### Инструменты:
- [Python 3.11]([Python](https://docs.python.org/3.11/))
- [Django 3.2](https://docs.djangoproject.com/en/4.2/releases/3.2/)
- [Django Rest Framework 3.12](https://www.django-rest-framework.org/)
- [Simple JWT 5.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
### Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
- Windows & Linux/MacOS:
```bash
git clone git@github.com:Wiz410/api_yamdb.git
cd api_yamdb
```
Cоздать и активировать виртуальное окружение:
- Windows:
```bash
python -m venv venv
source venv/Scripts/activate
```
- Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
Установить/обновить pip и зависимости:
- Windows:
```bash
python -m pip install --upgrade pip`
pip install -r requirements.txt
```
- Linux/MacOS:
```bash
python3 -m pip install --upgrade pip`
pip install -r requirements.txt
```

Применить миграции и запустить проект:
- Windows:
```bash
python manage.py migrate
python manage.py import
python manage.py runserver
```
- Linux/MacOS:
```bash
python3 manage.py migrate
python3 manage.py import
python3 manage.py runserver
```
### Примеры запросов и ответов на них в формате JSON:
- Категории `/api/v1/categories/`
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Фильм",
            "slug": "movie"
        },
        {
            "name": "Книга",
            "slug": "book"
        },
        {
            "name": "Музыка",
            "slug": "music"
        }
    ]
}
```
- Произведения `api/v1/titles/`
```json
{
    "count": 32,
    "next": "http://127.0.0.1:8000/api/v1/titles/?limit=5&offset=5",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Побег из Шоушенка",
            "year": 1994,
            "description": null,
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
            ],
            "rating": 10,
            "category": {
                "name": "Фильм",
                "slug": "movie"
            }
        },
        ...
        {
            "id": 5,
            "name": "Криминальное чтиво",
            "year": 1994,
            "description": null,
            "genre": [
                {
                    "name": "Комедия",
                    "slug": "comedy"
                },
                {
                    "name": "Детектив",
                    "slug": "detective"
                },
                {
                    "name": "Триллер",
                    "slug": "thriller"
                }
            ],
            "rating": 5,
            "category": {
                "name": "Фильм",
                "slug": "movie"
            }
        }
    ]
}
```
- Регистрация пользователя (запрос и ответ идентичны):
```json
{
    "username": "UserTest",
    "email": "UserMail@mail.ru"
}
```
- Присвоение токена (запрос):
```json
{
    "username": "UserTest",
    "confirmation_code": "bu6fsa-2b77d51dd9c5a6748dcbf60b03969cb9"
}
```
- Присвоение токена (ответ):
```json
{
    "token": "eyJ0eXAiO1NiJ9.eyOjN9.yNTY8v0tbsI-GdD6E5zEQ"
}
```
# Авторы проекта
[Данила Полунин](https://github.com/Wiz410)\
[Евгения Загородных](https://github.com/evgeniazagorodnykh)\
[Александр Волков](https://github.com/alextriano)
