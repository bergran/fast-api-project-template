import os
from datetime import timedelta


class Config:
    TEST = {
        'database': 'test_default',
    }

    _DATABASES = {
        'type': '',
        'username': '',
        'password': '',
        'host': '',
        'port': '',
        'database': '',
    }


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ('TRUE', '1')
    return result


# ~~~~~ PATH ~~~~~

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ~~~~~ TEST ~~~~~

TEST_RUN = getenv_boolean('TEST_RUN', False)

# ~~~~~ API ~~~~~


# ~~~~~ SECRET ~~~~~
SECRET_KEY = os.getenv('SECRET_KEY', 'cuerno de unicornio :D')

if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

# ~~~~~ APPS ~~~~~
APPS = [
    'health_check',
    'token',
    'hello_world'
]

# ~~~~~ JWT ~~~~~
JWT_EXPIRATION_DELTA = timedelta(hours=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 10)))  # in hours
JWT_REFRESH_EXPIRATION_DELTA = timedelta(hours=int(os.getenv('JWT_REFRESH_EXPIRATION_DELTA', 10)))  # in hours
JWT_AUTH_HEADER_PREFIX = os.getenv('JWT_AUTH_HEADER_PREFIX', 'JWT')
JWT_SECRET_KEY = SECRET_KEY

# ~~~~~ CORS ~~~~~

BACKEND_CORS_ORIGINS = os.getenv(
    'BACKEND_CORS_ORIGINS'
)  # a string of origins separated by commas, e.g: 'http://localhost, http://localhost:4200, http://localhost:3000

# ~~~~~ APP ~~~~~
PROJECT_NAME = os.getenv('PROJECT_NAME', 'Fastapi')

# ~~~~~ EMAIL ~~~~~
SENTRY_DSN = os.getenv('SENTRY_DSN')

SMTP_TLS = getenv_boolean('SMTP_TLS', True)
SMTP_PORT = None
_SMTP_PORT = os.getenv('SMTP_PORT')

if _SMTP_PORT is not None:
    SMTP_PORT = int(_SMTP_PORT)

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

EMAILS_FROM_EMAIL = os.getenv('EMAILS_FROM_EMAIL')
EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = '/app/app/email-templates/build'
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL

# ~~~~~ DATA_BASE ~~~~~

DATABASES = {
    'type': os.environ.get('type', 'postgresql'),
    'database': os.environ.get('database', 'fastapi'),
    'username': os.environ.get('username', 'myproject'),
    'password': os.environ.get('password', 'myproject'),
    'host': os.environ.get('host', 'localhost'),
    'port': os.environ.get('port', 5432)
}


# ~~~~~ OAUTH 2 ~~~~~

SCOPES = {
    'read': 'Read',
    'write': 'Write'
}
