from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from playlist_generator.app.libraries.get_playlist import get_last_fm_recommendations, lastFMStation

# Create your views here.

def baseView(request):

    lastFM_username = request.GET.get('lastFMUsername')

    context = {'Library': get_last_fm_recommendations(lastFMStation.LIBRARY, lastFM_username),
               'Mix': get_last_fm_recommendations(lastFMStation.MIX, lastFM_username),
               'Recommended': get_last_fm_recommendations(lastFMStation.RECOMMENDED, lastFM_username),
              }

    return render(request, 'base.html', context)
