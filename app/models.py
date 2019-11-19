from django.db import models

# Create your models here.
Class Song(models.Model):
  title = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  song_id = models.CharField(max_length=50)
  
Class Playlist(models.Model):
  songs = models.ManyToManyField(Song)
