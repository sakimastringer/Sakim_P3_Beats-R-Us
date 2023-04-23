from django.shortcuts import render, redirect
# Import the Cat Model
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Song


# Add this Albums list below the imports
album = [
    {'id': ''},
    {'name': ''},
    {'album_art': ''},
    {'artist_id': ''}
]
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
    return render(request, 'album/details.html', {'album': album})

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
    success_url = '/album'



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
