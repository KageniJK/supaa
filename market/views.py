from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        search = Product.search_bar(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'search': search})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})