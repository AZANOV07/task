from rest_framework import serializers
from .models import *


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ProductsListSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class FavoritesListSerializer(serializers.ModelSerializer):
    product = ProductsListSerializer(read_only=True)

    class Meta:
        model = Favorites
        fields = ['product']