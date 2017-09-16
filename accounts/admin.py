from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Interest)
admin.site.register(School)
admin.site.register(ExtUser)
admin.site.register(Event)
admin.site.register(Attendee)