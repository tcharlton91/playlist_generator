from rest_framework import routers
from app.viewsets import PlaylistViewSet, SongViewSet

router = routers.DefaultRouter()

router.register(r’app’, PlaylistViewSet)
router.register(r’app’, SongViewSet)