from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import ShippingDetail


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=User.objects.all(), message='Email Already Exist')])

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ShippingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetail
        fields = "__all__"


class CreateShippingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetail
        fields = ('address', 'city', 'state', 'country', 'postal_code')

    def create(self, validated_data, **kwargs):
        user = self.context['user']
        shipping = ShippingDetail.objects.create(
            user=user,
            address=validated_data['address'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
            postal_code=validated_data['postal_code']
        )
        shipping.save()
        return shipping
