# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = models.CharField(max_length=50, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "userprofile"
        verbose_name_plural = "userprofiles"

    def __str__(self):
        return '%s' % self.user
