from django.apps import AppConfig


class OpenprojectSyncConfig(AppConfig):
    name = 'openproject_sync'

    def ready(self):
        import openproject_sync.signals