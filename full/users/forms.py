# -*- coding: utf-8 -*-

from django import forms
from localflavor.pt.forms import PTPhoneNumberField

from users.models import UserProfile


class UserProfileForm(forms.ModelForm):

    phone = PTPhoneNumberField(required=False)

    class Meta:
        model = UserProfile
        fields = ['user', 'phone', 'created_on', 'updated_on']
