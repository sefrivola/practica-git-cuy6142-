import os
import requests
 
api_key = os.environ.get("7bbdb8484236cdcec84dc185e6fb0281")
if not api_key:
    raise SystemExit("Falta definir la variable OPENWEATHER_API_KEY")
ciudad = "Santiago"
url = "https://api.openweathermap.org/data/2.5/weather"
parametros = {"q": ciudad, "appid": api_key, "units": "metric", "lang": "es"}
 
respuesta = requests.get(url, params=parametros, timeout=10)
respuesta.raise_for_status()
datos = respuesta.json()
print(f"Clima en {ciudad}: {datos['weather'][0]['description']}")
print(f"Temperatura: {datos['main']['temp']} °C")
import os
import requests
 
api_key = os.environ.get("7bbdb8484236cdcec84dc185e6fb0281")
if not api_key:
    raise SystemExit("Falta definir la variable OPENWEATHER_API_KEY")
 
ciudad = "Santiago"
url = "https://api.openweathermap.org/data/2.5/weather"
parametros = {"q": ciudad, "appid": api_key, "units": "metric", "lang": "es"}
 
respuesta = requests.get(url, params=parametros, timeout=10)
respuesta.raise_for_status()
datos = respuesta.json()
print(f"Clima en {ciudad}: {datos['weather'][0]['description']}")
print(f"Temperatura: {datos['main']['temp']} °C")
