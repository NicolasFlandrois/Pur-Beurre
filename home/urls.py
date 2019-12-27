from django.urls import path
from . import views

urlpatterns = [
    path('legal/', views.legal, name='legal'),
    path('', views.home, name='home'),
]
