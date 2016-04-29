# -*- coding: utf-8 -*-

import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import UserProfile

log = logging.getLogger('dorothy_console')


class UserProfileSerializer(serializers.ModelSerializer):
    api_token = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('phone', 'api_token',)

    def get_api_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj.user)
        return token.key


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(required=False)
    api_token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'name', 'password', 'api_token', 'user_profile',
            'last_login'
        )
        extra_kwargs = {'password': {'write_only': True, }, }

    def create(self, validated_data):
        # http://goo.gl/dElBKy
        profile_data = None
        if validated_data.get('user_profile'):
            profile_data = validated_data.pop('user_profile')

        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )

        user = get_user_model().objects.create(**validated_data)

        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )
        return super(UserSerializer, self).update(instance, validated_data)

    def get_api_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key




