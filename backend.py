from urllib.parse import urljoin
import requests
import json
import math
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")
URL = os.getenv("URL")

def get_weather_info(JSON):
    lat        =  JSON["coord"]["lon"]
    lon        =  JSON["coord"]["lat"] 
    weather    =  JSON["weather"][0]["description"]
    temp       =  round(JSON["main"]["temp"] - 273.15, 2)
    feels_like =  round(JSON["main"]["feels_like"] - 273.15, 2)
    temp_min   =  round(JSON["main"]["temp_min"] - 273.15,2 )
    temp_max   =  round(JSON["main"]["temp_max"] - 273.15, 2)
    pressure   =  JSON["main"]["pressure"]
    humidity   =  JSON["main"]["humidity"]
    name = JSON["name"]

    return {"name": name, "lat": lat, "lon": lon, "weather": weather, "temp": temp, "feels_like": feels_like, 
            "temp_min": temp_min, "temp_max": temp_max, "pressure": pressure, "humidity": humidity}

def get_by_city_name(params):
    city_name = params
    req = urljoin(URL, f"?q={city_name}&appid={KEY}")
    res = requests.get(req)
    return get_weather_info(res.json())

def get_by_lat_lon(params):
    lat, lon = params
    req = urljoin(URL, f"?lat={lat}&lon={lon}&appid={KEY}")
    res = requests.get(req)
    return get_weather_info(res.json())

if __name__ == "__main__":
    pass

#lat: 20.47, lon: 44.8
