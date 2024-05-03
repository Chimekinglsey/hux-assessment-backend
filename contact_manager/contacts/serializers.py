from rest_framework import serializers
from .models import Contact
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token obtain pair serializer to include additional user data in response.
    """
    @classmethod
    def get_token(cls, user):
        """Returns a JSON Web Token object"""
        token = super().get_token(user)
        return token

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.
    """
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number'] # the id will serve as a url for navigation
