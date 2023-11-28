from rest_framework.views import APIView
from .serializers import UserLoginSerializer, UserSignUpSerializer, UserUpdateSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, logout
from rest_framework.viewsets import ModelViewSet


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).exists()
        if user:
            usr = authenticate(username=username, password=password)
            if usr:
                data = {
                    "user_id": usr.id,
                    "username": usr.username,
                    "token": usr.auth_token.key
                }
                return Response({'user': data}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'User Doesnot Exist.'}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutAPIView(APIView):
    @staticmethod
    def post(request):
        logout(request)
        return Response({'message': 'User Logout Successfully.'}, status=status.HTTP_200_OK)


class SignUpViews(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return UserSignUpSerializer
