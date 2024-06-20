from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re


class ProviderForm(forms.Form):
    name = forms.CharField(min_length=10, max_length=255, label='Название компании')
    name_provider = forms.CharField(min_length=2, max_length=50, label='Имя')
    lastname_provider = forms.CharField(min_length=2, max_length=50, label='Фамилия')
    surname_provider = forms.CharField(min_length=2, max_length=50, label='Очество')
    phone = forms.CharField(max_length=20, label='Телефон')
    adress = forms.CharField(min_length=10, label='Адрес')
    
    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Название компании'})
    name_provider.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
    lastname_provider.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
    surname_provider.widget.attrs.update({'class': 'form-control', 'placeholder': 'Очество'})
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'Телефон'})
    adress.widget.attrs.update({'class': 'form-control', 'placeholder': 'Адрес'})
    
    def clean_telephone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone):
            return phone
        return False
    

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        username = forms.CharField(
            label='Имя',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        
        email = forms.EmailField(
            label='Email',
            widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
        
        password1 = forms.CharField(
            label='Пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
        
        password2 = forms.CharField(
            label='Повторите пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Введите логин',
        widget=forms.TextInput({'class': 'form-control'}),
        min_length=2
    )
    
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput({'class': 'form-control'}),
    )