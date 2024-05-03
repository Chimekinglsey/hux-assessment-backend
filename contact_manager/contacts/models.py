from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    """Model for storing contact information"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        """String representation of the contact object"""
        return f"{self.first_name} {self.last_name}"

