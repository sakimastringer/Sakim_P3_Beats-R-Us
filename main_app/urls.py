from django.contrib import admin
from django.urls import path, include
# from albums.views import AlbumList
# from .views import *
from . import views




urlpatterns = [
  # route for home 
  path('', views.home, name='home'),
  # route for about
  path('about/', views.about, name='about'),
  # route for album index
  path('albums/', views.album_index, name='index'),
  # route for album detail
  path('albums/<int:album_id>/', views.albums_detail, name='detail'),
  # route used to show a form and create an album
  path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
  path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
  path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete'), 
  path('albums/<int:album_id>/add_song/', views.add_song, name='add_song'),
  path('albums/<int:album_id>/add_photo/', views.add_photo, name='add_photo'),
  path('admin/', admin.site.urls),
  # # '' represents the "starts with" path
  # path('', include('main_app.urls')),

  path('accounts/signup/', views.signup, name='signup'),
  # include the built-in auth urls for the built-in views
  # path('accounts/', include('django.contrib.auth.urls')),
]
