from .models import User, Contact
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.
    """
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number']
