import os
from datetime import datetime

from rest_framework import serializers
from django.urls import reverse
from .models import User

class UserSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'family_role', 'profile_picture', 'profile_picture_url')
        read_only_fields = ('id', 'username', 'profile_picture_url')
        extra_kwargs = {
            'profile_picture': {'write_only': True}
        }
    
    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            request = self.context.get('request')
            if request:
                base_url = request.build_absolute_uri(
                    reverse('profile_picture', kwargs={'user_id': obj.id})
                )
                
                # Add cache-busting parameter based on file modification time
                try:
                    if os.path.exists(obj.profile_picture.path):
                        mtime = os.path.getmtime(obj.profile_picture.path)
                        return f"{base_url}?v={int(mtime)}"
                    else:
                        # If file doesn't exist, use current timestamp
                        return f"{base_url}?v={int(datetime.now().timestamp())}"
                except (OSError, ValueError):
                    # Fallback to current timestamp if there's any error
                    return f"{base_url}?v={int(datetime.now().timestamp())}"
        return None
    
    def update(self, instance, validated_data):
        # Handle profile picture update with cleanup
        if 'profile_picture' in validated_data:
            # Delete old profile picture if it exists
            if instance.profile_picture:
                old_picture = instance.profile_picture
                if os.path.exists(old_picture.path):
                    os.remove(old_picture.path)
        
        # Update all fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'family_role', 'profile_picture')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            family_role=validated_data.get('family_role', User.FamilyRole.GUEST),
            profile_picture=validated_data.get('profile_picture', None)
        )
        return user