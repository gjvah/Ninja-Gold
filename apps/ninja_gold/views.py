import random
from django.conf.urls import url
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # request.session['name'] = request.POST['name']
    # request.session['counter'] = 100
    
    if ('key' in request.session):
        request.session['key'] = "True"
    else:
        request.session['key'] = "False"

    if ('total_gold' not in request.session):
        request.session['total_gold'] = 0
        request.session['message'] = []
        request.session['moves'] = 0
        request.session['max_moves'] = 20
        request.session['max_gold'] = 250
        
    context = {
            "message": request.session['message']
        }
    return render(request, "ninja_gold/index.html", context)


def settings(request):
    request.session['total_gold'] = 0
    request.session['message'] = []
    request.session['moves'] = 0
    request.session['max_moves'] = int(request.POST["moves-requested"])
    request.session['max_gold'] = int(request.POST["gold"])

    return redirect('/ninja_gold')

def media(request):
    return redirect('/')



def process(request):
    location = request.POST['location']
    new_gold = 0
    moves = 0

    if location == "farm":
        new_gold = random.randint(5, 20)
        request.session['message'].insert(0, "<span class = 'green'>You went to the <strong>Farm</strong> and found <strong>" + str(new_gold) + "</strong> gold!<br></span>")
        moves = 1

    elif location == "cave":
        new_gold = random.randint(10, 15)
        request.session['message'].insert(0, "<span class = 'green'>You went to the <strong>Cave</strong> and found <strong>" + str(new_gold) + "</strong> gold!<br></span>")
        moves = 1

    elif location == "house":
        new_gold = random.randint(8, 12)
        request.session['message'].insert(0, "<span class = 'green'>You went to the <strong>House</strong> and found <strong>" + str(new_gold) + "</strong> gold!<br></span>")
        moves = 1

    elif location == "casino":
        new_gold = random.randint(-50, 50)
        if (new_gold > 0):
            request.session['message'].insert(0, "<span class = 'green'>You went to the <strong>Casino</strong> and won <strong>" + str(new_gold) + "</strong> gold!<br></span>")
        elif (new_gold < 0):
            request.session['message'].insert(0, "<span class = 'red'>You went to the <strong>Casino</strong> and lost <strong>" + str(new_gold * -1) + "</strong> gold!<br></span>")
        else:
            request.session['message'].insert(0, "<span class = 'green'>You went to the <strong>Casino and came out even <strong><br></span>")
        moves = 1

    request.session['total_gold'] += new_gold
    request.session['moves'] += moves

    return redirect('/ninja_gold')

def reset(request):
    request.session['total_gold'] = 0
    request.session['message'] = []
    request.session['moves'] = 0
    return redirect('/ninja_gold')

def defaults(request):
    request.session['total_gold'] = 0
    request.session['message'] = []
    request.session['moves'] = 0
    request.session['max_moves'] = 20
    request.session['max_gold'] = 250
    return redirect('/ninja_gold')

def register(request):
    request.session.clear()
    return redirect('my_app/index.html')