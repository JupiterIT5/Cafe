from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def list_product(request):
    model = Product.objects.all()
    context = {
        'products_list': model
    }
    return render(request, 'shop/product/all_product.html', context)


def get_one_product(request, id):
    model = get_object_or_404(Product, pk=id)
    context = {
        'product': model
    }
    return render(request, 'shop/product/one_product.html', context)

def get_one_filter(request):
    model = Product.objects.filter(is_exists = request.GET.get('is_ex'))
    context = {
        'list_product': model
    }
    return render(request, 'shop/product/all_product.html', context)

def get_more_filter(request):
    model = Product.objects.filter(
        price__lte = request.GET.get('max_price'),
        price__gt = request.GET.get('min_price'),
    )
    context = {
        'list_product': model
    }
    return render(request, 'shop/product/all_product.html', context)