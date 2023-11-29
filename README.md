# hackathon_yandex
Cоздание MVP внутреннего сервиса Яндекс Практикума “Трекер развития”, позволяющего строить план обучения от точки А до точки Б

Если не установлен poetry
```
pip install poetry
```

```
poetry init
```
```
poetry install
```

Создать в корне файл .env и скопировать в него содержимое из .env.example

Для создания SECRET_KEY заходим в терминал:
```
python manage.py shell
```
Импортируем utils:
```
from django.core.management import utils
```
Генерируем:
```
utils.get_random_secret_key()
```
Вставляем в .env
Или используем онлайн [сервис](https://djecrety.ir/)