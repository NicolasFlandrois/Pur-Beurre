from django import forms
from .models import Product


class SearchForm(forms.ModelForm):
    search = forms.CharField(label='Produit à substituer', max_length=100)

    class Meta:
        model = Product
        fields = ['name']
