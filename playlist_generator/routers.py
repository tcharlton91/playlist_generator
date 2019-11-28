from rest_framework import routers
from playlist_generator.app.viewsets import PlaylistViewSet, SongViewSet

router = routers.DefaultRouter()

router.register('app', PlaylistViewSet)
router.register('app', SongViewSet)