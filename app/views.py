from django.shortcuts import render
from django.http import HttpResponse

from .libraries.get_playlist import get_last_fm_recommendations, lastFMStation

# Create your views here.

def index(request):
    return HttpResponse('''
    <head></head>
    <body>
    <table>
    <tr>
    <td>Library</td>
    <td>Mix</td>
    <td>Recommended</td>
    </tr>
    <tr>
    <td>'''
    '<br >'.join([str(x) for x in get_last_fm_recommendations(lastFMStation.LIBRARY).items()]) +
    '</td><td>' +
    '<br >'.join([str(x) for x in get_last_fm_recommendations(lastFMStation.MIX).items()]) +
    '</td><td>' +
    '<br >'.join([str(x) for x in get_last_fm_recommendations(lastFMStation.RECOMMENDED).items()]) +
    '''</td>
    </tr>
    </table>
    </body>'''
    )
