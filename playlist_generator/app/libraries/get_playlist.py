import requests

from enum import Enum

class lastFMStation(Enum):
    LIBRARY = 1
    MIX = 2
    RECOMMENDED = 3

urls = {
    lastFMStation.LIBRARY: 'https://www.last.fm/player/station/user/Fuzwold/library',
    lastFMStation.MIX: 'https://www.last.fm/player/station/user/Fuzwold/mix',
    lastFMStation.RECOMMENDED: 'https://www.last.fm/player/station/user/Fuzwold/recommended',
}

def get_last_fm_recommendations(station):
    req = requests.get(urls[station])

    return {pl_item['artists'][0]['name']:pl_item['name'] for pl_item in req.json()['playlist']}
