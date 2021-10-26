from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(max_length=100, required=True, widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}))

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

WOMEN_STYLES = [
    ('all', 'All'),
    ('dress', 'Dresses'),
    ('top', 'Tops'),
    ('jumpsuit', 'Jumpsuits'),
    ('saree', 'Sarees')
    ]
MEN_STYLES = [
    ('all', 'All'),
    ('jacket', 'Jackets'),
    ('shirt', 'Shirts'),
    ('tshirt', 'tshirts')
    ]

class MenProductOptions(forms.Form):
    styles = forms.ChoiceField(label='', choices=MEN_STYLES, required=False)

class WomenProductOptions(forms.Form):
    styles = forms.ChoiceField(label='', choices=WOMEN_STYLES, required=False)

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)