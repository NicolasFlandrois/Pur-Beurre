from django.test import TestCase, Client
from django.urls import reverse
from snacks.models import Product, Favourite


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_allListView_GET(self):
        client = Client()
        response = client.get(reverse('snacks-allsearch'))
        self.assertEquals(response.status_code, 302)

    def test_errorView_GET(self):
        client = Client()
        response = client.get(reverse('snacks-error'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks/error.html')
