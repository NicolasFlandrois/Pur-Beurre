from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Product, Favourite


def errorView(request):
    context = {}
    return render(request, 'snacks/error.html', context)


class AllListView(ListView):
    model = Product
    template_name = 'snacks/list.html'
    context_object_name = 'results'
    ordering = ['nutriscore']
    paginate_by = 4

    def allView(request):
        print('All product')
        return Product.objects.all()


class SearchListView(ListView):
    model = Product
    template_name = 'snacks/list.html'
    context_object_name = 'results'
    ordering = ['nutriscore']
    paginate_by = 4

    def get_queryset(self):
        search = self.request.GET.get('search')

        if not search:
            return super().get_queryset()

        found = Product.objects.filter(name__icontains=search)

        if not found:
            raise Exception('Produit Non Trouvé')

        cat = found[0].category
        return Product.objects.filter(category=cat)


class FavouritesListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Favourite
    template_name = 'snacks/list.html'
    context_object_name = 'results'
    ordering = ['-date_added']
    paginate_by = 4

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user).order_by('-date_added')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'snacks/details.html'
    context_object_name = 'details'

    # need to compile info from OFF's Json API

    def get_queryset(self):
        prod_pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=prod_pk)
