from django.contrib import admin
from .models import BookAttribute
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser, CustomUserAdmin
admin.site.register(BookAttribute)

# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)