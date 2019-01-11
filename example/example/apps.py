from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "example"

    def ready(self):
        import example.signals