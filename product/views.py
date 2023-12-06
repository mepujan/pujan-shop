from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, Rating
from .serializers import CategorySerializer, ProductSerializer, RatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilterClass
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_fields = ['category', 'name', 'stock', 'price']
    filterset_class = ProductFilterClass
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
