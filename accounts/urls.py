from django.conf.urls import url

from FindTheLighthouse import views as lighthouse_views
from accounts import views as accounts_views

urlpatterns = [
    # Main landing page for the site
    url(r'^$', lighthouse_views.index, name='index'),
    # Registration page for new Users
    url(r'^register/', accounts_views.register, name='register'),
    # Viewing page for any User profile
    url(r'^account/(?P<username>\w+)/profile', accounts_views.profile, name='profile'),
    # Viewing page for request.User's preferences
    url(r'^account/(?P<username>\w+)/preferences', accounts_views.preferences, name='preferences'),
]
