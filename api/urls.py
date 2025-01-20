from django.urls import path
from .import views


urlpatterns = [
    path("posts/", views.PostListCreate.as_view(), name="post-list"),
    path("posts/delete/<int:pk>/",views.PostDelete.as_view(),name="post-delete"),
    path("posts/update/<int:pk>/",views.PostUpdate.as_view(),name="post-update"),
    path("posts/<int:pk>/", views.PostRetrieve.as_view(), name="post-retrieve"),  
    path("profile/",views.ProfileListCreate.as_view(),name="profile-list"),
    path("profile/update/<int:pk>/",views.ProfileUpdate.as_view(),name="profile-update"),
    path("comments/",views.CommentListCreate.as_view(),name="comment-list"),
    path("comments/<int:pk>/delete/",views.CommentDelete.as_view(),name="comment-delete"),
    path("myposts/",views.MyPostListCreate.as_view(),name="my-post"),

] 

