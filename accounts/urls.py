from django.conf.urls import url

from FindTheLighthouse import views as lighthouse_views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Registration page for new Users
    url(r'^register/', accounts_views.register, name='register'),
    # Login page for User
    url(r'^login/$', auth_views.login, name='login'),
    # Viewing page for any User profile
    url(r'^account/(?P<username>\w+)/profile', accounts_views.profile, name='profile'),
    # Viewing page for request.User's preferences
    url(r'^account/(?P<username>\w+)/preferences', accounts_views.preferences, name='preferences'),
]
