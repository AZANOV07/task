from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import *


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class AddToFavorite(views.APIView):
    def get(self, request, product_id):
        user = request.user
        product = Product.objects.get(id=product_id)

        favorite, created = Favorites.objects.get_or_create(user=user, product=product)

        if not created:
            favorite.delete()
            return Response('removed to favorites')
        return Response('added to favorites')


class FavoritesList(generics.ListAPIView):
    serializer_class = FavoritesListSerializer

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)