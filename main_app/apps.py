from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

    # Overriding the ready() method to register signals upon init. 
    # -> Used to create User Profile when User is created:
    def ready(self):
        import main_app.signals

