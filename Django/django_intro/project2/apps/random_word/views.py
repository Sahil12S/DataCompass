from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    num_attempt = request.session.get('num_attempt', 0)
    request.session['num_attempt'] = num_attempt + 1
    context = {
        'random_string': get_random_string(length=14),
        'num_attempt': num_attempt
    }
    if request.method == "POST":
        try:
            del request.session['num_attempt']
        except KeyError:
            pass
        print("POST METHOD")
        return redirect("/random_word")
    if request.method == "GET":
        print(request.GET)
        print(type(request.GET))
        print("GET METHOD")

    return render(request, 'random_word/index.html', context)
