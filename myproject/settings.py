import os
from pathlib import Path

# Определение базовой директории
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (лучше хранить в переменных окружения)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key-here')

# Режим отладки (отключай в продакшене)
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Разрешенные хосты
ALLOWED_HOSTS = ['*']  # Разрешаем все хосты

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',  # Ваше приложение
]

# Промежуточное ПО
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS должен быть первым
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Настройки CORS
# Настройки CORS
CORS_ALLOWED_ORIGINS = [
    "http://boodaikg.com",  # Разрешаем ваш фронтенд
    "https://boodaikg.com",  # Разрешаем ваш фронтенд
    "http://localhost:3000", # Для разработки, если нужно
]
CORS_ALLOW_CREDENTIALS = True  # Разрешаем куки и учетные данные
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
    "content-type",  # Добавляем content-type
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Конфигурация URL
ROOT_URLCONF = 'myproject.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
WSGI_APPLICATION = 'myproject.wsgi.application'

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

# Медиафайлы
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Автоинкремент полей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
