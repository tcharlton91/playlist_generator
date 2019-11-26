from django.shortcuts import render
from django.http import HttpResponse

from .libraries.get_playlist import get_last_fm_recommendations, lastFMStation

# Create your views here.

def index(request):
    return HttpResponse(get_last_fm_recommendations(lastFMStation.RECOMMENDED))
