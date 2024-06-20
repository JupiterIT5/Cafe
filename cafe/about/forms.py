from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re

MAX_LENGTH = 255

class SupplierForm(forms.Form):
    name = forms.CharField(max_length=MAX_LENGTH, label='Название компании')
    agent_lastname = forms.CharField(max_length=MAX_LENGTH, label='Фамилия представителя')
    agent_name = forms.CharField(max_length=MAX_LENGTH, label='Имя представителя')
    agent_surname = forms.CharField(max_length=MAX_LENGTH, label='Отчество представителя')
    phone = forms.CharField(max_length=16, label='Телефон представителя')
    location = forms.CharField(max_length=MAX_LENGTH, label='Адрес')
    
    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Название компании'})
    agent_lastname.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
    agent_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
    agent_surname.widget.attrs.update({'class': 'form-control', 'placeholder': 'Отчество'})
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'Телефон'})
    location.widget.attrs.update({'class': 'form-control', 'placeholder': 'Адрес'})
    
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