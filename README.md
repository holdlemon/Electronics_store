# Онлайн-платформа торговой сети электроники

## 📌 Описание проекта

Этот проект представляет собой API и админ-панель для управления сетью поставщиков электроники. Система позволяет:

- Управлять иерархией поставщиков (заводы, розничные сети, индивидуальные предприниматели).
- Фильтровать поставщиков по стране и городу.
- Работать с задолженностями перед поставщиками.
- Управлять товарами в системе.
- Ограничивать доступ к API только для активных сотрудников.

## 🛠️ Стек технологий

- **Язык:** Python 3.8+
- **Фреймворк:** Django 3+
- **API:** Django REST Framework (DRF) 3.10+
- **База данных:** PostgreSQL 10+
- **Аутентификация:** djangorestframework-simplejwt

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone git@github.com:holdlemon/Electronics_store.git
cd Electronics_store
```

### 2. Создание и активация виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных

Перед запуском необходимо создать базу данных в PostgreSQL и обновить настройки в `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'POSTGRES_DB': 'your_db_name',
        'POSTGRES_USER': 'your_db_user',
        'POSTGRES_PASSWORD': 'your_db_password',
        'POSTGRES_HOST': 'localhost',
        'POSTGRES_PORT': '5432',
    }
}
```

### 5. Выполнение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Создание суперпользователя

```bash
python manage.py csu
```

### 7. Создание тестовых пользователей и данных

```bash
python manage.py create_user  # Создание тестовых пользователей
python manage.py add_test_data  # Добавление тестовых данных
```

### 8. Запуск сервера

```bash
python manage.py runserver
```

Теперь API доступно по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔑 Авторизация

Доступ к API предоставляется только активным пользователям. Используется **JWT-токен**.

1. Получение токена:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

2. Использование токена в запросах:

```bash
curl -H "Authorization: Bearer your_token" http://127.0.0.1:8000/api/suppliers/
```

## 📌 Основные эндпоинты API

| Метод    | URL                    | Описание                    |
| -------- | ---------------------- | --------------------------- |
| `GET`    | `/api/suppliers/`      | Получить список поставщиков |
| `POST`   | `/api/suppliers/`      | Создать нового поставщика   |
| `GET`    | `/api/suppliers/{id}/` | Получить детали поставщика  |
| `PUT`    | `/api/suppliers/{id}/` | Обновить поставщика         |
| `DELETE` | `/api/suppliers/{id}/` | Удалить поставщика          |
| `GET`    | `/api/products/`       | Получить список продуктов   |
| `POST`   | `/api/products/`       | Создать новый продукт       |

## 🎯 Фильтрация поставщиков

Можно фильтровать поставщиков по стране:

```bash
curl -H "Authorization: Bearer your_token" "http://127.0.0.1:8000/api/suppliers/?country=Россия"
```

## 🛠 Админ-панель

Админка доступна по адресу: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Здесь можно управлять поставщиками, товарами и пользователями.

## 📜 Лицензия

Этот проект распространяется под MIT License.

---