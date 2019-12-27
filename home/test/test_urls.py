from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, legal


class TestUrls(SimpleTestCase):
    """Class Test - TestUrls"""

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_legal(self):
        url = reverse('legal')
        self.assertEquals(resolve(url).func, legal)
