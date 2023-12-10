[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">


## API внутреннего сервиса Яндекс Практикума “Трекер развития”, позволяющего строить план обучения от точки А до точки Б)




### Используемые технологии и библиотеки:
* Python 3.11
* Django 4.2.8
* djangorestframework 3.14.0
* Postgres 14.10
* psycopg2-binary 2.9.9
* Poetry 1.7.1
* black 23.11.0

## Сборка в контейнерах Docker  
Выполните в консоли:
```
git clone https://github.com/EmilAbushaev/hackathon_yandex.git
```
создайте .env файл в корне, используя [пример](https://github.com/EmilAbushaev/hackathon_yandex/blob/main/.env.example).  
Создайте SECRET_KEY, используя [сервис](https://djecrety.ir/)  

Создате сеть:  
```
docker compose up -d
```
Приментие миграции  
```
docker-compose exec backend python manage.py migrate
```
Добавьте тестовые данные
```
docker-compose exec backend python manage.py load_fixture
```
Копирование статики админки
```
docker-compose exec backend python manage.py collectstatic 
```
Проверьте [работоспособность](http://localhost:8000/api/docs/)

## Локальный запуск репозитория

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
Создайте в корне файл .env, используя [пример](https://github.com/EmilAbushaev/hackathon_yandex/blob/main/.env.example).  
Создайте SECRET_KEY, введя в терминале: 
```
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Cкопируйте полученный ключ в .env файл.  
Примените миграции:
```
python3 manage.py migrate
```
Добавьте тестовые данные:
```
python manage.py load_fixture
```
Запустите локальный сервер:
```
python manage.py runserver
```
## Документация:
```
http://127.0.0.1:8000/api/docs
```

## Примеры запросов к API:
CRUD
```
 /api/first-step/
```
GET:
```
/api/second-step/
/api/second-step/target
```
## Разработчики:  
[EmilAbushaev](https://github.com/EmilAbushaev)
[number92](https://github.com/number92)

