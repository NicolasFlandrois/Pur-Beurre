from django.test import SimpleTestCase
from django.urls import reverse, resolve
from snacks.views import allListView
from snacks.views import (SearchListView,
                          FavouritesListView,
                          ProductDetailView,
                          FavAddView,
                          FavDeleteView)


class TestUrls(SimpleTestCase):
    """Class Test - TestUrls - Testing URLs"""

    # Testing Function based url
    def test_search_all_view_url_resolves(self):
        url = reverse('allsearch')
        self.assertEquals(resolve(url).func, allListView)

    # Testing Class based url
    def test_SearchListView_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchListView)

    def test_FavouritesListView_url_resolves(self):
        url = reverse('favourites')
        self.assertEquals(resolve(url).func.view_class, FavouritesListView)

    def test_ProductDetailView_url_resolves(self):
        url = reverse('detail', args=['9'])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)

    def test_FavAddView_url_resolves(self):
        url = reverse('fav-add', args=['9'])
        self.assertEquals(resolve(url).func.view_class, FavAddView)

    def test_FavDeleteView_url_resolves(self):
        url = reverse('fav-del', args=['9'])
        self.assertEquals(resolve(url).func.view_class, FavDeleteView)
