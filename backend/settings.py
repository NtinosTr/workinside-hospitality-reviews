from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-oyrasl6^&7b4t(!q90kc=4s)86v3!yf$o#l7p_eg1dd6da!(65'

DEBUG = True  # αλλάζει αυτόματα από Render

ALLOWED_HOSTS = ["*"]


# ========================================
# INSTALLED APPS
# ========================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our app
    'reviews.apps.ReviewsConfig',

    # Third-party
    'rest_framework',
    'corsheaders',
]


# ========================================
# MIDDLEWARE
# ========================================
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


# ========================================
# CORS
# ========================================
CORS_ALLOW_ALL_ORIGINS = True


# ========================================
# URLS & TEMPLATES
# ========================================
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'backend' / 'templates',      # global templates
            BASE_DIR / 'reviews' / 'templates',      # app templates
        ],
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


WSGI_APPLICATION = 'backend.wsgi.application'


# ========================================
# DATABASE
# ========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ========================================
# STATIC FILES (CSS, JS, IMAGES)
# ========================================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"   # Render needs this


# ========================================
# EMAIL SETTINGS (gmail)
# ========================================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "workinside.contact@gmail.com"
EMAIL_HOST_PASSWORD = "nhemdippumoithho"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ========================================
# CUSTOM ERROR HANDLERS
# ========================================
HANDLER404 = "reviews.views.error_404"
HANDLER500 = "reviews.views.error_500"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
