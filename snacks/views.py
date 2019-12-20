from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Product, Favourite
from .nutriment import nutriments


def allListView(request):
    context = {}
    return redirect('/snacks/search/?search=', context)


class SearchListView(ListView):
    model = Product
    template_name = 'snacks/list.html'
    context_object_name = 'results'
    ordering = ['nutriscore']
    paginate_by = 4

    def get_context_data(self):
        context = super().get_context_data()
        context['url'] = f'/snacks/search/?search={self.request.GET.get("search")}'
        context['searched'] = self.request.GET.get('search')
        context['title'] = 'Recherche'
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')

        if not search:
            return super().get_queryset()

        found = Product.objects.filter(name__icontains=search)

        if not found:
            return Product.objects.none()

        cat = found[0].category
        return Product.objects.filter(category=cat)


class FavouritesListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Favourite
    template_name = 'snacks/list.html'
    context_object_name = 'results'
    ordering = ['-date_added']
    paginate_by = 4

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Favoris'
        return context

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user).order_by('-date_added')

    def test_func(self):
        if self.request.user:
            return True
        return False


class ProductDetailView(DetailView):
    model = Product
    template_name = 'snacks/details.html'
    context_object_name = 'details'

    def get_queryset(self):
        prod_pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=prod_pk)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['nutriments'] = nutriments(context['details'].ean)
        context['title'] = 'Fiche produit'
        return context
