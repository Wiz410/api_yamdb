# api_yamdb
api_yamdb
### API для Yatube

## Описание

Через API Yatube пользователи могут отслеживать посты любимых авторов и оставлять свои комментарии, а также делиться своими постами, добавлять к ним картинки. 

## Как запустить проект:

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source мenv/bin/activate
    ```

* Если у вас windows

    ```
    source мenv/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API:

GET /api/v1/posts/
***Response:**
```
[
    {
        "id": 2,
        "author": "regular_user",
        "image": null,
        "text": "Пост с группой",
        "pub_date": "2023-08-17T10:58:06.235231Z",
        "group": 1
    }
]
```

POST /api/v1/posts/4/comments/
**Response:**
```
{
    "id": 3,
    "author": "regular_user",
    "post": "4",
    "text": "Тестовый комментарий",
    "created": "2023-08-18T19:22:13.370713Z"
}
```

POST /api/v1/follow/
**Response:**
```
{
    "id": 1,
    "user": "regular_user",
    "following": "root"
}
```
