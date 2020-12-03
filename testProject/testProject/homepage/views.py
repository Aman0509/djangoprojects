from django.shortcuts import render
from .forms import NewUsersForm
from .models import NewUsers

# Create your views here.

def home(request):
    return render(request, 'homepage/index.html')

def signUp(request):
    form = NewUsersForm()
    if request.method == 'POST':
        form = NewUsersForm(request.POST)
        if form.is_valid():
            form.save()
        return home(request)
    return render(request, 'homepage/signup.html', {'form': form})



