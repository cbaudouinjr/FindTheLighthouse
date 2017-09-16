from django.shortcuts import render
from django.http import HttpResponse


# Main landing page of the site
def index(request):
    return render(request, 'index.html')


# View for "Find Your People"
def people(request):
    return render(request, 'people.html')


# View for "Meet Up"
def meetup(request):
    return render(request, 'meetup.html')
