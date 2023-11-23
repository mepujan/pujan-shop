from rest_framework import serializers
from .models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'user', 'quantity',
                  'total_price', 'grand_total')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['products', 'grand_total']
