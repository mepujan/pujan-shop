from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Carts
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
        qs = Carts.objects.filter(user=self.request.user)
        return qs
