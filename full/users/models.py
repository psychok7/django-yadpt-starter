# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    is_guest = models.BooleanField(default=False)
    guest_email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "userprofile"
        verbose_name_plural = "userprofiles"
        permissions = (
            ('view_userprofile', 'Can view UserProfile'),
        )

    def __str__(self):
        return '%s' % self.user
