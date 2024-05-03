""" This module contains business logic for the contacts app. """
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserTokenSerializer, RefreshToken

from .serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    def post(self, request):
        # Get the access token from the request headers
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return Response({'error': 'No authorization header provided'}, status=status.HTTP_401_UNAUTHORIZED)

        token = auth_header.split()[1]
        # Blacklist/Revoke the token using your JWT library method
        refresh = RefreshToken(token)
        refresh.blacklist()
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        # Add redirect information to the response header
        response.set_cookie('next', '/login/', httponly=True)
        return response