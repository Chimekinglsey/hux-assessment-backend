from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('auth/register/', views.UserRegistrationView.as_view(), name='register'),
    # path('auth/login/', views.UserLoginView.as_view(), name='login'),
    path('api/token/', views.TokenObtainPair.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('contact-list/', views.ContactListView.as_view()),  # List and search contacts
    path('get-contact/<int:pk>/', views.RetrieveContactView.as_view()),  # Retrieve contact details
    path('update-contacts/<int:pk>/', views.UpdateContactView.as_view()),  # Update contact details (PUT)
    path('delete-contact/<int:pk>/', views.DeleteContactView.as_view()),  # Delete contact (DELETE)
    path('create-contact/', views.CreateContactView.as_view()),  # Create new contact (POST)
]