from django.shortcuts import render
from django.contrib.auth.models import User


# Main landing page of the site
def index(request):

    logged_in = False
    username = ""

    if User.is_authenticated:
        logged_in = True
        username = request.user.username
        print(username)

    return render(request, 'index.html', context={"logged_in": logged_in,
                                                  "username": username})

# View for "Find Your People"
def people(request):
    return render(request, 'people.html')


# View for "Meet Up"
def meetup(request):
    return render(request, 'meetup.html')
