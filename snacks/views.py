from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Product, Favourite
from .parser import parser


def errorView(request):
    context = {}
    return render(request, 'snacks/error.html', context)


class SearchListView(ListView):
    model = Product
    template_name = 'snacks/search.html'
    context_object_name = 'results'
    ordering = ['-nutriscore']
    paginate_by = 4

    def get_queryset(self):
        # HERE ISSUE The GET param isn't transfered further
        query = self.kwargs['query']
        parsed = parser(query.lower())
        # Mettre un Try/Except (Except return E404)
        if parsed[1] > 0:
            search_result = Product.objects.filter(pk=int(parsed[0])).first()

            if not search_result is None:
                print("Successfull ",
                      search_result.pk, search_result.name)

                return Product.objects.filter(
                    category=search_result.category)
            else:
                print('Not in DB')
                return redirect('/error')

        else:
            print("No Query")
            return Product.objects.all()


class FavouritesListView(ListView):
    model = Favourite
    template_name = 'snacks/favourites.html'
    context_object_name = 'favourites'
    ordering = ['-date_added']
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-date_posted')


class ProductDetailView(DetailView):
    """docstring for ProductDetailView"""

    def __init__(self, arg):
        super(ProductDetailView, self).__init__()
        self.arg = arg
