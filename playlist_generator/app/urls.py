from django.urls import path

from . import views
from playlist_generator.app.libraries.submit_gmusic_playlist import submitPlaylistToGMusic

urlpatterns = [
        path('', views.baseView),
        path('submitPlaylist', submitPlaylistToGMusic),
        ]
