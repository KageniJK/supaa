from django.shortcuts import render, redirect
from .models import Product, Stock
from .forms import ProductForm, StockForm


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


def panel(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        stock_form = StockForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            return redirect('/panel')
        if stock_form.is_valid():
            item = stock_form.cleaned_data['product']
            if Stock.objects.get(product=item):
                stocked = Stock.objects.get(product=item)
                stocked.stock += stock_form.cleaned_data['stock']
                stocked.save()
            else:
                stock = stock_form.save(commit=False)
                stock.save()
    else:
        product_form = ProductForm()
        stock_form = StockForm()

    return render(request, 'panel.html', {'product_form': product_form, 'stock_form': stock_form})