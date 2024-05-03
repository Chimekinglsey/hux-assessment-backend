from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer # django Restframework is very efficient for handling request and response

@api_view(['POST'])
def create_contact(request):
    """
    Create a new contact.
    """
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_contacts(request):
    """
    Retrieve a list of all contacts.
    """
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_contact(request, pk):
    """
    Retrieve a single contact by ID.
    """
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact)
    return Response(serializer.data)

@api_view(['PUT'])
def update_contact(request, pk):
    """
    Update a contact.
    """
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_contact(request, pk):
    """
    Delete a contact.
    """
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
