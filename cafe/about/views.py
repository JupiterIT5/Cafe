from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import *
from .forms import *


def catalog_list(request):
    model = Product.objects.filter(is_exists = False)
    context = {
        'dish_list': model
    }
    return render(request, 'cafe/main/index.html', context)


def dish(request, id):
    model = get_object_or_404(Product, pk=id)
    context = {
        'dish': model
    }
    return render(request, 'cafe/dish/dish.html', context)


def all_supplier(request):
    model = Supplier.objects.all()
    context = {
        'all_supplier': model
    }
    return render(request, 'cafe/supplier/main/all.html', context)


def supplier(request, id):
    model = get_object_or_404(Supplier, pk=id)
    context = {
        'supplier': model
    }
    return render(request, 'cafe/supplier/supplier/supplier.html', context)


def add_supplier(request):
    if request.method == 'POST':
        form_add_supplier = SupplierForm(request.POST)
        if form_add_supplier.is_valid() and form_add_supplier.clean_telephone():
            new_supplier = Supplier(**form_add_supplier.cleaned_data)
            new_supplier.save()
            return redirect('all_supplier_list')
        return render(request, 'cafe/supplier/supplier/add_supplier.html', {'form': SupplierForm, 'error': 'error code'})
    else:
        form = SupplierForm
        context = {
            'form': form
        }
        return render(request, 'cafe/supplier/supplier/add_supplier.html', context)
    


def user_registraion(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('catalog_dish_page')
        messages.error(request, 'Данные введены не верно!')
    else:
        form = UserRegistration()
    return render(request, 'cafe/profile/reg.html', context={'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('anonim', request.user.is_anonymous)
            print('auth', request.user.is_authenticated)

            login(request, user)

            print('anonim', request.user.is_anonymous)
            print('auth', request.user.is_authenticated)
            print(user)

            messages.success(request, 'Вы успешно авторизовались')
            return redirect('catalog_dish_page')
        messages.error(request, 'Что-то заполнено не верно')
    else:
        form = LoginForm()
        return render(request, 'cafe/profile/login.html', {'form': form})
        

def user_logout(request):
    if not request.user.is_anonymous:
        logout(request)
        return redirect('catalog_dish_page')
    else:
        return redirect('log in')