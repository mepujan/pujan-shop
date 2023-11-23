from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework import status


class CartItemModelViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        qs = CartItem.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        cart = Cart.objects.create_or_update
        serializer.save(user=self.request.user)


class CartModelViewSet(ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        qs = Cart.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
