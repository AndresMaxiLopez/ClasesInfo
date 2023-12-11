"""
Django settings for proyecto project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os # importo sistema operativo desde django.urls importar reverse_lazy
from django.urls import reverse_lazy


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# AUTH 
LOGIN_REDIRECT_URL = reverse_lazy('Inicio') 
LOGOUT_REDIRECT_URL = reverse_lazy('Inicio') 
LOGIN_URL = reverse_lazy('Iniciar sesión')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0cr&d$dn9#3$z(o@0_h8lt%n2e*u@e#_x(s^l-6uqc)$chd85i'

# SECURITY WARNING: don't run with debug turned on in production!
# aqui iba el debug y el allowed_host los pegue en local


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.noticias', # siempre agregar las apps apenas las cree
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'templates')],
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

WSGI_APPLICATION = 'proyecto.wsgi.application'

# aqui iba la base de datos y la pegue en local

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# Configuración de idioma
LANGUAGE_CODE = 'es-ar'

# Configuración de zona horaria
TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Habilitar internacionalización
USE_I18N = True

# Habilitar localización
USE_L10N = True

# Habilitar el uso de zonas horarias
USE_TZ = True

# Configuración de URL estática
STATIC_URL = '/static/'

# Directorios para archivos estáticos
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
)

# Configuración de URL para archivos multimedia
MEDIA_URL = '/media/'

# Directorio para archivos multimedia
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

# Configuración del campo automático predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'