from django.contrib.auth.models import User

from rest_framework import generics
from .serializers import UserSerializer, PostSerializer, ProfileSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, Profile, Comment
from api import serializers



class PostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
class MyPostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all().filter(author = user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class PostDelete(generics.DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
class PostRetrieve(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all()


class PostUpdate(generics.UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

class ProfileListCreate(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)
class ProfileUpdate(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

# only user can only comment on a post
class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can comment

    def get_queryset(self):
        # Ensure `post` parameter is passed in the request query
        post_id = self.request.query_params.get('post')
        if post_id:
            try:
                return Comment.objects.filter(post_id=post_id)
            except ValueError:
                raise serializers.ValidationError({"post": "Invalid post ID."})
        return Comment.objects.none()  # Empty queryset if no post ID provided

    def perform_create(self, serializer):
        # Automatically associate the comment with the authenticated user
        post_id = self.request.data.get('post')  # Extract post ID from request
        if not post_id:
            raise serializers.ValidationError({"post": "This field is required."})

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError({"post": "Invalid post ID."})

        serializer.save(name=self.request.user, post=post)


            
class CommentDelete(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

    def get_queryset(self):
        # Only allow users to delete their own comments
        return Comment.objects.filter(name=self.request.user)

    def perform_destroy(self, instance):
        # Deletes the comment object
        instance.delete()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


