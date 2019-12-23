from django.test import TransactionTestCase
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class TestForms(TransactionTestCase):
    """Class Testing Forms in Users App"""

    def test_UserRegisterForm_valid_data(self):
        """Testing UserRegisterForm Class - Success Valid Form"""
        form = UserRegisterForm(data={
                                'username': 'TestForm_1',
                                'email': 'boggusmail@boggusmail.net',
                                'password1': 'jqsdBki_"E!',
                                'password2': 'jqsdBki_"E!'
                                })
        self.assertTrue(form.is_valid())

    def test_UserRegisterForm_no_data(self):
        """Testing UserRegisterForm Class
        - Not Successfull , form not valid"""
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_UserUpdateForm_valid_data(self):
        """Testing UserUpdateForm Class - Success Valid Form"""
        form = UserUpdateForm(data={
            'username': 'TestForm_1',
            'email': 'boggusmail@boggusmail.net'
        })
        self.assertTrue(form.is_valid())

    def test_UserUpdateForm_no_data(self):
        """Testing UserUpdateForm Class
        - Not Successfull , form not valid"""
        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_ProfileUpdateForm_valid_data(self):
        """Testing ProfileUpdateForm Class - Success Valid Form"""
        form = ProfileUpdateForm(data={
            'image': 'profile_default.jpg'
        })
        self.assertTrue(form.is_valid())

    # def test_ProfileUpdateForm_no_data(self):
    #     """Testing ProfileUpdateForm Class -
    # Not Successfull , form not valid"""
    #     form = ProfileUpdateForm(data={})

    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 1)

    # NB: This test cannot take place, as I installed a default value for this
    # field, therefore, it cannot get False
