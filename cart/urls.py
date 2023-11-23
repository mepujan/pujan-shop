from .views import CartModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'cart', CartModelViewSet, basename='cart')

app_name = 'cart'

urlpatterns = router.urls
