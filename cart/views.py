from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer


# class ListCreateCartItemAPIView(ListCreateAPIView):
#     serializer_class = CartItemSerializer

#     def get_queryset(self):
#         qs = CartItem.objects.filter(user=self.request.user)
#         return qs


# class CartModelViewSet(ModelViewSet):
# serializer_class = CartItemSerializer

# def get_queryset(self):
#     qs = CartItem.objects.filter(user=self.request.user)
#     return qs

class CartModelViewSet(ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        qs = Cart.objects.filter(user=self.request.user)
        return qs
