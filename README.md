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
python manage.py runserver
```
- Linux/MacOS:
```bash
python3 manage.py migrate
python3 manage.py runserver
```
### Примеры запросов и ответов на них в формате JSON:
- Регистрация пользователя (запрос и ответ идентичны):
```
{
    "username": "UserTest",
    "email": "UserMail@mail.ru"
}
```
- Присвоение токена (запрос):
```
{
    "username": "UserTest",
    "confirmation_code": "c695a768-2ffc-4286-a7ea-139a086"
}
```
- Присвоение токена (ответ):
```
{
    "token": "eyJ0eXAiO1NiJ9.eyOjN9.yNTY8v0tbsI-GdD6E5zEQ"
}
```
# Авторы проекта
[Данила Полунин](https://github.com/Wiz410)\
[Евгения Загородных](https://github.com/evgeniazagorodnykh)\
[Александр Волков](https://github.com/alextriano)
