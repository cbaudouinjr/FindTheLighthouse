"""FindTheLighthouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from FindTheLighthouse.views import *

urlpatterns = [
    # Main landing page for site
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),

    # Page dedicated to finding people
    url(r'^people', people, name='people'),

    # Page dedicated to finding events
    url(r'^meetup', meetup, name='meetup'),

    # Link for logout process
    url(r'^logout', logout_user, name='logout'),

    # Page dedicated to logging in
    url(r'^login', login_page, name='login_page'),
]
