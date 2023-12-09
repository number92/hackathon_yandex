[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">

# hackathon_yandex
## MVP внутреннего сервиса Яндекс Практикума “Трекер развития”, позволяющего строить план обучения от точки А до точки Б)




# Используемые технологии и библиотеки:
* Python 3.11
* Django 4.2.7
* djangorestframework 3.14.0
* psycopg2-binary 2.9.9
* PyJWT 2.8.0
* python-dotenv==1.0.0


# Сборка репозитория и локальный запуск

Выполните в консоли:
```
git clone https://github.com/EmilAbushaev/hackathon_yandex.git
```
Убедитесь, что вы работаете в виртуальной среде, если нет, то установите ее:
```
virtualenv venv
venv/bin/activate
```
Установите poetry:
```
python -m pip install --upgrade pip
pip install poetry
```
Установите зависимости:
```
poetry init
poetry install
```
Примените миграции:
```
python3 manage.py migrate
```

Создайте в корне файл .env и скопируйте в него следующее:
```
ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

DEBUG=True

SECRET_KEY='ключ, полченный в следующем шаге'
```

Создайте SECRET_KEY, введя в терминале:
```
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Скопируйте полученный ключ в .env файл.

Запустите локальный сервер:
```
python manage.py runserver
```

# Документация:
```
http://127.0.0.1:8000/redoc/
```

# Примеры запросов к API:
```
 /api/first-step/
```




# Разработчики:


