from django.shortcuts import render, HttpResponse

# Create your views here.


def register(request):
    return HttpResponse("placeholder for users to create a new user record")


def login(request):
    return HttpResponse("placeholder for users to log in")


def all(request):
    return HttpResponse("placeholder to later display all the list of users")
