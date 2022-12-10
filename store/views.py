from django.shortcuts import render

from .models import Product, Category

def categories(request):
    return {
        'categories': Category.object.all()
    }
     


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
