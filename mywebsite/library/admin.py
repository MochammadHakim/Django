from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import BookAttribute, CustomUser

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'CustomUser'

class UserAdmin(BaseUserAdmin):
    inlines = (CustomUserInline,)

# Unregister the default User admin and register the new UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register other models
admin.site.register(BookAttribute)
