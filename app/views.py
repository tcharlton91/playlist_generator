from django.shortcuts import render
from django.http import HttpResponse

import libraries.get_playlist

# Create your views here.

def index(request):
    return HttpResponse(get_last_fm_recommendations(lastFMStation.RECOMMENDED))
