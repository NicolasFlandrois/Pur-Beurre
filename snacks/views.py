from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Product, Category, Favourite


class ProductListView(ListView):
    model = Post
    template_name = 'snacks/products.html'
    context_object_name = 'search'
    # ordering = ['-date_added']
    paginate_by = 5


class UserProductListView(ListView):
    model = Post
    template_name = 'snacks/products.html'
    context_object_name = 'favourites'
    ordering = ['-date_added']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
