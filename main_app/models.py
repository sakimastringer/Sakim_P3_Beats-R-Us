from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User


# 
# Create your models here.
class Album(models.Model):
    # Name Model
    name = models.CharField(max_length=100)
    # Album Art Model that uploads photos folder byt Year, Month Day
    album_art = models.ImageField(upload_to='photos/%Y/%M/%D/')
    # artist_id = models.ForeignKey()
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)


