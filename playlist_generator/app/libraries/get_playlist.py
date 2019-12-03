import requests

from enum import Enum

class lastFMStation(Enum):
    LIBRARY = 1
    MIX = 2
    RECOMMENDED = 3

urls = {
    lastFMStation.LIBRARY: 'https://www.last.fm/player/station/user/{0}/library',
    lastFMStation.MIX: 'https://www.last.fm/player/station/user/{0}/mix',
    lastFMStation.RECOMMENDED: 'https://www.last.fm/player/station/user/{0}/recommended',
}

def get_last_fm_recommendations(station, username=''):

    if username == '':
        return {}

    req = requests.get(urls[station].format(username))

    return {pl_item['artists'][0]['name']:pl_item['name'] for pl_item in req.json()['playlist']}
