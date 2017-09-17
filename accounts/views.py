from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import ExtUser, School
from django.contrib.auth.models import User


# View for any profile (NOT editing)
def profile(request, username):
    user = User.objects.get(username=username)
    target = ExtUser.objects.get(user=user)
    is_self = False
    school = target.school
    print(school)

    if user.get_username() == request.user.username and request.user.is_authenticated:
        is_self = True

    return render(request, 'profile.html', context={"user": target, "is_self": is_self, "host": request.user})


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
