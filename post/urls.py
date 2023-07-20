
from django.contrib import admin
from django.urls import path

from post.views import index, NewPost, Post_details, like, favourite
from userauths.views import follow

urlpatterns = [
   path('', index, name='index'),
   path('newpost/', NewPost, name='newpost'),
   path('<uuid:post_id>/', Post_details, name='post-details'),
   path('<uuid:post_id>/like', like, name='post-like'),
   path('<uuid:post_id>/favourite', favourite, name='post-favourite'),
   path('<username>/follow/<option>', follow, name='follow')
]
