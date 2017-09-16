from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *


class ExtUserInline(admin.TabularInline):
    model = ExtUser
    fields = ('school', 'user', 'interests')


class MyUserAdmin(UserAdmin):
    inlines = (ExtUserInline, )


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Interest)
admin.site.register(School)
admin.site.register(ExtUser)
admin.site.register(Event)
admin.site.register(Attendee)
