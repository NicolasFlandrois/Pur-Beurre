# """django_blog URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.urls import path

from . import views as snacks_views

urlpatterns = [
    path('favourites/',
         snacks_views.FavouritesListView.as_view(),
         name='snacks-favourites'),

    path('product/<int:pk>/',
         snacks_views.ProductDetailView.as_view(),
         name='snacks-detail'),

    path('search/',
         snacks_views.SearchListView.as_view(),
         name='snacks-search'),

    path('error',
         snacks_views.errorView, name='snacks-error'),

    path('', snacks_views.allListView, name='snacks-allsearch')
]
