"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from .views import (PostListView,
#                     PostDetailView,
#                     PostCreateView,
#                     PostUpdateView,
#                     PostDeleteView,
#                     UserPostListView)
from .views import (SearchListView,
                    FavouritesListView)
from . import views

urlpatterns = [
    path('favourites/<str:username>', FavouritesListView.as_view(), name='user-favourites'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/<str:search>/', SearchListView.as_view(), name='product-search'),
    # path('product/new/', PostCreateView.as_view(), name='product-create'),
    # path('product/<int:pk>/update/', PostUpdateView.as_view(),
    #      name='product-update'),
    # path('product/<int:pk>/delete/', PostDeleteView.as_view(),
    #      name='product-delete'),
]
