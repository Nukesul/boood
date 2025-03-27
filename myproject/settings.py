# settings.py
import os
from pathlib import Path

# Определение базовой директории
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (лучше вынести в переменные окружения в продакшене)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key-here')  # Замените на безопасный ключ

# Режим отладки (отключите в продакшене)
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Разрешенные хосты
ALLOWED_HOSTS = ['boodaikg.com', 'nukesul-boood-2ab7.twc1.net', 'localhost', '127.0.0.1', 'vh438.timeweb.ru']

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Оставляем для возможного API в будущем
    'corsheaders',     # Для обработки CORS
    'api',             # Ваше приложение
]

# Промежуточное ПО (CORS идет первым)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Настройки CORS
CORS_ALLOWED_ORIGINS = [
    "http://boodaikg.com",
    "https://boodaikg.com",
    "http://localhost:3000",  # Для разработки
    "http://127.0.0.1:8000",
]
CORS_ALLOW_CREDENTIALS = True  # Разрешаем отправку куки и заголовков авторизации
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Настройки CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://boodaikg.com",
    "http://boodaikg.com",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "https://nukesul-boood-2ab7.twc1.net",  # Добавляем для обратной совместимости
]

# Конфигурация URL
ROOT_URLCONF = 'myproject.urls'  # Замените 'myproject' на имя вашего проекта

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Если используете кастомные шаблоны
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI приложение
WSGI_APPLICATION = 'myproject.wsgi.application'  # Замените 'myproject' на имя вашего проекта

# Подключение MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ch79145_boodai',
        'USER': 'ch79145_boodai',
        'PASSWORD': '16162007',
        'HOST': 'vh438.timeweb.ru',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Локализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Существующий путь
    '/opt/build/static',               # Добавленный путь
]

# Медиафайлы
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Автоинкремент полей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Дополнительные настройки для продакшена (рекомендации)
if not DEBUG:
    SECURE_SSL_REDIRECT = True  # Перенаправление на HTTPS
    SESSION_COOKIE_SECURE = True  # Куки только через HTTPS
    CSRF_COOKIE_SECURE = True  # CSRF только через HTTPS
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True