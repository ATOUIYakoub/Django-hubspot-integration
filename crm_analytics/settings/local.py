"""
Local settings for crm_analytics project.
"""

import os
from dotenv import load_dotenv

load_dotenv()

from .base import *

# SECURITY WARNING: keep the secret key used in production!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# HubSpot API Key
HUBSPOT_API_KEY = os.getenv('HUBSPOT_API_KEY')