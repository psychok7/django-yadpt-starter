# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth import get_user_model
from guardian.shortcuts import get_objects_for_group, assign_perm

from .models import UserProfile

from authtools.admin import NamedUserAdmin

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


# http://stackoverflow.com/a/10342823/977622
class UserAdmin(NamedUserAdmin):

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        super(UserAdmin, self).save_model(request, obj, form, change)

        # Assign permissions to group so that only members of specified group
        # can view these users
        for group in request.user.groups.all():
            assign_perm('view_user', group, obj)
            assign_perm('add_user', group, obj)
            assign_perm('change_user', group, obj)
            assign_perm('delete_user', group, obj)

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        # This will ensure we get all objects from all groups the user is in.
        # Not sure if django guardian has a better way of doing this.
        objects_for_all_groups = []
        for group in request.user.groups.all():
            objects_for_group = get_objects_for_group(
                group=group, klass=User, perms=[
                    'view_user', 'add_user', 'change_user', 'delete_user'
                ]
            ).values_list('id', flat=True)

            objects_for_all_groups.extend(list(objects_for_group))

        return qs.filter(id__in=objects_for_group)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

