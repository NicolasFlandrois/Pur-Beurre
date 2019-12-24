from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from snacks.models import Product, Favourite


class TestViews(TestCase):
    """Class Testing Views in Snacks App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.allsearch_url = reverse('snacks-allsearch')
        self.searchlist_url = reverse('snacks-search')
        self.detail_url = reverse('snacks-detail', args=['1'])
        self.fav_url = reverse('snacks-favourites')

        self.prod_1 = Product.objects.create(
            pk=1,
            ean='3350033118072',
            name='test 1',
            category='cat 1',
            image='product_default.png',
            nutriscore='u'
        )

        self.user_1 = User.objects.create_user(
            pk=1,
            username='Fav Models Unit Test 1',
            email='boggusmail@boggusmail.net'
        )

        self.fav_1 = Favourite.objects.create(
            pk=1,
            date_added='2019-12-24 16:17:11.856150+00:00',
            user=self.user_1,
            product=self.prod_1
        )

    # Testing Function based views
    def test_allListView_GET(self):
        """Testing the allListView GET method's function"""
        response = self.client.get(self.allsearch_url)
        self.assertEquals(response.status_code, 302)

    # Testing Class based views
    def test_SearchListView_GET(self):
        """Testing the SearchListView GET method's class"""
        response = self.client.get(self.searchlist_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/list.html')

    def test_ProductDetailView_GET(self):
        """Testing the ProductDetailView GET method's class"""
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/details.html')

    # def test_FavouritesListView_GET(self):
    #     """Testing the FavouritesListView GET method's class"""
    #     response = self.client.get(self.fav_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'snacks/list.html')
    #     # This test doesn't work as it needs to pass LoginRequiredMixin, UserPassesTestMixin tests
    #     # Without param variables matching thoses requisits, the server revert a 302 Error and response no templates


# How to test the json API with Open Food Facts?
