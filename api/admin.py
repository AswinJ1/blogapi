from django.contrib import admin

# Register your models here.
from .models import Post, Profile,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at','updated_at')



admin.site.register(Post, PostAdmin)

admin.site.register(Profile)
admin.site.register(Comment)