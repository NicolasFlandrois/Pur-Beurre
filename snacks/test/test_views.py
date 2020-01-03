from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from snacks.models import Product, Favourite


class TestViews(TestCase):
    """Class Testing Views in Snacks App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.allsearch_url = reverse('allsearch')
        self.searchlist_url = reverse('search')
        self.detail_url = reverse('detail', args=['1'])
        self.detail_fail_url = reverse('detail', args=['2'])
        self.fav_url = reverse('favourites')
        self.fav_add_url = reverse('fav-add', args=['1'])
        self.fav_del_url = reverse('fav-del', args=['1'])

        self.prod_1 = Product.objects.create(
            pk=1,
            ean='3350033118072',
            name='test 1',
            category='cat 1',
            image='product_default.png',
            nutriscore='u'
        )

        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
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

    def test_ProductDetailView_FAIL(self):
        """Testing the ProductDetailView GET method's class"""
        response = self.client.get(self.detail_fail_url)
        self.assertEquals(response.status_code, 404)

    def test_FavouritesListView_GET(self):
        """Testing the FavouritesListView GET method's class"""
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.fav_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/list.html')

    def test_FavAddView_GET(self):
        """Testing the FavAddView GET method's class"""
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.fav_add_url)
        self.assertEquals(response.status_code, 302)

    def test_FavDeleteView_GET(self):
        """Testing the FavDeleteView GET method's class"""
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.fav_del_url)
        self.assertEquals(response.status_code, 302)
