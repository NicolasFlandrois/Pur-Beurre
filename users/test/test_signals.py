from django.test import TestCase, Client
from django.contrib.auth.models import User
from users.signals import create_profile, save_profile
from users.models import Profile


# class TestSignals(TestCase):
#     """Class Testing Signals in Users App"""

#     def setUp(self):
#         """Set Up variables used in this test"""
#         self.client = Client()
#         self.user_1 = User.objects.create_user(
#             username='testuser', password='12345',
#             email='boggusmail@boggusmail.net'
#         )

#         self.profile_1 = create_profile(
#             sender=self.user_1,
#             instance=Profile.objects.create(image='profile_default.jpg'),
#             created=False
#         )

#     def test_create_profile(self):
#         """Testing the create_profile class' method"""
#         logged_in = self.client.login(username='testuser', password='12345')
#         self.assertEquals(self.profile_1.user.username, 'testuser')
#         self.assertEquals(self.profile_1.user.password, '12345')
#         self.assertEquals(self.profile_1.user.email,
#                           'boggusmail@boggusmail.net')
