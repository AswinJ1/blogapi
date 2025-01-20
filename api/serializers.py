from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Profile, Comment
class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(source='profile.profile_pic', allow_null=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile_pic']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Extract profile data if provided
        profile_data = validated_data.pop('profile', {})
        
        # Create the user
        user = User.objects.create_user(**validated_data)
        
        # Create the profile object if needed
        Profile.objects.create(user=user, **profile_data)
        
        return user
    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id","user","bio","profile_pic","title","website_url","linkedin_url"]
        extra_kwargs ={"user":{"required":False}}

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = ["id","title","author","body","category","picture","created_at","updated_at"]
        extra_kwargs ={"author":{"read_only": True}}

class CommentSerializer(serializers.ModelSerializer):
    name = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["id","post","name","body","date_added","parent"]
        extra_kwargs ={"post":{"read_only": True}}


