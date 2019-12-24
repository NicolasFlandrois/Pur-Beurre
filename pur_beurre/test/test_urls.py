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
        # self.password_reset_confirm_url = reverse('password_reset_confirm')
        self.password_reset_complete_url = reverse('password_reset_complete')

    # def test_admin(self):
    #     # path('admin/', admin.site.urls),
    #     url = reverse('admin')
    #     self.assertEquals(resolve(url).func, admin.site.urls)

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
        # self.assertEquals(resolve(url).func, auth_views.LoginView.as_view())
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout(self):
        """Testing URL - Logout"""
        response = self.client.get(self.logout_url)
        url = reverse('logout')
        # self.assertEquals(resolve(url).func, auth_views.LogoutView.as_view())
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')

    def test_password_reset(self):
        """Testing URL - Password Reset"""
        response = self.client.get(self.password_reset_url)
        url = reverse('password_reset')
        # self.assertEquals(resolve(url).func,
        #                   auth_views.PasswordResetView.as_view())
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset.html')

    def test_password_done_reset(self):
        """Testing URL - Password Done Reset"""
        response = self.client.get(self.password_reset_done_url)
        url = reverse('password_reset_done')
        # self.assertEquals(resolve(url).func,
        #                   auth_views.PasswordResetDoneView.as_view())
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
        # self.assertEquals(resolve(url).func,
        #                   auth_views.PasswordResetCompleteView.as_view())
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_reset_complete.html')

# PB:
# AssertionError: <function PasswordResetCompleteView at 0x7f27aba42400> != <function PasswordResetCompleteView at 0x7f27aba8fb70>
# On all tests
# &
# ERROR: test_password_reset_confirm (pur_beurre.test.test_urls.TestUrls)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/media/odin/RAGNAROCK_BACKUP/8_PurBeurre/P8_PROJECT/pur_beurre/test/test_urls.py", line 50, in test_password_reset_confirm
#     url = reverse('password_reset_confirm')
#   File "/home/odin/.pyenv/versions/3.7.0/lib/python3.7/site-packages/django/urls/base.py", line 90, in reverse
#     return iri_to_uri(resolver._reverse_with_prefix(view, prefix, *args, **kwargs))
#   File "/home/odin/.pyenv/versions/3.7.0/lib/python3.7/site-packages/django/urls/resolvers.py", line 668, in _reverse_with_prefix
#     raise NoReverseMatch(msg)
# django.urls.exceptions.NoReverseMatch: Reverse for 'password_reset_confirm' with no arguments not found. 1 pattern(s) tried: ['password\\-reset\\-confirm/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/$']
# >>>>
# This issue is linked to the Slug in URL, as: password-reset-confirm/<uidb64>/<token>/
# variable parameters needs to be created to pass the tests, maybe even mocktests
