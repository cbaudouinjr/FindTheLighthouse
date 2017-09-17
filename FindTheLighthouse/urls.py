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
import FindTheLighthouse.views as Lighthouse_views

urlpatterns = [
    # Main landing page for site
    url(r'^$', Lighthouse_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),

    # Page dedicated to finding people
    url(r'^people', Lighthouse_views.people, name='people'),

    # Page dedicated to finding events
    url(r'^meetup', Lighthouse_views.meetup, name='meetup'),

    # Link for logout process
    url(r'^logout', Lighthouse_views.logout_user, name='logout'),
]
