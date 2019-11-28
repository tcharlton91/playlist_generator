from rest_framework import viewsets
from playlist_generator.app.models import Song, Playlist
from playlist_generator.app.serializers import SongSerializer, PlaylistSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer