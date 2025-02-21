from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from . import views

app_name = "maincms"
#def superuser_required(view_func):
#    return user_passes_test(lambda u: u.is_superuser, login_url='/no-access/')(view_func)


urlpatterns = [
    #path('', superuser_required(views.maincms_in), name='maincms_in'),
    path('', views.maincms_in, name='maincms_in'),
    path('Artist_list.html', views.Artists, name='Artists'),
    path('Artist_create.html', views.create_artist, name='create_artist'),
    path('album_create.html', views.create_album, name='create_album'),
    path('test.html', views.test_go, name='test_test'),
    path('rightholder_cr.html', views.rightholder_cr_view, name='rightholder_cr'),
    path('rightholder_list.html', views.rightholder_list_view, name='rightholder_view'),
    path('api/artists/', views.get_artist_profiles, name='get_artist_profiles'),
    path('api/rightholder/', views.get_rightholder_profiles, name='get_rightholder_profiles'),
    path("save_album/", views.save_album, name="save_album"),
    path('artists/<int:artist_id>/', views.artist_detail),
    path('artists/<int:artist_id>/update/', views.artist_update, name='artist_update'),
    path('artists/<int:artist_id>/delete/', views.artist_delete, name='artist_delete'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)