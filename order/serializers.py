from django.db import transaction
from rest_framework import serializers
from .models import OrderItem, Order
from .utility import get_tracking_number
from cart.models import CartItem, Cart
from product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    orders = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'tracking_number', 'orders', 'order_status',
                  'ordered', 'total_price')


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField()

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']
            user = self.context['user']
            order = Order.objects.create(
                user=user, tracking_number=get_tracking_number(), ordered=True)

            cart_items = CartItem.objects.filter(cart_id=cart_id)
            order_items = []
            for item in cart_items:
                order_items.append(
                    OrderItem(
                        order=order,
                        product=item.product,
                        quantity=item.quantity
                    )
                )
            OrderItem.objects.bulk_create(order_items)
            Cart.objects.filter(id=cart_id).delete()
