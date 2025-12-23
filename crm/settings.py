"""
Django settings for crm project.
Production-ready for Render
"""

from pathlib import Path
import os

# --------------------------------------------------
# BASE DIR
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-change-this-in-render-env"
)

DEBUG = True  # ✅ MUST be False in production

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]


JAZZMIN_SETTINGS = {
    "site_title": "Furniture Admin",
    "site_header": "Furniture Dashboard",
    "welcome_sign": "Welcome to the Furniture Admin Panel",
    "site_brand": "Furniture Admin",

    "icons": {
        # --- Authentication ---
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        # --- Shop & Inventory ---
        "accounts.Category": "fas fa-stream",
        "accounts.Product": "fas fa-couch",
        "accounts.ProductDetail": "fas fa-info-circle",
        
        # --- Sales & Contacts ---
        "accounts.BillingDetail": "fas fa-file-invoice-dollar",
        "accounts.ContactMessage": "fas fa-envelope-open-text",
        "accounts.QRCode": "fas fa-qrcode",

        # --- Blog Section ---
        "accounts.BlogCategory": "fas fa-folder",
        "accounts.BlogTag": "fas fa-tags",
        "accounts.BlogPost": "fas fa-blog",

        # --- Website Content & Design ---
        "accounts.CarouselSlide": "fas fa-images",
        "accounts.AboutHeroImages": "fas fa-address-card",
        "accounts.ProjectSectionHeader": "fas fa-heading",
        "accounts.Project": "fas fa-tasks",
        "accounts.TeamSectionHeader": "fas fa-users-cog",
        "accounts.TeamMembers": "fas fa-user-tie",
        "accounts.TestimonialClient": "fas fa-comments",
    },
    # This sets default icons for any new models you add later
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
}

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # WhiteNoise
    "whitenoise.runserver_nostatic",

    # Third-party
    "ckeditor",

    # Local apps
    "accounts",
]



# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise MUST be directly after SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URLS / TEMPLATES
# --------------------------------------------------
ROOT_URLCONF = "crm.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # Custom
                "accounts.context_processors.cart_context",
            ],
        },
    },
]

WSGI_APPLICATION = "crm.wsgi.application"


# --------------------------------------------------
# DATABASE (SQLite – OK for small Render apps)
# --------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# STATIC FILES (RENDER + WHITENOISE)
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# --------------------------------------------------
# MEDIA FILES (UPLOADS)
# --------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# --------------------------------------------------
# CKEDITOR
# --------------------------------------------------
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "all",
        "skin": "moono",
        "codeSnippet_theme": "monokai",
        "extraPlugins": ",".join(
            [
                "codesnippet",
                "widget",
                "dialog",
            ]
        ),
    }
}


# --------------------------------------------------
# AUTH REDIRECTS
# --------------------------------------------------
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "indexFur"
LOGOUT_REDIRECT_URL = "login"


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
