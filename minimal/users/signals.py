# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserProfile


log = logging.getLogger('{{ project_name }}_console')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_admin_user_profile(sender, instance, created, **kwargs):
    # Since the API can create users we should avoid the IntegrityError by only
    # allowing this signal do run when we are creating in django admin.
    # This will not work when we use createsuperuser command.
    if instance.is_superuser or instance.is_staff:
        UserProfile.objects.get_or_create(user=instance)
