"""
WSGI config for data_analysis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import pathlib

import dotenv
from django.core.wsgi import get_wsgi_application

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE_PATH = BASE_DIR / '.env'
dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_analysis.settings')

application = get_wsgi_application()
