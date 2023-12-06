from django.urls import path, include
from .views import UserLoginView, UserLogoutAPIView, SignUpViews, ShippingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'signup', SignUpViews, basename='signup')
router.register(r'shipping-details', ShippingViewSet,
                basename='shipping_details')


app_name = 'account'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls))
]
