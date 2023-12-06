from rest_framework.viewsets import ModelViewSet
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer, AddtoCartSerializer, UpdateCartSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CartItemModelViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        qs = CartItem.objects.filter(user=self.request.user)
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Cart.DoesNotExist:
            return Response({'error': 'User doesnot exist'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):

        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(user=self.request.user, cart=cart)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddtoCartSerializer
        elif self.request.method in ['PATCH', 'PUT']:
            return UpdateCartSerializer
        return CartItemSerializer


class CartModelViewSet(ModelViewSet):
    serializer_class = CartSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        qs = Cart.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
