from django.apps import AppConfig

class AmmConfig(AppConfig):
    name = 'amm'

    def ready(self):
        import amm.signals