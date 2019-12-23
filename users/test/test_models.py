from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile


class TestModels(TestCase):
    """Class Testing Models in Users App"""

    def setUp(self):
        """Set Up variables used in this test"""
        # self.user_1 = User.objects.create_user(
        #     pk=1,
        #     username='ProfileTest_1',
        #     password='my_p@ssword123',
        #     email='boggusmail@boggusmail.net',
        #     first_name='Testing',
        #     last_name='T3st!ng'
        # )

        self.profile_1 = Profile.objects.create(
            user=User.objects.create_user(
                pk=1000001,
                username='ProfileTest_1',
                password='my_p@ssword123',
                email='boggusmail@boggusmail.net',
                first_name='Testing',
                last_name='T3st!ng'
            ),
            image='profile_default.jpg'
        )

    def test_Profile(self):
        """Testing the Profile class' object"""
        self.assertEquals(self.profile_1.user_id, 1)
        self.assertEquals(self.profile_1.user_id.username, 'ProfileTest_1')
        self.assertEquals(self.profile_1.user_id.password, 'my_p@ssword123')
        self.assertEquals(self.profile_1.user_id.email,
                          'boggusmail@boggusmail.net')
        self.assertEquals(self.profile_1.user_id.first_name, 'Testing')
        self.assertEquals(self.profile_1.user_id.last_name, 'T3st!ing')

    def test_Profile_is_saved_on_creation(self):
        """Testing if the overwitten save() methode works, from Profile"""
        self.assertEquals(self.profile_1.image, 'profile_default.jpg')
