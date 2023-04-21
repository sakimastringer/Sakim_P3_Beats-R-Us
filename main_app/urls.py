from django.urls import path
from . import views
from .views import AlbumList, AlbumCreate

urlpatterns = [
  # route for home 
  path('', views.home, name='home'),
  # route for about
  path('about/', views.about, name='about'),
  # route for album index
  path('album/', views.album_index, name='index'),
  path('album/<int:album_id>/', views.albums_detail, name='detail'),
  path('album/', views.album_index, name='albums_index'),
  path('album/create/', views.AlbumCreate.as_view(), name='albums_create'),
]
