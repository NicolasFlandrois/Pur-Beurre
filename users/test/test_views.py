from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile


class TestViews(TestCase):
    """docstring for TestViews"""
