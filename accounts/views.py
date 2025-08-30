# accounts/views.py
from rest_framework import generics, permissions # Add permissions here
from .serializers import RegistrationSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,) # Add this line