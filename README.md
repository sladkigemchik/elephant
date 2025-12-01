# 1. Клонировать репозиторий
git clone https://github.com/ваш-логин/elephant-computer-repair.git
cd elephant-computer-repair

# 2. Создать виртуальное окружение
python -m venv .venv

# 3. Активировать окружение
# Linux/Mac:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

# 4. Установить зависимости
pip install -r requirements.txt

# 5. Настроить базу данных
# Отредактировать elephant/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elephant_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 6. Применить миграции
python manage.py migrate

# 7. Создать суперпользователя
python manage.py createsuperuser

# 8. Запустить сервер
python manage.py runserver
