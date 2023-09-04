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
### Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Wiz410/api_yamdb.git
cd api_yamdb
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
Установить/обновить pip и зависимости:
```bash
python -m pip install --upgrade pip`
pip install -r requirements.txt
```

Применить миграции и запустить проект:
```bash
python manage.py migrate
python manage.py runserver
```


# Авторы проекта
[Данила Полунин](https://github.com/Wiz410)\
[Евгения Загородных](https://github.com/evgeniazagorodnykh)\
[Александр Волков](https://github.com/alextriano)
