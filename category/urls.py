from django.urls import path
from .views import *


urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:category_id>', CategoryCreateAPIView.as_view(), name='add-to-category'),
    path('category/create', CategoryRetrieveAPIView.as_view(), name='category-list')
]