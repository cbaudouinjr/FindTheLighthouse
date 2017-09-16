from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# For overriding the default User class
admin.site.register(User, UserAdmin)
