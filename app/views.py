from django.shortcuts import render
from django.http import HttpResponse

from .libraries.get_playlist import get_last_fm_recommendations, lastFMStation

# Create your views here.

def index(request):
    return HttpResponse('<br >'.join([get_last_fm_recommendations(lastFMStation.RECOMMENDED).items()])
