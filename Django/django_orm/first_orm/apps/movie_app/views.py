from django.shortcuts import render
from .models import Movies


def index(request):
    context = {
        "all_movies": Movies.objects.all()
    }
    return render(request, "movie_app/index.html", context)
