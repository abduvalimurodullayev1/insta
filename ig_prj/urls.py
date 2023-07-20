
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from directs.views import inbox, Directs
from userauths.models import Profile
from userauths.views import userProfile, follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('users/', include('userauths.urls')),
    path('message/', include('directs.urls')),
    path('message/', include('directs.urls')),
    path('profile/',include('userauths.urls')),
    # path('notifications/', include('notifaction.urls')),
    # Profle Url

    path('<username>/', userProfile, name='profile'),
    path('<username>/saved/', userProfile, name='profilefavourite'),
    path('<username>/follow/<option>', follow, name='follow'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
