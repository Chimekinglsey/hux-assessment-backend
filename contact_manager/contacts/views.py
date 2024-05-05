""" This module contains business logic for the contacts app. """
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, TokenPairSerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from django.db.models import Q

class TokenObtainPair(TokenObtainPairView):
    serializer_class = TokenPairSerializer

class UserRegistrationView(APIView):
    """Handle User Signup"""
    def post(self, request):
        """Create a new user"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class CreateContactView(generics.CreateAPIView):
    """Create a new contact"""
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) # Associate the contact with the current user


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
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk, owner=request.user)  # Verify user ownership
            serializer = ContactSerializer(contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)


class UpdateContactView(APIView):
    """Updates a single contact using provided primary key"""
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk, owner=request.user)  # Verify user ownership
            serializer = ContactSerializer(contact, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True) # Raise exceptioin for invalid data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)



class DeleteContactView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk, owner=request.user)  # Verify user ownership
            contact.delete()
            return Response(status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    def post(self, request):
        # Get the access token from the request headers
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return Response({'error': 'No authorization header provided'}, status=status.HTTP_401_UNAUTHORIZED)

        token = auth_header.split()[1] # retrieve the token discarding `Bearer`
        # Blacklist/Revoke the token using your JWT library method
        refresh = RefreshToken(token)
        refresh.blacklist()
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        # Add redirect information to the response header to login page
        response.set_cookie('next', '/login/', httponly=True)
        return response