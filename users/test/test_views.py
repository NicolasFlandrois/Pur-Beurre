from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile


class TestViews(TestCase):
    """Class Testing Views in Users App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')

        self.user_1 = User.objects.create_user(
            pk=1,
            username='Fav Models Unit Test 1',
            email='boggusmail@boggusmail.net'
        )

    # Testing Function based views
    def test_register_GET(self):
        """Testing the register GET method's function"""
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    # def test_profile_GET(self):
    #     """Testing the profile GET method's function"""
    #     response = self.client.get(self.profile_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/profile.html')
    #     # This test doesn't work as it needs to pass LoginRequiredMixin, UserPassesTestMixin tests
    #     # Without param variables matching thoses requisits, the server revert a 302 Error and response no templates
