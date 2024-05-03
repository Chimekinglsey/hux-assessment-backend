""" This module contains business logic for the contacts app. """
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserTokenSerializer, RefreshToken, ContactSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from django.db.models import Q
from .serializers import UserSerializer


class UserRegistrationView(APIView):
    """Handle User Signup"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    """Handles user credential validation for login"""
    def post(self, request):
        """logs the user in if credentials are correct"""
        serializer = UserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateContactView(APIView):
    """ Adds a new contact to the owners contact list"""
    permission_classes = [IsAuthenticated]  # Requires user authentication

    def post(self, request):
        """ post is required"""
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)  # Link contact to authenticated user
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactListView(APIView):
    """Returns all contacts """
    permission_classes = [IsAuthenticated]  # Requires user authentication

    def get(self, request):
        # Get search query parameter (if any)
        query = request.query_params.get('q', None)  # 'q' is a common search parameter name

        # Filter contacts based on user and search query (if provided)
        contacts = Contact.objects.filter(owner=request.user)
        if query:
            contacts = contacts.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )

        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveContactView(APIView):
    """Retrieves a single contact using provided primary key"""
    permission_classes = [IsAuthenticated]  # Requires user authentication

    def get(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk, owner=request.user)  # Verify user ownership
            serializer = ContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)


class UpdateContactView(APIView):
    """Updates a single contact using provided primary key"""
    permission_classes = [IsAuthenticated]  # Requires user authentication

    def put(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk, owner=request.user)  # Verify user ownership
            serializer = ContactSerializer(contact, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)



class DeleteContactView(APIView):
    permission_classes = [IsAuthenticated]  # Requires user authentication

    def delete(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk, owner=request.user)  # Verify user ownership
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)


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