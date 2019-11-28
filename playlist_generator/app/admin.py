from django.contrib import admin

# Register your models here.
from playlist_generator.app.models import Playlist

admin.site.register(Playlist)