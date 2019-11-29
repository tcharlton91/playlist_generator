from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .libraries.get_playlist import get_last_fm_recommendations, lastFMStation

# Create your views here.

def basicView(request):
    return HttpResponse('''
    <head></head>
    <body>
    <table>
    <tr>
    <th>Library</th>
    <th>Mix</th>
    <th>Recommended</th>
    </tr>
    <tr>
    <td>''' +
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

def libraryView(request):
  return JsonResponse(get_last_fm_recommendations(lastFMStation.LIBRARY))

def mixView(request):
  return JsonResponse(get_last_fm_recommendations(lastFMStation.MIX))

def recommendedView(request):
  return JsonResponse(get_last_fm_recommendations(lastFMStation.RECOMMENDED))

def libraryTemplateView(request):

    context = {'Library': get_last_fm_recommendations(lastFMStation.LIBRARY)}

    return render(request, 'libraryTemplate.html', context)

def mixTemplateView(request):

    context = {'Mix': get_last_fm_recommendations(lastFMStation.MIX)}

    return render(request, 'mixTemplate.html', context)
