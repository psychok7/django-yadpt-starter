# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from django.contrib.auth import get_user_model

from users.models import UserProfile

from authtools.admin import NamedUserAdmin

User = get_user_model()
USERNAME_FIELD = User.USERNAME_FIELD


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


# http://stackoverflow.com/a/10342823/977622
class UserAdmin(NamedUserAdmin):
    list_display = (
        'is_active', USERNAME_FIELD, 'is_superuser', 'is_staff', 'get_phone'
    )

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)

    def get_phone(self, obj):
        return obj.userprofile.phone

    get_phone.short_description = 'Phone'
    get_phone.admin_order_field = 'userprofile__phone'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
