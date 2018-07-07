# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ihecf5$#*jw@q42@pmc$lt$zwmv2asz42wk7$h_er!n+1nmt17'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dnd_social',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}