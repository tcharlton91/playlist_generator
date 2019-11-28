from django.db import models

# Create your models here.
class Song(models.Model):
  song_title = models.CharField(max_length=100)
  song_artist = models.CharField(max_length=100)
  song_id = models.CharField(max_length=50)
  
class Playlist(models.Model):
  playlist_songs = models.ManyToManyField(Song)
