from django.shortcuts import render, HttpResponse
from time import gmtime, strftime


# Create your views here.
def index(request):
    context ={
        "time": strftime("%a, %d %b %Y %I:%M %p", gmtime() )
    }
    return render(request, 'time_display/index.html', context )
    # return HttpResponse(f"Time: {context}")