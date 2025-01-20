from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime,date




    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic =  models.ImageField(null=True, blank=True, upload_to='images/profile/')
    title = models.CharField(max_length=100,null=True, blank=True)
    website_url = models.CharField(max_length=255,null=True, blank=True)
    linkedin_url = models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title + '|' + str(self.author)
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',  # Self-referential foreign key
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.parent:
            return f"Reply to {self.parent.name} - {self.name}"
        return f"{self.post.title} - {self.name}"