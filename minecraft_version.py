import requests
import json

url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

r = requests.get(url)

latest = r.json()['latest']['release']

print("Latest version: " + latest)

for i in r.json()['versions']:
    if i['type'] == "release" and i['id'] == latest:
        d_link = requests.get(i['url'])

        server = requests.get(d_link.json()['downloads']['server']['url'])

        f = open("server.jar", "wb")
        f.write(server.content)
        f.close()
