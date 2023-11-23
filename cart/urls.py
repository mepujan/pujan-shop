from .views import CartModelViewSet, CartItemModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'cart', CartModelViewSet, basename='cart')
router.register(r'cart_item', CartItemModelViewSet, basename='cart_item')

app_name = 'cart'

urlpatterns = router.urls
