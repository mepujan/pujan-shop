from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer, AddtoCartSerializer, UpdateCartSerializer


class CartItemModelViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        qs = CartItem.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddtoCartSerializer
        elif self.request.method in ['PATCH', 'PUT']:
            return UpdateCartSerializer
        return CartItemSerializer


class CartModelViewSet(ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        qs = Cart.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
