import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Song, Photo
from .forms import SongForm


# Add this Albums list below the imports
# album = [
#     {'id': ''},
#     {'name': ''},
#     {'album_art': ''},
#     {'artist_id': ''}
# ]
# Views
# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

@login_required
def album_index(request):
    albums = Album.objects.filter(user=request.user)
    return render(request, 'album/index.html', {'albums': albums})

@login_required
def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    
    song_form = SongForm()
    return render(request, 'album/details.html', {'album': album, 'song_form': song_form})

# Implement the index (view all) functionality for an Albums data resource:
class AlbumList(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/index.html'

class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'album_art']
    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        print(self)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'album_art']

class AlbumDelete(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = '/albums'

@login_required
def add_song(request, album_id):
    form = SongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.album_id = album_id
        new_song.user = request.user
        new_song.save()
    return redirect('detail', album_id=album_id)

# Add this import to access the env vars
import os

...

def add_photo(request, album_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, album_id=album_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', album_id=album_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
