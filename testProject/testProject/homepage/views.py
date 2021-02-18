from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'homepage/index.html')


@login_required
def gameplay(request):
    return render(request,'homepage/pig_game.html')







