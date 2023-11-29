from django.urls import path
from .views import MakePaymentView

app_name = 'checkout'

urlpatterns = [
    path('payment/', MakePaymentView.as_view(), name='payment')
]
