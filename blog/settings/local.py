from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
ALLOWED_HOSTS = ['FedericoD.pythonanywhere.com']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'FedericoD$default',
        'USER': 'FedericoD',
        'PASSWORD': 'rootroot',
        'HOST': 'FedericoD.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}

