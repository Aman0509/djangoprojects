from django.shortcuts import render
from .forms import ItemForm
from django.http import HttpResponse


def homepage(request):
    return render(request, 'sessionAPI/homepage.html')


def pageCount(request):
    count = request.session.get('count', 0) # We are initializing count with 0 inside get method
    count += 1
    request.session['count'] = count
    return render(request, 'sessionAPI/count.html', {'count': count})


def index(request):
    # raise("XXX")
    request.session.set_expiry(60)
    del request.session['count']
    return render(request, 'sessionAPI/index.html')


def addItem(request):
    form = ItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        # sending data into session
        request.session[name] = quantity  # key is the name and value of name is quantity
    return render(request, 'sessionAPI/addItem.html', {'form': form})


def displayCart(request):
    return render(request, 'sessionAPI/displayItem.html')