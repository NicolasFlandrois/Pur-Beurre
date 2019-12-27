from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views import View
from .models import Product, Favourite
from .nutriment import nutriments


def allListView(request):
    context = {}
    return redirect('/snacks/search/?search=', context)


class SearchListView(ListView):
    model = Product
    template_name = 'snacks/list.html'
    context_object_name = 'results'
    paginate_by = 6

    def get_context_data(self):
        context = super().get_context_data()
        context['url'] = f'/snacks/search/?search={self.request.GET.get("search")}'
        context['searched'] = self.request.GET.get('search')
        context['title'] = 'Recherche'
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')

        if not search or search == ' ':
            return super().get_queryset().order_by('nutriscore')

        found = Product.objects.filter(name__icontains=search)

        if not found:
            return Product.objects.none()

        cat = found[0].category
        return Product.objects.filter(category=cat).order_by('nutriscore')


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
    paginate_by = 6

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Favoris'
        context['url'] = f'/snacks/favourites/?'
        return context

    def get_queryset(self):
        return Favourite.objects.filter(
            user=self.request.user).order_by('-date_added')

    def test_func(self):
        if self.request.user:
            return True
        return False


class FavAddView(LoginRequiredMixin, View):
    model = Favourite

    def get(self, request, pk):

        if not pk:
            return HttpResponseRedirect('/favourites')

        prod = Product.objects.get(pk=pk)

        if not prod:
            return HttpResponseRedirect('/favourites')

        fav_new, created = Favourite.objects.get_or_create(
            user=auth.get_user(request),
            product=prod)

        if not created:
            pass

        return HttpResponseRedirect('/snacks/favourites')
        # ISSUE: When arbitrary want to add a prod that does not exists in DB.prod_tbl, ERROR page.. But I want it to redirect user to Fav page instead


class FavDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    model = Favourite

    def get(self, request, pk):

        if not pk:
            return HttpResponseRedirect('/favourites')

        prod = Product.objects.get(pk=pk)

        if not prod:
            return HttpResponseRedirect('/favourites')

        try:
            fav_del = Favourite.objects.get(
                user=auth.get_user(request),
                product=prod)
            fav_del.delete()
            # return HttpResponseRedirect('/snacks/favourites')
        except:
            pass
            # except Favourite.DoesNotExist:
            #     fav_del = None
        return HttpResponseRedirect('/snacks/favourites')

        # ISSUE: When arbitrary want to delete a fav that does not exists in DB.fav_tbl, ERROR page.. But I want it to redirect user to Fav page instead

    def test_func(self):
        prod_pk = self.kwargs.get('pk')
        fav = Favourite.objects.get(product=prod_pk)
        if self.request.user == fav.user:
            return True
        return False
