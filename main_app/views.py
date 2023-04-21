from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView 
# Import the Album Model
from .models import Album, Song

# Views
# Add this Albums list below the imports
album = [
  {'id': ''},
  {'name': ''}, 
  {'album_art': ''},
  {'artist_id': ''},
  
 
]

class AlbumList(ListView):
  model = Album
  template_name = 'Albums/index.html'

class AlbumCreate(CreateView):
  model = Album
  fields = '__all__'

class AlbumCreate(CreateView):
  model = Song
  fields = '__all__'



    
    

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# Define the about view
def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

# Add new view
def album_index(request):
  albums = Album.objects.all()
  return render(request, 'album/index.html', { 'album': albums })

def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  return render(request, 'album/detail.html', { 'album': album })
