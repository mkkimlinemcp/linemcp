from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from . import views

app_name = "maincms"

urlpatterns = [
    path('', views.maincms_in, name='maincms_in'),
    path('Artist_list.html', views.Artists, name='Artists'),
    path('Artist_create.html', views.create_artist, name='create_artist'),
    path('album_create.html', views.create_album, name='create_album'),
    path('test.html', views.test_go, name='test_test'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)