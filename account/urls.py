from django.urls import path, include
from .views import UserLoginView, UserLogoutAPIView, SignUpViews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'signup', SignUpViews, basename='signup')


app_name = 'account'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls))
]
