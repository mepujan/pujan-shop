from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField()
