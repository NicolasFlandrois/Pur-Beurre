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

  # retrieving URL parameters
  query = request.GET.get('query')
  # If there is no requested parameter we display all the products
  context = {}
  if not query:
    product = Product.objects.all()
  # Otherwise a parameter is transmitted
  else:
    # find a match by "product name"
    product = Product.objects.filter(name=query)

    # if the products do not exist
    if not product.exists():
      context["error"] = True
      context["Product"] = []
  #   else:
  #     context["product_research"] = product[0]
  #     liste_product = Product.objects.filter(
  #         category=product[0].category
  #     ).order_by('nutriscore')[:9]
  #     context["products_substitut"] = liste_product
  #     context["paginate"] = True
  # return render(request, template_name, context)


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
  # def __init__(self, arg):
  #   super(ProductDetailView, self).__init__()
  #   self.arg = arg
