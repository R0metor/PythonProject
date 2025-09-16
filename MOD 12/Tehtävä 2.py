import json
import requests

a = input("Anna kaupungin nimi: ")

def hae_saa_tila(kaupunki:str, apikey:str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url, params={"q": kaupunki, "appid": apikey})
    d = r.json()
    return f"{a}\nWeather: {d['weather'][0]['main']}\nTemperature: {d['main']['temp']-273.15:.2f}°C"

print(hae_saa_tila(a, "476e815699989021afb17d9517282368"))