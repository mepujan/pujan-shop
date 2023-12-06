from rest_framework.viewsets import ModelViewSet
from .serializers import OrderItemSerializer, OrderSerializer, CreateOrderSerializer
from .models import Order, OrderItem
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class OrderItemViewSet(ModelViewSet):

    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        qs = OrderItem.objects.filter(order__user=self.request.user)
        return qs


class OrderViewSet(ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['tracking_number']
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user)
        return qs
