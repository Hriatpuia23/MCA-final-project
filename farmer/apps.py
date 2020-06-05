from django.apps import AppConfig


class FarmerConfig(AppConfig):
    name = 'farmer'

    def ready(self):
        import farmer.signals
