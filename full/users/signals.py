# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.core import management
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from rest_framework.authtoken.models import Token
from users.models import UserProfile


log = logging.getLogger('dorothy_console')


def add_user_permissions(sender, **kwargs):
    # Add a custom permission with a post_migrate signal.
    content_type = ContentType.objects.get_for_model(get_user_model())
    permission, created = Permission.objects.get_or_create(
        codename='view_user', name='View user', content_type=content_type
    )

    if created:
        log.info('Added "view_user" permission to users'.format(**locals()))


def create_user_groups(sender, **kwargs):
    # Reloads permissions. Check http://stackoverflow.com/a/36160797/977622
    management.call_command('update_permissions')
    group, created = Group.objects.get_or_create(name='personal')
    if created:
        log.info('Added "personal" group'.format(**locals()))
        assign_perm('core.view_savedlocation', group)
        log.info('Assigned permissions to "personal"'.format(**locals()))

    group, created = Group.objects.get_or_create(name='business')
    if created:
        log.info('Added "business" group'.format(**locals()))
        assign_perm('core.add_savedlocation', group)
        assign_perm('core.change_savedlocation', group)
        assign_perm('core.view_savedlocation', group)
        assign_perm('core.delete_savedlocation', group)
        log.info('Assigned permissions to "business"'.format(**locals()))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_admin_user_profile(sender, instance, created, **kwargs):
    # Since the API can create users we should avoid the IntegrityError by only
    # allowing this signal do run when we are creating in django admin.
    # This will not work when we use createsuperuser command.
    if instance.is_superuser or instance.is_staff:
        UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
