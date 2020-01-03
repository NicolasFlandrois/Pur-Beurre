from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from django.contrib import admin
from users.views import register, profile


class TestUrls(SimpleTestCase):
    """Class Test - TestUrls"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.password_reset_url = reverse('password_reset')
        self.password_reset_done_url = reverse('password_reset_done')
        self.password_reset_complete_url = reverse('password_reset_complete')

    def test_register(self):
        """Testing URL - Register"""
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profile(self):
        """Testing URL - Profile"""
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_login(self):
        """Testing URL - Login"""
        response = self.client.get(self.login_url)
        url = reverse('login')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout(self):
        """Testing URL - Logout"""
        response = self.client.get(self.logout_url)
        url = reverse('logout')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')

    def test_password_reset(self):
        """Testing URL - Password Reset"""
        response = self.client.get(self.password_reset_url)
        url = reverse('password_reset')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset.html')

    def test_password_done_reset(self):
        """Testing URL - Password Done Reset"""
        response = self.client.get(self.password_reset_done_url)
        url = reverse('password_reset_done')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset_done.html')

    # SLUG: password-reset-confirm/<uidb64>/<token>/
    # def test_password_reset_confirm(self):
        """Testing URL - Password Reset Confirm"""
    #     response = self.client.get(self.password_reset_confirm_url)
    #     url = reverse('password_reset_confirm')
    #     self.assertEquals(resolve(url).func,
    #                       auth_views.PasswordResetConfirmView.as_view())
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/password_reset_confirm.html')

    def test_password_reset_complete(self):
        """Testing URL - Password Reset Complete"""
        response = self.client.get(self.password_reset_complete_url)
        url = reverse('password_reset_complete')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset_complete.html')
