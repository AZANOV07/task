from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductsList.as_view(), name='products-list'),
    path('products/add-to-favorite/<int:product_id>', AddToFavorite.as_view(), name='add-to-favorite'),
    path('products/favorites', FavoritesList.as_view(), name='favorites-list')
]