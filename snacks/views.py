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
from .forms import SearchForm


def errorView(request):
    context = {}
    return render(request, 'snacks/error.html', context)


class SearchListView(ListView):
    model = Product
    template_name = 'snacks/search.html'
    context_object_name = 'results'
    ordering = ['nutriscore']
    paginate_by = 4

    def search(request):
        query = request.GET['search']
        print('Got GET request query', query)
        try:
            parsed = parser(query.lower())
            if parsed[1] > 0:
                search_result = Product.objects.filter(
                    pk=int(parsed[0])).first()

                if search_result is not None:
                    return Product.objects.filter(
                        category=search_result.category)
                else:
                    raise

            else:
                # return Product.objects.all()
                raise

        except:
            return redirect('/error')


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
