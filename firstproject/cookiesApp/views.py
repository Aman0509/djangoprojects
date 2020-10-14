from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm


def homepage(request):
    return render(request, 'cookiesApp/homepage.html')


def setCookie(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Testing cookie option is enabled on browser or not</h2>")


def validateCookie(request):
    if request.session.test_cookie_worked():
        print("Cookies are enabled")  # This will be print on console
        request.session.delete_test_cookie()
    return HttpResponse("<h2>Cookies Validation Completed</h2>")


def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count']) + 1
    else:
        count = 1
    response = render(request, 'cookiesApp/count.html', {'count': count})
    response.set_cookie('count', count)
    return response


def index(request):
    return render(request, 'cookiesApp/index.html')


def addItem(request):
    form = ItemForm()
    response = render(request, 'cookiesApp/addItem.html', {'form': form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 120)  # In cookie, add item is getting saved and setting also the
            # cookie timeout to 120 sec
    return response


def displayCart(request):
    return render(request, 'cookiesApp/displayItem.html')
