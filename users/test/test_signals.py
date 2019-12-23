from django.test import TestCase
from django.contrib.auth.models import User
from users.signals import create_profile, save_profile
from users.models import Profile


# class TestSignals(TestCase):
#     """Class Testing Signals in Users App"""

#     def setUp(self):
#         """Set Up variables used in this test"""
#         # self.user_1 = User.objects.create_user(
#         #     pk=1,
#         #     username='ProfileTest_1',
#         #     password='my_p@ssword123',
#         #     email='boggusmail@boggusmail.net',
#         #     first_name='Testing',
#         #     last_name='T3st!ng'
#         # )

#         self.profile_1 = create_profile(
#             sender=User,
#             instance=Profile.objects.create(pk=1000001,
#                                             user.username='ProfileTest_1',
#                                             user.password='my_p@ssword123',
#                                             user.email='boggusmail@boggusmail.net',
#                                             user.first_name='Testing',
#                                             user.last_name='T3st!ng',
#                                             image='profile_default.jpg'),
#             created=False
#         )

    # def test_create_profile(self):
    #     """Testing the create_profile class' method"""
    #     self.assertEquals(self.profile_1.user_id, 1)
    #     self.assertEquals(self.profile_1.user_id.username, 'ProfileTest_1')
    #     self.assertEquals(self.profile_1.user_id.password, 'my_p@ssword123')
    #     self.assertEquals(self.profile_1.user_id.email,
    #                       'boggusmail@boggusmail.net')
    #     self.assertEquals(self.profile_1.user_id.first_name, 'Testing')
    #     self.assertEquals(self.profile_1.user_id.last_name, 'T3st!ing')
