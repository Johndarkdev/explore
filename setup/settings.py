from pathlib import Path from dj_database_url import parse as db_url from decouple import config import cloudinary

Base do projeto

BASE_DIR = Path(file).resolve().parent.parent

SECURITY

SECRET_KEY = config("SECRET_KEY", default="insecure-secret")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1").split(",")

Apps

THIRDY_PART_APPS = [ 'django_ckeditor_5', 'cloudinary', 'cloudinary_storage' ]

MY_APPS = [ 'blog.apps.BlogConfig', ]

DJANGO_APPS = [ "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles", "django.contrib.sitemaps" ]

INSTALLED_APPS = DJANGO_APPS + MY_APPS + THIRDY_PART_APPS

Middleware

MIDDLEWARE = [ "django.middleware.security.SecurityMiddleware", "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static files na produção "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware", "django.middleware.clickjacking.XFrameOptionsMiddleware", ]

ROOT_URLCONF = "setup.urls"

TEMPLATES = [ { "BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True, "OPTIONS": { "context_processors": [ "django.template.context_processors.debug", "django.template.context_processors.request", "django.contrib.auth.context_processors.auth", "django.contrib.messages.context_processors.messages", ], }, }, ]

WSGI_APPLICATION = "setup.wsgi.application"

Database

DATABASES = { "default": db_url( config("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}") ) }

Password validation

AUTH_PASSWORD_VALIDATORS = [ {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",}, {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",}, {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",}, {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",}, ]

Internationalization

LANGUAGE_CODE = "pt-br" TIME_ZONE = "Africa/Luanda" USE_I18N = True USE_TZ = True

Static files

STATIC_URL = "/static/" STATICFILES_DIRS = [BASE_DIR / "static"]      # arquivos do projeto STATIC_ROOT = BASE_DIR / "staticfiles"        # coletados na produção STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

Media

MEDIA_URL = "/media/" MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEditor

CKEDITOR_5_UPLOADS_PATH = "image/uploads/"

CKEDITOR_5_CONFIGS = { 'default': { 'toolbar': [ 'heading', '|', 'bold', 'italic', 'link', '|', 'numberedList', 'bulletedList', '|', 'imageUpload', 'blockQuote', 'undo', 'redo' ], 'height': 400, 'width': '100%', }, }

Cloudinary

CLOUDINARY_STORAGE = { "CLOUD_NAME": config("CLOUD_NAME"), "API_KEY": config("API_KEY"), "API_SECRET": config("API_SECRET"), }

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CKEDITOR_5_FILE_STORAGE = DEFAULT_FILE_STORAGE

cloudinary.config( cloud_name=config("CLOUD_NAME"), api_key=config("API_KEY"), api_secret=config("API_SECRET"), secure=True )

News API

NEWSAPI_KEY = config("NEWSAPI_KEY", default="")

