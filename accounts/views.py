from django.shortcuts import render, redirect
from accounts.models import ExtUser, Interest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from accounts.forms import RegistrationForm


# A new User registers with the site
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            first = form.cleaned_data.get("first_name")
            last = form.cleaned_data.get("last_name")
            school = form.cleaned_data.get("school")
            interests = form.cleaned_data.get("interest_input")

            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first
            new_user.last_name = last
            new_user.save()

            ext_new = ExtUser.objects.create(school=school, user=new_user)

            if interests:
                parseInterests(ext_new, interests)

            ext_new.save()

            login(request, new_user)
            return redirect('index')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# Parse the comma-separated list of interests from the registration form
def parseInterests(ext_user, interests):
    """
    :param ext_user: ExtUser to add the interests to as they are created.
    :param interests: Comma separated list of interests
    :return: void
    """
    interest_list = interests.split(",")
    for item in interest_list:
        data = item.strip().lower()
        if Interest.objects.filter(name=data).exists():
            ext_user.interests.add(Interest.objects.get(name=data))
        else:
            new_interest = Interest.objects.create(name=data)
            new_interest.save()

            ext_user.interests.add(new_interest)


# View for logging in to site
def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        redirect('index')
    else:
        # Return/display login error
        pass


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
