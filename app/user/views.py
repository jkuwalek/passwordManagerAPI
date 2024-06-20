"""
Views for the user API
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import Website as WebsiteModel
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    WebsiteSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class ManageWebsitesView(generics.ListAPIView):
    """Lists all the authenticated user's saved website credentials"""
    serializer_class = WebsiteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WebsiteModel.objects.filter(userId=self.request.user.id).all()


class ManageWebsiteView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user's saved website credentials'"""
    serializer_class = WebsiteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WebsiteModel.objects.filter(userId=self.request.user.id).all()


class AddWebsiteView(generics.CreateAPIView):
    """Create a new authenticated user's saved website credentials'"""
    serializer_class = WebsiteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)
