from django.urls import path
from . import views

urlpatterns = [
  # route for home 
  path('', views.home, name='home'),
  # route for about
  path('about/', views.about, name='about'),
  # route for album index
  path('album/', views.album_index, name='index'),
]
