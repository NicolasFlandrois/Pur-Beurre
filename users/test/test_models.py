from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from users.models import Profile


class TestModels(TestCase):
    """Class Testing Models in Users App"""

    def setUp(self):
        """Set Up variables used in this test"""

        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

        # self.profile_1 = Profile.objects.create(user=self.user_1,
        #                                         image='profile_default.jpg')

    def test_Profile(self):
        """Testing the Profile class' object"""
        self.assertEquals(self.user_1.username, 'testuser')
        # self.assertEquals(self.user_1.password, '12345')
        self.assertEquals(self.user_1.email,
                          'boggusmail@boggusmail.net')

    # def test_Profile_is_saved_on_creation(self):
    #     """Testing if the overwitten save() methode works, from Profile"""
    #     self.assertEquals(self.profile_1.image, 'profile_default.jpg')
