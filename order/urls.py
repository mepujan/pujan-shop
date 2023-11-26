from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet, OrderViewSet

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='orders')

app_name = "order"

urlpatterns = router.urls
