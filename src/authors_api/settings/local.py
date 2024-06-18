from .base import * #noqa
from .base import env



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",
    default="pJda0Lckwg1RBwNMv8T5mL9DKhTIOplFOHTSPqIXTaR3Ph-enHQ",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL= "sivaniavella@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME= "Authors Sivani"
