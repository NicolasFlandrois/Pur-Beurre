from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Product, Category, Favourite


class SearchListView(ListView):
    model = Product
    template_name = 'snacks/search.html'
    context_object_name = 'search'
    # ordering = ['-date_added']
    paginate_by = 6


class FavouritesListView(ListView):
    model = Favourite
    template_name = 'snacks/favourites.html'
    context_object_name = 'favourites'
    ordering = ['-date_added']
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-date_posted')
