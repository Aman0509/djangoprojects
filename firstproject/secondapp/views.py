from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from . import forms

def secondhomepage(request):
    return render(request, 'secondapp/temp0.html')


def displayquote(request):
    return HttpResponse("<H2>Honesty is the best policy!!</H2>")


def test(request):
    return HttpResponse("<body>Django Framework</body>")


def photo(request):
    return render(request, 'secondapp/temp2.html')


def empdata(request):
    emp = Employee.objects.all()
    emp_dict = {"employees": emp}
    return render(request, 'secondapp/temp1.html', emp_dict)


def userRegistration(request):
    form = forms.UserRegistrationForm()
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
    return render(request, 'secondapp/userRegistration.html', {'form': form})
