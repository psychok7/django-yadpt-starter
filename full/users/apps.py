from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
        post_migrate.connect(users.signals.add_user_permissions, sender=self)
        post_migrate.connect(users.signals.create_user_groups, sender=self)
