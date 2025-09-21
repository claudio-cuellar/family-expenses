from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
import mimetypes
from .models import User
from .serializers import UserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class ProfilePictureView(generics.RetrieveAPIView):
    """
    Serve profile pictures only to the owner
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, user_id):
        # Only allow users to see their own profile picture
        if str(request.user.id) != str(user_id):
            raise Http404("Profile picture not found")
        
        user = get_object_or_404(User, id=user_id)
        
        if not user.profile_picture:
            raise Http404("No profile picture")
        
        # Serve the file with proper content type
        file_path = user.profile_picture.path
        if os.path.exists(file_path):
            # Detect content type
            content_type, _ = mimetypes.guess_type(file_path)
            if not content_type:
                content_type = 'image/jpeg'  # Default fallback
            
            # Get file modification time for ETag
            mtime = os.path.getmtime(file_path)
            etag = f'"{int(mtime)}"'
            
            # Check if client has the current version
            if_none_match = request.META.get('HTTP_IF_NONE_MATCH')
            if if_none_match == etag:
                return HttpResponse(status=304)  # Not Modified
            
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type=content_type)
                # Set cache headers to prevent stale cache
                response['ETag'] = etag
                response['Cache-Control'] = 'private, must-revalidate, max-age=0'
                response['Last-Modified'] = mtime
                return response
        else:
            raise Http404("Profile picture file not found")