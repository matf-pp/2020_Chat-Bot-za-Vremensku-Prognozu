from urllib.parse import urljoin
import requests
import os
from dotenv import load_dotenv
from json_parser import (CompleteWeatherInfo, parse_json)

load_dotenv()

KEY = os.getenv("KEY")
URL = os.getenv("URL")


def scale_temperature(temp):   
    
    return round(temp - 273.15, 2)


def kelvins_to_degrees(obj:CompleteWeatherInfo):
    obj.main.temp       = scale_temperature(obj.main.temp)
    obj.main.feels_like = scale_temperature(obj.main.feels_like)
    obj.main.temp_min   = scale_temperature(obj.main.temp_min)
    obj.main.temp_max   = scale_temperature(obj.main.temp_max)

    return obj


def get_by_city_name(params):
    city_name = params
    req = urljoin(URL, f"?q={city_name}&appid={KEY}")
    res = requests.get(req)
    weather_obj = parse_json(res.json())
    weather_obj_scaled = kelvins_to_degrees(weather_obj)
    
    return weather_obj_scaled
   

def get_by_lat_lon(params):
    lat, lon = params
    req = urljoin(URL, f"?lat={lat}&lon={lon}&appid={KEY}")
    res = requests.get(req)
    weather_obj = parse_json(res.json())
    weather_obj_scaled = kelvins_to_degrees(weather_obj)
    
    return weather_obj_scaled
    
if __name__ == "__main__":
    pass
