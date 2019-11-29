from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Product


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class SearchForm(forms.ModelForm):
    # email = forms.EmailField()
    search = #Continue Here

    class Meta:
        model = Product
        fields = ['Produit à substituer']
