from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import ExtUser
from django.contrib.auth.models import User


# View for any profile (NOT editing)
def profile(request, username):
    user = User.objects.get(username=username)
    target = ExtUser.objects.get(user=user)
    return render(request, 'profile.html')


# View for a User's preferences (NOT editing)
def preferences(request, username):
    user = User.objects.get(username=username)
    target = ExtUser.objects.get(user=user)
    return render(request, 'preferences.html')


# View for editing the request.User's profile info
def editProfile(request, username):
    pass


# View for editing the request.User's preferences
def editPreferences(request, username):
    pass
