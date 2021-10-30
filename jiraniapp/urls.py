from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
urlpatterns = [
    path('',views.index,name='Index'),
    path('my-profile/',views.my_profile, name='my-profile'),
    path('user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    path('create/profile',views.create_profile, name='create-profile'),    
    path('update/profile',views.update_profile, name='update-profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)