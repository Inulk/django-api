"""
Configurations for user app
"""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """user configurations"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
