from rest_framework import routers
from playlist_generator.app.viewsets import PlaylistViewSet, SongViewSet

router = routers.DefaultRouter()

router.register('playlist', PlaylistViewSet)
router.register('song', SongViewSet)