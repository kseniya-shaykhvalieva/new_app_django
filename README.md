# Интернет-магазин (SkyStore)

Проект интернет-магазина на Django. (будет дорабатываться)

## Структура проекта
```
new_app_django/
├── catalog/ # приложение каталога
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py # маршруты приложения
│ └── views.py # контроллеры
├── config/ # настройки проекта
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py # главные маршруты
│ └── wsgi.py
├── templates/ # HTML-шаблоны
│ ├── home.html
│ └── contacts.html
├── .gitignore
├── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md
```
## Установка и запуск

1. **Клонирование и переход в директорию**

2. **Установка зависимостей (Poetry):**
```
poetry install
```
3. **Запуск сервера:**
```
python manage.py runserver
```
4. **Страницы:**
- Главная: `http://127.0.0.1:8000/home/`
- Контакты: `http://127.0.0.1:8000/contacts/`

## Функциональности

- Главная страница с карточками товаров
- Страница с контактной информацией
- Шаблоны на Bootstrap
- Контроллеры `home` и `contacts` с рендерингом через `render()`

## Инструменты

- Python
- Django
- Bootstrap (CDN)
- Poetry
- Git (GitFlow)