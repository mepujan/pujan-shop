from rest_framework.viewsets import ModelViewSet
from .serializers import OrderItemSerializer, OrderSerializer, CreateOrderSerializer
from .models import Order, OrderItem


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
