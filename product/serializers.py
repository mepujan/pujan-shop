from rest_framework import serializers
from .models import Category, Product, Rating
from django.core.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'slug', 'descriptions',
                  'image', 'created', 'updated', 'avg_rating')
        depth = 1


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise ValidationError(
                "Rating Should be in range 1 to 5 inclusive.")
        return rating
