from rest_framework.views import APIView
from paypalrestsdk import Payment
from rest_framework.response import Response
from cart.models import Cart
from .serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class MakePaymentView(APIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        total_price = cart.total_price()
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "transactions": [{
                "amount": {
                    "total": total_price,
                    "currency": "USD",
                },
                "description": "Payment description",
            }],
            "redirect_urls": {
                "return_url": "http://yourdomain.com/execute-payment/",
                "cancel_url": "http://yourdomain.com/cancel-payment/",
            },
        })

        if payment.create():
            approval_url = payment.links[1].href
            return Response({"approval_url": approval_url})
        else:
            return Response({"error": "Payment creation failed."})
