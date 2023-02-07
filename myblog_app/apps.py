from django.apps import AppConfig


class MyblogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblog_app'
    verbose_name = 'Приложение для книг'