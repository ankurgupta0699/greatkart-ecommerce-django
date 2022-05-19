from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts import models as accounts_models


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff')
    list_display_links = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(accounts_models.Account, AccountAdmin)
