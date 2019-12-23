from django.test import TestCase, Client
from django.urls import reverse
from snacks.models import Product, Favourite


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.allsearch_url = reverse('snacks-allsearch')
        self.searchlist_url = reverse('snacks-search')
        self.detail_url = reverse('snacks-detail', args=['1'])
        self.prod_test_1 = Product.objects.create(
            pk='1',
            ean='3350033118072',
            name='test 1',
            category='cat 1',
            image='product_default.png',
            nutriscore='a'
        )
        # self.fav_url = reverse('snacks-favourites')
        # self.fav_test_1 = Favourite.objects.create(
        #     date='2019-12-20 09:00:00',
        #     user=1, #ValueError: Cannot assign "1": "Favourite.user" must be a "User" instance.
        #     product=1
        # )

    # Testing Function based views
    def test_allListView_GET(self):
        response = self.client.get(self.allsearch_url)
        self.assertEquals(response.status_code, 302)

    # Testing Class based views
    def test_SearchListView_GET(self):
        response = self.client.get(self.searchlist_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/list.html')

    def test_ProductDetailView_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/details.html')

    # def test_FavouritesListView_GET(self):
    #     response = self.client.get(self.fav_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'snacks/list.html')
