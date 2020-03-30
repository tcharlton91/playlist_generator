from django.urls import path

from . import views
from playlist_generator.app.libraries.submit_gmusic_playlist import perform_oauth_and_get_credentials, login, import_playlist

urlpatterns = [
        path('', views.baseView),
        path('performOauth', perform_oauth_and_get_credentials),
        path('importPlaylist', import_playlist),
        path('login', login),
        ]
