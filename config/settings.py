from pathlib import Path
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = env('SECRET_KEY')
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainsite.apps.MainsiteConfig',
    'profiles',
    # third party
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'django_cleanup.apps.CleanupConfig',
    'imagekit',
    'django.contrib.postgres',  # needed for unaccent field lookup
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
    }
}

# Password validation
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

# Extended User Model Settings
AUTH_USER_MODEL = 'profiles.Profile'
LOGOUT_REDIRECT_URL = 'profiles:login'
LOGIN_REDIRECT_URL = 'mainsite:index'

# Internationalization
LANGUAGE_CODE = 'tr-TR'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# STATIC_ROOT = '/home/username/projectnamefolder/staticfiles/'  # in production mode
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles/')  # in production mode
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.Optimistic'

# CKEDITOR SETTINGS
CKEDITOR_UPLOAD_PATH = os.path.join("img/uploads/")
AWS_QUERYSTRING_AUTH = False
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
    },
}

# CRISPY SETTINGS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Admin ordering settings
# ADMIN_ORDERING = [
#     ("mainsite", [
#         "IndexPage",
#         "Aboutus",
#         "ProductCategory",
#         "Brands",
#         "Product",
#         "Blog",
#         "ContactUs",
#         "ContactForm",
#     ]),
#     ("sites", [
#         "Site",
#     ]),
#     ("auth", [
#         "Group",
#         "User"
#     ])
# ]

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587  # in production mode
EMAIL_PORT = 465
# EMAIL_USE_TLS = True  # in production mode
EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False  # in production mode
EMAIL_USE_SSL = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_ADMIN = env('EMAIL_ADMIN')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# SERVER SECURITY SETTINGS IN PRODUCTION MODE
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PHOTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = "DENY"
