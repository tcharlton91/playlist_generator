import requests

req = requests.get('https://www.last.fm/player/station/user/Fuzwold/recommended')

for pl_item in req.json()['playlist']:
  print(f"Artist: {pl_item['artists'][0]['name']}, title: {pl_item['name']}")
