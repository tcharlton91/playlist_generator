import requests

#url = 'https://www.last.fm/player/station/user/Fuzwold/library'
url = 'https://www.last.fm/player/station/user/Fuzwold/mix'
#url = 'https://www.last.fm/player/station/user/Fuzwold/recommended'

req = requests.get(url)

for pl_item in req.json()['playlist']:
  print(f"Artist: {pl_item['artists'][0]['name']}, title: {pl_item['name']}")
