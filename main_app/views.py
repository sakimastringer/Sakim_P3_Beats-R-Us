from django.shortcuts import render

# Views
# Add this Albums list below the imports
album = [
  {'id': ''},
  {'name': ''}, 
  {'album_art': ''},
  {'artist_id': ''},
  
 
]
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
  # We pass data to a template very much like we did in Express!
  return render(request, 'album/index.html', {
    'album': album
  })
