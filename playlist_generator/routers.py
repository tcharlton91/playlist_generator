from rest_framework import routers
from playlist_generator.app.viewsets import PlaylistViewSet, SongViewSet, AppViewSet

router = routers.DefaultRouter()

router.register('playlist', PlaylistViewSet)
router.register('song', SongViewSet)
router.register('app', AppViewSet)
