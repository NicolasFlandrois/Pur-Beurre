from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
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
        return Favourite.objects.filter(
            user=self.request.user).order_by('-date_added')

    def test_func(self):
        if self.request.user:
            return True
        return False


# class FavCreateView(LoginRequiredMixin, CreateView):
#     model = Favourite
#     # fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.user = self.request.user.pk
#         form.instance.product = self.request.product.pk
#         return super().form_valid(form)


# class FavDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Favourite
#     # success_url = '/'

#     def test_func(self):
#         fav = self.get_object()
#         if self.request.user == fav.user:
#             return True
#         return False


def fav_add(request):
    fav = Favourite(user=request.user, product=request.product)
    fav.save()


def fav_del(request):
    fav = Favourite(pk=request.pk)
    fav.delete()
# >>> from snacks.models import Favourite
# >>> from snacks.models import Product
# >>> from django.contrib.auth.models import User
# >>> user = User.objects.get(pk=5)
# >>> user
# <User: admin-PurBeurre>
# >>> prod = Product.objects.get(pk=113)
# >>> prod
# <Product: patamilka - milka>
# >>> Favourite.objects.count()
# 1
# >>> fav = Favourite(user=user, product=prod)
# >>> fav
# <Favourite: User: admin-PurBeurre, Favourite: patamilka - milka, Date: 2019-12-24 16:41:30.428154+00:00>
# >>> fav.save()
# >>> Favourite.objects.count()
# 2
# >>> fav_del = Favourite.objects.get(pk=2)
# >>> fav_del.delete()
# (1, {'snacks.Favourite': 1})
# >>> Favourite.objects.count()
# 1
# >>> fav.save()
