
from django.contrib import admin
from django.urls import path

from directs import views
# from directs.views import inbox
from directs.views import Directs, SendMessagee, UserSearch, Newmessage
from post.views import index, NewPost, Post_details, like, favourite
from userauths.views import follow

urlpatterns = [
   path('inbox/', views.inbox, name='message'),
   path('direct/<username>', Directs, name='directs'),
   path('send/', SendMessagee, name='send-message'),
   path('new/',UserSearch, name='user-search'),
   path('new/<username>',Newmessage, name='new-message'),


]
