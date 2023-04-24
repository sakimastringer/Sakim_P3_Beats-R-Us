from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 5-tuples
GENRES = (
    ('A', 'AfroBeat'),
    ('C', 'ChillHop'),
    ('H', 'Hip-Hop'),
    ('R', 'RockHop'),
    ('S', 'SynthWave')
)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_color = models.CharField(max_length=50)

class Album(models.Model):
    # Name Model
    name = models.CharField(max_length=100)
    # Album Art Model
    album_art = models.ImageField(blank=True)
    # artist_id = models.ForeignKey()
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name 
    # This way the update functionality.
    def get_absolute_url(self):
        print(self.id, self.pk)
        return reverse('detail', kwargs={'album_id': self.id})
    
class Song(models.Model):
     # the first optional positional argument overrides the label
    # date = models.DateField('song name')
    # Name Model
    name = models.CharField(max_length=100)
    # Duration Model
    duration = models.DurationField()
    # Genre Model
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=GENRES[0][0]
        )   

    # User Model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Create an album_id FK
    album = models.ForeignKey(Album, on_delete=models.CASCADE) 
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_genre_display()} on {self.name}" 
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for album_id: {self.album_id} @{self.url}"


