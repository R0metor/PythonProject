import json
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        jsonvastaus = vastaus.json()
        print(jsonvastaus["value"])
except requests.exceptions.RequestException as e:
    print(e)