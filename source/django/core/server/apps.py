# ⚠️ Deprecated module
# This code is no longer maintained.
# Do not use for new features.

from django.apps import AppConfig

class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'
    verbose_name = 'Api server'
