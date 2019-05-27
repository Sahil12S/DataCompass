from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random
import math

# Helper function


def generateRandom(min, max):
    return math.floor(random.random() * (max - min) + min)


# Create your views here.
def index(request, gold=0):

    gold = request.session.get('gold', 0)
    activities = request.session.get('activities', [])

    context = {
        'gold': gold,
        'activities': activities
    }
    return render(request, 'goldapp/index.html', context)


def process(request):
    # Returns value of session or 0
    gold = request.session.get('gold', 0)
    activities = request.session.get('activities', [])

    if request.method == "POST":
        time = strftime("%Y/%m/%d %I:%M %p", gmtime())
        if "farm" in request.POST:
            g = generateRandom(10, 20)
            request.session['gold'] = gold + g
            activities.append(
                f"Earned {g} golds from the farm! ({time})")
        elif "cave" in request.POST:
            g = generateRandom(5, 10)
            request.session['gold'] = gold + g
            activities.append(
                f"Earned {g} golds from the cave! ({time})")
        elif "house" in request.POST:
            g = generateRandom(2, 5)
            request.session['gold'] = gold + g
            activities.append(
                f"Earned {g} golds from the house! ({time})")
        elif "casino" in request.POST:
            g = generateRandom(-50, 50)
            request.session['gold'] = gold + g
            if g < 0:
                activities.append(
                    f"Entered a casino and lost {g} golds... Ouch! ({time})")
            else:
                request.session['activities'].append(
                    f"Entered a casino and won {g} golds... Yay! ({time})")
    request.session['activities'] = activities
    return redirect(index)


def reset(request):
    if request.method == "POST":
        try:
            del request.session['gold']
            del request.session['activities']
        except KeyError:
            pass
    return redirect(index)
