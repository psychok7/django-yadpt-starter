# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_guest', models.BooleanField(default=False)),
                ('guest_email', models.EmailField(max_length=255, blank=True, null=True)),
                ('phone', models.CharField(max_length=50, blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_userprofile', 'Can view UserProfile'),),
                'verbose_name': 'userprofile',
                'verbose_name_plural': 'userprofiles',
            },
        ),
    ]
