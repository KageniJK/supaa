from django import forms
from .models import Product, Stock


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'picture']


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'stock']


